# AssetSense Fault Diagnostic Test Report

## Metadata
- **Test Date/Time**: `2026-06-25 15:37:48`
- **Last Updated**: `2026-06-25 15:48:05`
- **Elapsed Duration**: `10m 16s`
- **Target Asset**: `Steam Turbine Block - 1 (AS-FCRST-DT-01)`
- **Environment**: Playwright Test Runner (Brave Browser)

---

## Executive Summary
| Status | Count |
|---|---|
| ✅ Success | 2 |
| ❌ Fail / Timeout | 2 |
| **Total Tested** | **4** |

---

## Detailed Summary Table
| # | Fault Name | Fault Code | Status | Time to Detect | Time to Reset |
|---|---|---|---|---|---|
| 1 | HP Terminal Attemperator Failure (R) | `FCRST-ME-011` | ✅ Success | 60.2s | 15:39:49 |
| 2 | HRH Terminal Attemperator Failure (R) | `FCRST-ME-012` | ❌ Fail | N/A | 15:42:51 |
| 3 | IP Seal Failure (R) | `FCRST-ME-005` | ❌ Fail | N/A | 15:45:53 |
| 4 | Reheater Tube Failure (R) | `FCRST-ME-009` | ✅ Success | 70.2s | 15:48:05 |

---

## Diagnostic Logs per Fault Option

### 1. HP Terminal Attemperator Failure (R) (`FCRST-ME-011`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 15:37:48`
- **Resolved Time**: `2026-06-25 15:39:49`

#### Event Timeline
- [15:37:48] Induced fault 'HP Terminal Attemperator Failure (R)' (FCRST-ME-011).
- [15:37:58] Checked status. Active codes in state: []
- [15:38:08] Checked status. Active codes in state: []
- [15:38:18] Checked status. Active codes in state: []
- [15:38:29] Checked status. Active codes in state: []
- [15:38:39] Checked status. Active codes in state: []
- [15:38:49] Checked status. Active codes in state: ['FCRST-ME-011']
- [15:38:53] Reset dropdown to Normal.
- [15:38:53] Alignment Phase - Checked status. Active codes: ['FCRST-ME-011']
- [15:38:58] Alignment Phase - Checked status. Active codes: ['FCRST-ME-011']
- [15:39:03] Alignment Phase - Checked status. Active codes: ['FCRST-ME-011']
- [15:39:08] Alignment Phase - Checked status. Active codes: ['FCRST-ME-011']
- [15:39:13] Alignment Phase - Checked status. Active codes: ['FCRST-ME-011']
- [15:39:18] Alignment Phase - Checked status. Active codes: ['FCRST-ME-011']
- [15:39:23] Alignment Phase - Checked status. Active codes: ['FCRST-ME-011']
- [15:39:28] Alignment Phase - Checked status. Active codes: ['FCRST-ME-011']
- [15:39:33] Alignment Phase - Checked status. Active codes: ['FCRST-ME-011']
- [15:39:38] Alignment Phase - Checked status. Active codes: ['FCRST-ME-011']
- [15:39:43] Alignment Phase - Checked status. Active codes: ['FCRST-ME-011']
- [15:39:48] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:39:49] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HP Terminal Attemperator Failure",
      "possible_causes": "Terminal attemperator control valve stuck open, Excessive spray water injection before HP turbine, Spray water bypass valve leakage, Main steam temperature control loop error",
      "observations_analysis": "The observations indicate a decrease in hp_turbine_power_output, primary_superheater_heat_duty, and secondary_superheater_heat_duty, which aligns with the effects of an HP Terminal Attemperator Failure. This suggests that the control valve might be stuck open or there is excessive spray water injection, leading to reduced efficiency in the superheaters and turbine power output.",
      "recommendations": "Inspect and repair the terminal attemperator control valve to ensure it is functioning correctly. Check for any leaks in the spray water bypass valve and rectify them. Review and calibrate the main steam temperature control loop to prevent excessive spray water injection.",
      "fault_code": "FCRST-ME-011",
      "analysis_flag": true
    }
  ]
}
```

---

### 2. HRH Terminal Attemperator Failure (R) (`FCRST-ME-012`)
- **Status**: **❌ FAILURE**
- **Induced Time**: `2026-06-25 15:39:51`
- **Resolved Time**: `2026-06-25 15:42:51`

#### Event Timeline
- [15:39:51] Induced fault 'HRH Terminal Attemperator Failure (R)' (FCRST-ME-012).
- [15:40:01] Checked status. Active codes in state: ['FCRST-00-000']
- [15:40:11] Checked status. Active codes in state: ['FCRST-00-000']
- [15:40:21] Checked status. Active codes in state: ['FCRST-00-000']
- [15:40:31] Checked status. Active codes in state: ['FCRST-00-000']
- [15:40:41] Checked status. Active codes in state: ['FCRST-00-000']
- [15:40:51] Checked status. Active codes in state: ['FCRST-00-000']
- [15:41:01] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:41:01] Incorrect fault code detected. Reduced max timeout to 120s.
- [15:41:11] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:41:21] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:41:31] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:41:41] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:41:51] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:41:51] Timeout reached. Played chime sound.
- [15:41:55] Reset dropdown to Normal.
- [15:41:55] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:42:00] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:42:05] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:42:10] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:42:15] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:42:20] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:42:25] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:42:30] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:42:36] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:42:41] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:42:46] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:42:51] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:42:51] Graphs successfully aligned back to Normal.

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

### 3. IP Seal Failure (R) (`FCRST-ME-005`)
- **Status**: **❌ FAILURE**
- **Induced Time**: `2026-06-25 15:42:53`
- **Resolved Time**: `2026-06-25 15:45:53`

#### Event Timeline
- [15:42:53] Induced fault 'IP Seal Failure (R)' (FCRST-ME-005).
- [15:43:03] Checked status. Active codes in state: ['FCRST-00-000']
- [15:43:13] Checked status. Active codes in state: ['FCRST-00-000']
- [15:43:23] Checked status. Active codes in state: ['FCRST-00-000']
- [15:43:33] Checked status. Active codes in state: ['FCRST-00-000']
- [15:43:43] Checked status. Active codes in state: ['FCRST-00-000']
- [15:43:53] Checked status. Active codes in state: ['FCRST-00-000']
- [15:44:03] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:44:03] Incorrect fault code detected. Reduced max timeout to 120s.
- [15:44:13] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:44:23] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:44:33] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:44:43] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:44:53] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:44:53] Timeout reached. Played chime sound.
- [15:44:57] Reset dropdown to Normal.
- [15:44:57] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:45:02] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:45:07] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:45:12] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:45:17] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:45:23] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:45:28] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:45:33] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:45:38] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:45:43] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:45:48] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:45:53] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:45:53] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Steam Pressure Loss",
      "possible_causes": "Steam pipe leak before HP inlet, Steam strainer blockage, Main steam stop valve failure, Piping pressure drops due to corrosion",
      "observations_analysis": "The observations indicate a decrease in steam flow and pressure at the HP turbine inlet, along with reduced power output across the turbines. These symptoms align with the context of steam pressure loss, suggesting potential issues such as leaks, blockages, or valve failures that are causing pressure drops.",
      "recommendations": "Conduct a thorough inspection of the steam pipes and strainers for leaks or blockages. Check the main steam stop valve for any operational failures. Inspect the piping for signs of corrosion that could lead to pressure drops. Implement necessary repairs or replacements to restore normal steam pressure and flow.",
      "fault_code": "FCRST-HY-002",
      "analysis_flag": true
    }
  ]
}
```

---

### 4. Reheater Tube Failure (R) (`FCRST-ME-009`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 15:45:55`
- **Resolved Time**: `2026-06-25 15:48:05`

#### Event Timeline
- [15:45:55] Induced fault 'Reheater Tube Failure (R)' (FCRST-ME-009).
- [15:46:05] Checked status. Active codes in state: ['FCRST-00-000']
- [15:46:15] Checked status. Active codes in state: ['FCRST-00-000']
- [15:46:25] Checked status. Active codes in state: ['FCRST-00-000']
- [15:46:35] Checked status. Active codes in state: ['FCRST-00-000']
- [15:46:45] Checked status. Active codes in state: ['FCRST-00-000']
- [15:46:55] Checked status. Active codes in state: ['FCRST-00-000']
- [15:47:05] Checked status. Active codes in state: ['FCRST-ME-009']
- [15:47:09] Reset dropdown to Normal.
- [15:47:09] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [15:47:14] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [15:47:19] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [15:47:25] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [15:47:30] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [15:47:35] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [15:47:40] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [15:47:45] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [15:47:50] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [15:47:55] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [15:48:00] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [15:48:05] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:48:05] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Reheater Tube Failure",
      "possible_causes": "Creep rupture of reheater tubes, Flue gas ash erosion on reheater section, Thermal stress during rapid hot start-ups, Corrosion on gas side of reheater tubes",
      "observations_analysis": "The current observations indicate a decrease in the steam flow and power output of the intermediate and low-pressure turbines, as well as a reduction in the overall steam turbine net power. These symptoms are consistent with a reheater tube failure, which can lead to reduced efficiency and performance of the steam turbine system.",
      "recommendations": "It is recommended to conduct a thorough inspection of the reheater tubes to identify any signs of creep rupture, erosion, or corrosion. Implementing regular maintenance and monitoring of the reheater section can help prevent future failures. Additionally, optimizing startup procedures to minimize thermal stress can reduce the risk of tube failure.",
      "fault_code": "FCRST-ME-009",
      "analysis_flag": true
    }
  ]
}
```

---
