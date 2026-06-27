# AssetSense Fault Diagnostic Test Report

## Metadata
- **Test Date/Time**: `2026-06-25 14:55:31`
- **Last Updated**: `2026-06-25 15:34:36`
- **Elapsed Duration**: `39m 5s`
- **Target Asset**: `Steam Turbine Block - 1 (AS-FCRST-DT-01)`
- **Environment**: Playwright Test Runner (Brave Browser)

---

## Executive Summary
| Status | Count |
|---|---|
| ✅ Success | 13 |
| ❌ Fail / Timeout | 4 |
| **Total Tested** | **17** |

---

## Detailed Summary Table
| # | Fault Name | Fault Code | Status | Time to Detect | Time to Reset |
|---|---|---|---|---|---|
| 1 | Corrosion (R) | `FCRST-OT-002` | ✅ Success | 60.2s | 14:57:31 |
| 2 | Evaporator Tube Failure (R) | `FCRST-ME-008` | ✅ Success | 60.2s | 14:59:33 |
| 3 | Feedwater Flow Restriction (R) | `FCRST-HY-001` | ✅ Success | 70.2s | 15:01:45 |
| 4 | HP Blade Deformation (R) | `FCRST-ME-001` | ✅ Success | 60.2s | 15:03:47 |
| 5 | HP Interstage Attemperator Failure (R) | `FCRST-ME-010` | ✅ Success | 60.2s | 15:05:50 |
| 6 | HP Seal Failure (R) | `FCRST-ME-004` | ✅ Success | 60.2s | 15:07:52 |
| 7 | HP Terminal Attemperator Failure (R) | `FCRST-ME-011` | ❌ Fail | N/A | 15:10:49 |
| 8 | HRH Terminal Attemperator Failure (R) | `FCRST-ME-012` | ❌ Fail | N/A | 15:13:51 |
| 9 | HRSG Fouling (R) | `FCRST-OT-003` | ✅ Success | 70.2s | 15:16:04 |
| 10 | IP Blade Deformation (R) | `FCRST-ME-002` | ✅ Success | 60.2s | 15:18:06 |
| 11 | IP Seal Failure (R) | `FCRST-ME-005` | ❌ Fail | N/A | 15:21:03 |
| 12 | LP Blade Deformation (R) | `FCRST-ME-003` | ✅ Success | 60.2s | 15:23:05 |
| 13 | LP Seal Failure (R) | `FCRST-ME-006` | ✅ Success | 60.2s | 15:25:07 |
| 14 | Reheater Tube Failure (R) | `FCRST-ME-009` | ❌ Fail | N/A | 15:28:10 |
| 15 | Steam Pressure Loss (R) | `FCRST-HY-002` | ✅ Success | 60.2s | 15:30:12 |
| 16 | Superheater Tube Failure (R) | `FCRST-ME-007` | ✅ Success | 70.2s | 15:32:24 |
| 17 | Vacuum Loss (R) | `FCRST-HY-003` | ✅ Success | 70.2s | 15:34:36 |

---

## Diagnostic Logs per Fault Option

### 1. Corrosion (R) (`FCRST-OT-002`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 14:55:31`
- **Resolved Time**: `2026-06-25 14:57:31`

#### Event Timeline
- [14:55:31] Induced fault 'Corrosion (R)' (FCRST-OT-002).
- [14:55:41] Checked status. Active codes in state: []
- [14:55:51] Checked status. Active codes in state: []
- [14:56:01] Checked status. Active codes in state: []
- [14:56:11] Checked status. Active codes in state: []
- [14:56:21] Checked status. Active codes in state: []
- [14:56:31] Checked status. Active codes in state: ['FCRST-OT-002']
- [14:56:35] Reset dropdown to Normal.
- [14:56:35] Alignment Phase - Checked status. Active codes: ['FCRST-OT-002']
- [14:56:40] Alignment Phase - Checked status. Active codes: ['FCRST-OT-002']
- [14:56:45] Alignment Phase - Checked status. Active codes: ['FCRST-OT-002']
- [14:56:50] Alignment Phase - Checked status. Active codes: ['FCRST-OT-002']
- [14:56:55] Alignment Phase - Checked status. Active codes: ['FCRST-OT-002']
- [14:57:00] Alignment Phase - Checked status. Active codes: ['FCRST-OT-002']
- [14:57:06] Alignment Phase - Checked status. Active codes: ['FCRST-OT-002']
- [14:57:11] Alignment Phase - Checked status. Active codes: ['FCRST-OT-002']
- [14:57:16] Alignment Phase - Checked status. Active codes: ['FCRST-OT-002']
- [14:57:21] Alignment Phase - Checked status. Active codes: ['FCRST-OT-002']
- [14:57:26] Alignment Phase - Checked status. Active codes: ['FCRST-OT-002']
- [14:57:31] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [14:57:31] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Corrosion",
      "possible_causes": "High oxygen level in boiler feedwater, Acidic attack on economizer tubes, Sulfur dew point corrosion on flue gas side, Condensation of acidic gases during shutdown",
      "observations_analysis": "The current observations indicate a decrease in economizer heat duty, which is consistent with corrosion issues. Corrosion can lead to reduced heat transfer efficiency, particularly in the economizer section, due to the buildup of corrosion products on heat exchange surfaces. This aligns with the provided context where corrosion is identified as a problem affecting various parameters.",
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
- **Induced Time**: `2026-06-25 14:57:33`
- **Resolved Time**: `2026-06-25 14:59:33`

#### Event Timeline
- [14:57:33] Induced fault 'Evaporator Tube Failure (R)' (FCRST-ME-008).
- [14:57:43] Checked status. Active codes in state: ['FCRST-00-000']
- [14:57:53] Checked status. Active codes in state: ['FCRST-00-000']
- [14:58:03] Checked status. Active codes in state: ['FCRST-00-000']
- [14:58:13] Checked status. Active codes in state: ['FCRST-00-000']
- [14:58:23] Checked status. Active codes in state: ['FCRST-00-000']
- [14:58:33] Checked status. Active codes in state: ['FCRST-ME-008']
- [14:58:37] Reset dropdown to Normal.
- [14:58:37] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [14:58:42] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [14:58:47] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [14:58:52] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [14:58:57] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [14:59:03] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [14:59:08] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [14:59:13] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [14:59:18] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [14:59:23] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [14:59:28] Alignment Phase - Checked status. Active codes: ['FCRST-ME-008']
- [14:59:33] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [14:59:33] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Evaporator Tube Failure",
      "possible_causes": "Waterwall tube corrosion or pitting, Thermal fatigue of evaporator tubes, Scale formation causing localized tube overheating, High stress due to pressure transients",
      "observations_analysis": "The observations indicate a decrease in evaporator steam generation rate, ip turbine exhaust crossover pressure, lp turbine inlet crossover pressure, main steam flow rate, primary superheater heat duty, and secondary superheater heat duty. Additionally, there is an increase in stack flue gas temperature. These changes suggest that the evaporator tubes are not functioning optimally, likely due to one or more of the identified causes such as corrosion, thermal fatigue, or scale formation, leading to reduced efficiency and performance of the steam turbine.",
      "recommendations": "It is recommended to conduct a thorough inspection of the evaporator tubes to identify any signs of corrosion, pitting, or scale formation. Implementing regular maintenance and cleaning schedules can help prevent scale buildup. Additionally, monitoring and controlling pressure transients can reduce stress on the tubes. Consider using corrosion-resistant materials or coatings to extend the lifespan of the tubes.",
      "fault_code": "FCRST-ME-008",
      "analysis_flag": true
    }
  ]
}
```

---

### 3. Feedwater Flow Restriction (R) (`FCRST-HY-001`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 14:59:35`
- **Resolved Time**: `2026-06-25 15:01:45`

#### Event Timeline
- [14:59:35] Induced fault 'Feedwater Flow Restriction (R)' (FCRST-HY-001).
- [14:59:45] Checked status. Active codes in state: ['FCRST-00-000']
- [14:59:55] Checked status. Active codes in state: ['FCRST-00-000']
- [15:00:05] Checked status. Active codes in state: ['FCRST-00-000']
- [15:00:15] Checked status. Active codes in state: ['FCRST-00-000']
- [15:00:25] Checked status. Active codes in state: ['FCRST-00-000']
- [15:00:35] Checked status. Active codes in state: ['FCRST-00-000']
- [15:00:45] Checked status. Active codes in state: ['FCRST-HY-001']
- [15:00:49] Reset dropdown to Normal.
- [15:00:49] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [15:00:54] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [15:01:00] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [15:01:05] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [15:01:10] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [15:01:15] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [15:01:20] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [15:01:25] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [15:01:30] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [15:01:35] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [15:01:40] Alignment Phase - Checked status. Active codes: ['FCRST-HY-001']
- [15:01:45] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:01:45] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Feedwater Flow Restriction",
      "possible_causes": "Feedwater pump speed control failure, Strainer blockage in economizer feed line, Control valve stuck partially closed, Feedwater flow measurement sensor error",
      "observations_analysis": "The observations indicate a decrease in economizer heat duty, evaporator heat duty, and steam generation rate, which are consistent with a feedwater flow restriction. This restriction could be due to issues such as a malfunctioning feedwater pump speed control, a blockage in the strainer of the economizer feed line, a control valve that is stuck partially closed, or an error in the feedwater flow measurement sensor.",
      "recommendations": "Inspect and repair the feedwater pump speed control system. Check and clean the strainer in the economizer feed line. Ensure that all control valves are operating correctly and not stuck. Verify the accuracy of the feedwater flow measurement sensor and recalibrate if necessary.",
      "fault_code": "FCRST-HY-001",
      "analysis_flag": true
    }
  ]
}
```

---

### 4. HP Blade Deformation (R) (`FCRST-ME-001`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 15:01:47`
- **Resolved Time**: `2026-06-25 15:03:47`

#### Event Timeline
- [15:01:47] Induced fault 'HP Blade Deformation (R)' (FCRST-ME-001).
- [15:01:57] Checked status. Active codes in state: ['FCRST-00-000']
- [15:02:07] Checked status. Active codes in state: ['FCRST-00-000']
- [15:02:17] Checked status. Active codes in state: ['FCRST-00-000']
- [15:02:27] Checked status. Active codes in state: ['FCRST-00-000']
- [15:02:37] Checked status. Active codes in state: ['FCRST-00-000']
- [15:02:47] Checked status. Active codes in state: ['FCRST-ME-001']
- [15:02:51] Reset dropdown to Normal.
- [15:02:51] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [15:02:57] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [15:03:02] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [15:03:07] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [15:03:12] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [15:03:17] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [15:03:22] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [15:03:27] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [15:03:32] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [15:03:37] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [15:03:42] Alignment Phase - Checked status. Active codes: ['FCRST-ME-001']
- [15:03:47] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:03:47] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HP Blade Deformation",
      "possible_causes": "Thermal stress or creep deformation on HP rotor, HP turbine blade erosion or solid particle impact, Shroud or tip rubbing in HP section, Deposits on HP casing nozzle partition",
      "observations_analysis": "The observations indicate a decrease in hp_turbine_power_output and reheater_heat_duty, which are consistent with the effects of HP Blade Deformation. This suggests that the deformation is affecting the efficiency and performance of the turbine, likely due to one or more of the identified causes such as thermal stress or erosion.",
      "recommendations": "Conduct a thorough inspection of the HP rotor and blades for signs of thermal stress, erosion, or rubbing. Consider implementing maintenance procedures to address any deposits on the HP casing nozzle partition. Regular monitoring and maintenance can help prevent further degradation and improve turbine performance.",
      "fault_code": "FCRST-ME-001",
      "analysis_flag": true
    }
  ]
}
```

---

### 5. HP Interstage Attemperator Failure (R) (`FCRST-ME-010`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 15:03:49`
- **Resolved Time**: `2026-06-25 15:05:50`

#### Event Timeline
- [15:03:49] Induced fault 'HP Interstage Attemperator Failure (R)' (FCRST-ME-010).
- [15:03:59] Checked status. Active codes in state: ['FCRST-00-000']
- [15:04:10] Checked status. Active codes in state: ['FCRST-00-000']
- [15:04:20] Checked status. Active codes in state: ['FCRST-00-000']
- [15:04:30] Checked status. Active codes in state: ['FCRST-00-000']
- [15:04:40] Checked status. Active codes in state: ['FCRST-00-000']
- [15:04:50] Checked status. Active codes in state: ['FCRST-ME-010']
- [15:04:54] Reset dropdown to Normal.
- [15:04:54] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [15:04:59] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [15:05:04] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [15:05:09] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [15:05:14] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [15:05:19] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [15:05:24] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [15:05:29] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [15:05:34] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [15:05:39] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [15:05:44] Alignment Phase - Checked status. Active codes: ['FCRST-ME-010']
- [15:05:50] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:05:50] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HP Interstage Attemperator Failure",
      "possible_causes": "Attemperator spray control valve stuck open, Spray nozzle damage causing over-spraying, Spray water piping leak or control failure, Incorrect temperature transmitter calibration",
      "observations_analysis": "The observations indicate that the HP Interstage Attemperator is not functioning correctly, leading to an imbalance in the heat duties of the superheaters. The primary superheater heat duty has increased, while the secondary superheater heat duty has decreased. This suggests that the attemperator is either over-spraying or not controlling the spray effectively, possibly due to a stuck valve or nozzle damage.",
      "recommendations": "Inspect and repair or replace the attemperator spray control valve and nozzles. Check for leaks or control failures in the spray water piping. Calibrate the temperature transmitters to ensure accurate readings.",
      "fault_code": "FCRST-ME-010",
      "analysis_flag": true
    }
  ]
}
```

---

### 6. HP Seal Failure (R) (`FCRST-ME-004`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 15:05:52`
- **Resolved Time**: `2026-06-25 15:07:52`

#### Event Timeline
- [15:05:52] Induced fault 'HP Seal Failure (R)' (FCRST-ME-004).
- [15:06:02] Checked status. Active codes in state: ['FCRST-00-000']
- [15:06:12] Checked status. Active codes in state: ['FCRST-00-000']
- [15:06:22] Checked status. Active codes in state: ['FCRST-00-000']
- [15:06:32] Checked status. Active codes in state: ['FCRST-00-000']
- [15:06:42] Checked status. Active codes in state: ['FCRST-00-000']
- [15:06:52] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:06:56] Reset dropdown to Normal.
- [15:06:56] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:07:01] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:07:06] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:07:11] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:07:16] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:07:21] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:07:26] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:07:31] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:07:36] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:07:42] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:07:47] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:07:52] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:07:52] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HP Seal Failure",
      "possible_causes": "Gland seal wear on HP casing outer shaft, HP stage-to-stage labyrinth seal wear, Excessive shaft vibration damaging HP seals, Thermal transient casing distortion",
      "observations_analysis": "The observations indicate a decrease in power output across the HP, IP, and LP turbines, as well as a reduction in steam turbine net power and reheater heat duty. These symptoms align with the effects of an HP Seal Failure, where the integrity of the seals is compromised, leading to inefficiencies in steam flow and energy conversion.",
      "recommendations": "Conduct a thorough inspection of the HP seals, focusing on the gland seal and stage-to-stage labyrinth seals. Check for signs of wear or damage. Monitor shaft vibrations and assess for any thermal distortions in the casing. Implement corrective measures such as seal replacement or realignment to restore optimal turbine performance.",
      "fault_code": "FCRST-ME-004",
      "analysis_flag": true
    }
  ]
}
```

---

### 7. HP Terminal Attemperator Failure (R) (`FCRST-ME-011`)
- **Status**: **❌ FAILURE**
- **Induced Time**: `2026-06-25 15:07:54`
- **Resolved Time**: `2026-06-25 15:10:49`

#### Event Timeline
- [15:07:54] Induced fault 'HP Terminal Attemperator Failure (R)' (FCRST-ME-011).
- [15:08:04] Checked status. Active codes in state: ['FCRST-00-000']
- [15:08:14] Checked status. Active codes in state: ['FCRST-00-000']
- [15:08:24] Checked status. Active codes in state: ['FCRST-00-000']
- [15:08:34] Checked status. Active codes in state: ['FCRST-00-000']
- [15:08:44] Checked status. Active codes in state: ['FCRST-00-000']
- [15:08:54] Checked status. Active codes in state: ['FCRST-00-000']
- [15:09:04] Checked status. Active codes in state: ['FCRST-OT-003']
- [15:09:04] Incorrect fault code detected. Reduced max timeout to 120s.
- [15:09:14] Checked status. Active codes in state: ['FCRST-OT-003']
- [15:09:24] Checked status. Active codes in state: ['FCRST-OT-003']
- [15:09:34] Checked status. Active codes in state: ['FCRST-OT-003']
- [15:09:44] Checked status. Active codes in state: ['FCRST-OT-003']
- [15:09:54] Checked status. Active codes in state: ['FCRST-OT-003']
- [15:09:54] Timeout reached. Played chime sound.
- [15:09:58] Reset dropdown to Normal.
- [15:09:58] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:10:03] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:10:08] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:10:13] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:10:19] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:10:24] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:10:29] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:10:34] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:10:39] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:10:44] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:10:49] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:10:49] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HRSG Fouling",
      "possible_causes": "Soot or ash deposition on gas side of tubes, Internal tube scaling or corrosion, Poor gas distribution inside casing, Inadequate tube sootblowing maintenance",
      "observations_analysis": "The observations indicate a decrease in economizer discharge water temperature, economizer heat duty, and steam turbine net power, while there is an increase in evaporator heat duty and stack flue gas temperature. These changes are consistent with HRSG fouling, where soot or ash deposition and internal scaling reduce heat transfer efficiency, leading to lower temperatures and power output.",
      "recommendations": "It is recommended to perform regular sootblowing and maintenance to remove deposits from the tubes. Inspect and clean the internal surfaces of the tubes to prevent scaling and corrosion. Ensure proper gas distribution within the casing to optimize heat transfer efficiency.",
      "fault_code": "FCRST-OT-003",
      "analysis_flag": true
    }
  ]
}
```

---

### 8. HRH Terminal Attemperator Failure (R) (`FCRST-ME-012`)
- **Status**: **❌ FAILURE**
- **Induced Time**: `2026-06-25 15:10:51`
- **Resolved Time**: `2026-06-25 15:13:51`

#### Event Timeline
- [15:10:51] Induced fault 'HRH Terminal Attemperator Failure (R)' (FCRST-ME-012).
- [15:11:01] Checked status. Active codes in state: ['FCRST-00-000']
- [15:11:11] Checked status. Active codes in state: ['FCRST-00-000']
- [15:11:21] Checked status. Active codes in state: ['FCRST-00-000']
- [15:11:31] Checked status. Active codes in state: ['FCRST-00-000']
- [15:11:41] Checked status. Active codes in state: ['FCRST-00-000']
- [15:11:51] Checked status. Active codes in state: ['FCRST-00-000']
- [15:12:01] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:12:01] Incorrect fault code detected. Reduced max timeout to 120s.
- [15:12:11] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:12:21] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:12:31] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:12:41] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:12:51] Checked status. Active codes in state: ['FCRST-ME-004']
- [15:12:51] Timeout reached. Played chime sound.
- [15:12:55] Reset dropdown to Normal.
- [15:12:55] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:13:01] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:13:06] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:13:11] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:13:16] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:13:21] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:13:26] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:13:31] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:13:36] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:13:41] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:13:46] Alignment Phase - Checked status. Active codes: ['FCRST-ME-004']
- [15:13:51] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:13:51] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HP Seal Failure",
      "possible_causes": "Gland seal wear on HP casing outer shaft, HP stage-to-stage labyrinth seal wear, Excessive shaft vibration damaging HP seals, Thermal transient casing distortion",
      "observations_analysis": "The observations indicate a decrease in power output across the HP, IP, and LP turbines, as well as a reduction in steam turbine net power and reheater heat duty. These symptoms align with the effects of an HP Seal Failure, where the integrity of the seals is compromised, leading to inefficiencies in steam flow and energy conversion.",
      "recommendations": "Conduct a thorough inspection of the HP casing outer shaft and stage-to-stage labyrinth seals for wear and damage. Monitor and address any excessive shaft vibrations to prevent further seal damage. Evaluate the system for any thermal transient issues that may cause casing distortion. Implement regular maintenance checks to ensure seal integrity and optimal turbine performance.",
      "fault_code": "FCRST-ME-004",
      "analysis_flag": true
    }
  ]
}
```

---

### 9. HRSG Fouling (R) (`FCRST-OT-003`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 15:13:53`
- **Resolved Time**: `2026-06-25 15:16:04`

#### Event Timeline
- [15:13:53] Induced fault 'HRSG Fouling (R)' (FCRST-OT-003).
- [15:14:03] Checked status. Active codes in state: ['FCRST-00-000']
- [15:14:13] Checked status. Active codes in state: ['FCRST-00-000']
- [15:14:23] Checked status. Active codes in state: ['FCRST-00-000']
- [15:14:34] Checked status. Active codes in state: ['FCRST-00-000']
- [15:14:44] Checked status. Active codes in state: ['FCRST-00-000']
- [15:14:54] Checked status. Active codes in state: ['FCRST-00-000']
- [15:15:04] Checked status. Active codes in state: ['FCRST-OT-003']
- [15:15:08] Reset dropdown to Normal.
- [15:15:08] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:15:13] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:15:18] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:15:23] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:15:28] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:15:33] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:15:38] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:15:43] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:15:48] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:15:53] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:15:58] Alignment Phase - Checked status. Active codes: ['FCRST-OT-003']
- [15:16:04] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:16:04] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HRSG Fouling",
      "possible_causes": "Soot or ash deposition on gas side of tubes, Internal tube scaling or corrosion, Poor gas distribution inside casing, Inadequate tube sootblowing maintenance",
      "observations_analysis": "The observations indicate a decrease in economizer discharge water temperature, economizer heat duty, and steam turbine net power, while there is an increase in evaporator heat duty and stack flue gas temperature. These changes are consistent with HRSG fouling, where the heat transfer efficiency is reduced due to deposits or scaling, leading to decreased performance in certain areas and increased temperatures in others.",
      "recommendations": "It is recommended to perform regular maintenance and cleaning of the HRSG components to remove soot, ash, and scale deposits. Improving the sootblowing schedule and ensuring proper gas distribution can also help mitigate the fouling effects. Regular inspections and monitoring of the HRSG performance parameters should be conducted to detect early signs of fouling.",
      "fault_code": "FCRST-OT-003",
      "analysis_flag": true
    }
  ]
}
```

---

### 10. IP Blade Deformation (R) (`FCRST-ME-002`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 15:16:06`
- **Resolved Time**: `2026-06-25 15:18:06`

#### Event Timeline
- [15:16:06] Induced fault 'IP Blade Deformation (R)' (FCRST-ME-002).
- [15:16:16] Checked status. Active codes in state: ['FCRST-00-000']
- [15:16:26] Checked status. Active codes in state: ['FCRST-00-000']
- [15:16:36] Checked status. Active codes in state: ['FCRST-00-000']
- [15:16:46] Checked status. Active codes in state: ['FCRST-00-000']
- [15:16:56] Checked status. Active codes in state: ['FCRST-00-000']
- [15:17:06] Checked status. Active codes in state: ['FCRST-ME-002']
- [15:17:10] Reset dropdown to Normal.
- [15:17:10] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [15:17:15] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [15:17:20] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [15:17:25] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [15:17:30] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [15:17:35] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [15:17:40] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [15:17:45] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [15:17:50] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [15:17:56] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [15:18:01] Alignment Phase - Checked status. Active codes: ['FCRST-ME-002']
- [15:18:06] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:18:06] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "IP Blade Deformation",
      "possible_causes": "Creep or mechanical fatigue of IP rotor blades, Corrosion fatigue or erosion in IP section, IP turbine blade tip clearance rubbing, Scale buildup on IP guide vanes",
      "observations_analysis": "The decrease in IP turbine power output suggests a potential deformation of the IP blades. This could be due to mechanical fatigue or corrosion, which are common issues in the IP section of a fully connected reheat steam turbine. The normal operation of other parameters indicates that the issue is localized to the IP section.",
      "recommendations": "Conduct a thorough inspection of the IP rotor blades for signs of creep or mechanical fatigue. Check for corrosion or erosion in the IP section and inspect the blade tip clearance for any rubbing. Additionally, examine the IP guide vanes for scale buildup and perform necessary maintenance or replacements.",
      "fault_code": "FCRST-ME-002",
      "analysis_flag": true
    }
  ]
}
```

---

### 11. IP Seal Failure (R) (`FCRST-ME-005`)
- **Status**: **❌ FAILURE**
- **Induced Time**: `2026-06-25 15:18:08`
- **Resolved Time**: `2026-06-25 15:21:03`

#### Event Timeline
- [15:18:08] Induced fault 'IP Seal Failure (R)' (FCRST-ME-005).
- [15:18:18] Checked status. Active codes in state: ['FCRST-00-000']
- [15:18:28] Checked status. Active codes in state: ['FCRST-00-000']
- [15:18:38] Checked status. Active codes in state: ['FCRST-00-000']
- [15:18:48] Checked status. Active codes in state: ['FCRST-00-000']
- [15:18:58] Checked status. Active codes in state: ['FCRST-00-000']
- [15:19:08] Checked status. Active codes in state: ['FCRST-00-000']
- [15:19:18] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:19:18] Incorrect fault code detected. Reduced max timeout to 120s.
- [15:19:28] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:19:38] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:19:48] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:19:58] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:20:08] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:20:08] Timeout reached. Played chime sound.
- [15:20:12] Reset dropdown to Normal.
- [15:20:12] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:20:17] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:20:22] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:20:27] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:20:32] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:20:38] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:20:43] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:20:48] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:20:53] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:20:58] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:21:03] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:21:03] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Steam Pressure Loss",
      "possible_causes": "Steam pipe leak before HP inlet, Steam strainer blockage, Main steam stop valve failure, Piping pressure drops due to corrosion",
      "observations_analysis": "The observations indicate a decrease in steam pressure and flow at the HP turbine inlet, which aligns with the symptoms of steam pressure loss. This could be due to a leak in the steam pipe, blockage in the steam strainer, failure of the main steam stop valve, or pressure drops caused by corrosion in the piping.",
      "recommendations": "Conduct a thorough inspection of the steam pipes for leaks and corrosion. Check the steam strainer for blockages and ensure the main steam stop valve is functioning correctly. Regular maintenance and monitoring of these components can prevent future occurrences.",
      "fault_code": "FCRST-HY-002",
      "analysis_flag": true
    }
  ]
}
```

---

### 12. LP Blade Deformation (R) (`FCRST-ME-003`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 15:21:05`
- **Resolved Time**: `2026-06-25 15:23:05`

#### Event Timeline
- [15:21:05] Induced fault 'LP Blade Deformation (R)' (FCRST-ME-003).
- [15:21:15] Checked status. Active codes in state: ['FCRST-00-000']
- [15:21:25] Checked status. Active codes in state: ['FCRST-00-000']
- [15:21:35] Checked status. Active codes in state: ['FCRST-00-000']
- [15:21:45] Checked status. Active codes in state: ['FCRST-00-000']
- [15:21:55] Checked status. Active codes in state: ['FCRST-00-000']
- [15:22:05] Checked status. Active codes in state: ['FCRST-ME-003']
- [15:22:09] Reset dropdown to Normal.
- [15:22:09] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [15:22:14] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [15:22:19] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [15:22:24] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [15:22:30] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [15:22:35] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [15:22:40] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [15:22:45] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [15:22:50] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [15:22:55] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [15:23:00] Alignment Phase - Checked status. Active codes: ['FCRST-ME-003']
- [15:23:05] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:23:05] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "LP Blade Deformation",
      "possible_causes": "Erosion from water droplets in LP casing, LP turbine blade fatigue or crack propagation, Mechanical rubbing in LP casing shroud, Corrosion pitting on LP exhaust stages",
      "observations_analysis": "The observations indicate a decrease in LP turbine power output, which aligns with the effects of LP Blade Deformation. This deformation can be caused by factors such as erosion, fatigue, mechanical rubbing, or corrosion, all of which can lead to inefficiencies and reduced power output.",
      "recommendations": "Conduct a thorough inspection of the LP turbine blades for signs of erosion, fatigue, or corrosion. Implement regular maintenance schedules to prevent mechanical rubbing and address any identified issues promptly to restore optimal turbine performance.",
      "fault_code": "FCRST-ME-003",
      "analysis_flag": true
    }
  ]
}
```

---

### 13. LP Seal Failure (R) (`FCRST-ME-006`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 15:23:07`
- **Resolved Time**: `2026-06-25 15:25:07`

#### Event Timeline
- [15:23:07] Induced fault 'LP Seal Failure (R)' (FCRST-ME-006).
- [15:23:17] Checked status. Active codes in state: ['FCRST-00-000']
- [15:23:27] Checked status. Active codes in state: ['FCRST-00-000']
- [15:23:37] Checked status. Active codes in state: ['FCRST-00-000']
- [15:23:47] Checked status. Active codes in state: ['FCRST-00-000']
- [15:23:57] Checked status. Active codes in state: ['FCRST-00-000']
- [15:24:07] Checked status. Active codes in state: ['FCRST-ME-006']
- [15:24:11] Reset dropdown to Normal.
- [15:24:11] Alignment Phase - Checked status. Active codes: ['FCRST-ME-006']
- [15:24:16] Alignment Phase - Checked status. Active codes: ['FCRST-ME-006']
- [15:24:22] Alignment Phase - Checked status. Active codes: ['FCRST-ME-006']
- [15:24:27] Alignment Phase - Checked status. Active codes: ['FCRST-ME-006']
- [15:24:32] Alignment Phase - Checked status. Active codes: ['FCRST-ME-006']
- [15:24:37] Alignment Phase - Checked status. Active codes: ['FCRST-ME-006']
- [15:24:42] Alignment Phase - Checked status. Active codes: ['FCRST-ME-006']
- [15:24:47] Alignment Phase - Checked status. Active codes: ['FCRST-ME-006']
- [15:24:52] Alignment Phase - Checked status. Active codes: ['FCRST-ME-006']
- [15:24:57] Alignment Phase - Checked status. Active codes: ['FCRST-ME-006']
- [15:25:02] Alignment Phase - Checked status. Active codes: ['FCRST-ME-006']
- [15:25:07] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:25:07] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "LP Seal Failure",
      "possible_causes": "Labyrinth packing degradation in LP section, Shaft vibration damaging LP gland seals, LP casing joint leakage or seal wear, Water droplets erosion on seal fins",
      "observations_analysis": "The observations indicate a decrease in LP turbine inlet steam flow and LP turbine power output, which are consistent with the effects of an LP Seal Failure. This suggests that the integrity of the seals in the LP section is compromised, leading to steam leakage and reduced efficiency.",
      "recommendations": "Inspect and replace any degraded labyrinth packing in the LP section. Check for and address any shaft vibrations that may be damaging the LP gland seals. Examine the LP casing joints for leakage or wear and repair as necessary. Investigate and mitigate any water droplet erosion on seal fins to prevent further damage.",
      "fault_code": "FCRST-ME-006",
      "analysis_flag": true
    }
  ]
}
```

---

### 14. Reheater Tube Failure (R) (`FCRST-ME-009`)
- **Status**: **❌ FAILURE**
- **Induced Time**: `2026-06-25 15:25:09`
- **Resolved Time**: `2026-06-25 15:28:10`

#### Event Timeline
- [15:25:09] Induced fault 'Reheater Tube Failure (R)' (FCRST-ME-009).
- [15:25:19] Checked status. Active codes in state: ['FCRST-00-000']
- [15:25:29] Checked status. Active codes in state: ['FCRST-00-000']
- [15:25:39] Checked status. Active codes in state: ['FCRST-00-000']
- [15:25:49] Checked status. Active codes in state: ['FCRST-00-000']
- [15:26:00] Checked status. Active codes in state: ['FCRST-00-000']
- [15:26:10] Checked status. Active codes in state: ['FCRST-00-000']
- [15:26:20] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:26:20] Incorrect fault code detected. Reduced max timeout to 120s.
- [15:26:30] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:26:40] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:26:50] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:27:00] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:27:10] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:27:10] Timeout reached. Played chime sound.
- [15:27:14] Reset dropdown to Normal.
- [15:27:14] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:27:19] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:27:24] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:27:29] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:27:34] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:27:39] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:27:44] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:27:49] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:27:54] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:27:59] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:28:05] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:28:10] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:28:10] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Steam Pressure Loss",
      "possible_causes": "Steam pipe leak before HP inlet, Steam strainer blockage, Main steam stop valve failure, Piping pressure drops due to corrosion",
      "observations_analysis": "The observations indicate a decrease in steam pressure and flow at the HP turbine inlet, along with reduced power output across the turbines. These symptoms align with the context of steam pressure loss, suggesting potential issues such as leaks, blockages, or valve failures.",
      "recommendations": "Conduct a thorough inspection of the steam pipes for leaks, check and clean the steam strainer, inspect the main steam stop valve for proper operation, and assess the piping for signs of corrosion that could lead to pressure drops.",
      "fault_code": "FCRST-HY-002",
      "analysis_flag": true
    }
  ]
}
```

---

### 15. Steam Pressure Loss (R) (`FCRST-HY-002`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 15:28:12`
- **Resolved Time**: `2026-06-25 15:30:12`

#### Event Timeline
- [15:28:12] Induced fault 'Steam Pressure Loss (R)' (FCRST-HY-002).
- [15:28:22] Checked status. Active codes in state: ['FCRST-00-000']
- [15:28:32] Checked status. Active codes in state: ['FCRST-00-000']
- [15:28:42] Checked status. Active codes in state: ['FCRST-00-000']
- [15:28:52] Checked status. Active codes in state: ['FCRST-00-000']
- [15:29:02] Checked status. Active codes in state: ['FCRST-00-000']
- [15:29:12] Checked status. Active codes in state: ['FCRST-HY-002']
- [15:29:16] Reset dropdown to Normal.
- [15:29:16] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:29:21] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:29:26] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:29:31] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:29:36] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:29:41] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:29:46] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:29:51] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:29:57] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:30:02] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:30:07] Alignment Phase - Checked status. Active codes: ['FCRST-HY-002']
- [15:30:12] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:30:12] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Steam Pressure Loss",
      "possible_causes": "Steam pipe leak before HP inlet, Steam strainer blockage, Main steam stop valve failure, Piping pressure drops due to corrosion",
      "observations_analysis": "The observations indicate a decrease in steam pressure and flow at the HP turbine inlet, along with reduced power output across the turbines. These symptoms align with the typical effects of steam pressure loss, suggesting issues such as leaks, blockages, or valve failures.",
      "recommendations": "Conduct a thorough inspection of the steam pipes for leaks, check and clean the steam strainer, inspect the main steam stop valve for proper operation, and assess the piping for signs of corrosion or pressure drops.",
      "fault_code": "FCRST-HY-002",
      "analysis_flag": true
    }
  ]
}
```

---

### 16. Superheater Tube Failure (R) (`FCRST-ME-007`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 15:30:14`
- **Resolved Time**: `2026-06-25 15:32:24`

#### Event Timeline
- [15:30:14] Induced fault 'Superheater Tube Failure (R)' (FCRST-ME-007).
- [15:30:24] Checked status. Active codes in state: ['FCRST-00-000']
- [15:30:34] Checked status. Active codes in state: ['FCRST-00-000']
- [15:30:44] Checked status. Active codes in state: ['FCRST-00-000']
- [15:30:54] Checked status. Active codes in state: ['FCRST-00-000']
- [15:31:04] Checked status. Active codes in state: ['FCRST-00-000']
- [15:31:14] Checked status. Active codes in state: ['FCRST-00-000']
- [15:31:24] Checked status. Active codes in state: ['FCRST-ME-007']
- [15:31:28] Reset dropdown to Normal.
- [15:31:28] Alignment Phase - Checked status. Active codes: ['FCRST-ME-007']
- [15:31:33] Alignment Phase - Checked status. Active codes: ['FCRST-ME-007']
- [15:31:38] Alignment Phase - Checked status. Active codes: ['FCRST-ME-007']
- [15:31:43] Alignment Phase - Checked status. Active codes: ['FCRST-ME-007']
- [15:31:48] Alignment Phase - Checked status. Active codes: ['FCRST-ME-007']
- [15:31:54] Alignment Phase - Checked status. Active codes: ['FCRST-ME-007']
- [15:31:59] Alignment Phase - Checked status. Active codes: ['FCRST-ME-007']
- [15:32:04] Alignment Phase - Checked status. Active codes: ['FCRST-ME-007']
- [15:32:09] Alignment Phase - Checked status. Active codes: ['FCRST-ME-007']
- [15:32:14] Alignment Phase - Checked status. Active codes: ['FCRST-ME-007']
- [15:32:19] Alignment Phase - Checked status. Active codes: ['FCRST-ME-007']
- [15:32:24] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:32:24] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Superheater Tube Failure",
      "possible_causes": "Thermal fatigue of superheater tube welds, High temperature creep rupture in superheater section, Localized flue gas erosion on superheater tubes, Scaling inside superheater causing overheating",
      "observations_analysis": "The observations indicate a decrease in key performance metrics such as hp_superheater_outlet_temperature_main_steam, hp_turbine_inlet_steam_flow, and steam_turbine_net_power, which are consistent with a superheater tube failure. The increase in stack_flue_gas_temperature and water_flow_rate further supports this diagnosis, as these are typical responses to compromised heat transfer efficiency in the superheater section.",
      "recommendations": "Conduct a thorough inspection of the superheater tubes for signs of thermal fatigue, creep rupture, and erosion. Implement regular maintenance schedules to prevent scaling and ensure optimal heat transfer. Consider upgrading materials or design to withstand high temperatures and reduce the risk of future failures.",
      "fault_code": "FCRST-ME-007",
      "analysis_flag": true
    }
  ]
}
```

---

### 17. Vacuum Loss (R) (`FCRST-HY-003`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-25 15:32:26`
- **Resolved Time**: `2026-06-25 15:34:36`

#### Event Timeline
- [15:32:26] Induced fault 'Vacuum Loss (R)' (FCRST-HY-003).
- [15:32:36] Checked status. Active codes in state: ['FCRST-00-000']
- [15:32:46] Checked status. Active codes in state: ['FCRST-00-000']
- [15:32:56] Checked status. Active codes in state: ['FCRST-00-000']
- [15:33:06] Checked status. Active codes in state: ['FCRST-00-000']
- [15:33:16] Checked status. Active codes in state: ['FCRST-00-000']
- [15:33:26] Checked status. Active codes in state: ['FCRST-00-000']
- [15:33:36] Checked status. Active codes in state: ['FCRST-HY-003']
- [15:33:40] Reset dropdown to Normal.
- [15:33:40] Alignment Phase - Checked status. Active codes: ['FCRST-HY-003']
- [15:33:45] Alignment Phase - Checked status. Active codes: ['FCRST-HY-003']
- [15:33:51] Alignment Phase - Checked status. Active codes: ['FCRST-HY-003']
- [15:33:56] Alignment Phase - Checked status. Active codes: ['FCRST-HY-003']
- [15:34:01] Alignment Phase - Checked status. Active codes: ['FCRST-HY-003']
- [15:34:06] Alignment Phase - Checked status. Active codes: ['FCRST-HY-003']
- [15:34:11] Alignment Phase - Checked status. Active codes: ['FCRST-HY-003']
- [15:34:16] Alignment Phase - Checked status. Active codes: ['FCRST-HY-003']
- [15:34:21] Alignment Phase - Checked status. Active codes: ['FCRST-HY-003']
- [15:34:26] Alignment Phase - Checked status. Active codes: ['FCRST-HY-003']
- [15:34:31] Alignment Phase - Checked status. Active codes: ['FCRST-HY-003']
- [15:34:36] Alignment Phase - Checked status. Active codes: ['FCRST-00-000']
- [15:34:36] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Vacuum Loss",
      "possible_causes": "Condenser cooling water pump trip, Condenser tube fouling or scaling, Air ingress through LP casing seals, Vacuum pump or ejector malfunction, Excessive cooling water inlet temperature",
      "observations_analysis": "The observations indicate a decrease in lp_turbine_power_output and steam_turbine_net_power, along with an increase in lp_turbine_exhaust_enthalpy, lp_turbine_exhaust_pressure_condenser_pressure, and lp_turbine_exhaust_temperature. These changes are consistent with a vacuum loss in the condenser, which can be caused by issues such as a malfunctioning vacuum pump or ejector, air ingress through LP casing seals, or problems with the condenser cooling system.",
      "recommendations": "Inspect and repair or replace the vacuum pump or ejector if malfunctioning. Check for and seal any air ingress points in the LP casing seals. Ensure the condenser cooling water pump is operational and that there is no fouling or scaling in the condenser tubes. Monitor and control the cooling water inlet temperature to prevent excessive temperatures.",
      "fault_code": "FCRST-HY-003",
      "analysis_flag": true
    }
  ]
}
```

---
