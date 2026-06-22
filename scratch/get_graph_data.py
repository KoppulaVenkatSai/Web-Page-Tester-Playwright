import asyncio
import os
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as playwright:
        profile_dir = os.path.join(os.getcwd(), "brave_profile")
        brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
        
        # Connect to the persistent profile
        context = await playwright.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            executable_path=brave_path,
            headless=False,
            no_viewport=True,
        )
        
        page = context.pages[0] if context.pages else await context.new_page()
        await page.wait_for_timeout(2000)
        
        js_extract = """
        () => {
            const activeWrapper = document.querySelector('.dt-observations-wrapper.active-view') || document;
            const visibleBoxes = Array.from(activeWrapper.querySelectorAll('.dashboard-box')).filter(box => {
                const rect = box.getBoundingClientRect();
                return rect.width > 0 && rect.height > 0;
            });
            
            if (visibleBoxes.length === 0) return { error: "No visible graphs found on page" };
            
            const box = visibleBoxes[0];
            const header = box.querySelector('h3, h4, .box-header, .dashboard-box-header, label');
            const title = header ? header.innerText.trim() : 'Unknown';
            
            const paths = Array.from(box.querySelectorAll('svg path'));
            let actual = null;
            let expected = null;
            
            paths.forEach(p => {
                const stroke = p.getAttribute('stroke') || '';
                const data = p.__data__;
                if (data && Array.isArray(data) && data.length > 0) {
                    const values = data.map(d => {
                        if (d && typeof d === 'object') {
                            return (typeof d.y !== 'undefined') ? d.y : d.value;
                        }
                        return d;
                    }).filter(v => typeof v === 'number' && !isNaN(v));
                    
                    if (stroke.includes('255, 127, 14') || stroke.includes('255,127,14')) {
                        actual = values;
                    } else if (stroke.includes('31, 119, 180') || stroke.includes('31,119,180')) {
                        expected = values;
                    }
                }
            });
            
            return {
                title: title,
                actual: actual,
                expected: expected
            };
        }
        """
        
        result = await page.evaluate(js_extract)
        await context.close()
        
        if "error" in result:
            print(f"Error: {result['error']}")
            return
            
        actual = result["actual"] or []
        expected = result["expected"] or []
        
        print(f"Graph Title: {result['title']}")
        print(f"\n--- Actual Values ({len(actual)} points) ---")
        print(actual)
        
        print(f"\n--- Expected Values ({len(expected)} points) ---")
        print(expected)
        
        if actual:
            mean_act = sum(actual) / len(actual)
            print(f"\nActual Mean: {mean_act:.4f}")
        else:
            mean_act = 0.0
            print("\nActual Mean: N/A (no data)")
            
        if expected:
            mean_exp = sum(expected) / len(expected)
            print(f"Expected Mean: {mean_exp:.4f}")
        else:
            mean_exp = 0.0
            print("Expected Mean: N/A (no data)")
            
        if actual and expected:
            diff = abs(mean_act - mean_exp)
            rel_diff = (diff / mean_exp) * 100 if mean_exp != 0 else 0.0
            print(f"Absolute Difference: {diff:.4f}")
            print(f"Relative Difference: {rel_diff:.2f}%")

if __name__ == "__main__":
    asyncio.run(run())
