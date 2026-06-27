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
        
        print("[~] Starting browser and navigating to Digital Twin...")
        context, page = await step1_open_browser.run(playwright, target_url)
        await step2_play_sound.run(page)
        await step3_click_digital_twin.run(page)
        await step4_click_asset.run(page)
        await step5_simulation_mode.run(page)
        
        from steps.graph_utils import extract_graphs, print_graph_report
        
        print("[~] Starting 5-second polling loop for visible graph data...")
        max_attempts = 24  # 2 minutes maximum
        attempt = 0
        graphs = []
        
        while attempt < max_attempts:
            graphs = await extract_graphs(page, visible_only=True)
            
            # Check if all visible graphs have both actual and expected data points
            all_ready = True
            if not graphs:
                all_ready = False
            else:
                for g in graphs:
                    act_len = len(g["actual"]) if g["actual"] is not None else 0
                    exp_len = len(g["expected"]) if g["expected"] is not None else 0
                    if act_len == 0 or exp_len == 0:
                        all_ready = False
                        break
            
            if all_ready:
                print(f"[+] Data detected for all visible graphs after {attempt * 5}s!")
                break
                
            print(f"[~] Waiting for data... (Elapsed: {attempt * 5}s)")
            await asyncio.sleep(5)
            attempt += 1
            
        print("[~] Performing final extraction...")
        all_graphs = await extract_graphs(page, visible_only=False)
        await context.close()
        print("[+] Browser closed.")
        
        print_graph_report(all_graphs)

if __name__ == "__main__":
    asyncio.run(main())

