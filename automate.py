import asyncio
import os
import sys
import glob
import importlib
import traceback
from playwright.async_api import async_playwright
from steps import step1_open_browser
from steps import step2_play_sound

async def run_step(step_num: int, page, *args, **kwargs) -> bool:
    """
    Dynamically searches, imports/reloads, and runs a step file by its number.
    e.g., 'r 3' looks for steps/step3_*.py, reloads it, and calls module.run(page, *args, **kwargs)
    """
    # Find any file starting with step{step_num}_ in the steps directory
    pattern = os.path.join("steps", f"step{step_num}_*.py")
    matching_files = glob.glob(pattern)
    
    if not matching_files:
        print(f"[-] No file found matching step {step_num} (e.g., steps/step{step_num}_*.py)")
        return False
        
    filepath = matching_files[0]
    # Convert file path to module import path (e.g. steps.step3_click_digital_twin)
    module_path = filepath.replace("/", ".").replace("\\", ".").replace(".py", "")
    
    print(f"[~] Loading/Reloading module {module_path}...")
    try:
        if "steps.graph_utils" in sys.modules:
            importlib.reload(sys.modules["steps.graph_utils"])
            
        if module_path in sys.modules:
            # Hot-reload the module so code changes take effect immediately
            module = importlib.reload(sys.modules[module_path])
        else:
            module = importlib.import_module(module_path)
            
        print(f"[+] Running Step {step_num}...")
        res = await module.run(page, *args, **kwargs)
        if isinstance(res, bool):
            return res
        return True
    except Exception as e:
        print(f"[-] Error executing Step {step_num}: {e}")
        traceback.print_exc()
        return False

async def main():
    async with async_playwright() as playwright:
        target_url = "https://qa73.assetsense.com/c2/launchpad.html"
        
        # 1. Run Step 1 (Open Browser)
        context, page = await step1_open_browser.run(playwright, target_url)
        print("[+] Step 1 completed: Brave Browser launched and page loaded.")
        
        # 2. Run Step 2 (Play sound & wait for user login)
        await step2_play_sound.run(page)
        print("[+] Step 2 completed: User logged in.")
        
        # 3. Load ECNs to test from configuration
        from config import BaseConfig
        ecns_to_test = getattr(BaseConfig, "ecns_to_test", [])
        print(f"[+] Loaded ECNs to test: {ecns_to_test}")
        
        for ecn in ecns_to_test:
            print(f"\n==================================================")
            print(f" STARTING TEST PROCESS FOR ASSET ECN: {ecn}")
            print(f"==================================================")
            
            # Navigate back to Launchpad page to ensure a clean start
            print(f"[~] Navigating to Launchpad URL...")
            await page.goto(target_url)
            
            # Run Step 3 (Click Digital Twin)
            step3_success = await run_step(3, page)
            if not step3_success:
                print(f"[-] Step 3 (Digital Twin) failed for ECN {ecn}. Skipping this asset.")
                continue
                
            # Run Step 4 (Click Asset ECN)
            asset_found = await run_step(4, page, ecn=ecn)
            if not asset_found:
                print(f"[-] Asset ECN '{ecn}' not found in options. Moving to next ECN.")
                continue
                
            # Run the remaining steps for this asset
            print(f"[+] Asset '{ecn}' loaded successfully. Running remaining steps...")
            
            # Step 5: Simulation Mode
            await run_step(5, page)
            # Step 6: Wait Graphs
            await run_step(6, page)
            # Step 7: Induce Fault
            await run_step(7, page, ecn=ecn)
            # Step 8: Get Status Fields
            await run_step(8, page)
            
            print(f"[+] Finished test process for asset ECN: {ecn}")
        
        # 4. Enter Interactive Hot-Reload Console Loop
        print("\n" + "="*50)
        print("  INTERACTIVE CONTROL CONSOLE ACTIVE")
        print("="*50)
        print("Commands:")
        print("  r <num>  - Reload and run step <num> (e.g., 'r 3' or 'r 4')")
        print("  status   - Print the current page URL and title")
        print("  exit     - Close browser and exit")
        print("="*50)
        
        try:
            while True:
                # Ask user for command asynchronously so it doesn't freeze browser
                cmd = await asyncio.to_thread(
                    input, 
                    "\nConsole > "
                )
                cmd = cmd.strip()
                if not cmd:
                    continue
                    
                cmd_parts = cmd.split()
                primary_cmd = cmd_parts[0].lower()
                
                if primary_cmd == "exit":
                    break
                elif primary_cmd == "status":
                    print(f"Current URL: {page.url}")
                    print(f"Current Title: {await page.title()}")
                elif primary_cmd == "r" and len(cmd_parts) > 1:
                    try:
                        num = int(cmd_parts[1])
                        await run_step(num, page)
                    except ValueError:
                        print("[-] Please enter a valid step number. Example: 'r 4'")
                else:
                    print("[-] Unknown command. Available: 'r <num>', 'status', 'exit'")
                    
        except KeyboardInterrupt:
            print("\nExiting interactive loop...")
        finally:
            await context.close()
            print("Browser closed.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nSession stopped.")
