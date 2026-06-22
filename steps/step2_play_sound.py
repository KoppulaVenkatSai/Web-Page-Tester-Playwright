import os
import subprocess
import asyncio
from playwright.async_api import Page

async def run(page: Page) -> None:
    """
    Step 2: Monitor and detect when the Launchpad screen itself is visible.
    Checks every 5 seconds for up to 5 minutes (300 seconds) automatically.
    If not logged in/redirected, prompts the user and plays a system sound.
    """
    max_wait = 300
    check_interval = 5
    elapsed = 0
    prompted = False
    
    def play_sound():
        sound_path = "/System/Library/Sounds/Glass.aiff"
        if os.path.exists(sound_path):
            try:
                subprocess.Popen(["afplay", sound_path])
            except Exception:
                print("\a", end="", flush=True)
        else:
            print("\a", end="", flush=True)

    print("[~] Checking if Launchpad screen is visible (will check for up to 5 minutes)...")
    
    while elapsed < max_wait:
        try:
            # Check if launchpad elements are visible
            is_launchpad = await page.get_by_text("Digital Twin").first.is_visible()
            is_dt_module = await page.get_by_text("Steam Turbine Block - 1").first.is_visible()
            
            # Fallback checks: URL and Page Title
            current_url = page.url
            current_title = ""
            try:
                current_title = await page.title()
            except Exception:
                pass
                
            is_url_launchpad = "launchpad.html" in current_url
            is_title_launchpad = "launch pad" in current_title.lower() or "launchpad" in current_title.lower()
            
            # If any of these are true, we can see the launch pad screen
            if is_launchpad or is_dt_module or is_url_launchpad or is_title_launchpad:
                if elapsed == 0:
                    print("[+] Already logged in and Launchpad screen detected! Skipping login wait.")
                else:
                    print(f"[+] Launchpad screen detected after {elapsed}s! Resuming automation...")
                return
                
            # If not visible, check if we should display the prompt
            if not prompted:
                print("\n" + "*" * 60)
                print("ACTION REQUIRED: Please enter details and log in on the website now.")
                print("The script will automatically detect when you log in and resume.")
                print("*" * 60 + "\n")
                play_sound()
                prompted = True
            elif elapsed % 30 == 0:
                # Play reminder chime every 30 seconds if still not logged in
                play_sound()
                
        except Exception as e:
            print(f"[~] Error checking login/launchpad status: {e}")
            
        await asyncio.sleep(check_interval)
        elapsed += check_interval
        
    print("[-] Timeout: Launchpad screen was not detected within 5 minutes. Proceeding anyway...")
