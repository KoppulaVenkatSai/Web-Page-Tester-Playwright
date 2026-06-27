import asyncio
import os
import sys
from playwright.async_api import async_playwright

# Add current directory to path so we can import steps
sys.path.append(os.getcwd())

from steps import step1_open_browser
from steps import step2_play_sound
from steps import step3_click_digital_twin
from steps import step4_click_asset
from steps import step5_simulation_mode

async def main():
    async with async_playwright() as playwright:
        target_url = "https://qa73.assetsense.com/c2/launchpad.html"
        
        print("[~] Starting browser and navigating...")
        context, page = await step1_open_browser.run(playwright, target_url)
        await step2_play_sound.run(page)
        await step3_click_digital_twin.run(page)
        await step4_click_asset.run(page)
        await step5_simulation_mode.run(page)
        
        print("Waiting 5 seconds for graphs to load data...")
        await page.wait_for_timeout(5000)
        
        js_inspect_visibility = """
        () => {
            if (typeof window.globalCache === 'undefined') {
                return { error: 'globalCache is not defined' };
            }
            
            // Find DigitalTwinManager in globalCache
            let twin = null;
            for (const key of Object.keys(window.globalCache)) {
                // If it is an internal store, search its values
                // But globalCache has getObject, so we query candidates
            }
            
            // We know 'digitalTwin1' is the key from our previous inspection
            twin = window.globalCache.getObject('digitalTwin1');
            if (!twin) return { error: 'digitalTwin1 manager not found' };
            
            const screens = twin.screensList;
            if (!screens || !Array.isArray(screens)) return { error: 'screensList is not an array' };
            
            function isElementVisible(el) {
                if (!el) return false;
                const rect = el.getBoundingClientRect();
                if (rect.width <= 0 || rect.height <= 0) return false;
                
                let parent = el;
                while (parent && parent !== document.body) {
                    const style = window.getComputedStyle(parent);
                    if (style.display === 'none' || style.visibility === 'hidden' || style.opacity === '0') {
                        return false;
                    }
                    parent = parent.parentElement;
                }
                return true;
            }
            
            return screens.map((s, idx) => {
                const containerNode = (s.lineInstance && s.lineInstance.container && s.lineInstance.container.node) ? s.lineInstance.container.node() : null;
                
                let el = containerNode;
                if (!el && s.screenId) {
                    el = document.getElementById(s.screenId) || document.querySelector('.' + s.screenId) || document.querySelector('[id*="' + s.screenId + '"]');
                }
                
                const visible = el ? isElementVisible(el) : false;
                
                const actualObj = s.data ? s.data.Actual : null;
                const expectedObj = s.data ? s.data.Expected : null;
                
                const actualLen = actualObj ? (Array.isArray(actualObj) ? actualObj.length : 0) : 0;
                const expectedLen = expectedObj ? (Array.isArray(expectedObj) ? expectedObj.length : 0) : 0;
                
                return {
                    index: idx,
                    screenId: s.screenId,
                    screenName: s.screenName,
                    hasContainerNode: !!containerNode,
                    hasFallbackElement: !!el,
                    visible: visible,
                    actualLen: actualLen,
                    expectedLen: expectedLen
                };
            });
        }
        """
        
        try:
            result = await page.evaluate(js_inspect_visibility)
            import pprint
            # Filter and print only visible screens
            visible_screens = [r for r in result if isinstance(r, dict) and r.get('visible')]
            print(f"\nFound {len(visible_screens)} visible screens out of {len(result)} total screens:")
            pprint.pprint(visible_screens)
            
            print("\nSample of non-visible screens (first 3):")
            non_visible = [r for r in result if isinstance(r, dict) and not r.get('visible')]
            pprint.pprint(non_visible[:3])
        except Exception as e:
            print(f"Error: {e}")
            
        await context.close()

if __name__ == "__main__":
    asyncio.run(main())
