# AssetSense Fault Diagnostic Test Report

## Metadata
- **Test Date/Time**: `2026-06-25 12:24:50`
- **Last Updated**: `2026-06-25 13:28:27`
- **Elapsed Duration**: `63m 37s`
- **Target Asset**: `Steam Turbine Block - 1 (AS-FCRST-DT-01)`
- **Environment**: Playwright Test Runner (Brave Browser)

---

## Executive Summary
| Status | Count |
|---|---|
| ✅ Success | 14 |
| ❌ Fail / Timeout | 3 |
| **Total Tested** | **17** |

---

## Detailed Summary Table
| # | Fault Name | Fault Code | Status | Time to Detect | Time to Reset |
|---|---|---|---|---|---|
| 1 | Corrosion (R) | `FCRST-OT-002` | ✅ Success | 10.0s | 12:28:06 |
| 2 | Evaporator Tube Failure (R) | `FCRST-ME-008` | ✅ Success | 60.1s | 12:32:15 |
| 3 | Feedwater Flow Restriction (R) | `FCRST-HY-001` | ✅ Success | 80.2s | 12:36:44 |
| 4 | HP Blade Deformation (R) | `FCRST-ME-001` | ✅ Success | 60.2s | 12:40:52 |
| 5 | HP Interstage Attemperator Failure (R) | `FCRST-ME-010` | ✅ Success | 60.2s | 12:45:01 |
| 6 | HP Seal Failure (R) | `FCRST-ME-004` | ✅ Success | 70.1s | 12:49:20 |
| 7 | HP Terminal Attemperator Failure (R) | `FCRST-ME-011` | ❌ Fail | N/A | 12:54:28 |
| 8 | HRH Terminal Attemperator Failure (R) | `FCRST-ME-012` | ✅ Success | 60.1s | 12:58:37 |
| 9 | HRSG Fouling (R) | `FCRST-OT-003` | ✅ Success | 60.1s | 13:02:46 |
| 10 | IP Blade Deformation (R) | `FCRST-ME-002` | ✅ Success | 60.2s | 13:06:55 |
| 11 | IP Seal Failure (R) | `FCRST-ME-005` | ❌ Fail | N/A | 13:12:03 |
| 12 | LP Blade Deformation (R) | `FCRST-ME-003` | ✅ Success | 60.2s | 13:16:12 |
| 13 | LP Seal Failure (R) | `FCRST-ME-006` | ❌ Fail | N/A | 13:22:21 |
| 14 | Reheater Tube Failure (R) | `FCRST-ME-009` | ✅ Success | 70.2s | 13:24:58 |
| 15 | Steam Pressure Loss (R) | `FCRST-HY-002` | ✅ Success | 60.2s | 13:26:05 |
| 16 | Superheater Tube Failure (R) | `FCRST-ME-007` | ✅ Success | 60.2s | 13:27:11 |
| 17 | Vacuum Loss (R) | `FCRST-HY-003` | ✅ Success | 70.2s | 13:28:27 |

---

## Diagnostic Logs per Fault Option

### 1. Corrosion (R) (`FCRST-OT-002`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 12:24:50`
- **Resolved Time**: `2026-06-25 12:28:06`

#### Event Timeline
- [12:24:50] Induced fault 'Corrosion (R)' (FCRST-OT-002).
- [12:25:00] Checked status. Active codes in state: ['FCRST-OT-002']
- [12:25:04] Reset dropdown to Normal.
- [12:25:04] Alignment Phase - Checked status. Active codes: ['FCRST-OT-002']
- [12:25:09] Alignment Phase - Checked status. Active codes: ['FCRST-OT-002']
- [12:25:14] Alignment Phase - Checked status. Active codes: ['FCRST-OT-002']
- [12:25:19] Alignment Phase - Checked status. Active codes: ['FCRST-OT-002']
- [12:25:24] Alignment Phase - Checked status. Active codes: ['FCRST-OT-002']
- [12:25:29] Alignment Phase - Checked status. Active codes: ['FCRST-OT-002']
- [12:25:34] Alignment Phase - Checked status. Active codes: ['FCRST-OT-002']
- [12:25:39] Alignment Phase - Checked status. Active codes: ['FCRST-OT-002']
- [12:25:45] Alignment Phase - Checked status. Active codes: ['FCRST-00-000', 'FCRST-OT-002']
- [12:25:50] Alignment Phase - Checked status. Active codes: ['FCRST-00-000', 'FCRST-OT-002']
- [12:25:55] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:26:00] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:26:05] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:26:10] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:26:15] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:26:20] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:26:25] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:26:30] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:26:35] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:26:40] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:26:45] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:26:50] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:26:56] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:27:01] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:27:06] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:27:11] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:27:16] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:27:21] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:27:26] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:27:31] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:27:36] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:27:41] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:27:46] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:27:51] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:27:56] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:28:01] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:28:06] Warning: Graphs did not fully align within 3 mins.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Corrosion",
      "possible_causes": "High oxygen level in boiler feedwater, Acidic attack on economizer tubes, Sulfur dew point corrosion on flue gas side, Condensation of acidic gases during shutdown",
      "observations_analysis": "The current observations indicate a decrease in economizer heat duty, which is consistent with corrosion issues. Corrosion can lead to reduced heat transfer efficiency, particularly in the economizer section, due to the buildup of corrosion products on heat exchange surfaces. This aligns with the provided context where corrosion is a known problem affecting various parameters in the steam turbine system.",
      "recommendations": "It is recommended to monitor and control the oxygen levels in the boiler feedwater to prevent corrosion. Regular inspection and maintenance of economizer tubes should be conducted to detect and mitigate acidic attacks. Implementing measures to prevent sulfur dew point corrosion and ensuring proper shutdown procedures to avoid condensation of acidic gases can also help in mitigating corrosion issues.",
      "fault_code": "FCRST-OT-002",
      "analysis_flag": true
    }
  ]
}
```

---

### 2. Evaporator Tube Failure (R) (`FCRST-ME-008`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 12:28:08`
- **Resolved Time**: `2026-06-25 12:32:15`

#### Event Timeline
- [12:28:08] Induced fault 'Evaporator Tube Failure (R)' (FCRST-ME-008).
- [12:28:18] Checked status. Active codes in state: ['FCRST-00-000']
- [12:28:29] Checked status. Active codes in state: ['FCRST-00-000']
- [12:28:39] Checked status. Active codes in state: ['FCRST-00-000']
- [12:28:49] Checked status. Active codes in state: ['FCRST-00-000']
- [12:28:59] Checked status. Active codes in state: ['FCRST-00-000']
- [12:29:09] Checked status. Active codes in state: ['FCRST-ME-008']
- [12:29:13] Reset dropdown to Normal.
- [12:29:13] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [12:29:18] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [12:29:23] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [12:29:28] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [12:29:33] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [12:29:38] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [12:29:43] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [12:29:48] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [12:29:53] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [12:29:58] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [12:30:03] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [12:30:08] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:30:13] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:30:18] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:30:24] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:30:29] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:30:34] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:30:39] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:30:44] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:30:49] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:30:54] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:30:59] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:31:04] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:31:09] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:31:14] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:31:19] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:31:24] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:31:29] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:31:35] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:31:40] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:31:45] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:31:50] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:31:55] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:32:00] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:32:05] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:32:10] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:32:15] Warning: Graphs did not fully align within 3 mins.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Evaporator Tube Failure",
      "possible_causes": "Waterwall tube corrosion or pitting, Thermal fatigue of evaporator tubes, Scale formation causing localized tube overheating, High stress due to pressure transients",
      "observations_analysis": "The observations indicate a decrease in evaporator steam generation rate, ip turbine exhaust crossover pressure, lp turbine inlet crossover pressure, main steam flow rate, primary superheater heat duty, and secondary superheater heat duty. Additionally, there is an increase in stack flue gas temperature. These changes suggest that the evaporator tubes are not functioning optimally, likely due to one or more of the identified causes such as corrosion, thermal fatigue, or scale formation.",
      "recommendations": "It is recommended to conduct a thorough inspection of the evaporator tubes to identify any signs of corrosion, pitting, or scale formation. Implementing regular maintenance and monitoring of tube conditions can help prevent future failures. Consider adjusting operational parameters to reduce thermal fatigue and pressure transients.",
      "fault_code": "FCRST-ME-008",
      "analysis_flag": true
    }
  ]
}
```

---

### 3. Feedwater Flow Restriction (R) (`FCRST-HY-001`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 12:32:17`
- **Resolved Time**: `2026-06-25 12:36:44`

#### Event Timeline
- [12:32:17] Induced fault 'Feedwater Flow Restriction (R)' (FCRST-HY-001).
- [12:32:27] Checked status. Active codes in state: ['FCRST-00-000']
- [12:32:37] Checked status. Active codes in state: ['FCRST-00-000']
- [12:32:47] Checked status. Active codes in state: ['FCRST-00-000']
- [12:32:57] Checked status. Active codes in state: ['FCRST-00-000']
- [12:33:07] Checked status. Active codes in state: ['FCRST-00-000']
- [12:33:17] Checked status. Active codes in state: ['FCRST-00-000']
- [12:33:27] Checked status. Active codes in state: ['FCRST-00-000']
- [12:33:37] Checked status. Active codes in state: ['FCRST-HY-001']
- [12:33:41] Reset dropdown to Normal.
- [12:33:41] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [12:33:46] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [12:33:51] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [12:33:56] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [12:34:02] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [12:34:07] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [12:34:12] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [12:34:17] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [12:34:22] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [12:34:27] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [12:34:32] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [12:34:37] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:34:42] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:34:47] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:34:52] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:34:57] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:35:02] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:35:07] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:35:13] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:35:18] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:35:23] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:35:28] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:35:33] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:35:38] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:35:43] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:35:48] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:35:53] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:35:58] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:36:03] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:36:08] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:36:13] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:36:18] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:36:23] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:36:29] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:36:34] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:36:39] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:36:44] Warning: Graphs did not fully align within 3 mins.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Feedwater Flow Restriction",
      "possible_causes": "Feedwater pump speed control failure, Strainer blockage in economizer feed line, Control valve stuck partially closed, Feedwater flow measurement sensor error",
      "observations_analysis": "The observations indicate a decrease in economizer heat duty, evaporator heat duty, and steam generation rate, which are consistent with a feedwater flow restriction. This restriction could be due to mechanical issues such as a control valve being stuck or a blockage in the feed line. Additionally, the increase in stack flue gas temperature suggests that less heat is being absorbed by the feedwater, further supporting the diagnosis of a flow restriction.",
      "recommendations": "Inspect and test the feedwater pump speed control system for any malfunctions. Check the strainer in the economizer feed line for blockages and clean if necessary. Examine the control valve for any mechanical issues that may cause it to be partially closed. Verify the accuracy of the feedwater flow measurement sensor and recalibrate if needed.",
      "fault_code": "FCRST-HY-001",
      "analysis_flag": true
    }
  ]
}
```

---

### 4. HP Blade Deformation (R) (`FCRST-ME-001`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 12:36:46`
- **Resolved Time**: `2026-06-25 12:40:52`

#### Event Timeline
- [12:36:46] Induced fault 'HP Blade Deformation (R)' (FCRST-ME-001).
- [12:36:56] Checked status. Active codes in state: ['FCRST-00-000']
- [12:37:06] Checked status. Active codes in state: ['FCRST-00-000']
- [12:37:16] Checked status. Active codes in state: ['FCRST-00-000']
- [12:37:26] Checked status. Active codes in state: ['FCRST-00-000']
- [12:37:36] Checked status. Active codes in state: ['FCRST-00-000']
- [12:37:46] Checked status. Active codes in state: ['FCRST-ME-001']
- [12:37:50] Reset dropdown to Normal.
- [12:37:50] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [12:37:55] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [12:38:00] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [12:38:05] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [12:38:10] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [12:38:15] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [12:38:20] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [12:38:25] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [12:38:31] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [12:38:36] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [12:38:41] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [12:38:46] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:38:51] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:38:56] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:39:01] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:39:06] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:39:11] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:39:16] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:39:21] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:39:26] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:39:31] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:39:36] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:39:41] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:39:47] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:39:52] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:39:57] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:40:02] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:40:07] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:40:12] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:40:17] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:40:22] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:40:27] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:40:32] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:40:37] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:40:42] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:40:47] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:40:52] Warning: Graphs did not fully align within 3 mins.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HP Blade Deformation",
      "possible_causes": "Thermal stress or creep deformation on HP rotor, HP turbine blade erosion or solid particle impact, Shroud or tip rubbing in HP section, Deposits on HP casing nozzle partition",
      "observations_analysis": "The observations indicate a decrease in hp_turbine_power_output and reheater_heat_duty, which are consistent with the effects of HP Blade Deformation. This suggests that the deformation is affecting the efficiency and performance of the turbine, likely due to one or more of the identified causes such as thermal stress or erosion.",
      "recommendations": "Conduct a thorough inspection of the HP rotor and blades for signs of thermal stress, erosion, or rubbing. Consider implementing regular maintenance checks to prevent deposit buildup on the HP casing nozzle partition. If deformation is confirmed, plan for necessary repairs or replacements to restore optimal turbine performance.",
      "fault_code": "FCRST-ME-001",
      "analysis_flag": true
    }
  ]
}
```

---

### 5. HP Interstage Attemperator Failure (R) (`FCRST-ME-010`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 12:40:54`
- **Resolved Time**: `2026-06-25 12:45:01`

#### Event Timeline
- [12:40:54] Induced fault 'HP Interstage Attemperator Failure (R)' (FCRST-ME-010).
- [12:41:04] Checked status. Active codes in state: ['FCRST-00-000']
- [12:41:14] Checked status. Active codes in state: ['FCRST-00-000']
- [12:41:24] Checked status. Active codes in state: ['FCRST-00-000']
- [12:41:34] Checked status. Active codes in state: ['FCRST-00-000']
- [12:41:45] Checked status. Active codes in state: ['FCRST-00-000']
- [12:41:55] Checked status. Active codes in state: ['FCRST-ME-010']
- [12:41:59] Reset dropdown to Normal.
- [12:41:59] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [12:42:04] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [12:42:09] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [12:42:14] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [12:42:19] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [12:42:24] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [12:42:29] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [12:42:34] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [12:42:39] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [12:42:44] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [12:42:49] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [12:42:54] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:42:59] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:43:04] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:43:10] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:43:15] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:43:20] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:43:25] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:43:30] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:43:35] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:43:40] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:43:45] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:43:50] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:43:55] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:44:00] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:44:05] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:44:10] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:44:15] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:44:21] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:44:26] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:44:31] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:44:36] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:44:41] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:44:46] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:44:51] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:44:56] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:45:01] Warning: Graphs did not fully align within 3 mins.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HP Interstage Attemperator Failure",
      "possible_causes": "Attemperator spray control valve stuck open, Spray nozzle damage causing over-spraying, Spray water piping leak or control failure, Incorrect temperature transmitter calibration",
      "observations_analysis": "The observations indicate a failure in the HP Interstage Attemperator, as evidenced by the increase in primary superheater heat duty and the decrease in secondary superheater heat duty. These changes suggest an imbalance in the heat distribution, likely due to excessive or insufficient attemperation. The normal readings in other parameters further support that the issue is localized to the attemperator system.",
      "recommendations": "Inspect and repair or replace the attemperator spray control valve if it is stuck open. Check for any damage to the spray nozzle that might cause over-spraying. Examine the spray water piping for leaks or control failures. Verify the calibration of the temperature transmitter to ensure accurate readings.",
      "fault_code": "FCRST-ME-010",
      "analysis_flag": true
    }
  ]
}
```

---

### 6. HP Seal Failure (R) (`FCRST-ME-004`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 12:45:03`
- **Resolved Time**: `2026-06-25 12:49:20`

#### Event Timeline
- [12:45:03] Induced fault 'HP Seal Failure (R)' (FCRST-ME-004).
- [12:45:13] Checked status. Active codes in state: ['FCRST-00-000']
- [12:45:23] Checked status. Active codes in state: ['FCRST-00-000']
- [12:45:33] Checked status. Active codes in state: ['FCRST-00-000']
- [12:45:43] Checked status. Active codes in state: ['FCRST-00-000']
- [12:45:53] Checked status. Active codes in state: ['FCRST-00-000']
- [12:46:03] Checked status. Active codes in state: ['FCRST-00-000']
- [12:46:13] Checked status. Active codes in state: ['FCRST-ME-004']
- [12:46:17] Reset dropdown to Normal.
- [12:46:17] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:46:22] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:46:27] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:46:32] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:46:37] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:46:43] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:46:48] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:46:53] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:46:58] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:47:03] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:47:08] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:47:13] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:47:18] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:47:23] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:47:28] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:47:33] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:47:38] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:47:43] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:47:48] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:47:54] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:47:59] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:48:04] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:48:09] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:48:14] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:48:19] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:48:24] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:48:29] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:48:34] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:48:39] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:48:44] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:48:49] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:48:54] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:48:59] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:49:04] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:49:10] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:49:15] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:49:20] Warning: Graphs did not fully align within 3 mins.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HP Seal Failure",
      "possible_causes": "Gland seal wear on HP casing outer shaft, HP stage-to-stage labyrinth seal wear, Excessive shaft vibration damaging HP seals, Thermal transient casing distortion",
      "observations_analysis": "The observations indicate a decrease in power output across the HP, IP, and LP turbines, as well as a reduction in steam turbine net power and reheater heat duty. These symptoms align with the effects of an HP Seal Failure, where the integrity of the seals is compromised, leading to inefficiencies in steam flow and energy conversion.",
      "recommendations": "Inspect and replace worn gland seals and labyrinth seals on the HP casing. Monitor and mitigate excessive shaft vibrations to prevent further damage to the seals. Evaluate and address any thermal transient issues causing casing distortion. Regular maintenance and monitoring can prevent recurrence.",
      "fault_code": "FCRST-ME-004",
      "analysis_flag": true
    }
  ]
}
```

---

### 7. HP Terminal Attemperator Failure (R) (`FCRST-ME-011`)
- **Status**: **❌ FAILURE**
- **Induced Time**: `2026-06-25 12:49:22`
- **Resolved Time**: `2026-06-25 12:54:28`

#### Event Timeline
- [12:49:22] Induced fault 'HP Terminal Attemperator Failure (R)' (FCRST-ME-011).
- [12:49:32] Checked status. Active codes in state: ['FCRST-00-000']
- [12:49:42] Checked status. Active codes in state: ['FCRST-00-000']
- [12:49:52] Checked status. Active codes in state: ['FCRST-00-000']
- [12:50:02] Checked status. Active codes in state: ['FCRST-00-000']
- [12:50:12] Checked status. Active codes in state: ['FCRST-00-000']
- [12:50:22] Checked status. Active codes in state: ['FCRST-00-000']
- [12:50:32] Checked status. Active codes in state: ['FCRST-00-000']
- [12:50:42] Checked status. Active codes in state: ['FCRST-00-000']
- [12:50:52] Checked status. Active codes in state: ['FCRST-OT-003']
- [12:50:52] Incorrect fault code detected. Reduced max timeout to 120s.
- [12:51:02] Checked status. Active codes in state: ['FCRST-OT-003']
- [12:51:12] Checked status. Active codes in state: ['FCRST-OT-003']
- [12:51:22] Checked status. Active codes in state: ['FCRST-OT-003']
- [12:51:22] Timeout reached. Played chime sound.
- [12:51:26] Reset dropdown to Normal.
- [12:51:26] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [12:51:31] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [12:51:36] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [12:51:41] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [12:51:46] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [12:51:51] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [12:51:56] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [12:52:01] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [12:52:07] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [12:52:12] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [12:52:17] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [12:52:22] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:52:27] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:52:32] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:52:37] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:52:42] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:52:47] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:52:52] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:52:57] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:53:02] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:53:07] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:53:12] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:53:18] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:53:23] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:53:28] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:53:33] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:53:38] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:53:43] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:53:48] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:53:53] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:53:58] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:54:03] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:54:08] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:54:13] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:54:18] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:54:23] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:54:28] Warning: Graphs did not fully align within 3 mins.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HRSG Fouling",
      "possible_causes": "Soot or ash deposition on gas side of tubes, Internal tube scaling or corrosion, Poor gas distribution inside casing, Inadequate tube sootblowing maintenance",
      "observations_analysis": "The observations indicate a decrease in economizer discharge water temperature, economizer heat duty, and steam turbine net power, while there is an increase in evaporator heat duty and stack flue gas temperature. These changes are consistent with HRSG fouling, where the heat transfer efficiency is reduced due to deposits on the heat exchange surfaces, leading to decreased performance in certain areas and increased temperatures in others.",
      "recommendations": "It is recommended to perform regular maintenance and cleaning of the HRSG components to remove soot and ash deposits. Implementing a more effective sootblowing schedule and inspecting for internal tube scaling or corrosion can help prevent further fouling. Additionally, ensuring proper gas distribution inside the casing can improve overall efficiency.",
      "fault_code": "FCRST-OT-003",
      "analysis_flag": true
    }
  ]
}
```

---

### 8. HRH Terminal Attemperator Failure (R) (`FCRST-ME-012`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 12:54:30`
- **Resolved Time**: `2026-06-25 12:58:37`

#### Event Timeline
- [12:54:30] Induced fault 'HRH Terminal Attemperator Failure (R)' (FCRST-ME-012).
- [12:54:40] Checked status. Active codes in state: ['FCRST-00-000']
- [12:54:50] Checked status. Active codes in state: ['FCRST-00-000']
- [12:55:01] Checked status. Active codes in state: ['FCRST-00-000']
- [12:55:11] Checked status. Active codes in state: ['FCRST-00-000']
- [12:55:21] Checked status. Active codes in state: ['FCRST-00-000']
- [12:55:31] Checked status. Active codes in state: ['FCRST-ME-004']
- [12:55:31] Mapped induced fault 'HRH Terminal Attemperator Failure (R)' to active fault 'HP Seal Failure' (Code: FCRST-ME-004) via name overlap.
- [12:55:35] Reset dropdown to Normal.
- [12:55:35] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:55:40] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:55:45] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:55:50] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:55:55] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:56:00] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:56:05] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:56:10] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:56:15] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:56:20] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:56:25] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [12:56:30] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:56:35] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:56:40] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:56:46] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:56:51] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:56:56] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:57:01] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:57:06] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:57:11] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:57:16] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:57:21] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:57:26] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:57:31] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:57:36] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:57:41] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:57:46] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:57:51] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:57:57] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:58:02] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:58:07] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:58:12] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:58:17] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:58:22] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:58:27] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:58:32] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [12:58:37] Warning: Graphs did not fully align within 3 mins.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HP Seal Failure",
      "possible_causes": "Gland seal wear on HP casing outer shaft, HP stage-to-stage labyrinth seal wear, Excessive shaft vibration damaging HP seals, Thermal transient casing distortion",
      "observations_analysis": "The observations indicate a decrease in power output across the HP, IP, and LP turbines, as well as a reduction in steam turbine net power and reheater heat duty. These symptoms align with the effects of an HP Seal Failure, where the integrity of the seals is compromised, leading to inefficiencies in steam flow and energy conversion.",
      "recommendations": "Inspect and replace worn gland seals and labyrinth seals on the HP casing. Monitor and mitigate excessive shaft vibrations to prevent further damage to the seals. Evaluate and address any thermal transient issues that may cause casing distortion. Regular maintenance and monitoring of seal conditions can prevent recurrence.",
      "fault_code": "FCRST-ME-004",
      "analysis_flag": true
    }
  ]
}
```

---

### 9. HRSG Fouling (R) (`FCRST-OT-003`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 12:58:39`
- **Resolved Time**: `2026-06-25 13:02:46`

#### Event Timeline
- [12:58:39] Induced fault 'HRSG Fouling (R)' (FCRST-OT-003).
- [12:58:49] Checked status. Active codes in state: ['FCRST-00-000']
- [12:58:59] Checked status. Active codes in state: ['FCRST-00-000']
- [12:59:09] Checked status. Active codes in state: ['FCRST-00-000']
- [12:59:19] Checked status. Active codes in state: ['FCRST-00-000']
- [12:59:29] Checked status. Active codes in state: ['FCRST-00-000']
- [12:59:39] Checked status. Active codes in state: ['FCRST-OT-003']
- [12:59:43] Reset dropdown to Normal.
- [12:59:43] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [12:59:48] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [12:59:53] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [12:59:58] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [13:00:04] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [13:00:09] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [13:00:14] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [13:00:19] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [13:00:24] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [13:00:29] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [13:00:34] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [13:00:39] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:00:44] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:00:49] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:00:54] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:00:59] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:01:04] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:01:09] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:01:15] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:01:20] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:01:25] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:01:30] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:01:35] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:01:40] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:01:45] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:01:50] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:01:55] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:02:00] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:02:05] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:02:10] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:02:15] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:02:20] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:02:25] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:02:31] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:02:36] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:02:41] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:02:46] Warning: Graphs did not fully align within 3 mins.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HRSG Fouling",
      "possible_causes": "Soot or ash deposition on gas side of tubes, Internal tube scaling or corrosion, Poor gas distribution inside casing, Inadequate tube sootblowing maintenance",
      "observations_analysis": "The observations indicate a decrease in economizer discharge water temperature, economizer heat duty, and steam turbine net power, while there is an increase in evaporator heat duty and stack flue gas temperature. These changes are consistent with HRSG fouling, where the heat transfer efficiency is reduced due to deposits on the heat exchange surfaces, leading to decreased performance in certain areas and increased temperatures in others.",
      "recommendations": "It is recommended to perform regular maintenance and cleaning of the HRSG components to remove soot and ash deposits. Implementing a more effective sootblowing schedule and inspecting for internal tube scaling or corrosion can help prevent further fouling. Additionally, ensuring proper gas distribution inside the casing can improve overall efficiency.",
      "fault_code": "FCRST-OT-003",
      "analysis_flag": true
    }
  ]
}
```

---

### 10. IP Blade Deformation (R) (`FCRST-ME-002`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 13:02:48`
- **Resolved Time**: `2026-06-25 13:06:55`

#### Event Timeline
- [13:02:48] Induced fault 'IP Blade Deformation (R)' (FCRST-ME-002).
- [13:02:58] Checked status. Active codes in state: ['FCRST-00-000']
- [13:03:08] Checked status. Active codes in state: ['FCRST-00-000']
- [13:03:18] Checked status. Active codes in state: ['FCRST-00-000']
- [13:03:28] Checked status. Active codes in state: ['FCRST-00-000']
- [13:03:38] Checked status. Active codes in state: ['FCRST-00-000']
- [13:03:48] Checked status. Active codes in state: ['FCRST-ME-002']
- [13:03:52] Reset dropdown to Normal.
- [13:03:52] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [13:03:57] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [13:04:02] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [13:04:07] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [13:04:12] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [13:04:17] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [13:04:22] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [13:04:27] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [13:04:33] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [13:04:38] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [13:04:43] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [13:04:48] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:04:53] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:04:58] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:05:03] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:05:08] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:05:13] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:05:18] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:05:23] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:05:28] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:05:33] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:05:38] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:05:44] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:05:49] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:05:54] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:05:59] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:06:04] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:06:09] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:06:14] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:06:19] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:06:24] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:06:29] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:06:34] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:06:39] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:06:44] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:06:49] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:06:55] Warning: Graphs did not fully align within 3 mins.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "IP Blade Deformation",
      "possible_causes": "Creep or mechanical fatigue of IP rotor blades, Corrosion fatigue or erosion in IP section, IP turbine blade tip clearance rubbing, Scale buildup on IP guide vanes",
      "observations_analysis": "The decrease in IP turbine power output suggests a potential deformation of the IP blades. This could be due to mechanical fatigue or corrosion, which are common issues in the IP section of a fully connected reheat steam turbine. The normal operation of other parameters indicates that the issue is localized to the IP section.",
      "recommendations": "Conduct a thorough inspection of the IP rotor blades for signs of creep or mechanical fatigue. Check for corrosion or erosion in the IP section and inspect the blade tip clearance for any rubbing. Additionally, examine the IP guide vanes for scale buildup and clean if necessary.",
      "fault_code": "FCRST-ME-002",
      "analysis_flag": true
    }
  ]
}
```

---

### 11. IP Seal Failure (R) (`FCRST-ME-005`)
- **Status**: **❌ FAILURE**
- **Induced Time**: `2026-06-25 13:06:57`
- **Resolved Time**: `2026-06-25 13:12:03`

#### Event Timeline
- [13:06:57] Induced fault 'IP Seal Failure (R)' (FCRST-ME-005).
- [13:07:07] Checked status. Active codes in state: ['FCRST-00-000']
- [13:07:17] Checked status. Active codes in state: ['FCRST-00-000']
- [13:07:27] Checked status. Active codes in state: ['FCRST-00-000']
- [13:07:37] Checked status. Active codes in state: ['FCRST-00-000']
- [13:07:47] Checked status. Active codes in state: ['FCRST-00-000']
- [13:07:57] Checked status. Active codes in state: ['FCRST-00-000']
- [13:08:07] Checked status. Active codes in state: ['FCRST-HY-002']
- [13:08:07] Incorrect fault code detected. Reduced max timeout to 120s.
- [13:08:17] Checked status. Active codes in state: ['FCRST-HY-002']
- [13:08:27] Checked status. Active codes in state: ['FCRST-HY-002']
- [13:08:37] Checked status. Active codes in state: ['FCRST-HY-002']
- [13:08:47] Checked status. Active codes in state: ['FCRST-HY-002']
- [13:08:57] Checked status. Active codes in state: ['FCRST-HY-002']
- [13:08:57] Timeout reached. Played chime sound.
- [13:09:01] Reset dropdown to Normal.
- [13:09:01] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [13:09:06] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [13:09:11] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [13:09:16] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [13:09:21] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [13:09:26] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [13:09:31] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [13:09:36] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [13:09:41] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [13:09:46] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [13:09:52] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [13:09:57] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:10:02] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:10:07] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:10:12] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:10:17] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:10:22] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:10:27] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:10:32] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:10:37] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:10:42] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:10:47] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:10:52] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:10:57] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:11:03] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:11:08] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:11:13] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:11:18] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:11:23] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:11:28] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:11:33] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:11:38] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:11:43] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:11:48] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:11:53] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:11:58] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:12:03] Warning: Graphs did not fully align within 3 mins.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Steam Pressure Loss",
      "possible_causes": "Steam pipe leak before HP inlet, Steam strainer blockage, Main steam stop valve failure, Piping pressure drops due to corrosion",
      "observations_analysis": "The observations indicate a decrease in steam flow and pressure at the HP turbine inlet, along with reduced power output across the turbines. These symptoms align with the context of steam pressure loss, suggesting potential issues such as leaks, blockages, or valve failures.",
      "recommendations": "Conduct a thorough inspection of the steam pipes for leaks, check and clean the steam strainer, inspect the main steam stop valve for proper operation, and assess the piping for signs of corrosion and pressure drops.",
      "fault_code": "FCRST-HY-002",
      "analysis_flag": true
    }
  ]
}
```

---

### 12. LP Blade Deformation (R) (`FCRST-ME-003`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 13:12:05`
- **Resolved Time**: `2026-06-25 13:16:12`

#### Event Timeline
- [13:12:05] Induced fault 'LP Blade Deformation (R)' (FCRST-ME-003).
- [13:12:15] Checked status. Active codes in state: ['FCRST-00-000']
- [13:12:25] Checked status. Active codes in state: ['FCRST-00-000']
- [13:12:35] Checked status. Active codes in state: ['FCRST-00-000']
- [13:12:45] Checked status. Active codes in state: ['FCRST-00-000']
- [13:12:55] Checked status. Active codes in state: ['FCRST-00-000']
- [13:13:05] Checked status. Active codes in state: ['FCRST-ME-003']
- [13:13:09] Reset dropdown to Normal.
- [13:13:10] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [13:13:15] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [13:13:20] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [13:13:25] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [13:13:30] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [13:13:35] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [13:13:40] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [13:13:45] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [13:13:50] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [13:13:55] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [13:14:00] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [13:14:05] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:14:10] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:14:15] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:14:21] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:14:26] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:14:31] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:14:36] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:14:41] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:14:46] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:14:51] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:14:56] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:15:01] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:15:06] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:15:11] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:15:16] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:15:21] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:15:26] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:15:31] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:15:37] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:15:42] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:15:47] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:15:52] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:15:57] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:16:02] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:16:07] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:16:12] Warning: Graphs did not fully align within 3 mins.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "LP Blade Deformation",
      "possible_causes": "Erosion from water droplets in LP casing, LP turbine blade fatigue or crack propagation, Mechanical rubbing in LP casing shroud, Corrosion pitting on LP exhaust stages",
      "observations_analysis": "The analysis of the current real-time data indicates a decrease in LP turbine power output, which aligns with the effects of LP Blade Deformation. This suggests that the deformation is likely causing inefficiencies in the turbine's operation, leading to reduced power output.",
      "recommendations": "Conduct a thorough inspection of the LP turbine blades for signs of erosion, fatigue, or mechanical damage. Implement regular maintenance checks to prevent corrosion and ensure the integrity of the turbine casing. Consider installing moisture separators to reduce water droplet erosion.",
      "fault_code": "FCRST-ME-003",
      "analysis_flag": true
    }
  ]
}
```

---

### 13. LP Seal Failure (R) (`FCRST-ME-006`)
- **Status**: **❌ FAILURE**
- **Induced Time**: `2026-06-25 13:16:14`
- **Resolved Time**: `2026-06-25 13:22:21`

#### Event Timeline
- [13:16:14] Induced fault 'LP Seal Failure (R)' (FCRST-ME-006).
- [13:16:24] Checked status. Active codes in state: ['FCRST-00-000']
- [13:16:34] Checked status. Active codes in state: ['FCRST-00-000']
- [13:16:44] Checked status. Active codes in state: ['FCRST-00-000']
- [13:16:54] Checked status. Active codes in state: ['FCRST-00-000']
- [13:17:04] Checked status. Active codes in state: ['FCRST-00-000']
- [13:17:14] Checked status. Active codes in state: []
- [13:17:24] Checked status. Active codes in state: []
- [13:17:34] Checked status. Active codes in state: []
- [13:17:44] Checked status. Active codes in state: []
- [13:17:54] Checked status. Active codes in state: []
- [13:18:04] Checked status. Active codes in state: []
- [13:18:14] Checked status. Active codes in state: []
- [13:18:24] Checked status. Active codes in state: []
- [13:18:34] Checked status. Active codes in state: []
- [13:18:44] Checked status. Active codes in state: []
- [13:18:54] Checked status. Active codes in state: []
- [13:19:04] Checked status. Active codes in state: []
- [13:19:14] Checked status. Active codes in state: []
- [13:19:14] Timeout reached. Played chime sound.
- [13:19:18] Reset dropdown to Normal.
- [13:19:18] Alignment Phase - Checked status. Active codes: []
- [13:19:24] Alignment Phase - Checked status. Active codes: []
- [13:19:29] Alignment Phase - Checked status. Active codes: []
- [13:19:34] Alignment Phase - Checked status. Active codes: []
- [13:19:39] Alignment Phase - Checked status. Active codes: []
- [13:19:44] Alignment Phase - Checked status. Active codes: []
- [13:19:49] Alignment Phase - Checked status. Active codes: []
- [13:19:54] Alignment Phase - Checked status. Active codes: []
- [13:19:59] Alignment Phase - Checked status. Active codes: []
- [13:20:04] Alignment Phase - Checked status. Active codes: []
- [13:20:09] Alignment Phase - Checked status. Active codes: []
- [13:20:14] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:20:19] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:20:24] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:20:29] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:20:35] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:20:40] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:20:45] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:20:50] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:20:55] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:21:00] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:21:05] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:21:10] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:21:15] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:21:20] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:21:25] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:21:30] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:21:35] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:21:40] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:21:45] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:21:51] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:21:56] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:22:01] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:22:06] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:22:11] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:22:16] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:22:21] Warning: Graphs did not fully align within 3 mins.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "either actual or expected data is not sent for a tag",
      "possible_causes": "-",
      "observations_analysis": "-",
      "analysis_flag": false
    }
  ]
}
```

---

### 14. Reheater Tube Failure (R) (`FCRST-ME-009`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 13:22:23`
- **Resolved Time**: `2026-06-25 13:24:58`

#### Event Timeline
- [13:22:23] Induced fault 'Reheater Tube Failure (R)' (FCRST-ME-009).
- [13:22:33] Checked status. Active codes in state: ['FCRST-00-000']
- [13:22:43] Checked status. Active codes in state: ['FCRST-00-000']
- [13:22:53] Checked status. Active codes in state: ['FCRST-00-000']
- [13:23:03] Checked status. Active codes in state: ['FCRST-00-000']
- [13:23:13] Checked status. Active codes in state: ['FCRST-00-000']
- [13:23:23] Checked status. Active codes in state: ['FCRST-00-000']
- [13:23:33] Checked status. Active codes in state: ['FCRST-ME-009']
- [13:23:37] Reset dropdown to Normal.
- [13:23:37] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [13:23:42] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [13:23:47] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [13:23:52] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [13:23:57] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [13:24:03] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [13:24:08] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [13:24:13] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [13:24:18] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [13:24:23] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [13:24:28] Alignment Phase - Checked status. Active codes: ['FCRST-ME-009']
- [13:24:33] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:24:38] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:24:43] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:24:48] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:24:53] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:24:58] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [13:24:58] Graphs successfully aligned back to Normal.

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

### 15. Steam Pressure Loss (R) (`FCRST-HY-002`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 13:25:00`
- **Resolved Time**: `2026-06-25 13:26:05`

#### Event Timeline
- [13:25:00] Induced fault 'Steam Pressure Loss (R)' (FCRST-HY-002).
- [13:25:10] Checked status. Active codes in state: ['FCRST-00-000']
- [13:25:20] Checked status. Active codes in state: ['FCRST-00-000']
- [13:25:30] Checked status. Active codes in state: ['FCRST-00-000']
- [13:25:41] Checked status. Active codes in state: ['FCRST-00-000']
- [13:25:51] Checked status. Active codes in state: ['FCRST-00-000']
- [13:26:01] Checked status. Active codes in state: ['FCRST-HY-002']
- [13:26:05] Reset dropdown to Normal.
- [13:26:05] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [13:26:05] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Steam Pressure Loss",
      "possible_causes": "Steam pipe leak before HP inlet, Steam strainer blockage, Main steam stop valve failure, Piping pressure drops due to corrosion",
      "observations_analysis": "The observations indicate a decrease in steam flow and pressure at the HP turbine inlet, along with reduced power output across the turbines. These symptoms align with the context of steam pressure loss, suggesting potential issues such as leaks, blockages, or valve failures.",
      "recommendations": "Conduct a thorough inspection of the steam pipes for leaks, check and clean the steam strainer, inspect the main steam stop valve for proper operation, and assess the piping for signs of corrosion that could lead to pressure drops.",
      "fault_code": "FCRST-HY-002",
      "analysis_flag": true
    }
  ]
}
```

---

### 16. Superheater Tube Failure (R) (`FCRST-ME-007`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 13:26:07`
- **Resolved Time**: `2026-06-25 13:27:11`

#### Event Timeline
- [13:26:07] Induced fault 'Superheater Tube Failure (R)' (FCRST-ME-007).
- [13:26:17] Checked status. Active codes in state: ['FCRST-HY-002']
- [13:26:17] Incorrect fault code detected. Reduced max timeout to 120s.
- [13:26:27] Checked status. Active codes in state: ['FCRST-HY-002']
- [13:26:37] Checked status. Active codes in state: ['FCRST-HY-002']
- [13:26:47] Checked status. Active codes in state: ['FCRST-HY-002']
- [13:26:57] Checked status. Active codes in state: ['FCRST-HY-002']
- [13:27:07] Checked status. Active codes in state: ['FCRST-ME-007']
- [13:27:11] Reset dropdown to Normal.
- [13:27:11] Alignment Phase - Checked status. Active codes: ['FCRST-ME-007']
- [13:27:11] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Superheater Tube Failure",
      "possible_causes": "Thermal fatigue of superheater tube welds, High temperature creep rupture in superheater section, Localized flue gas erosion on superheater tubes, Scaling inside superheater causing overheating",
      "observations_analysis": "The observations indicate a decrease in key performance metrics such as hp_superheater_outlet_temperature_main_steam, hp_turbine_inlet_steam_flow, and steam_turbine_net_power, which are consistent with a superheater tube failure. The increase in stack_flue_gas_temperature and water_flow_rate further supports this diagnosis, as these changes can result from compromised heat transfer efficiency due to tube damage or scaling.",
      "recommendations": "Conduct a thorough inspection of the superheater tubes to identify any signs of thermal fatigue, creep rupture, or erosion. Implement regular maintenance and cleaning schedules to prevent scaling. Consider upgrading materials or design to withstand high temperatures and reduce the risk of future failures.",
      "fault_code": "FCRST-ME-007",
      "analysis_flag": true
    }
  ]
}
```

---

### 17. Vacuum Loss (R) (`FCRST-HY-003`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 13:27:13`
- **Resolved Time**: `2026-06-25 13:28:27`

#### Event Timeline
- [13:27:13] Induced fault 'Vacuum Loss (R)' (FCRST-HY-003).
- [13:27:23] Checked status. Active codes in state: ['FCRST-ME-007']
- [13:27:23] Incorrect fault code detected. Reduced max timeout to 120s.
- [13:27:33] Checked status. Active codes in state: ['FCRST-ME-007']
- [13:27:43] Checked status. Active codes in state: ['FCRST-ME-007']
- [13:27:53] Checked status. Active codes in state: ['FCRST-ME-007']
- [13:28:03] Checked status. Active codes in state: ['FCRST-ME-007']
- [13:28:13] Checked status. Active codes in state: ['FCRST-ME-007']
- [13:28:23] Checked status. Active codes in state: ['FCRST-HY-003']
- [13:28:27] Reset dropdown to Normal.
- [13:28:27] Alignment Phase - Checked status. Active codes: ['FCRST-HY-003']
- [13:28:27] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Vacuum Loss",
      "possible_causes": "Condenser cooling water pump trip, Condenser tube fouling or scaling, Air ingress through LP casing seals, Vacuum pump or ejector malfunction, Excessive cooling water inlet temperature",
      "observations_analysis": "The observations indicate a decrease in lp_turbine_power_output and steam_turbine_net_power, along with an increase in lp_turbine_exhaust_enthalpy, lp_turbine_exhaust_pressure_condenser_pressure, and lp_turbine_exhaust_temperature. These changes are consistent with a vacuum loss in the condenser, which can be caused by issues such as a condenser cooling water pump trip or air ingress through LP casing seals.",
      "recommendations": "Inspect and ensure the proper functioning of the condenser cooling water pump. Check for fouling or scaling in the condenser tubes and clean if necessary. Verify the integrity of LP casing seals to prevent air ingress. Examine the vacuum pump or ejector for any malfunctions. Monitor and control the cooling water inlet temperature to maintain optimal conditions.",
      "fault_code": "FCRST-HY-003",
      "analysis_flag": true
    }
  ]
}
```

---
