# AssetSense Fault Diagnostic Test Report

## Metadata
- **Test Date/Time**: `2026-06-25 15:50:27`
- **Last Updated**: `2026-06-25 15:56:25`
- **Elapsed Duration**: `5m 57s`
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
| 1 | HRH Terminal Attemperator Failure (R) | `FCRST-ME-012` | ❌ Fail | N/A | 15:53:23 |
| 2 | IP Seal Failure (R) | `FCRST-ME-005` | ❌ Fail | N/A | 15:56:25 |

---

## Diagnostic Logs per Fault Option

### 1. HRH Terminal Attemperator Failure (R) (`FCRST-ME-012`)
- **Status**: **❌ FAILURE**
- **Induced Time**: `2026-06-25 15:50:27`
- **Resolved Time**: `2026-06-25 15:53:23`

#### Event Timeline
- [15:50:27] Induced fault 'HRH Terminal Attemperator Failure (R)' (FCRST-ME-012).
- [15:50:37] Checked status. Active codes in state: []
- [15:50:47] Checked status. Active codes in state: []
- [15:50:57] Checked status. Active codes in state: []
- [15:51:07] Checked status. Active codes in state: []
- [15:51:17] Checked status. Active codes in state: []
- [15:51:27] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:51:27] Incorrect fault code detected. Reduced max timeout to 120s.
- [15:51:38] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:51:48] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:51:58] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:52:08] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:52:18] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:52:28] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:52:28] Timeout reached. Played chime sound.
- [15:52:32] Reset dropdown to Normal.
- [15:52:32] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:52:37] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:52:42] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:52:47] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:52:52] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:52:57] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:53:02] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:53:07] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:53:12] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:53:17] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:53:22] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:53:23] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HP Seal Failure",
      "possible_causes": "Gland seal wear on HP casing outer shaft, HP stage-to-stage labyrinth seal wear, Excessive shaft vibration damaging HP seals, Thermal transient casing distortion",
      "observations_analysis": "The observations indicate a decrease in power output across the HP, IP, and LP turbines, as well as a reduction in steam turbine net power and reheater heat duty. These symptoms align with the effects of an HP Seal Failure, where the integrity of the seals is compromised, leading to inefficiencies in steam flow and energy conversion.",
      "recommendations": "Inspect and replace worn gland seals and labyrinth seals on the HP casing. Monitor and mitigate excessive shaft vibrations to prevent further damage to the seals. Evaluate and address any thermal transient issues that may cause casing distortion. Regular maintenance and monitoring can prevent recurrence.",
      "fault_code": "FCRST-ME-004",
      "analysis_flag": true
    }
  ]
}
```

---

### 2. IP Seal Failure (R) (`FCRST-ME-005`)
- **Status**: **❌ FAILURE**
- **Induced Time**: `2026-06-25 15:53:25`
- **Resolved Time**: `2026-06-25 15:56:25`

#### Event Timeline
- [15:53:25] Induced fault 'IP Seal Failure (R)' (FCRST-ME-005).
- [15:53:35] Checked status. Active codes in state: ['FCRST-00-000']
- [15:53:45] Checked status. Active codes in state: ['FCRST-00-000']
- [15:53:55] Checked status. Active codes in state: ['FCRST-00-000']
- [15:54:05] Checked status. Active codes in state: ['FCRST-00-000']
- [15:54:15] Checked status. Active codes in state: ['FCRST-00-000']
- [15:54:25] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:54:25] Incorrect fault code detected. Reduced max timeout to 120s.
- [15:54:35] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:54:45] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:54:55] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:55:05] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:55:15] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:55:25] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:55:25] Timeout reached. Played chime sound.
- [15:55:29] Reset dropdown to Normal.
- [15:55:29] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:55:34] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:55:39] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:55:44] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:55:49] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:55:54] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:55:59] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:56:04] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:56:09] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:56:15] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:56:20] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:56:25] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:56:25] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Steam Pressure Loss",
      "possible_causes": "Steam pipe leak before HP inlet, Steam strainer blockage, Main steam stop valve failure, Piping pressure drops due to corrosion",
      "observations_analysis": "The observations indicate a decrease in steam flow and pressure at the HP turbine inlet, along with reduced power output across the turbines. These symptoms align with the context of steam pressure loss, suggesting issues such as leaks, blockages, or valve failures that are causing a drop in pressure and flow.",
      "recommendations": "Conduct a thorough inspection of the steam pipes for leaks, check and clean the steam strainer, inspect the main steam stop valve for any malfunctions, and assess the piping for signs of corrosion that could be causing pressure drops.",
      "fault_code": "FCRST-HY-002",
      "analysis_flag": true
    }
  ]
}
```

---
