# AssetSense Fault Diagnostic Test Report

## Metadata
- **Test Date/Time**: `2026-06-25 13:34:56`
- **Last Updated**: `2026-06-25 13:36:52`
- **Elapsed Duration**: `1m 56s`
- **Target Asset**: `Steam Turbine Block - 1 (AS-FCRST-DT-01)`
- **Environment**: Playwright Test Runner (Brave Browser)

---

## Executive Summary
| Status | Count |
|---|---|
| ✅ Success | 3 |
| ❌ Fail / Timeout | 0 |
| **Total Tested** | **3** |

---

## Detailed Summary Table
| # | Fault Name | Fault Code | Status | Time to Detect | Time to Reset |
|---|---|---|---|---|---|
| 1 | HP Terminal Attemperator Failure (R) | `FCRST-ME-011` | ✅ Success | 80.3s | 13:36:20 |
| 2 | IP Seal Failure (R) | `FCRST-ME-005` | ✅ Success | 10.0s | 13:36:36 |
| 3 | LP Seal Failure (R) | `FCRST-ME-006` | ✅ Success | 10.0s | 13:36:52 |

---

## Diagnostic Logs per Fault Option

### 1. HP Terminal Attemperator Failure (R) (`FCRST-ME-011`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 13:34:56`
- **Resolved Time**: `2026-06-25 13:36:20`

#### Event Timeline
- [13:34:56] Induced fault 'HP Terminal Attemperator Failure (R)' (FCRST-ME-011).
- [13:35:06] Checked status. Active codes in state: []
- [13:35:16] Checked status. Active codes in state: []
- [13:35:26] Checked status. Active codes in state: []
- [13:35:36] Checked status. Active codes in state: []
- [13:35:46] Checked status. Active codes in state: []
- [13:35:56] Checked status. Active codes in state: []
- [13:36:06] Checked status. Active codes in state: []
- [13:36:16] Checked status. Active codes in state: ['FCRST-ME-011']
- [13:36:20] Reset dropdown to Normal.
- [13:36:20] Alignment Phase - Checked status. Active codes: ['FCRST-ME-011']
- [13:36:20] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HP Terminal Attemperator Failure",
      "possible_causes": "Terminal attemperator control valve stuck open, Excessive spray water injection before HP turbine, Spray water bypass valve leakage, Main steam temperature control loop error",
      "observations_analysis": "The observations indicate a decrease in hp_turbine_power_output, primary_superheater_heat_duty, and secondary_superheater_heat_duty, which are consistent with the effects of an HP Terminal Attemperator Failure. This suggests that the control valve might be stuck open or there is excessive spray water injection, leading to reduced efficiency in the superheaters and turbine power output.",
      "recommendations": "Inspect and repair the terminal attemperator control valve to ensure it is functioning correctly. Check for any leaks in the spray water bypass valve and rectify them. Review and recalibrate the main steam temperature control loop to prevent excessive spray water injection.",
      "fault_code": "FCRST-ME-011",
      "analysis_flag": true
    }
  ]
}
```

---

### 2. IP Seal Failure (R) (`FCRST-ME-005`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 13:36:22`
- **Resolved Time**: `2026-06-25 13:36:36`

#### Event Timeline
- [13:36:22] Induced fault 'IP Seal Failure (R)' (FCRST-ME-005).
- [13:36:32] Checked status. Active codes in state: ['FCRST-ME-011']
- [13:36:32] Mapped induced fault 'IP Seal Failure (R)' to active fault 'HP Terminal Attemperator Failure' (Code: FCRST-ME-011) via name overlap.
- [13:36:36] Reset dropdown to Normal.
- [13:36:36] Alignment Phase - Checked status. Active codes: ['FCRST-ME-011']
- [13:36:36] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HP Terminal Attemperator Failure",
      "possible_causes": "Terminal attemperator control valve stuck open, Excessive spray water injection before HP turbine, Spray water bypass valve leakage, Main steam temperature control loop error",
      "observations_analysis": "The observations indicate a decrease in hp_turbine_power_output, primary_superheater_heat_duty, and secondary_superheater_heat_duty, which are consistent with the effects of an HP Terminal Attemperator Failure. This suggests that the control valve might be stuck open or there is excessive spray water injection, leading to reduced efficiency in the superheaters and turbine power output.",
      "recommendations": "Inspect and repair the terminal attemperator control valve to ensure it is functioning correctly. Check for any leaks in the spray water bypass valve and rectify them. Review and recalibrate the main steam temperature control loop to prevent excessive spray water injection.",
      "fault_code": "FCRST-ME-011",
      "analysis_flag": true
    }
  ]
}
```

---

### 3. LP Seal Failure (R) (`FCRST-ME-006`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 13:36:38`
- **Resolved Time**: `2026-06-25 13:36:52`

#### Event Timeline
- [13:36:38] Induced fault 'LP Seal Failure (R)' (FCRST-ME-006).
- [13:36:48] Checked status. Active codes in state: ['FCRST-ME-011']
- [13:36:48] Mapped induced fault 'LP Seal Failure (R)' to active fault 'HP Terminal Attemperator Failure' (Code: FCRST-ME-011) via name overlap.
- [13:36:52] Reset dropdown to Normal.
- [13:36:52] Alignment Phase - Checked status. Active codes: ['FCRST-ME-011']
- [13:36:52] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HP Terminal Attemperator Failure",
      "possible_causes": "Terminal attemperator control valve stuck open, Excessive spray water injection before HP turbine, Spray water bypass valve leakage, Main steam temperature control loop error",
      "observations_analysis": "The observations indicate a decrease in hp_turbine_power_output, primary_superheater_heat_duty, and secondary_superheater_heat_duty, which are consistent with the effects of an HP Terminal Attemperator Failure. This suggests that the control valve might be stuck open or there is excessive spray water injection, leading to reduced efficiency in the superheaters and turbine power output.",
      "recommendations": "Inspect and repair the terminal attemperator control valve to ensure it is functioning correctly. Check for any leaks in the spray water bypass valve and rectify them. Review and recalibrate the main steam temperature control loop to prevent excessive spray water injection.",
      "fault_code": "FCRST-ME-011",
      "analysis_flag": true
    }
  ]
}
```

---
