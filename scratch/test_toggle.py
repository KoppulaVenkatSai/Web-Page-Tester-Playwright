import asyncio
import os
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as playwright:
        profile_dir = os.path.join(os.getcwd(), "brave_profile")
        brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
        
        print("Launching Brave Browser...")
        context = await playwright.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            executable_path=brave_path,
            headless=False,
            no_viewport=True,
            args=["--disable-infobars", "--start-maximized"]
        )
        
        page = context.pages[0] if context.pages else await context.new_page()
        
        print("Navigating...")
        await page.goto("https://qa73.assetsense.com/c2/launchpad.html")
        await page.wait_for_timeout(5000)
        
        # Click Digital Twin
        await page.locator("text=Digital Twin").first.click()
        await page.wait_for_timeout(3000)
        
        # Click Steam Turbine Block - 1
        await page.locator("text=Steam Turbine Block - 1").first.click()
        await page.wait_for_timeout(3000)
        
        # Get toggle element and state
        toggle_id = "toggle-button"
        input_exists = await page.evaluate(f"() => !!document.getElementById('{toggle_id}')")
        if not input_exists:
            print("toggle-button not found yet!")
            await context.close()
            return
            
        initial_checked = await page.evaluate(f"() => document.getElementById('{toggle_id}').checked")
        initial_html = await page.evaluate(f"() => document.getElementById('{toggle_id}').outerHTML")
        print(f"Initial JS Checked: {initial_checked}")
        print(f"Initial HTML: {initial_html}")
        
        # Take initial screenshot
        await page.screenshot(path="screenshot_toggle_initial.png")
        print("Saved screenshot_toggle_initial.png")
        
        # Click label to toggle
        print("Clicking toggle label...")
        await page.locator("label[for='toggle-button']").click()
        await page.wait_for_timeout(2000)
        
        post_checked = await page.evaluate(f"() => document.getElementById('{toggle_id}').checked")
        post_html = await page.evaluate(f"() => document.getElementById('{toggle_id}').outerHTML")
        print(f"Post Click JS Checked: {post_checked}")
        print(f"Post Click HTML: {post_html}")
        
        # Take post click screenshot
        await page.screenshot(path="screenshot_toggle_clicked.png")
        print("Saved screenshot_toggle_clicked.png")
        
        await context.close()

if __name__ == "__main__":
    asyncio.run(main())
