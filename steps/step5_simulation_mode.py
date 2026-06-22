import asyncio
from playwright.async_api import Page

async def run(page: Page) -> None:
    """
    Step 5: Checks if "Simulation Mode" is on. If off, turns it on.
    """
    print("Waiting for page load...")
    try:
        # Wait up to 10 seconds for network requests to settle
        await page.wait_for_load_state("networkidle", timeout=10000)
    except Exception:
        pass
        
    target_text = "Simulation Mode"
    print(f"Searching for '{target_text}' element...")
    
    # 1. Look for 'Simulation Mode' text on the page
    label_locator = page.locator(f"text={target_text}")
    try:
        # Wait up to 15 seconds for the text to appear
        await label_locator.first.wait_for(state="visible", timeout=15000)
    except Exception:
        print(f"[-] Error: Could not find '{target_text}' text on the page.")
        print(f"Current URL: {page.url}")
        print(f"Current Title: {await page.title()}")
        return
        
    count = await label_locator.count()
    print(f"[+] Found {count} element(s) with text '{target_text}'.")
    
    # Let's inspect the first label and its parent
    first_label = label_locator.first
    parent = first_label.locator("xpath=..")
    
    # Print the outer HTML of the parent to help us inspect it in detail
    try:
        parent_html = await parent.evaluate("el => el.outerHTML")
        print(f"[~] Toggle Parent HTML:\n{parent_html[:400]}")
    except Exception as e:
        print(f"[-] Could not read parent HTML: {e}")
        parent_html = ""

    # Let's find the toggle target.
    # We check if there's a checkbox/switch role or an input tag nearby.
    toggle = page.get_by_role("checkbox", name=target_text, exact=False)
    is_role_checkbox = await toggle.count() > 0
    
    if not is_role_checkbox:
        toggle = page.get_by_role("switch", name=target_text, exact=False)
        is_role_switch = await toggle.count() > 0
    else:
        is_role_switch = False
        
    if not (is_role_checkbox or is_role_switch):
        nested_input = first_label.locator("input[type='checkbox']")
        if await nested_input.count() > 0:
            toggle = nested_input.first
            is_role_checkbox = True
            print("[~] Found nested checkbox input inside the label.")
        else:
            # Sibling checkbox
            sibling_input = parent.locator("input[type='checkbox']")
            if await sibling_input.count() > 0:
                toggle = sibling_input.first
                is_role_checkbox = True
                print("[~] Found sibling checkbox input.")
            else:
                # Default to clicking the label itself
                toggle = first_label
                print("[~] Using the text label itself as the toggle target.")
            
    # Check if the toggle has aria-checked attribute
    aria_checked = await toggle.get_attribute("aria-checked")
    if aria_checked is None:
        aria_checked = await parent.get_attribute("aria-checked")

    # Check state
    is_on = False
    
    if aria_checked is not None:
        is_on = aria_checked == "true"
        print(f"[~] Detected aria-checked attribute: '{aria_checked}' (State: {'ON' if is_on else 'OFF'})")
    elif is_role_checkbox:
        is_on = await toggle.is_checked()
        print(f"[~] Detected checkbox state: {'ON' if is_on else 'OFF'}")
    else:
        # Custom Toggle: Check classes of the element and its parent by splitting them
        parent_class = await parent.get_attribute("class") or ""
        self_class = await toggle.get_attribute("class") or ""
        classes_str = (parent_class + " " + self_class).lower()
        classes_set = set(classes_str.split())
        
        # Only match exact class names to avoid matching substrings (like "on" in "button")
        active_indicators = {"checked", "active", "on", "selected", "true", "enabled"}
        matched_indicators = classes_set.intersection(active_indicators)
        
        if matched_indicators:
            is_on = True
            print(f"[~] Detected active state indicators in class names: {matched_indicators}")
        else:
            print(f"[~] No active state indicators in class names: {classes_set}")

    # Toggle the state if it is OFF
    if not is_on:
        print("[+] Simulation Mode is OFF. Turning ON...")
        clicked = False
        
        # 1. Try to find the associated label for the checkbox (this handles hidden inputs)
        if is_role_checkbox:
            try:
                input_id = await toggle.get_attribute("id")
                if input_id:
                    associated_label = parent.locator(f"label[for='{input_id}']")
                    if await associated_label.count() > 0:
                        print(f"[~] Clicking associated label element: label[for='{input_id}']")
                        await associated_label.click()
                        clicked = True
            except Exception as e:
                print(f"[-] Sibling label click failed: {e}")
                
        # 2. Sibling toggle element fallback (looks for label with class 'toggle')
        if not clicked and is_role_checkbox:
            try:
                sibling_labels = parent.locator("label")
                count_labels = await sibling_labels.count()
                for i in range(count_labels):
                    lbl = sibling_labels.nth(i)
                    lbl_class = await lbl.get_attribute("class") or ""
                    if "toggle" in lbl_class.lower():
                        print(f"[~] Clicking sibling label with class '{lbl_class}'")
                        await lbl.click()
                        clicked = True
                        break
            except Exception as e:
                print(f"[-] Sibling toggle class click failed: {e}")
                
        # 3. Fallback: Force checking the input directly
        if not clicked:
            print("[~] Clicking label failed. Attempting force action directly on input...")
            try:
                if is_role_checkbox:
                    await toggle.check(force=True)
                else:
                    await toggle.click(force=True)
                clicked = True
                print("[+] Force action completed.")
            except Exception as e:
                print(f"[-] Force action also failed: {e}")
                
        # Verify the new state
        await page.wait_for_timeout(1000)
        if is_role_checkbox:
            is_on = await toggle.is_checked()
        else:
            aria_checked = await toggle.get_attribute("aria-checked")
            is_on = aria_checked == "true"
        print(f"[+] Verified state after toggle: {'ON' if is_on else 'OFF'}")
        
    else:
        print("[+] Simulation Mode is already ON.")
            
    print("Step 5 finished.")
