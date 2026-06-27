import json
from playwright.async_api import Page

async def get_active_fault_codes(page: Page) -> list[str]:
    """
    Extracts the currently active fault codes from GWT cache or DOM scraping.
    """
    return await page.evaluate("""
        () => {
            function getTwin() {
                if (typeof window.globalCache === 'undefined') return null;
                const commonKeys = ['digitalTwin1', 'digital-twin-wrapper', 'digitalTwinManager'];
                for (const key of commonKeys) {
                    try {
                        const obj = window.globalCache.getObject(key);
                        if (obj && (obj.statusAnalysis || obj.screensList)) return obj;
                    } catch(e){}
                }
                try {
                    const keys = typeof window.globalCache.keys === 'function' ? window.globalCache.keys() : Object.keys(window.globalCache);
                    for (const key of keys) {
                        try {
                            const obj = window.globalCache.getObject(key);
                            if (obj && (obj.statusAnalysis || obj.screensList || obj.allFaults)) return obj;
                        } catch(e){}
                    }
                } catch(e){}
                return null;
            }

            const codes = new Set();

            // 1. Extract from GWT
            try {
                const twin = getTwin();
                if (twin && twin.statusAnalysis && twin.statusAnalysis.faults) {
                    twin.statusAnalysis.faults.forEach(f => {
                        if (f && f.fault_code) codes.add(f.fault_code);
                    });
                }
            } catch(e){}

            // 2. Extract from DOM
            try {
                function isInsideDropdown(el) {
                    if (!el) return false;
                    if (el.tagName === 'SELECT' || el.tagName === 'OPTION') return true;
                    let parent = el;
                    while (parent && parent !== document.body) {
                        const className = (parent.className || '').toString().toLowerCase();
                        const id = (parent.id || '').toString().toLowerCase();
                        if (className.includes('dropdown') || className.includes('select') || id.includes('dropdown') || id.includes('select')) {
                            return true;
                        }
                        parent = parent.parentElement;
                    }
                    return false;
                }

                // Check elements with text containing "Status:"
                const statusRegex = /Status:\s*(FCRST-[A-Z0-9]+-\d+)/i;
                const allEls = document.querySelectorAll('div, span, p, label, b, td, th');
                allEls.forEach(el => {
                    if (isInsideDropdown(el)) return;
                    const match = (el.innerText || '').match(statusRegex);
                    if (match) codes.add(match[1].trim());
                });

                // Check combined analysis container or similar
                const analysisRegex = /FCRST-[A-Z0-9]+-\d+/g;
                const analysisEls = document.querySelectorAll('.dt-combined-analysis, .fault-analysis, #fault-analysis, [class*="analysis"], [id*="analysis"]');
                analysisEls.forEach(container => {
                    if (isInsideDropdown(container)) return;
                    const text = container.innerText || '';
                    let match;
                    while ((match = analysisRegex.exec(text)) !== null) {
                        codes.add(match[0].trim());
                    }
                });

                // Check badges or buttons with fault code patterns
                const badgeRegex = /^FCRST-[A-Z0-9]+-\d+$/;
                const badgeEls = document.querySelectorAll('.badge, .btn, .label, .status, [class*="badge"], [class*="status"]');
                badgeEls.forEach(badge => {
                    if (isInsideDropdown(badge)) return;
                    const text = (badge.innerText || '').trim();
                    if (badgeRegex.test(text)) codes.add(text);
                });
            } catch(e){}

            return Array.from(codes);
        }
    """)

async def get_status_analysis(page: Page) -> dict | None:
    """
    Extracts the status analysis report data structure (Likely Fault, Causes, Observations, Recommendations).
    """
    return await page.evaluate("""
        () => {
            function getTwin() {
                if (typeof window.globalCache === 'undefined') return null;
                const commonKeys = ['digitalTwin1', 'digital-twin-wrapper', 'digitalTwinManager'];
                for (const key of commonKeys) {
                    try {
                        const obj = window.globalCache.getObject(key);
                        if (obj && (obj.statusAnalysis || obj.screensList)) return obj;
                    } catch(e){}
                }
                try {
                    const keys = typeof window.globalCache.keys === 'function' ? window.globalCache.keys() : Object.keys(window.globalCache);
                    for (const key of keys) {
                        try {
                            const obj = window.globalCache.getObject(key);
                            if (obj && (obj.statusAnalysis || obj.screensList || obj.allFaults)) return obj;
                        } catch(e){}
                    }
                } catch(e){}
                return null;
            }

            function getDOMStatusAnalysis() {
                const findTextAfterLabel = (label) => {
                    const els = Array.from(document.querySelectorAll('div, p, span, td, li'));
                    for (const el of els) {
                        const text = el.innerText || '';
                        const index = text.toLowerCase().indexOf(label.toLowerCase());
                        if (index !== -1) {
                            const val = text.substring(index + label.length).replace(/^[:\s\-]+/, '').trim();
                            if (val) return val;
                        }
                        if (index !== -1 && el.nextElementSibling) {
                            const nextText = el.nextElementSibling.innerText.trim();
                            if (nextText) return nextText;
                        }
                    }
                    return '';
                };

                const likelyFault = findTextAfterLabel('Likely Fault');
                const possibleCauses = findTextAfterLabel('Possible Causes');
                const observations = findTextAfterLabel('Observations Analysis');
                const recommendations = findTextAfterLabel('Recommendations');
                
                let fault_code = '';
                let fault_name = likelyFault;
                const match = likelyFault.match(/(FCRST-[A-Z0-9]+-\d+)/);
                if (match) {
                    fault_code = match[1];
                    fault_name = likelyFault.replace(/\s*\(\s*FCRST-[A-Z0-9]+-\d+\s*\)\s*/g, '').trim();
                }
                
                if (!fault_code) {
                    const badgeEls = document.querySelectorAll('.badge, .btn, .label, .status, [class*="badge"], [class*="status"]');
                    for (const badge of badgeEls) {
                        const text = (badge.innerText || '').trim();
                        if (/^FCRST-[A-Z0-9]+-\d+$/.test(text)) {
                            fault_code = text;
                            break;
                        }
                    }
                }

                if (!fault_code && !fault_name && !possibleCauses) {
                    return null;
                }

                return {
                    faults: [
                        {
                            fault_code: fault_code,
                            fault_name: fault_name,
                            possible_causes: possibleCauses,
                            observations: observations,
                            recommendations: recommendations
                        }
                    ]
                };
            }

            const twin = getTwin();
            const statusAnalysis = (twin && twin.statusAnalysis) ? twin.statusAnalysis : getDOMStatusAnalysis();
            const allFaults = (twin && twin.allFaults) ? twin.allFaults : null;
            
            return {
                statusAnalysis: statusAnalysis,
                allFaults: allFaults
            };
        }
    """)

async def run(page: Page) -> None:
    """
    Step 8: Retrieve and display the current active fault codes and status fields.
    """
    print("[~] Extracting active fault codes...")
    active_codes = await get_active_fault_codes(page)
    print(f"[+] Active fault codes: {active_codes}")
    
    print("[~] Extracting status analysis details...")
    analysis_data = await get_status_analysis(page)
    if analysis_data and analysis_data.get("statusAnalysis"):
        print("[+] Status Analysis details:")
        print(json.dumps(analysis_data.get("statusAnalysis"), indent=2))
    else:
        print("[-] No active status analysis data found on the page.")
