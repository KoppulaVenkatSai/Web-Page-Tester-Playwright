import os
import sys
from playwright.async_api import BrowserContext, Page

async def run(playwright, url: str) -> tuple[BrowserContext, Page]:
    """
    Step 1: Launches Brave Browser with a persistent profile and opens the target URL.
    Returns the BrowserContext and Page objects.
    """
    profile_dir = os.path.join(os.getcwd(), "brave_profile")
    brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
    
    if not os.path.exists(brave_path):
        print(f"Error: Brave Browser not found at: {brave_path}")
        sys.exit(1)
        
    print(f"Launching Brave Browser with persistent profile in: {profile_dir}")
    context = await playwright.chromium.launch_persistent_context(
        user_data_dir=profile_dir,
        executable_path=brave_path,
        headless=False,
        no_viewport=True,
        args=[
            "--disable-infobars", 
            "--start-maximized",
            "--restore-last-session=false",
            "--disable-session-crashed-bubble"
        ]
    )
    
    # Close all other tabs/pages except the first one to avoid multiple tabs and session restore issues
    while len(context.pages) > 1:
        try:
            await context.pages[-1].close()
        except Exception:
            break
            
    page = context.pages[0] if context.pages else await context.new_page()
    
    print(f"Navigating to: {url}...")
    await page.goto(url, timeout=100000)
    
    # Wait for the network to go idle (no active requests) so all login scripts/assets load
    print("Waiting for page assets and network to stabilize...")
    try:
        await page.wait_for_load_state("networkidle", timeout=15000)
    except Exception:
        print("Network didn't go fully idle, but proceeding anyway.")
        
    # Wait for at least one input field to appear (indicating login form is rendered) if not already logged in
    if "launchpad.html" not in page.url:
        try:
            await page.wait_for_selector("input", state="attached", timeout=10000)
        except Exception:
            print("Could not detect input fields, continuing...")
        
    return context, page
