import asyncio
from playwright.async_api import Page

async def run(page: Page) -> None:
    """
    Step 6: Waits until all visible D3 graphs have low difference between expected and actual values.
    """
    import sys
    import importlib
    if "steps.graph_utils" in sys.modules:
        importlib.reload(sys.modules["steps.graph_utils"])
    from steps.graph_utils import extract_graphs

    threshold = 0.05  # 5% relative difference threshold
    max_wait_seconds = 180  # Max time to wait (3 minutes)
    check_interval = 5  # Check every 5 seconds
    elapsed = 0

    print(f"Starting graph mean-value wait loop (checking every {check_interval}s up to {max_wait_seconds}s)...")

    while elapsed < max_wait_seconds:
        try:
            graphs = await extract_graphs(page, visible_only=True)
        except Exception as e:
            print(f"[-] Error evaluating JS graph scanner: {e}")
            await asyncio.sleep(check_interval)
            elapsed += check_interval
            continue
            
        if not graphs:
            print(f"[~] No visible graphs found yet. (Elapsed: {elapsed}s)")
            await asyncio.sleep(check_interval)
            elapsed += check_interval
            continue
            
        all_aligned = True
        active_comparisons = 0
        graphs_status = []
        
        for g in graphs:
            title = g.get('title', 'Unknown')
            actual_vals = g.get('actual')
            expected_vals = g.get('expected')
            
            if actual_vals is None or expected_vals is None:
                # Skip graphs that do not have both series (e.g. legend or single line)
                continue
                
            # If either array is empty, we must wait for simulation data
            if not actual_vals or not expected_vals:
                all_aligned = False
                graphs_status.append(f"  - '{title}': Waiting for data (Actual len: {len(actual_vals)}, Expected len: {len(expected_vals)}) [NOT ALIGNED]")
                active_comparisons += 1
                continue
                
            # Compute means
            mean_act = sum(actual_vals) / len(actual_vals)
            mean_exp = sum(expected_vals) / len(expected_vals)
            
            # Relative difference
            denom = max(abs(mean_exp), 1e-5)
            diff = abs(mean_act - mean_exp) / denom
            
            active_comparisons += 1
            is_graph_aligned = diff <= threshold
            
            status_str = f"Actual={mean_act:.2f}, Expected={mean_exp:.2f} (Diff: {diff*100:.1f}%)"
            if not is_graph_aligned:
                all_aligned = False
                graphs_status.append(f"  - '{title}': {status_str} [NOT ALIGNED]")
            else:
                graphs_status.append(f"  - '{title}': {status_str} [ALIGNED]")
                
        # Print status
        print(f"\n--- Checking graphs (Elapsed: {elapsed}s) ---")
        if active_comparisons == 0:
            print("[~] No active visible comparison series found yet (waiting for data)...")
            all_aligned = False
        else:
            not_aligned_count = len([s for s in graphs_status if 'NOT ALIGNED' in s])
            print(f"[~] {not_aligned_count} / {active_comparisons} graphs still not aligned:")
            for status in graphs_status:
                print(status)
                
            # Debug path details printing removed to reduce console clutter
                
        if all_aligned and active_comparisons > 0:
            print(f"\n[+] Success! All {active_comparisons} graphs are aligned within {threshold*100}% difference.")
            break
            
        await asyncio.sleep(check_interval)
        elapsed += check_interval

    if elapsed >= max_wait_seconds:
        print("[-] Timeout: Reached maximum wait time. Proceeding anyway...")
        
    print("Step 6 finished.")



