# AssetSense Fault Diagnostic Test Report

## Metadata
- **Test Date/Time**: `2026-06-27 13:53:09`
- **Last Updated**: `2026-06-27 13:55:09`
- **Elapsed Duration**: `2m 0s`
- **Target Asset**: `Steam Turbine Block - 1 (AS-FCRST-DT-01)`
- **Environment**: Playwright Test Runner (Brave Browser)

---

## Executive Summary
| Status | Count |
|---|---|
| ✅ Success | 1 |
| ❌ Fail / Timeout | 0 |
| **Total Tested** | **1** |

---

## Detailed Summary Table
| # | Fault Name | Fault Code | Status | Time to Detect | Time to Reset |
|---|---|---|---|---|---|
| 1 | HRH Terminal Attemperator Failure (R) | `FCRST-ME-012` | ✅ Success | 60.2s | 13:55:09 |

---

## Diagnostic Logs per Fault Option

### 1. HRH Terminal Attemperator Failure (R) (`FCRST-ME-012`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-27 13:53:09`
- **Resolved Time**: `2026-06-27 13:55:09`

#### Event Timeline
- [13:53:09] Induced fault 'HRH Terminal Attemperator Failure (R)' (FCRST-ME-012).
- [13:53:19] Checked status. Active codes in state: []
- [13:53:29] Checked status. Active codes in state: []
- [13:53:39] Checked status. Active codes in state: []
- [13:53:49] Checked status. Active codes in state: []
- [13:54:00] Checked status. Active codes in state: []
- [13:54:10] Checked status. Active codes in state: ['FCRST-ME-012']
- [13:54:14] Reset dropdown to Normal.
- [13:54:14] Alignment Phase - Checked status. Active codes: ['FCRST-ME-012']
- [13:54:19] Alignment Phase - Checked status. Active codes: ['FCRST-ME-012']
- [13:54:24] Alignment Phase - Checked status. Active codes: ['FCRST-ME-012']
- [13:54:29] Alignment Phase - Checked status. Active codes: ['FCRST-ME-012']
- [13:54:34] Alignment Phase - Checked status. Active codes: ['FCRST-ME-012']
- [13:54:39] Alignment Phase - Checked status. Active codes: ['FCRST-ME-012']
- [13:54:44] Alignment Phase - Checked status. Active codes: ['FCRST-ME-012']
- [13:54:49] Alignment Phase - Checked status. Active codes: ['FCRST-ME-012']
- [13:54:54] Alignment Phase - Checked status. Active codes: ['FCRST-ME-012']
- [13:54:59] Alignment Phase - Checked status. Active codes: ['FCRST-ME-012']
- [13:55:04] Alignment Phase - Checked status. Active codes: ['FCRST-ME-012']
- [13:55:09] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:55:09] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HRH Terminal Attemperator Failure",
      "possible_causes": "Reheater attemperator control valve stuck open, Spray water nozzle erosion in reheater line, Hot reheat spray control bypass leakage, Hot reheat temperature loop tuning failure",
      "observations_analysis": "The observations indicate a decrease in the power output of the intermediate pressure (IP) and low pressure (LP) turbines, as well as a reduction in the reheater heat duty and outlet temperature. These symptoms are consistent with a failure in the HRH terminal attemperator, which can lead to inadequate reheating of steam, thus affecting the efficiency and power output of the steam turbine.",
      "recommendations": "Inspect and repair or replace the reheater attemperator control valve if it is stuck open. Check for erosion in the spray water nozzles and replace if necessary. Investigate and fix any leakage in the hot reheat spray control bypass. Review and retune the hot reheat temperature control loop to ensure optimal performance.",
      "fault_code": "FCRST-ME-012",
      "analysis_flag": true
    }
  ]
}
```

---
