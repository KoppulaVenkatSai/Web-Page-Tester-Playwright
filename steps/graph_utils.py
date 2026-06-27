import asyncio
from playwright.async_api import Page

JS_EXTRACT_FROM_MANAGER = """
() => {
    function isElementVisible(el, checkSize = true) {
        if (!el) return false;
        if (!el.isConnected) return false;
        if (checkSize) {
            const rect = el.getBoundingClientRect();
            if (rect.width <= 0 || rect.height <= 0) return false;
        }
        
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
    
    // Find all dashboard boxes
    const boxes = Array.from(document.querySelectorAll('.dashboard-box'));
    return boxes.map(box => {
        const header = box.querySelector('h3, h4, .box-header, .dashboard-box-header, label');
        const title = header ? header.innerText.trim() : 'Unknown';
        const visible = isElementVisible(box, true);
        
        // Find line paths inside this box
        const paths = Array.from(box.querySelectorAll('svg path.line'));
        let actualValues = null;
        let expectedValues = null;
        let actualSample = null;
        let expectedSample = null;
        
        const mapToValues = (arr) => {
            if (!Array.isArray(arr)) return null;
            return arr.map(d => {
                if (d === null || d === undefined) return null;
                if (typeof d === 'number') return d;
                if (typeof d === 'object') {
                    if (typeof d.y === 'number') return d.y;
                    if (typeof d.value === 'number') return d.value;
                    if (typeof d.val === 'number') return d.val;
                    if (typeof d.v === 'number') return d.v;
                    
                    const keys = Object.keys(d);
                    for (const k of keys) {
                        if (['x', 'date', 'time', 'timestamp', 'label'].includes(k.toLowerCase())) {
                            continue;
                        }
                        if (typeof d[k] === 'number') return d[k];
                        const num = parseFloat(d[k]);
                        if (!isNaN(num)) return num;
                    }
                }
                return parseFloat(d);
            }).filter(v => typeof v === 'number' && !isNaN(v));
        };
        
        paths.forEach(p => {
            if (!isElementVisible(p, false)) return; // Skip hidden/stale paths
            
            const stroke = p.getAttribute('stroke') || '';
            const computedStroke = window.getComputedStyle(p).stroke || '';
            const data = p.__data__;
            
            if (data && Array.isArray(data)) {
                const values = mapToValues(data);
                const color = stroke || computedStroke || '';
                const sample = data.slice(0, 2);
                
                if (color.includes('255, 127, 14') || color.includes('255,127,14')) {
                    if (!actualValues || (values && values.length > actualValues.length)) {
                        actualValues = values;
                        actualSample = sample;
                    }
                } else if (color.includes('31, 119, 180') || color.includes('31,119,180')) {
                    if (!expectedValues || (values && values.length > expectedValues.length)) {
                        expectedValues = values;
                        expectedSample = sample;
                    }
                }
            }
        });
        
        const debug_paths = paths.map(p => {
            const stroke = p.getAttribute('stroke') || '';
            const computedStroke = window.getComputedStyle(p).stroke || '';
            return {
                class: p.getAttribute('class') || '',
                stroke: stroke,
                computedStroke: computedStroke,
                dataLen: p.__data__ ? (Array.isArray(p.__data__) ? p.__data__.length : typeof p.__data__) : 0,
                dataType: p.__data__ ? (Array.isArray(p.__data__) ? 'array' : typeof p.__data__) : 'null/undefined',
                keys: p.__data__ ? Object.keys(p.__data__) : null,
                actualLen: actualValues ? actualValues.length : -1,
                expectedLen: expectedValues ? expectedValues.length : -1,
                actualType: actualValues ? typeof actualValues : 'none',
                actualSample: actualValues ? JSON.stringify(actualValues.slice(0, 3)) : ''
            };
        });
        
        return {
            title: title,
            actual: actualValues,
            expected: expectedValues,
            visible: visible,
            debug_paths: debug_paths,
            actual_sample: actualSample,
            expected_sample: expectedSample
        };
    });
}
"""

async def extract_graphs(page: Page, visible_only: bool = True) -> list:
    """
    Extracts actual and expected data points for graphs from the page.
    """
    graphs = await page.evaluate(JS_EXTRACT_FROM_MANAGER)
    if visible_only:
        return [g for g in graphs if g.get("visible")]
    return graphs

def print_graph_report(graphs: list) -> int:
    """
    Calculates and prints the mean value of actual/expected datasets for each graph
    along with the difference of the means in percentage.
    """
    print(f"\n==================================================")
    print(f"            GRAPH DATA EXTRACTION REPORT          ")
    print(f"==================================================\n")
    
    extracted_count = 0
    for g in graphs:
        title = g.get("title", "Unknown")
        actual = g.get("actual")
        expected = g.get("expected")
        
        if actual or expected:
            extracted_count += 1
            print(f"Graph #{extracted_count}: {title}")
            print("-" * 50)
            
            mean_act = None
            mean_exp = None
            
            if actual:
                print(f"Actual (len: {len(actual)}): {actual}")
                mean_act = sum(actual) / len(actual)
                print(f"Actual Mean: {mean_act:.4f}")
            else:
                print("Actual: No data points")
                
            if expected:
                print(f"Expected (len: {len(expected)}): {expected}")
                mean_exp = sum(expected) / len(expected)
                print(f"Expected Mean: {mean_exp:.4f}")
            else:
                print("Expected: No data points")
                
            if mean_act is not None and mean_exp is not None:
                diff = abs(mean_act - mean_exp)
                denom = max(abs(mean_exp), 1e-5)
                rel_diff = (diff / denom) * 100
                print(f"Absolute Difference of Means: {diff:.4f}")
                print(f"Relative Difference of Means: {rel_diff:.2f}%")
            else:
                print("Diff: N/A (requires both Actual and Expected series)")
            print("\n")

    print(f"==================================================")
    print(f"Successfully processed {extracted_count} graphs with data.")
    print(f"==================================================")
    return extracted_count
