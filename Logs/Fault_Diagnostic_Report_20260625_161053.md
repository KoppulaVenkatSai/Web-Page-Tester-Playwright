# AssetSense Fault Diagnostic Test Report

## Metadata
- **Test Date/Time**: `2026-06-25 16:10:53`
- **Last Updated**: `2026-06-25 16:16:56`
- **Elapsed Duration**: `6m 2s`
- **Target Asset**: `Steam Turbine Block - 1 (AS-FCRST-DT-01)`
- **Environment**: Playwright Test Runner (Brave Browser)

---

## Executive Summary
| Status | Count |
|---|---|
| ✅ Success | 0 |
| ❌ Fail / Timeout | 2 |
| **Total Tested** | **2** |

---

## Detailed Summary Table
| # | Fault Name | Fault Code | Status | Time to Detect | Time to Reset |
|---|---|---|---|---|---|
| 1 | HRH Terminal Attemperator Failure (R) | `FCRST-ME-012` | ❌ Fail | N/A | 16:13:53 |
| 2 | IP Seal Failure (R) | `FCRST-ME-005` | ❌ Fail | N/A | 16:16:56 |

---

## Diagnostic Logs per Fault Option

### 1. HRH Terminal Attemperator Failure (R) (`FCRST-ME-012`)
- **Status**: **❌ FAILURE**
- **Induced Time**: `2026-06-25 16:10:53`
- **Resolved Time**: `2026-06-25 16:13:53`

#### Event Timeline
- [16:10:53] Induced fault 'HRH Terminal Attemperator Failure (R)' (FCRST-ME-012).
- [16:11:03] Checked status. Active codes in state: []
- [16:11:13] Checked status. Active codes in state: []
- [16:11:23] Checked status. Active codes in state: []
- [16:11:33] Checked status. Active codes in state: []
- [16:11:43] Checked status. Active codes in state: []
- [16:11:53] Checked status. Active codes in state: []
- [16:12:03] Checked status. Active codes in state: ['FCRST-HY-002']
- [16:12:03] Incorrect fault code detected. Reduced max timeout to 120s.
- [16:12:13] Checked status. Active codes in state: ['FCRST-HY-002']
- [16:12:23] Checked status. Active codes in state: ['FCRST-HY-002']
- [16:12:34] Checked status. Active codes in state: ['FCRST-HY-002']
- [16:12:44] Checked status. Active codes in state: ['FCRST-HY-002']
- [16:12:54] Checked status. Active codes in state: ['FCRST-HY-002']
- [16:12:54] Timeout reached. Played chime sound.
- [16:12:58] Reset dropdown to Normal.
- [16:12:58] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:13:03] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:13:08] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:13:13] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:13:18] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:13:23] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:13:28] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:13:33] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:13:38] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:13:43] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:13:48] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:13:53] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [16:13:53] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Steam Pressure Loss",
      "possible_causes": "Steam pipe leak before HP inlet, Steam strainer blockage, Main steam stop valve failure, Piping pressure drops due to corrosion",
      "observations_analysis": "The observations indicate a decrease in steam flow and pressure at the HP turbine inlet, along with reduced power output across the turbines. These symptoms align with the context of steam pressure loss, suggesting issues such as leaks, blockages, or valve failures that could be causing the pressure drop.",
      "recommendations": "Conduct a thorough inspection of the steam pipes for leaks, check and clean the steam strainer, inspect the main steam stop valve for proper operation, and assess the piping for signs of corrosion that could be contributing to pressure drops.",
      "fault_code": "FCRST-HY-002",
      "analysis_flag": true
    }
  ]
}
```

---

### 2. IP Seal Failure (R) (`FCRST-ME-005`)
- **Status**: **❌ FAILURE**
- **Induced Time**: `2026-06-25 16:13:55`
- **Resolved Time**: `2026-06-25 16:16:56`

#### Event Timeline
- [16:13:55] Induced fault 'IP Seal Failure (R)' (FCRST-ME-005).
- [16:14:06] Checked status. Active codes in state: ['FCRST-00-000']
- [16:14:16] Checked status. Active codes in state: ['FCRST-00-000']
- [16:14:26] Checked status. Active codes in state: ['FCRST-00-000']
- [16:14:36] Checked status. Active codes in state: ['FCRST-00-000']
- [16:14:46] Checked status. Active codes in state: ['FCRST-00-000']
- [16:14:56] Checked status. Active codes in state: ['FCRST-00-000']
- [16:15:06] Checked status. Active codes in state: ['FCRST-HY-002']
- [16:15:06] Incorrect fault code detected. Reduced max timeout to 120s.
- [16:15:16] Checked status. Active codes in state: ['FCRST-HY-002']
- [16:15:26] Checked status. Active codes in state: ['FCRST-HY-002']
- [16:15:36] Checked status. Active codes in state: ['FCRST-HY-002']
- [16:15:46] Checked status. Active codes in state: ['FCRST-HY-002']
- [16:15:56] Checked status. Active codes in state: ['FCRST-HY-002']
- [16:15:56] Timeout reached. Played chime sound.
- [16:16:00] Reset dropdown to Normal.
- [16:16:00] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:16:05] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:16:10] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:16:15] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:16:20] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:16:25] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:16:30] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:16:35] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:16:40] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:16:46] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:16:51] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [16:16:56] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [16:16:56] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Steam Pressure Loss",
      "possible_causes": "Steam pipe leak before HP inlet, Steam strainer blockage, Main steam stop valve failure, Piping pressure drops due to corrosion",
      "observations_analysis": "The observations indicate a decrease in steam flow and pressure at the HP turbine inlet, along with reduced power output across the turbines. These symptoms align with the context of steam pressure loss, suggesting potential issues such as leaks, blockages, or valve failures that are causing the pressure drop.",
      "recommendations": "Conduct a thorough inspection of the steam pipes for leaks, check and clean the steam strainer, inspect the main steam stop valve for any malfunctions, and assess the piping for signs of corrosion that could be contributing to pressure drops.",
      "fault_code": "FCRST-HY-002",
      "analysis_flag": true
    }
  ]
}
```

---
