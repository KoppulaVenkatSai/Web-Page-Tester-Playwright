import asyncio
from playwright.async_api import Page

async def run(page: Page, ecn: str = None) -> bool:
    """
    Step 4: Checks if the ECN (e.g. "AS-FCRST-DT-01") is present in the choosable asset options.
    If yes, clicks it and returns True. Else, logs it not found and returns False.
    """
    if not ecn:
        from config import BaseConfig
        if getattr(BaseConfig, "ecns_to_test", None):
            ecn = BaseConfig.ecns_to_test[0]
        else:
            print("[-] No ECN provided and BaseConfig.ecns_to_test is empty.")
            return False

    print("Waiting for page load after entering Digital Twin...")
    try:
        # Wait up to 10 seconds for network requests to settle
        await page.wait_for_load_state("networkidle", timeout=10000)
    except Exception:
        print("Timeout waiting for network idle, proceeding...")

    target_text = f"({ecn})"
    print(f"Searching for asset option containing '{target_text}'...")
    
    # Locate elements containing target text (case-insensitive)
    locator = page.locator(f"text={target_text}")
    
    try:
        # Wait up to 15 seconds for the ECN to be attached
        await locator.first.wait_for(state="attached", timeout=15000)
    except Exception:
        print(f"[-] ECN '{ecn}' (as '{target_text}') not found in the choosable asset options.")
        return False

    if not await locator.first.is_visible():
        print(f"[-] ECN '{ecn}' was found attached but is not visible on page.")
        return False

    count = await locator.count()
    print(f"Found {count} element(s) matching ECN '{ecn}'.")
    
    # Print the tag name and text of each found element for debugging
    for i in range(count):
        try:
            el = locator.nth(i)
            tag = await el.evaluate("el => el.tagName")
            text = await el.inner_text()
            print(f"  [{i}]: Tag=<{tag}>, Text='{text.strip().replace(chr(10), ' ')[:50]}'")
        except Exception as e:
            print(f"  [{i}]: Error inspecting element: {e}")

    # Click the first matching element
    print(f"Clicking the first element matching ECN '{ecn}'...")
    try:
        await locator.first.click()
        print("Click action dispatched.")
    except Exception as e:
        print(f"Normal click failed: {e}")
        print("Attempting force click...")
        try:
            await locator.first.click(force=True)
            print("Force click dispatched.")
        except Exception as fe:
            print(f"Force click also failed: {fe}")
            return False
            
    # Give the page 3 seconds to process the click/navigation
    await page.wait_for_timeout(3000)
    print("Step 4 finished.")
    return True
