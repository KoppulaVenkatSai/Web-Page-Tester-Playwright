import asyncio
import json
import time
import os
import subprocess
import datetime
from playwright.async_api import Page

def play_chime():
    """Plays Mac system glass sound as a failure chime."""
    sound_path = "/System/Library/Sounds/Glass.aiff"
    if os.path.exists(sound_path):
        try:
            subprocess.Popen(["afplay", sound_path])
        except Exception:
            print("\a", end="", flush=True)
    else:
        print("\a", end="", flush=True)

def check_name_match(induced_name: str, active_name: str) -> bool:
    """
    Checks if the induced fault name matches the active fault name
    using a robust specific word overlap check, avoiding generic matches
    like 'Failure' and mismatched location markers.
    """
    ind = induced_name.lower().replace("(r)", "").strip()
    act = active_name.lower().replace("(r)", "").strip()
    
    if ind == act:
        return True
        
    if ind in act or act in ind:
        return True
        
    locations = {"hp", "ip", "lp", "hrh"}
    
    def get_words(s):
        return set(w.strip(",().-") for w in s.split() if w.strip(",().-"))
        
    ind_words = get_words(ind)
    act_words = get_words(act)
    
    # Verify location markers match
    ind_loc = ind_words & locations
    act_loc = act_words & locations
    if ind_loc != act_loc:
        return False
        
    generic = {"failure", "defect", "fault", "error", "problem", "issue", "block", "deviation", "r", "system"}
    ind_specific = ind_words - generic - locations
    act_specific = act_words - generic - locations
    
    # Check if there are conflicting modifiers
    modifiers = {"terminal", "interstage", "seal", "blade", "tube", "flow", "pressure", "vacuum", "fouling", "corrosion", "reheater", "superheater", "evaporator", "economizer", "feedwater"}
    ind_mods = ind_specific & modifiers
    act_mods = act_specific & modifiers
    if ind_mods and act_mods and ind_mods != act_mods:
        return False
        
    overlap = ind_specific & act_specific
    return len(overlap) > 0

async def wait_for_graphs_alignment(page: Page, actions_log: list, get_active_fault_codes, timeout_seconds=180, interval=5) -> bool:
    import sys
    import importlib
    if "steps.graph_utils" in sys.modules:
        importlib.reload(sys.modules["steps.graph_utils"])
    from steps.graph_utils import extract_graphs
    start_time = time.time()
    
    while time.time() - start_time < timeout_seconds:
        # Retrieve active fault codes and log them to the event timeline during alignment
        try:
            active_codes = await get_active_fault_codes(page)
            check_time = datetime.datetime.now().strftime("%H:%M:%S")
            actions_log.append(f"[{check_time}] Alignment Phase - Checked status. Active codes: {active_codes}")
            print(f"    [{check_time}] Alignment Phase - Active fault codes: {active_codes}")
        except Exception as e:
            pass

        try:
            graphs = await extract_graphs(page, visible_only=True)
        except Exception as e:
            print(f"    [~] Error extracting graphs during alignment: {e}")
            await asyncio.sleep(interval)
            continue
            
        if not graphs:
            await asyncio.sleep(interval)
            continue
            
        all_aligned = True
        active_comparisons = 0
        not_aligned_list = []
        
        # Ensure active fault codes are cleared (Normal) before asserting alignment is complete
        has_active_fault = False
        for c in active_codes:
            if c != "FCRST-00-000" and c != "":
                has_active_fault = True
                break
                
        if has_active_fault:
            all_aligned = False
            not_aligned_list.append("Active fault codes still present (not yet returned to Normal)")
        
        for g in graphs:
            title = g.get('title', 'Unknown')
            actual_vals = g.get('actual')
            expected_vals = g.get('expected')
            
            if actual_vals is None or expected_vals is None:
                continue
            if not actual_vals or not expected_vals:
                all_aligned = False
                active_comparisons += 1
                not_aligned_list.append(f"'{title}': Waiting for data (Actual len: {len(actual_vals) if actual_vals else 0}, Expected len: {len(expected_vals) if expected_vals else 0})")
                continue
                
            mean_act = sum(actual_vals) / len(actual_vals)
            mean_exp = sum(expected_vals) / len(expected_vals)
            diff = abs(mean_act - mean_exp) / max(abs(mean_exp), 1e-5)
            
            active_comparisons += 1
            if diff > 0.05:
                all_aligned = False
                not_aligned_list.append(f"'{title}': Diff={diff*100:.2f}% (Actual={mean_act:.2f}, Expected={mean_exp:.2f}) [Len: {len(actual_vals)} / {len(expected_vals)}] [Sample: {g.get('actual_sample')}]")
                
        if all_aligned and active_comparisons > 0:
            return True
            
        # Print status of not aligned graphs
        elapsed_sec = int(time.time() - start_time)
        print(f"    [~] Alignment check (Elapsed: {elapsed_sec}s): {len(not_aligned_list)} / {active_comparisons} graphs still not aligned.")
        for msg in not_aligned_list[:5]:  # print up to 5 not aligned
            print(f"        - {msg}")
        if len(not_aligned_list) > 5:
            print(f"        - ... and {len(not_aligned_list) - 5} more")
            
        await asyncio.sleep(interval)
        
    return False

def write_diagnostic_report(report_path, test_results, overall_start_time, overall_end_time=None):
    """Generates and writes a beautiful markdown report of all test results so far."""
    if overall_end_time is None:
        overall_end_time = datetime.datetime.now()
    total_elapsed = (overall_end_time - overall_start_time).total_seconds()
    
    success_count = len([r for r in test_results if r['status'] == 'Success'])
    fail_count = len([r for r in test_results if r['status'] == 'Failure'])
    
    report_md = f"""# AssetSense Fault Diagnostic Test Report

## Metadata
- **Test Date/Time**: `{overall_start_time.strftime('%Y-%m-%d %H:%M:%S')}`
- **Last Updated**: `{overall_end_time.strftime('%Y-%m-%d %H:%M:%S')}`
- **Elapsed Duration**: `{int(total_elapsed // 60)}m {int(total_elapsed % 60)}s`
- **Target Asset**: `Steam Turbine Block - 1 (AS-FCRST-DT-01)`
- **Environment**: Playwright Test Runner (Brave Browser)

---

## Executive Summary
| Status | Count |
|---|---|
| ✅ Success | {success_count} |
| ❌ Fail / Timeout | {fail_count} |
| **Total Tested** | **{len(test_results)}** |

---

## Detailed Summary Table
| # | Fault Name | Fault Code | Status | Time to Detect | Time to Reset |
|---|---|---|---|---|---|
"""
    
    for r in test_results:
        status_icon = "✅ Success" if r["status"] == "Success" else "❌ Fail"
        dur_str = f"{r['duration']:.1f}s" if r["duration"] is not None else "N/A"
        report_md += f"| {r['index']} | {r['name']} | `{r['code']}` | {status_icon} | {dur_str} | {r['resolved_time'].split()[-1]} |\n"

    report_md += "\n---\n\n## Diagnostic Logs per Fault Option\n"
    
    for r in test_results:
        status_icon = "✅ SUCCESS" if r["status"] == "Success" else "❌ FAILURE"
        report_md += f"""
### {r['index']}. {r['name']} (`{r['code']}`)
- **Status**: **{status_icon}**
- **Induced Time**: `{r['induced_time']}`
- **Resolved Time**: `{r['resolved_time']}`

#### Event Timeline
"""
        for act in r["actions_log"]:
            report_md += f"- {act}\n"

        report_md += f"""
#### JSON Response Details
```json
{json.dumps(r['json'], indent=2) if r['json'] else "N/A"}
```
"""
            
        report_md += "\n---\n"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_md)

async def run(page: Page) -> None:
    """
    Step 7: Sequential Fault Testing.
    Induces each fault, waits up to 120s (checking every 10s) for the status analysis
    to match the induced code, chimes on timeout/failure, resets to Normal,
    waits up to 3 mins for graph averages to align, and generates a detailed report.
    """
    print("Waiting for page load...")
    try:
        await page.wait_for_load_state("networkidle", timeout=5000)
    except Exception:
        pass

    print("Locating 'Induce Fault:' dropdown...")
    label_locator = page.locator("text=Induce Fault")
    try:
        await label_locator.first.wait_for(state="visible", timeout=15000)
    except Exception:
        print("[-] Error: Could not find 'Induce Fault' text on the page.")
        return

    label_element = label_locator.first
    parent = label_element.locator("xpath=..")
    
    select_element = parent.locator("select")
    is_standard_select = await select_element.count() > 0
    
    options = []
    
    if is_standard_select:
        print("[~] Detected a standard HTML <select> dropdown.")
        select = select_element.first
        options_locator = select.locator("option")
        count = await options_locator.count()
        for i in range(count):
            opt = options_locator.nth(i)
            text = await opt.inner_text()
            val = await opt.get_attribute("value") or ""
            options.append((text.strip(), val.strip()))
    else:
        print("[~] Custom dropdown detected. Attempting to expand it to read options...")
        trigger = parent.locator("button, input, [role='combobox'], .dropdown-toggle, span, div").first
        if await trigger.count() == 0:
            trigger = label_element
        await trigger.click()
        await page.wait_for_timeout(1000)
        
        options_locator = page.locator("[role='option'], .dropdown-item, .option, li")
        count = await options_locator.count()
        for i in range(count):
            opt = options_locator.nth(i)
            if await opt.is_visible():
                text = await opt.inner_text()
                options.append((text.strip(), text.strip()))
        await trigger.click()

    if not options:
        print("[-] Error: No options found in the dropdown.")
        return

    print(f"[+] Found {len(options)} total options in dropdown.")

    # Find the Normal option
    normal_opt = None
    normal_val = "FCRST-00-000"
    for text, val in options:
        if val == "FCRST-00-000" or text.lower() == "normal":
            normal_opt = (text, val)
            normal_val = val
            break
    if not normal_opt:
        normal_opt = options[0]
        normal_val = options[0][1]

    # Faults are options that are not Normal and not placeholders
    fault_options = []
    for idx, (text, val) in enumerate(options):
        if val == normal_val or text.lower() == "normal":
            continue
        if any(k in text.lower() for k in ["select", "choose", "none", "please", "---"]):
            continue
        fault_options.append((idx, text, val))

    print(f"[+] Identified {len(fault_options)} faults to test sequentially.")

    # Check for previous failed faults in the most recent diagnostic report
    try:
        import glob
        import re
        report_files = sorted(glob.glob(os.path.join("Logs", "Fault_Diagnostic_Report_*.md")))
        if report_files:
            latest_report = report_files[-1]
            failed_codes = set()
            with open(latest_report, "r", encoding="utf-8") as f:
                report_content = f.read()
            for line in report_content.splitlines():
                if "|" in line and "❌" in line:
                    match = re.search(r"`(FCRST-[A-Z0-9]+-\d+)`", line)
                    if match:
                        failed_codes.add(match.group(1))
            
            if failed_codes:
                print(f"\n[~] Found recent report: {latest_report}")
                print(f"[~] Recently failed faults ({len(failed_codes)}): {list(failed_codes)}")
                # Ask user via console input
                user_ans = await asyncio.to_thread(
                    input,
                    "Do you want to ONLY run these recently failed faults? (y/N): "
                )
                if user_ans.strip().lower() in ("y", "yes"):
                    filtered_options = [fo for fo in fault_options if fo[2] in failed_codes]
                    if filtered_options:
                        fault_options = filtered_options
                        print(f"[+] Filtered to run only {len(fault_options)} failed faults.")
                    else:
                        print("[-] None of the failed faults match current dropdown options. Running all faults.")
    except Exception as e:
        print(f"[-] Error checking for recently failed faults: {e}")

    async def select_option(opt_text, opt_val):
        if is_standard_select:
            await select.select_option(value=opt_val)
        else:
            trigger = parent.locator("button, input, [role='combobox'], .dropdown-toggle, span, div").first
            if await trigger.count() == 0:
                trigger = label_element
            await trigger.click()
            await page.wait_for_timeout(500)
            options_locator = page.locator("[role='option'], .dropdown-item, .option, li")
            count = await options_locator.count()
            for i in range(count):
                opt = options_locator.nth(i)
                opt_text_cur = await opt.inner_text()
                if opt_text_cur.strip() == opt_text:
                    await opt.click()
                    break
            await page.wait_for_timeout(500)

    from steps.step8_get_status_fields import get_active_fault_codes, get_status_analysis

    test_results = []
    overall_start_time = datetime.datetime.now()
    
    # Generate report path with timestamp once
    os.makedirs("Logs", exist_ok=True)
    timestamp_str = overall_start_time.strftime("%Y%m%d_%H%M%S")
    report_path = f"Logs/Fault_Diagnostic_Report_{timestamp_str}.md"

    for i, (orig_idx, name, code) in enumerate(fault_options, 1):
        print(f"\n==================================================")
        print(f" TESTING FAULT {i}/{len(fault_options)}: {name} (Code: {code})")
        print(f"==================================================")

        induced_time = datetime.datetime.now()
        actions_log = []
        status_str = "Failure"
        detection_duration = None
        ui_analysis_text = ""
        analysis_details = None

        # 1. Induce the fault
        print(f"[{induced_time.strftime('%H:%M:%S')}] Selecting dropdown option '{name}'...")
        actions_log.append(f"[{induced_time.strftime('%H:%M:%S')}] Induced fault '{name}' ({code}).")
        await select_option(name, code)

        # 2. Wait up to 120s/180s (checking status every 10s, letting webpage update automatically)
        check_interval = 10.0
        max_duration = 180.0  # Default to 180 seconds if no response comes
        elapsed = 0.0
        success = False

        print(f"[~] Monitoring bottom Fault Analysis section every {check_interval}s...")
        
        while elapsed < max_duration:
            # Sleep the interval
            await asyncio.sleep(check_interval)
            elapsed += check_interval
            
            # Read state
            active_codes = await get_active_fault_codes(page)
            check_time = datetime.datetime.now().strftime("%H:%M:%S")
            actions_log.append(f"[{check_time}] Checked status. Active codes in state: {active_codes}")
            print(f"    [{check_time}] Active fault codes detected: {active_codes}")
            
            # Retrieve status analysis details to check name similarity if code differs
            analysis_data = await get_status_analysis(page)
            if analysis_data:
                analysis_details = analysis_data.get("statusAnalysis")
                
            matched = False
            if code in active_codes:
                matched = True
            elif analysis_details and "faults" in analysis_details:
                for f in analysis_details["faults"]:
                    active_name = f.get("fault_name") or f.get("likely_fault") or ""
                    active_code = f.get("fault_code") or ""
                    
                    if check_name_match(name, active_name):
                        matched = True
                        print(f"    [~] Mapped induced fault '{name}' to active fault '{active_name}' (Code: {active_code}) via name overlap.")
                        actions_log.append(f"[{check_time}] Mapped induced fault '{name}' to active fault '{active_name}' (Code: {active_code}) via name overlap.")
                        break

            if matched:
                success = True
                status_str = "Success"
                detection_duration = (datetime.datetime.now() - induced_time).total_seconds()
                
                try:
                    ui_analysis_text = await page.locator(".dt-combined-analysis").inner_text()
                except Exception as e:
                    ui_analysis_text = f"Error reading DOM: {e}"
                
                print(f"[+] SUCCESS: Fault detected correctly in {detection_duration:.1f}s.")
                break

            # If we get any fault response that is incorrect, limit/keep the timeout to 120s
            has_incorrect = False
            for c in active_codes:
                if c != "FCRST-00-000" and c != code:
                    # check if this code matches the induced name via name overlap
                    matched_this = False
                    if analysis_details and "faults" in analysis_details:
                        for f in analysis_details["faults"]:
                            if f.get("fault_code") == c:
                                active_name = f.get("fault_name") or f.get("likely_fault") or ""
                                if check_name_match(name, active_name):
                                    matched_this = True
                                    break
                    if not matched_this:
                        has_incorrect = True
                        break
                        
            if has_incorrect and max_duration != 120.0:
                print(f"    [~] Incorrect fault code detected. Reducing max wait timeout to 120s.")
                actions_log.append(f"[{check_time}] Incorrect fault code detected. Reduced max timeout to 120s.")
                max_duration = 120.0

        if not success:
            print(f"[-] FAILURE / TIMEOUT: Fault {code} not detected within {max_duration}s.")
            actions_log.append(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Timeout reached. Played chime sound.")
            play_chime()
            
            # Retrieve whatever incorrect response was present at timeout
            try:
                analysis_data = await get_status_analysis(page)
                if analysis_data:
                    analysis_details = analysis_data.get("statusAnalysis")
            except Exception as e:
                print(f"    [~] Error capturing timeout JSON response: {e}")

        # Pause to visually observe
        await asyncio.sleep(4.0)

        # 3. Reset to Normal and Wait for Graph Alignment (Averages to go low again)
        reset_time = datetime.datetime.now()
        print(f"[{reset_time.strftime('%H:%M:%S')}] Resetting status to Normal...")
        actions_log.append(f"[{reset_time.strftime('%H:%M:%S')}] Reset dropdown to Normal.")
        await select_option(normal_opt[0], normal_opt[1])

        print("[~] Waiting for graph actual/expected averages to align back to normal (Max 3 mins)...")
        aligned = await wait_for_graphs_alignment(page, actions_log, get_active_fault_codes, timeout_seconds=180, interval=5)
        
        aligned_time = datetime.datetime.now()
        if aligned:
            print(f"[{aligned_time.strftime('%H:%M:%S')}] Graphs successfully aligned.")
            actions_log.append(f"[{aligned_time.strftime('%H:%M:%S')}] Graphs successfully aligned back to Normal.")
        else:
            print(f"[{aligned_time.strftime('%H:%M:%S')}] Warning: Graphs did not fully align within 3 mins.")
            actions_log.append(f"[{aligned_time.strftime('%H:%M:%S')}] Warning: Graphs did not fully align within 3 mins.")

        # Store test result
        test_results.append({
            "index": i,
            "name": name,
            "code": code,
            "status": status_str,
            "duration": detection_duration,
            "induced_time": induced_time.strftime("%Y-%m-%d %H:%M:%S"),
            "resolved_time": aligned_time.strftime("%Y-%m-%d %H:%M:%S"),
            "actions_log": actions_log,
            "ui_text": ui_analysis_text,
            "json": analysis_details
        })
        
        # DYNAMIC REPORT UPDATE: Update the report file immediately after this iteration finishes
        write_diagnostic_report(report_path, test_results, overall_start_time)
        print(f"[+] Dynamic Report updated: {report_path}")
        
        await asyncio.sleep(2.0)

    print("\n==================================================")
    print(f"Completed sequential testing of all {len(fault_options)} faults.")
    print("==================================================")
