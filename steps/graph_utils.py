import asyncio
from playwright.async_api import Page

JS_EXTRACT_FROM_MANAGER = """
() => {
    if (typeof window.globalCache === 'undefined') {
        return [];
    }
    
    // Find DigitalTwinManager in globalCache
    let twin = window.globalCache.getObject('digitalTwin1');
    if (!twin) {
        for (const key of Object.keys(window.globalCache)) {
            const obj = window.globalCache.getObject(key);
            if (obj && obj.constructor && obj.constructor.name === 'DigitalTwinManager') {
                twin = obj;
                break;
            }
        }
    }
    
    if (!twin || !twin.screensList) {
        return [];
    }
    
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
    
    return twin.screensList.map((s, idx) => {
        const title = s.screenName || 'Unknown';
        
        // Check visibility of the graph container
        const containerNode = (s.lineInstance && s.lineInstance.container && s.lineInstance.container.node) ? s.lineInstance.container.node() : null;
        let el = containerNode;
        if (!el && s.screenId) {
            el = document.getElementById(s.screenId) || document.querySelector('.' + s.screenId) || document.querySelector('[id*="' + s.screenId + '"]');
        }
        
        const visible = el ? isElementVisible(el) : false;
        
        const actualObj = s.data ? s.data.Actual : null;
        const expectedObj = s.data ? s.data.Expected : null;
        
        const actualValues = actualObj ? actualObj.map(d => typeof d.y !== 'undefined' ? d.y : d.value).filter(v => typeof v === 'number' && !isNaN(v)) : null;
        const expectedValues = expectedObj ? expectedObj.map(d => typeof d.y !== 'undefined' ? d.y : d.value).filter(v => typeof v === 'number' && !isNaN(v)) : null;
        
        const debug_paths = [];
        if (el) {
            const paths = Array.from(el.querySelectorAll('svg path.line'));
            paths.forEach((p, pIdx) => {
                debug_paths.push({
                    class: p.getAttribute('class') || '',
                    stroke: p.getAttribute('stroke') || '',
                    computedStroke: window.getComputedStyle(p).stroke || '',
                    dataLen: p.__data__ ? (Array.isArray(p.__data__) ? p.__data__.length : typeof p.__data__) : 0
                });
            });
        }
        
        return {
            title: title,
            actual: actualValues,
            expected: expectedValues,
            visible: visible,
            debug_paths: debug_paths
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
