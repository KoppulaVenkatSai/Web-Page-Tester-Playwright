import asyncio
import os
import sys
from playwright.async_api import async_playwright

async def inspect():
    async with async_playwright() as playwright:
        profile_dir = os.path.join(os.getcwd(), "brave_profile")
        brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
        
        print("Launching Brave Browser...")
        context = await playwright.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            executable_path=brave_path,
            headless=False,
            no_viewport=True,
        )
        
        page = context.pages[0] if context.pages else await context.new_page()
        
        # Wait a bit for session restore / page load
        await page.wait_for_timeout(3000)
        
        print(f"Current URL: {page.url}")
        print(f"Current Title: {page.title()}")
        
        # Check if we need to navigate
        if "launchpad.html" not in page.url and "assetsense.com" not in page.url:
            print("Navigating to launchpad...")
            await page.goto("https://qa73.assetsense.com/c2/launchpad.html")
            await page.wait_for_load_state("networkidle")
            
        print("Waiting up to 10 seconds for observations wrapper to be present...")
        try:
            await page.wait_for_selector(".dt-observations-wrapper", timeout=10000)
        except Exception:
            print("Wrapper not found yet. Current HTML may not have loaded observations.")
            
        js_inspect = """
        () => {
            const results = [];
            const wrappers = Array.from(document.querySelectorAll('.dt-observations-wrapper'));
            results.push({
                total_wrappers: wrappers.length,
                active_wrappers: wrappers.filter(w => w.classList.contains('active-view')).length,
                classes: wrappers.map(w => w.className)
            });
            
            const activeWrapper = document.querySelector('.dt-observations-wrapper.active-view');
            if (activeWrapper) {
                const boxes = Array.from(activeWrapper.querySelectorAll('.dashboard-box'));
                results.push({
                    total_boxes_in_active: boxes.length,
                    boxes_details: boxes.map((box, idx) => {
                        const header = box.querySelector('h3, h4, .box-header, .dashboard-box-header, label');
                        const headerText = header ? header.innerText.trim() : 'No Header';
                        
                        // Let's find ALL svg paths in this box
                        const paths = Array.from(box.querySelectorAll('svg path'));
                        const pathsDetails = paths.map(p => {
                            const data = p.__data__;
                            return {
                                stroke: p.getAttribute('stroke') || '',
                                className: p.getAttribute('class') || '',
                                hasData: !!data,
                                dataLength: data ? data.length : 0,
                            };
                        });
                        return {
                            boxIdx: idx,
                            headerText: headerText,
                            pathsCount: paths.length,
                            pathsDetails: pathsDetails,
                            boxHTML: box.outerHTML.substring(0, 500)
                        };
                    })
                });
            } else {
                results.push({error: "No active wrapper found"});
            }
            return results;
        }
        """
        
        data = await page.evaluate(js_inspect)
        import pprint
        pprint.pprint(data)
        
        await context.close()

if __name__ == "__main__":
    asyncio.run(inspect())
