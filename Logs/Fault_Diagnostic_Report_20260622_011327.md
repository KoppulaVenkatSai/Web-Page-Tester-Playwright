# AssetSense Fault Diagnostic Test Report

## Metadata
- **Test Date/Time**: `2026-06-22 01:13:27`
- **Last Updated**: `2026-06-22 01:26:34`
- **Elapsed Duration**: `13m 6s`
- **Target Asset**: `Steam Turbine Block - 1 (AS-FCRST-DT-01)`
- **Environment**: Playwright Test Runner (Brave Browser)

---

## Executive Summary
| Status | Count |
|---|---|
| ✅ Success | 4 |
| ❌ Fail / Timeout | 1 |
| **Total Tested** | **5** |

---

## Detailed Summary Table
| # | Fault Name | Fault Code | Status | Time to Detect | Time to Reset |
|---|---|---|---|---|---|
| 1 | Corrosion (R) | `FCRST-OT-002` | ✅ Success | 60.0s | 01:16:02 |
| 2 | Evaporator Tube Failure (R) | `FCRST-ME-008` | ✅ Success | 60.0s | 01:19:09 |
| 3 | Feedwater Flow Restriction (R) | `FCRST-HY-001` | ❌ Fail | N/A | 01:22:36 |
| 4 | HP Blade Deformation (R) | `FCRST-ME-001` | ✅ Success | 60.0s | 01:23:42 |
| 5 | HP Interstage Attemperator Failure (R) | `FCRST-ME-010` | ✅ Success | 60.0s | 01:26:34 |

---

## Diagnostic Logs per Fault Option

### 1. Corrosion (R) (`FCRST-OT-002`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-22 01:13:27`
- **Resolved Time**: `2026-06-22 01:16:02`

#### Event Timeline
- [01:13:27] Induced fault 'Corrosion (R)' (FCRST-OT-002).
- [01:13:37] Checked status. Active codes in state: []
- [01:13:47] Checked status. Active codes in state: []
- [01:13:57] Checked status. Active codes in state: []
- [01:14:07] Checked status. Active codes in state: []
- [01:14:17] Checked status. Active codes in state: []
- [01:14:27] Checked status. Active codes in state: ['FCRST-OT-002']
- [01:14:31] Reset dropdown to Normal.
- [01:16:02] Graphs successfully aligned back to Normal.

#### UI Analysis Displayed
```text
Fault Analysis
FCRST-OT-002
Likely Fault:
Corrosion (FCRST-OT-002)
Possible Causes:
High oxygen level in boiler feedwater, Acidic attack on economizer tubes, Sulfur dew point corrosion on flue gas side, Condensation of acidic gases during shutdown
Observations Analysis:
The current data indicates a decrease in economizer heat duty, which suggests potential corrosion issues affecting the efficiency of heat transfer. The presence of high oxygen levels in the boiler feedwater could lead to accelerated corrosion, while acidic conditions may be impacting the economizer tubes. Additionally, sulfur dew point corrosion and condensation of acidic gases during shutdown periods could further exacerbate the corrosion problem.
Recommendations:
It is recommended to monitor and control the oxygen levels in the boiler feedwater to minimize corrosion risks. Regular inspections of the economizer tubes should be conducted to identify any signs of acidic attack. Implementing measures to manage flue gas temperatures and prevent condensation during shutdowns can also help mitigate corrosion effects.
```

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Corrosion",
      "possible_causes": "High oxygen level in boiler feedwater, Acidic attack on economizer tubes, Sulfur dew point corrosion on flue gas side, Condensation of acidic gases during shutdown",
      "observations_analysis": "The current data indicates a decrease in economizer heat duty, which suggests potential corrosion issues affecting the efficiency of heat transfer. The presence of high oxygen levels in the boiler feedwater could lead to accelerated corrosion, while acidic conditions may be impacting the economizer tubes. Additionally, sulfur dew point corrosion and condensation of acidic gases during shutdown periods could further exacerbate the corrosion problem.",
      "recommendations": "It is recommended to monitor and control the oxygen levels in the boiler feedwater to minimize corrosion risks. Regular inspections of the economizer tubes should be conducted to identify any signs of acidic attack. Implementing measures to manage flue gas temperatures and prevent condensation during shutdowns can also help mitigate corrosion effects.",
      "fault_code": "FCRST-OT-002",
      "analysis_flag": true
    }
  ]
}
```

---

### 2. Evaporator Tube Failure (R) (`FCRST-ME-008`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-22 01:16:04`
- **Resolved Time**: `2026-06-22 01:19:09`

#### Event Timeline
- [01:16:04] Induced fault 'Evaporator Tube Failure (R)' (FCRST-ME-008).
- [01:16:14] Checked status. Active codes in state: ['FCRST-00-000']
- [01:16:24] Checked status. Active codes in state: ['FCRST-00-000']
- [01:16:34] Checked status. Active codes in state: ['FCRST-00-000']
- [01:16:44] Checked status. Active codes in state: ['FCRST-00-000']
- [01:16:54] Checked status. Active codes in state: ['FCRST-00-000']
- [01:17:04] Checked status. Active codes in state: ['FCRST-ME-008']
- [01:17:08] Reset dropdown to Normal.
- [01:19:09] Graphs successfully aligned back to Normal.

#### UI Analysis Displayed
```text
Fault Analysis
FCRST-ME-008
Likely Fault:
Evaporator Tube Failure (FCRST-ME-008)
Possible Causes:
Waterwall tube corrosion or pitting, Thermal fatigue of evaporator tubes, Scale formation causing localized tube overheating, High stress due to pressure transients
Observations Analysis:
The current data indicates a decrease in evaporator steam generation rate and fluctuations in pressure readings, which are consistent with potential evaporator tube failures. Additionally, the increase in stack flue gas temperature suggests that the heat exchange process is being compromised, likely due to overheating or failure of the evaporator tubes.
Recommendations:
Conduct a thorough inspection of the evaporator tubes for signs of corrosion, pitting, or thermal fatigue. Implement regular maintenance checks to monitor for scale formation and pressure transients. Consider upgrading materials or protective coatings to enhance tube longevity.
```

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Evaporator Tube Failure",
      "possible_causes": "Waterwall tube corrosion or pitting, Thermal fatigue of evaporator tubes, Scale formation causing localized tube overheating, High stress due to pressure transients",
      "observations_analysis": "The current data indicates a decrease in evaporator steam generation rate and fluctuations in pressure readings, which are consistent with potential evaporator tube failures. Additionally, the increase in stack flue gas temperature suggests that the heat exchange process is being compromised, likely due to overheating or failure of the evaporator tubes.",
      "recommendations": "Conduct a thorough inspection of the evaporator tubes for signs of corrosion, pitting, or thermal fatigue. Implement regular maintenance checks to monitor for scale formation and pressure transients. Consider upgrading materials or protective coatings to enhance tube longevity.",
      "fault_code": "FCRST-ME-008",
      "analysis_flag": true
    }
  ]
}
```

---

### 3. Feedwater Flow Restriction (R) (`FCRST-HY-001`)
- **Status**: **❌ FAILURE**
- **Induced Time**: `2026-06-22 01:19:11`
- **Resolved Time**: `2026-06-22 01:22:36`

#### Event Timeline
- [01:19:11] Induced fault 'Feedwater Flow Restriction (R)' (FCRST-HY-001).
- [01:19:21] Checked status. Active codes in state: ['FCRST-00-000']
- [01:19:31] Checked status. Active codes in state: ['FCRST-00-000']
- [01:19:41] Checked status. Active codes in state: ['FCRST-00-000']
- [01:19:51] Checked status. Active codes in state: ['FCRST-00-000']
- [01:20:01] Checked status. Active codes in state: ['FCRST-00-000']
- [01:20:11] Checked status. Active codes in state: ['FCRST-00-000']
- [01:20:21] Checked status. Active codes in state: ['FCRST-00-000']
- [01:20:31] Checked status. Active codes in state: ['FCRST-00-000']
- [01:20:41] Checked status. Active codes in state: ['FCRST-00-000']
- [01:20:51] Checked status. Active codes in state: ['FCRST-00-000']
- [01:21:01] Checked status. Active codes in state: ['FCRST-00-000']
- [01:21:11] Checked status. Active codes in state: ['FCRST-00-000']
- [01:21:11] Timeout reached. Played chime sound.
- [01:21:15] Reset dropdown to Normal.
- [01:22:36] Graphs successfully aligned back to Normal.

*No UI Analysis display was captured due to timeout/failure.*

---

### 4. HP Blade Deformation (R) (`FCRST-ME-001`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-22 01:22:38`
- **Resolved Time**: `2026-06-22 01:23:42`

#### Event Timeline
- [01:22:38] Induced fault 'HP Blade Deformation (R)' (FCRST-ME-001).
- [01:22:48] Checked status. Active codes in state: ['FCRST-00-000']
- [01:22:58] Checked status. Active codes in state: ['FCRST-00-000']
- [01:23:08] Checked status. Active codes in state: ['FCRST-00-000']
- [01:23:18] Checked status. Active codes in state: ['FCRST-00-000']
- [01:23:28] Checked status. Active codes in state: ['FCRST-00-000']
- [01:23:38] Checked status. Active codes in state: ['FCRST-ME-001']
- [01:23:42] Reset dropdown to Normal.
- [01:23:42] Graphs successfully aligned back to Normal.

#### UI Analysis Displayed
```text
Fault Analysis
FCRST-ME-001
Likely Fault:
HP Blade Deformation (FCRST-ME-001)
Possible Causes:
Thermal stress or creep deformation on HP rotor, HP turbine blade erosion or solid particle impact, Shroud or tip rubbing in HP section, Deposits on HP casing nozzle partition
Observations Analysis:
The current data indicates a decrease in hp_turbine_power_output and reheater_heat_duty, which suggests potential issues with the HP turbine blades. The observed parameters may point towards thermal stress or erosion affecting the blade integrity, leading to performance degradation.
Recommendations:
Conduct a thorough inspection of the HP turbine blades for signs of deformation or erosion. Evaluate the thermal conditions and operational parameters to identify any contributing factors. Implement corrective measures such as blade replacement or repairs, and consider optimizing operating conditions to mitigate further damage.
```

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HP Blade Deformation",
      "possible_causes": "Thermal stress or creep deformation on HP rotor, HP turbine blade erosion or solid particle impact, Shroud or tip rubbing in HP section, Deposits on HP casing nozzle partition",
      "observations_analysis": "The current data indicates a decrease in hp_turbine_power_output and reheater_heat_duty, which suggests potential issues with the HP turbine blades. The observed parameters may point towards thermal stress or erosion affecting the blade integrity, leading to performance degradation.",
      "recommendations": "Conduct a thorough inspection of the HP turbine blades for signs of deformation or erosion. Evaluate the thermal conditions and operational parameters to identify any contributing factors. Implement corrective measures such as blade replacement or repairs, and consider optimizing operating conditions to mitigate further damage.",
      "fault_code": "FCRST-ME-001",
      "analysis_flag": true
    }
  ]
}
```

---

### 5. HP Interstage Attemperator Failure (R) (`FCRST-ME-010`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-22 01:23:44`
- **Resolved Time**: `2026-06-22 01:26:34`

#### Event Timeline
- [01:23:44] Induced fault 'HP Interstage Attemperator Failure (R)' (FCRST-ME-010).
- [01:23:54] Checked status. Active codes in state: ['FCRST-ME-001']
- [01:24:04] Checked status. Active codes in state: ['FCRST-ME-001']
- [01:24:14] Checked status. Active codes in state: ['FCRST-ME-001']
- [01:24:24] Checked status. Active codes in state: ['FCRST-ME-001']
- [01:24:34] Checked status. Active codes in state: ['FCRST-ME-001']
- [01:24:44] Checked status. Active codes in state: ['FCRST-ME-010']
- [01:24:48] Reset dropdown to Normal.
- [01:26:34] Graphs successfully aligned back to Normal.

#### UI Analysis Displayed
```text
Fault Analysis
FCRST-ME-010
Likely Fault:
HP Interstage Attemperator Failure (FCRST-ME-010)
Possible Causes:
Attemperator spray control valve stuck open, Spray nozzle damage causing over-spraying, Spray water piping leak or control failure, Incorrect temperature transmitter calibration
Observations Analysis:
The current data indicates an increase in primary superheater heat duty while the secondary superheater heat duty has decreased. This suggests that there may be an issue with the attemperator system, potentially due to a stuck control valve or damage to the spray nozzle, leading to improper temperature control in the steam cycle.
Recommendations:
Inspect the attemperator spray control valve for proper operation and ensure it is not stuck open. Check the spray nozzles for any damage and replace if necessary. Additionally, verify the integrity of the spray water piping for leaks and ensure that the temperature transmitters are calibrated correctly.
```

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HP Interstage Attemperator Failure",
      "possible_causes": "Attemperator spray control valve stuck open, Spray nozzle damage causing over-spraying, Spray water piping leak or control failure, Incorrect temperature transmitter calibration",
      "observations_analysis": "The current data indicates an increase in primary superheater heat duty while the secondary superheater heat duty has decreased. This suggests that there may be an issue with the attemperator system, potentially due to a stuck control valve or damage to the spray nozzle, leading to improper temperature control in the steam cycle.",
      "recommendations": "Inspect the attemperator spray control valve for proper operation and ensure it is not stuck open. Check the spray nozzles for any damage and replace if necessary. Additionally, verify the integrity of the spray water piping for leaks and ensure that the temperature transmitters are calibrated correctly.",
      "fault_code": "FCRST-ME-010",
      "analysis_flag": true
    }
  ]
}
```

---
