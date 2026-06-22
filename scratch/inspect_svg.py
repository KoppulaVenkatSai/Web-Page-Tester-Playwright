import asyncio
import os
import sys
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as playwright:
        profile_dir = os.path.join(os.getcwd(), "brave_profile")
        brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
        
        context = await playwright.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            executable_path=brave_path,
            headless=False,
            no_viewport=True,
        )
        
        page = context.pages[0] if context.pages else await context.new_page()
        await page.wait_for_timeout(3000) # Wait for page to settle
        
        js_inspect = """
        () => {
            const activeWrapper = document.querySelector('.dt-observations-wrapper.active-view') || document;
            const boxes = Array.from(activeWrapper.querySelectorAll('.dashboard-box')).filter(box => {
                const rect = box.getBoundingClientRect();
                return rect.width > 0 && rect.height > 0;
            });
            
            return boxes.slice(0, 3).map((box, idx) => {
                const header = box.querySelector('h3, h4, .box-header, .dashboard-box-header, label');
                const title = header ? header.innerText.trim() : ('Graph ' + idx);
                
                const paths = Array.from(box.querySelectorAll('svg path'));
                const pathDetails = paths.map(p => {
                    return {
                        class: p.getAttribute('class') || '',
                        stroke: p.getAttribute('stroke') || '',
                        strokeWidth: p.getAttribute('stroke-width') || '',
                        hasData: !!p.__data__,
                        dataLength: p.__data__ && Array.isArray(p.__data__) ? p.__data__.length : 0
                    };
                });
                
                return {
                    title: title,
                    paths: pathDetails
                };
            });
        }
        """
        
        results = await page.evaluate(js_inspect)
        await context.close()
        
        for idx, res in enumerate(results):
            print(f"Graph #{idx+1}: {res['title']}")
            print("-" * 60)
            for p_idx, p in enumerate(res['paths']):
                print(f"  Path {p_idx+1}: Class='{p['class']}', Stroke='{p['stroke']}', StrokeWidth='{p['strokeWidth']}', HasData={p['hasData']}, DataLen={p['dataLength']}")
            print()

if __name__ == "__main__":
    asyncio.run(main())
