import asyncio
from playwright.async_api import Page

async def run(page: Page) -> None:
    """
    Step 3: Clicks on the icon/element that says "Digital Twin".
    """
    print("Waiting for launchpad page to load completely...")
    try:
        # Wait up to 10 seconds for network requests to settle
        await page.wait_for_load_state("networkidle", timeout=10000)
    except Exception:
        print("Timeout waiting for network idle, proceeding...")

    print("Searching for 'Digital Twin' elements...")
    
    # Locate elements containing "Digital Twin" (case-insensitive)
    locator = page.locator("text=Digital Twin")
    
    try:
        # Wait up to 15 seconds for the first match to be visible
        await locator.first.wait_for(state="visible", timeout=15000)
    except Exception as e:
        print(f"Error: 'Digital Twin' text did not become visible within 15 seconds.")
        print(f"Current URL: {page.url}")
        print(f"Current Title: {await page.title()}")
        return

    count = await locator.count()
    print(f"Found {count} element(s) with text 'Digital Twin'.")
    
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
    print("Clicking the first 'Digital Twin' element...")
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
            
    # Give the page 3 seconds to process the click/navigation
    await page.wait_for_timeout(3000)
    print("Step 3 finished.")
