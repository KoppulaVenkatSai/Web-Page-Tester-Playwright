import asyncio
from playwright.async_api import Page

async def run(page: Page) -> None:
    """
    Step 6: Waits until all visible D3 graphs have low difference between expected and actual values.
    """
    print("Waiting for page and graphs to initialize...")
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
                
            # Print debug path details for up to 3 non-aligned graphs
            printed_debug = 0
            for g in graphs:
                title = g.get('title', 'Unknown')
                actual_vals = g.get('actual')
                expected_vals = g.get('expected')
                debug_paths = g.get('debug_paths', [])
                
                is_not_aligned = False
                if actual_vals is None or expected_vals is None:
                    continue
                if not actual_vals or not expected_vals:
                    is_not_aligned = True
                else:
                    mean_act = sum(actual_vals) / len(actual_vals)
                    mean_exp = sum(expected_vals) / len(expected_vals)
                    denom = max(abs(mean_exp), 1e-5)
                    diff = abs(mean_act - mean_exp) / denom
                    if diff > threshold:
                        is_not_aligned = True
                        
                if is_not_aligned and printed_debug < 3:
                    print(f"\n[DEBUG] Path details for '{title}':")
                    for p_idx, p in enumerate(debug_paths):
                        print(f"  Path {p_idx+1}: Class='{p['class']}', Stroke='{p['stroke']}', ComputedStroke='{p['computedStroke']}', DataLen={p['dataLen']}, DataType='{p.get('dataType')}', Keys={p.get('keys')}")
                    printed_debug += 1
                
        if all_aligned and active_comparisons > 0:
            print(f"\n[+] Success! All {active_comparisons} graphs are aligned within {threshold*100}% difference.")
            break
            
        await asyncio.sleep(check_interval)
        elapsed += check_interval

    if elapsed >= max_wait_seconds:
        print("[-] Timeout: Reached maximum wait time. Proceeding anyway...")
        
    print("Step 6 finished.")



