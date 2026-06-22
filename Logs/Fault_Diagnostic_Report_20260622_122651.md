# AssetSense Fault Diagnostic Test Report

## Metadata
- **Test Date/Time**: `2026-06-22 12:26:51`
- **Last Updated**: `2026-06-22 13:14:25`
- **Elapsed Duration**: `47m 33s`
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
| 1 | Corrosion (R) | `FCRST-OT-002` | ❌ Fail | N/A | 12:30:31 |
| 2 | Evaporator Tube Failure (R) | `FCRST-ME-008` | ✅ Success | 60.0s | 12:33:38 |
| 3 | Feedwater Flow Restriction (R) | `FCRST-HY-001` | ✅ Success | 120.1s | 12:36:50 |
| 4 | HP Blade Deformation (R) | `FCRST-ME-001` | ✅ Success | 60.1s | 12:39:17 |
| 5 | HP Interstage Attemperator Failure (R) | `FCRST-ME-010` | ✅ Success | 60.0s | 12:42:09 |
| 6 | HP Seal Failure (R) | `FCRST-ME-004` | ✅ Success | 70.0s | 12:43:25 |
| 7 | HP Terminal Attemperator Failure (R) | `FCRST-ME-011` | ❌ Fail | N/A | 12:47:07 |
| 8 | HRH Terminal Attemperator Failure (R) | `FCRST-ME-012` | ✅ Success | 70.1s | 12:48:23 |
| 9 | HRSG Fouling (R) | `FCRST-OT-003` | ✅ Success | 100.0s | 12:52:05 |
| 10 | IP Blade Deformation (R) | `FCRST-ME-002` | ✅ Success | 60.0s | 12:53:11 |
| 11 | IP Seal Failure (R) | `FCRST-ME-005` | ✅ Success | 100.0s | 12:56:02 |
| 12 | LP Blade Deformation (R) | `FCRST-ME-003` | ✅ Success | 60.1s | 12:57:09 |
| 13 | LP Seal Failure (R) | `FCRST-ME-006` | ✅ Success | 60.0s | 12:59:10 |
| 14 | Reheater Tube Failure (R) | `FCRST-ME-009` | ❌ Fail | N/A | 13:02:37 |
| 15 | Steam Pressure Loss (R) | `FCRST-HY-002` | ✅ Success | 110.1s | 13:05:54 |
| 16 | Superheater Tube Failure (R) | `FCRST-ME-007` | ✅ Success | 100.0s | 13:09:30 |
| 17 | Vacuum Loss (R) | `FCRST-HY-003` | ❌ Fail | N/A | 13:14:25 |

---

## Diagnostic Logs per Fault Option

### 1. Corrosion (R) (`FCRST-OT-002`)
- **Status**: **❌ FAILURE**
- **Induced Time**: `2026-06-22 12:26:51`
- **Resolved Time**: `2026-06-22 12:30:31`

#### Event Timeline
- [12:26:51] Induced fault 'Corrosion (R)' (FCRST-OT-002).
- [12:27:01] Checked status. Active codes in state: []
- [12:27:11] Checked status. Active codes in state: []
- [12:27:21] Checked status. Active codes in state: []
- [12:27:31] Checked status. Active codes in state: []
- [12:27:41] Checked status. Active codes in state: []
- [12:27:51] Checked status. Active codes in state: ['FCRST-OT-100']
- [12:28:01] Checked status. Active codes in state: ['FCRST-OT-100']
- [12:28:11] Checked status. Active codes in state: ['FCRST-OT-100']
- [12:28:21] Checked status. Active codes in state: ['FCRST-OT-100']
- [12:28:31] Checked status. Active codes in state: ['FCRST-OT-100']
- [12:28:41] Checked status. Active codes in state: ['FCRST-OT-100']
- [12:28:51] Checked status. Active codes in state: ['FCRST-OT-100']
- [12:28:51] Timeout reached. Played chime sound.
- [12:28:55] Reset dropdown to Normal.
- [12:30:31] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
N/A
```

---

### 2. Evaporator Tube Failure (R) (`FCRST-ME-008`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-22 12:30:33`
- **Resolved Time**: `2026-06-22 12:33:38`

#### Event Timeline
- [12:30:33] Induced fault 'Evaporator Tube Failure (R)' (FCRST-ME-008).
- [12:30:43] Checked status. Active codes in state: ['FCRST-00-000']
- [12:30:53] Checked status. Active codes in state: ['FCRST-00-000']
- [12:31:03] Checked status. Active codes in state: ['FCRST-00-000']
- [12:31:13] Checked status. Active codes in state: ['FCRST-00-000']
- [12:31:23] Checked status. Active codes in state: ['FCRST-00-000']
- [12:31:33] Checked status. Active codes in state: ['FCRST-ME-008']
- [12:31:37] Reset dropdown to Normal.
- [12:33:38] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Evaporator Tube Failure",
      "possible_causes": "Waterwall tube corrosion or pitting, Thermal fatigue of evaporator tubes, Scale formation causing localized tube overheating, High stress due to pressure transients",
      "observations_analysis": "An analysis of the real-time data reveals critical indicators pointing to an Evaporator Tube Failure. There is a noticeable decrease in key steam-side performance metrics, including the evaporator steam generation rate, main steam flow rate, and heat duties of both primary and secondary superheaters, alongside drops in turbine crossover pressures (IP exhaust and LP inlet). This is accompanied by an increase in stack flue gas temperature, indicating that heat is not being efficiently transferred to the water/steam circuit due to the leak. Meanwhile, parameters such as economizer pressures, feedwater temperatures, and gas turbine exhaust specifications remain normal, which helps rule out external combustion or primary feedwater feed system issues and isolates the fault to the evaporator section.",
      "recommendations": "1. Perform immediate visual inspection and non-destructive testing (NDT), such as ultrasonic testing (UT), on the evaporator tubes to locate the breach and assess wall thickness. 2. Repair or replace the damaged tube sections to prevent further steam leakage. 3. Review and optimize boiler water chemistry controls to mitigate risks of scale formation, localized overheating, and corrosion/pitting. 4. Monitor pressure transients and start-up thermal ramps to reduce high mechanical stress and thermal fatigue on the tubes.",
      "fault_code": "FCRST-ME-008",
      "analysis_flag": true
    }
  ]
}
```

---

### 3. Feedwater Flow Restriction (R) (`FCRST-HY-001`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-22 12:33:40`
- **Resolved Time**: `2026-06-22 12:36:50`

#### Event Timeline
- [12:33:40] Induced fault 'Feedwater Flow Restriction (R)' (FCRST-HY-001).
- [12:33:50] Checked status. Active codes in state: ['FCRST-00-000']
- [12:34:00] Checked status. Active codes in state: ['FCRST-00-000']
- [12:34:10] Checked status. Active codes in state: ['FCRST-00-000']
- [12:34:20] Checked status. Active codes in state: ['FCRST-00-000']
- [12:34:30] Checked status. Active codes in state: ['FCRST-00-000']
- [12:34:40] Checked status. Active codes in state: ['FCRST-00-000']
- [12:34:50] Checked status. Active codes in state: ['FCRST-00-000']
- [12:35:00] Checked status. Active codes in state: ['FCRST-00-000']
- [12:35:10] Checked status. Active codes in state: ['FCRST-00-000']
- [12:35:20] Checked status. Active codes in state: ['FCRST-00-000']
- [12:35:30] Checked status. Active codes in state: ['FCRST-00-000']
- [12:35:40] Checked status. Active codes in state: ['FCRST-HY-001']
- [12:35:44] Reset dropdown to Normal.
- [12:36:50] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Feedwater Flow Restriction",
      "possible_causes": "Feedwater pump speed control failure, Strainer blockage in economizer feed line, Control valve stuck partially closed, Feedwater flow measurement sensor error",
      "observations_analysis": "Analysis of the real-time operational data indicates a clear anomaly characterized by a decrease in water flow rate, economizer heat duty, evaporator steam generation rate, and main steam flow rate. At the same time, there is a noticeable increase in stack flue gas temperature, which suggests that less heat is being transferred to the water cycle, leaving the flue gas hotter as it exits. Because critical parameters such as evaporator drum water pressure, turbine exhaust pressures, and various steam temperatures remain within normal ranges, the system points directly to a localized feedwater flow restriction rather than a broader system-wide thermal or mechanical failure.",
      "recommendations": "1. Perform a physical inspection and cleaning of the strainer in the economizer feed line to clear any potential blockages. 2. Inspect the feedwater control valve to ensure it is not stuck partially closed, and verify its actuator and positioner operation. 3. Check and calibrate the feedwater flow measurement sensor to rule out instrument error. 4. Evaluate the feedwater pump speed control system to ensure proper signal response and speed regulation.",
      "fault_code": "FCRST-HY-001",
      "analysis_flag": true
    }
  ]
}
```

---

### 4. HP Blade Deformation (R) (`FCRST-ME-001`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-22 12:36:52`
- **Resolved Time**: `2026-06-22 12:39:17`

#### Event Timeline
- [12:36:52] Induced fault 'HP Blade Deformation (R)' (FCRST-ME-001).
- [12:37:02] Checked status. Active codes in state: ['FCRST-00-000']
- [12:37:12] Checked status. Active codes in state: ['FCRST-00-000']
- [12:37:22] Checked status. Active codes in state: ['FCRST-00-000']
- [12:37:32] Checked status. Active codes in state: ['FCRST-00-000']
- [12:37:42] Checked status. Active codes in state: ['FCRST-00-000']
- [12:37:52] Checked status. Active codes in state: ['FCRST-ME-001']
- [12:37:56] Reset dropdown to Normal.
- [12:39:17] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HP Blade Deformation",
      "possible_causes": "Thermal stress or creep deformation on HP rotor, HP turbine blade erosion or solid particle impact, Shroud or tip rubbing in HP section, Deposits on HP casing nozzle partition",
      "observations_analysis": "An analysis of the real-time data indicates a notable decrease in 'hp_turbine_power_output' and 'reheater_heat_duty'. At the same time, all other core steam cycle parameters, including primary and secondary superheater performance, main steam flow rate, and economizer/evaporator metrics remain completely normal. This specific combination of normal system-wide parameters with a drop in HP power output and reheat section duty strongly indicates physical or aerodynamic degradation localized within the HP turbine stage, highly consistent with HP blade deformation.",
      "recommendations": "1. Schedule a visual and borescope inspection of the HP turbine internal stages to check for blade deformation, shroud rubbing, or solid particle erosion. 2. Perform a detailed thermodynamic audit to calculate the internal efficiency of the HP turbine. 3. Monitor vibration sensors and rotor expansion indicators for any anomalies pointing to rotor creep or shroud contact. 4. Review boiler steam chemistry to prevent further solid particle impact or chemical deposition on the HP nozzle partition.",
      "fault_code": "FCRST-ME-001",
      "analysis_flag": true
    }
  ]
}
```

---

### 5. HP Interstage Attemperator Failure (R) (`FCRST-ME-010`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-22 12:39:19`
- **Resolved Time**: `2026-06-22 12:42:09`

#### Event Timeline
- [12:39:19] Induced fault 'HP Interstage Attemperator Failure (R)' (FCRST-ME-010).
- [12:39:29] Checked status. Active codes in state: ['FCRST-00-000']
- [12:39:39] Checked status. Active codes in state: ['FCRST-00-000']
- [12:39:49] Checked status. Active codes in state: ['FCRST-00-000']
- [12:39:59] Checked status. Active codes in state: ['FCRST-00-000']
- [12:40:09] Checked status. Active codes in state: ['FCRST-00-000']
- [12:40:19] Checked status. Active codes in state: ['FCRST-ME-010']
- [12:40:23] Reset dropdown to Normal.
- [12:42:09] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HP Interstage Attemperator Failure",
      "possible_causes": "Attemperator spray control valve stuck open, Spray nozzle damage causing over-spraying, Spray water piping leak or control failure, Incorrect temperature transmitter calibration",
      "observations_analysis": "Based on the real-time thermal data of the fully connected reheat steam turbine, we observe a distinct decrease in the secondary superheater heat duty alongside an increase in the primary superheater heat duty. Crucial system parameters\u2014such as evaporator drum water pressure, main steam flow rate, and steam turbine net power\u2014remain completely normal. This specific signature indicates a localized thermal control anomaly between the superheater stages. Excessive or uncontrolled attemperation water is being sprayed into the steam path, drastically lowering the steam temperature before it enters the secondary superheater, which consequently reduces its heat duty while the primary stage attempts to compensate.",
      "recommendations": "1. Perform a stroke test on the HP attemperator spray control valve to check if it is mechanically stuck open or experiencing actuator failure. 2. Inspect the interstage attemperator spray nozzles for physical damage, wear, or erosion that could cause over-spraying. 3. Calibrate and test the temperature transmitters downstream of the attemperator to rule out false readings. 4. Verify the integrity of the spray water piping and the functionality of the associated control loop.",
      "fault_code": "FCRST-ME-010",
      "analysis_flag": true
    }
  ]
}
```

---

### 6. HP Seal Failure (R) (`FCRST-ME-004`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-22 12:42:11`
- **Resolved Time**: `2026-06-22 12:43:25`

#### Event Timeline
- [12:42:11] Induced fault 'HP Seal Failure (R)' (FCRST-ME-004).
- [12:42:21] Checked status. Active codes in state: ['FCRST-00-000']
- [12:42:31] Checked status. Active codes in state: ['FCRST-00-000']
- [12:42:41] Checked status. Active codes in state: ['FCRST-00-000']
- [12:42:51] Checked status. Active codes in state: ['FCRST-00-000']
- [12:43:01] Checked status. Active codes in state: ['FCRST-00-000']
- [12:43:11] Checked status. Active codes in state: ['FCRST-00-000']
- [12:43:21] Checked status. Active codes in state: ['FCRST-ME-004']
- [12:43:25] Reset dropdown to Normal.
- [12:43:25] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HP Seal Failure",
      "possible_causes": "Gland seal wear on HP casing outer shaft, HP stage-to-stage labyrinth seal wear, Excessive shaft vibration damaging HP seals, Thermal transient casing distortion",
      "observations_analysis": "A thorough analysis of the real-time operational data reveals a marked drop in power production across the entire steam turbine train. Specifically, we observe a decrease in the hp_turbine_power_output, ip_turbine_power_output, lp_turbine_power_output, and overall steam_turbine_net_power. Additionally, both lp_turbine_inlet_steam_flow and reheater_heat_duty have decreased. Meanwhile, upstream boiler and HRSG parameters\u2014such as feedwater pressures, economizer and superheater temperatures, and steam generation rates\u2014remain completely normal. This combination of normal steam generation and poor mechanical power output strongly indicates internal steam leakage inside the high-pressure turbine casing. The failure of HP seals allows steam to bypass the turbine stages, directly reducing the thermodynamic work extraction capacity of the HP turbine and starving the downstream IP and LP sections.",
      "recommendations": "1. Review turbine vibration monitoring logs to identify if excessive shaft vibration triggered the seal wear. 2. Inspect HP casing gland seals and stage-to-stage labyrinth seals for physical deterioration or rubbing during the next planned shutdown. 3. Evaluate startup, shutdown, and loading procedures to ensure thermal transients are managed to prevent casing distortion. 4. Coordinate a maintenance outage to replace worn seal assemblies and restore optimal clearance and turbine efficiency.",
      "fault_code": "FCRST-ME-004",
      "analysis_flag": true
    }
  ]
}
```

---

### 7. HP Terminal Attemperator Failure (R) (`FCRST-ME-011`)
- **Status**: **❌ FAILURE**
- **Induced Time**: `2026-06-22 12:43:27`
- **Resolved Time**: `2026-06-22 12:47:07`

#### Event Timeline
- [12:43:27] Induced fault 'HP Terminal Attemperator Failure (R)' (FCRST-ME-011).
- [12:43:37] Checked status. Active codes in state: ['FCRST-ME-004']
- [12:43:47] Checked status. Active codes in state: ['FCRST-ME-004']
- [12:43:57] Checked status. Active codes in state: ['FCRST-ME-004']
- [12:44:07] Checked status. Active codes in state: ['FCRST-ME-004']
- [12:44:17] Checked status. Active codes in state: ['FCRST-ME-004']
- [12:44:27] Checked status. Active codes in state: ['FCRST-ME-004']
- [12:44:37] Checked status. Active codes in state: ['FCRST-ME-004']
- [12:44:47] Checked status. Active codes in state: ['FCRST-ME-004']
- [12:44:57] Checked status. Active codes in state: ['FCRST-ME-004']
- [12:45:07] Checked status. Active codes in state: ['FCRST-ME-004']
- [12:45:17] Checked status. Active codes in state: ['FCRST-ME-004']
- [12:45:27] Checked status. Active codes in state: ['FCRST-ME-004']
- [12:45:27] Timeout reached. Played chime sound.
- [12:45:31] Reset dropdown to Normal.
- [12:47:07] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
N/A
```

---

### 8. HRH Terminal Attemperator Failure (R) (`FCRST-ME-012`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-22 12:47:09`
- **Resolved Time**: `2026-06-22 12:48:23`

#### Event Timeline
- [12:47:09] Induced fault 'HRH Terminal Attemperator Failure (R)' (FCRST-ME-012).
- [12:47:19] Checked status. Active codes in state: ['FCRST-ME-011']
- [12:47:29] Checked status. Active codes in state: ['FCRST-00-000']
- [12:47:39] Checked status. Active codes in state: ['FCRST-00-000']
- [12:47:49] Checked status. Active codes in state: ['FCRST-00-000']
- [12:47:59] Checked status. Active codes in state: ['FCRST-00-000']
- [12:48:09] Checked status. Active codes in state: ['FCRST-00-000']
- [12:48:19] Checked status. Active codes in state: ['FCRST-ME-012']
- [12:48:23] Reset dropdown to Normal.
- [12:48:23] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HRH Terminal Attemperator Failure",
      "possible_causes": "Reheater attemperator control valve stuck open, Spray water nozzle erosion in reheater line, Hot reheat spray control bypass leakage, Hot reheat temperature loop tuning failure",
      "observations_analysis": "Based on the real-time data analysis of the fully connected reheat steam turbine, we observe a critical decrease in the reheater outlet temperature of the hot reheat steam and the overall reheater heat duty. This uncontrolled subcooling has caused a cascading reduction in the ip_turbine_power_output, lp_turbine_power_output, and overall steam_turbine_net_power. Because upstream and downstream parameters such as HP turbine exhaust temperature, main steam parameters, evaporator conditions, and feedwater properties remain completely normal, the thermal degradation is isolated specifically to the HRH attemperation system, strongly indicating an over-spray condition.",
      "recommendations": "1. Inspect and stroke-test the reheater attemperator control valve to ensure it is not mechanically stuck in an open or partially open position. 2. Check the hot reheat spray control bypass valve for leakage that might be introducing unmetered spray water. 3. Perform a borescope inspection of the reheater line spray water nozzle to identify any physical erosion or damage. 4. Verify and recalibrate the hot reheat temperature control loop tuning to ensure stable automatic operation.",
      "fault_code": "FCRST-ME-012",
      "analysis_flag": true
    }
  ]
}
```

---

### 9. HRSG Fouling (R) (`FCRST-OT-003`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-22 12:48:25`
- **Resolved Time**: `2026-06-22 12:52:05`

#### Event Timeline
- [12:48:25] Induced fault 'HRSG Fouling (R)' (FCRST-OT-003).
- [12:48:35] Checked status. Active codes in state: ['FCRST-ME-012']
- [12:48:45] Checked status. Active codes in state: ['FCRST-ME-012']
- [12:48:55] Checked status. Active codes in state: ['FCRST-ME-012']
- [12:49:05] Checked status. Active codes in state: ['FCRST-ME-012']
- [12:49:15] Checked status. Active codes in state: ['FCRST-ME-012']
- [12:49:25] Checked status. Active codes in state: ['FCRST-ME-012']
- [12:49:35] Checked status. Active codes in state: ['FCRST-ME-012']
- [12:49:45] Checked status. Active codes in state: ['FCRST-ME-012']
- [12:49:55] Checked status. Active codes in state: ['FCRST-ME-012']
- [12:50:05] Checked status. Active codes in state: ['FCRST-OT-003']
- [12:50:09] Reset dropdown to Normal.
- [12:52:05] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "HRSG Fouling",
      "possible_causes": "Soot or ash deposition on gas side of tubes, Internal tube scaling or corrosion, Poor gas distribution inside casing, Inadequate tube sootblowing maintenance",
      "observations_analysis": "Based on the real-time data analysis of the fully connected reheat steam turbine, we observe a notable decrease in the heat duty of the economizer, primary superheater, secondary superheater, and reheater, which has subsequently caused a drop in the economizer discharge water temperature, HP superheater outlet temperature (main steam), primary superheater outlet steam temperature, and overall steam turbine net power. Conversely, there is a distinct increase in both the stack flue gas temperature and the evaporator heat duty, while gas flow rates, feedwater inlet conditions, and operating pressures remain normal. The combination of reduced heat transfer in the superheaters/reheaters and elevated stack gas temperature is a classic indicator that the heat recovery steam generator (HRSG) tubes are fouled, restricting efficient thermal energy transfer.",
      "recommendations": "1. Schedule an immediate inspection of the gas-side tube surfaces for soot, ash, or debris accumulation. 2. Perform targeted cleaning or sootblowing of the economizer, superheater, and reheater tube bundles. 3. Review and optimize the sootblower operational frequency and steam/air pressure to prevent future fouling. 4. Conduct non-destructive testing or borescope inspections to check for internal tube scaling or corrosion. 5. Evaluate the gas flow distribution within the casing to ensure uniform gas-side velocities.",
      "fault_code": "FCRST-OT-003",
      "analysis_flag": true
    }
  ]
}
```

---

### 10. IP Blade Deformation (R) (`FCRST-ME-002`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-22 12:52:07`
- **Resolved Time**: `2026-06-22 12:53:11`

#### Event Timeline
- [12:52:07] Induced fault 'IP Blade Deformation (R)' (FCRST-ME-002).
- [12:52:17] Checked status. Active codes in state: ['FCRST-00-000']
- [12:52:27] Checked status. Active codes in state: ['FCRST-00-000']
- [12:52:37] Checked status. Active codes in state: ['FCRST-00-000']
- [12:52:47] Checked status. Active codes in state: ['FCRST-00-000']
- [12:52:57] Checked status. Active codes in state: ['FCRST-00-000']
- [12:53:07] Checked status. Active codes in state: ['FCRST-ME-002']
- [12:53:11] Reset dropdown to Normal.
- [12:53:11] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "IP Blade Deformation",
      "possible_causes": "Creep or mechanical fatigue of IP rotor blades, Corrosion fatigue or erosion in IP section, IP turbine blade tip clearance rubbing, Scale buildup on IP guide vanes",
      "observations_analysis": "Based on the realtime data analysis of the fully connected reheat steam turbine, there is an isolated decrease in the 'ip_turbine_power_output'. Meanwhile, all other critical parameters\u2014including steam flow rates, pressures, temperatures across the HP/LP turbines, economizer, evaporator, and superheater sections\u2014remain completely normal. This highly localized drop in IP turbine power generation, without any external steam path or thermal deviations, strongly indicates an internal aerodynamic or physical degradation in the IP section, specifically IP blade deformation which reduces the stage efficiency.",
      "recommendations": "1. Conduct a detailed borescope inspection of the IP turbine section to visually check for blade deformation, scale deposits, or evidence of tip rubbing. 2. Closely monitor IP turbine shaft vibration signatures and bearing metal temperatures for anomalies. 3. Review water and steam chemistry logs to identify and mitigate factors causing scale buildup or corrosion fatigue. 4. Plan for a maintenance outage to measure blade tip clearances and perform necessary refurbishment or replacement of the deformed IP blades.",
      "fault_code": "FCRST-ME-002",
      "analysis_flag": true
    }
  ]
}
```

---

### 11. IP Seal Failure (R) (`FCRST-ME-005`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-22 12:53:13`
- **Resolved Time**: `2026-06-22 12:56:02`

#### Event Timeline
- [12:53:13] Induced fault 'IP Seal Failure (R)' (FCRST-ME-005).
- [12:53:23] Checked status. Active codes in state: ['FCRST-ME-002']
- [12:53:33] Checked status. Active codes in state: ['FCRST-ME-002']
- [12:53:43] Checked status. Active codes in state: ['FCRST-ME-002']
- [12:53:53] Checked status. Active codes in state: ['FCRST-ME-002']
- [12:54:03] Checked status. Active codes in state: ['FCRST-ME-002']
- [12:54:13] Checked status. Active codes in state: ['FCRST-ME-002']
- [12:54:23] Checked status. Active codes in state: ['FCRST-ME-002']
- [12:54:33] Checked status. Active codes in state: ['FCRST-ME-002']
- [12:54:43] Checked status. Active codes in state: ['FCRST-ME-002']
- [12:54:53] Checked status. Active codes in state: ['FCRST-ME-005']
- [12:54:57] Reset dropdown to Normal.
- [12:56:02] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "IP Seal Failure",
      "possible_causes": "Labyrinth seal degradation in IP section, Diaphragm packing seal wear, Shaft vibration damaging IP gland seals, Abrasive rubbing during start-up cycle",
      "observations_analysis": "Based on the real-time data analysis, we observe a distinct decrease in the IP turbine power output, LP turbine inlet steam flow, LP turbine power output, and overall steam turbine net power. Meanwhile, all major HP turbine, reheater, and HRSG parameters (such as steam temperatures, pressures, and flow rates) remain entirely normal. This highly localized performance degradation specifically in the IP and LP stages strongly indicates steam leakage through the intermediate pressure (IP) gland and diaphragm seals, which reduces the effective steam expansion within the IP turbine and consequently lowers the steam flow available to the LP turbine.",
      "recommendations": "1. Schedule an inspection of the IP section gland seals and diaphragm packings to assess wear.\n2. Monitor and analyze shaft vibration signatures to ensure vibrations are not actively damaging the IP seals.\n3. Review start-up operating procedures to prevent abrasive rubbing of seals during thermal expansion phases.\n4. Replace degraded labyrinth seals and restore proper clearances to recover lost power output and plant efficiency.",
      "fault_code": "FCRST-ME-005",
      "analysis_flag": true
    }
  ]
}
```

---

### 12. LP Blade Deformation (R) (`FCRST-ME-003`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-22 12:56:04`
- **Resolved Time**: `2026-06-22 12:57:09`

#### Event Timeline
- [12:56:04] Induced fault 'LP Blade Deformation (R)' (FCRST-ME-003).
- [12:56:15] Checked status. Active codes in state: ['FCRST-00-000']
- [12:56:25] Checked status. Active codes in state: ['FCRST-00-000']
- [12:56:35] Checked status. Active codes in state: ['FCRST-00-000']
- [12:56:45] Checked status. Active codes in state: ['FCRST-00-000']
- [12:56:55] Checked status. Active codes in state: ['FCRST-00-000']
- [12:57:05] Checked status. Active codes in state: ['FCRST-ME-003']
- [12:57:09] Reset dropdown to Normal.
- [12:57:09] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "LP Blade Deformation",
      "possible_causes": "Erosion from water droplets in LP casing, LP turbine blade fatigue or crack propagation, Mechanical rubbing in LP casing shroud, Corrosion pitting on LP exhaust stages",
      "observations_analysis": "Based on the real-time operational data, there is a localized drop in 'lp_turbine_power_output' while all other critical parameters\u2014including HP and IP turbine parameters, steam pressures, temperatures, flow rates, and HRSG heat duties\u2014remain entirely normal. This isolated decrease in LP turbine performance is highly indicative of LP Blade Deformation. The physical deformation of the blades disrupts the designed aerodynamic flow path of steam, leading to significant aerodynamic losses and a drop in power output without affecting the upstream thermodynamic cycle.",
      "recommendations": "1. Schedule an immediate borescope inspection of the LP turbine casing to visually check for blade deformation, cracks, and structural integrity. 2. Conduct Non-Destructive Testing (NDT), such as dye penetrant or ultrasonic testing, on the LP turbine blades to identify fatigue cracks or corrosion pitting. 3. Check and adjust the clearances between the LP turbine blades and the casing shroud to eliminate mechanical rubbing. 4. Review the moisture separator and extraction system performance to reduce water droplet erosion on the exhaust stages.",
      "fault_code": "FCRST-ME-003",
      "analysis_flag": true
    }
  ]
}
```

---

### 13. LP Seal Failure (R) (`FCRST-ME-006`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-22 12:57:11`
- **Resolved Time**: `2026-06-22 12:59:10`

#### Event Timeline
- [12:57:11] Induced fault 'LP Seal Failure (R)' (FCRST-ME-006).
- [12:57:21] Checked status. Active codes in state: ['FCRST-ME-003']
- [12:57:31] Checked status. Active codes in state: ['FCRST-ME-003']
- [12:57:41] Checked status. Active codes in state: ['FCRST-ME-003']
- [12:57:51] Checked status. Active codes in state: ['FCRST-ME-003']
- [12:58:01] Checked status. Active codes in state: ['FCRST-ME-003']
- [12:58:11] Checked status. Active codes in state: ['FCRST-ME-006']
- [12:58:15] Reset dropdown to Normal.
- [12:59:10] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "LP Seal Failure",
      "possible_causes": "Labyrinth packing degradation in LP section, Shaft vibration damaging LP gland seals, LP casing joint leakage or seal wear, Water droplets erosion on seal fins",
      "observations_analysis": "Real-time process data indicates a targeted decrease in both the lp_turbine_inlet_steam_flow and lp_turbine_power_output, while all upstream systems\u2014including the HP/IP turbine power outputs, feed water parameters, HRSG heat duties, and steam temperatures\u2014remain completely normal. This combination of normal upstream behavior paired with a localized loss of flow and power at the LP stage points directly to steam escaping or bypassing the active turbine stages, which is a classic indicator of LP Seal Failure.",
      "recommendations": "1. Schedule a visual and borescope inspection of the LP section gland seals and labyrinth packings for degradation or physical wear. 2. Analyze turbine shaft vibration logs to determine if excessive vibration is contributing to seal damage, and perform balancing if necessary. 3. Check the LP casing joint for signs of steam leakage. 4. Ensure adequate steam superheating and examine the upstream moisture separation systems to prevent water droplet erosion on the seal fins.",
      "fault_code": "FCRST-ME-006",
      "analysis_flag": true
    }
  ]
}
```

---

### 14. Reheater Tube Failure (R) (`FCRST-ME-009`)
- **Status**: **❌ FAILURE**
- **Induced Time**: `2026-06-22 12:59:12`
- **Resolved Time**: `2026-06-22 13:02:37`

#### Event Timeline
- [12:59:12] Induced fault 'Reheater Tube Failure (R)' (FCRST-ME-009).
- [12:59:22] Checked status. Active codes in state: ['FCRST-00-000']
- [12:59:32] Checked status. Active codes in state: ['FCRST-00-000']
- [12:59:42] Checked status. Active codes in state: ['FCRST-00-000']
- [12:59:52] Checked status. Active codes in state: ['FCRST-00-000']
- [13:00:02] Checked status. Active codes in state: ['FCRST-00-000']
- [13:00:12] Checked status. Active codes in state: ['FCRST-00-000']
- [13:00:22] Checked status. Active codes in state: ['FCRST-00-000']
- [13:00:32] Checked status. Active codes in state: ['FCRST-00-000']
- [13:00:42] Checked status. Active codes in state: ['FCRST-00-000']
- [13:00:52] Checked status. Active codes in state: ['FCRST-00-000']
- [13:01:02] Checked status. Active codes in state: ['FCRST-00-000']
- [13:01:12] Checked status. Active codes in state: ['FCRST-00-000']
- [13:01:12] Timeout reached. Played chime sound.
- [13:01:16] Reset dropdown to Normal.
- [13:02:37] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
N/A
```

---

### 15. Steam Pressure Loss (R) (`FCRST-HY-002`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-22 13:02:39`
- **Resolved Time**: `2026-06-22 13:05:54`

#### Event Timeline
- [13:02:39] Induced fault 'Steam Pressure Loss (R)' (FCRST-HY-002).
- [13:02:49] Checked status. Active codes in state: ['FCRST-00-000']
- [13:02:59] Checked status. Active codes in state: ['FCRST-00-000']
- [13:03:09] Checked status. Active codes in state: ['FCRST-00-000']
- [13:03:19] Checked status. Active codes in state: ['FCRST-00-000']
- [13:03:29] Checked status. Active codes in state: ['FCRST-00-000']
- [13:03:39] Checked status. Active codes in state: ['FCRST-00-000']
- [13:03:49] Checked status. Active codes in state: ['FCRST-00-000']
- [13:03:59] Checked status. Active codes in state: ['FCRST-00-000']
- [13:04:09] Checked status. Active codes in state: ['FCRST-00-000']
- [13:04:19] Checked status. Active codes in state: ['FCRST-00-000']
- [13:04:29] Checked status. Active codes in state: ['FCRST-HY-002']
- [13:04:33] Reset dropdown to Normal.
- [13:05:54] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Steam Pressure Loss",
      "possible_causes": "Steam pipe leak before HP inlet, Steam strainer blockage, Main steam stop valve failure, Piping pressure drops due to corrosion",
      "observations_analysis": "The real-time data analysis indicates a distinct drop in several critical parameters while others remain normal. Specifically, there is a marked decrease in HP turbine inlet steam flow, HP turbine inlet steam pressure, and HP turbine power output. This cascading effect has also caused a decrease in IP turbine inlet steam flow, IP turbine power output, LP turbine inlet steam flow, LP turbine power output, reheater heat duty, and the overall steam turbine net power. Since primary variables like feedwater parameters, economizer/evaporator pressures, temperatures, and main steam flow rates remain completely normal, the issue is isolated to a pressure loss after the primary steam generation stage but before or at the HP turbine inlet.",
      "recommendations": "1. Conduct a thorough visual and thermal inspection of the steam piping before the HP turbine inlet to locate and repair any potential steam leaks. 2. Inspect the steam strainers for blockages or debris buildup and clean them as necessary. 3. Check the mechanical and electrical integrity of the main steam stop valve to ensure it is fully operational and not stuck in a partially closed position. 4. Perform wall thickness measurements and pressure drop assessments on the piping to identify and mitigate corrosion-induced restrictions.",
      "fault_code": "FCRST-HY-002",
      "analysis_flag": true
    }
  ]
}
```

---

### 16. Superheater Tube Failure (R) (`FCRST-ME-007`)
- **Status**: **✅ SUCCESS**
- **Induced Time**: `2026-06-22 13:05:56`
- **Resolved Time**: `2026-06-22 13:09:30`

#### Event Timeline
- [13:05:56] Induced fault 'Superheater Tube Failure (R)' (FCRST-ME-007).
- [13:06:06] Checked status. Active codes in state: [None]
- [13:06:16] Checked status. Active codes in state: [None]
- [13:06:26] Checked status. Active codes in state: [None]
- [13:06:36] Checked status. Active codes in state: [None]
- [13:06:46] Checked status. Active codes in state: [None]
- [13:06:56] Checked status. Active codes in state: [None]
- [13:07:06] Checked status. Active codes in state: [None]
- [13:07:16] Checked status. Active codes in state: [None]
- [13:07:26] Checked status. Active codes in state: [None]
- [13:07:36] Checked status. Active codes in state: ['FCRST-ME-007']
- [13:07:40] Reset dropdown to Normal.
- [13:09:30] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
{
  "faults": [
    {
      "likely_fault": "Superheater Tube Failure",
      "possible_causes": "Thermal fatigue of superheater tube welds, High temperature creep rupture in superheater section, Localized flue gas erosion on superheater tubes, Scaling inside superheater causing overheating",
      "observations_analysis": "Based on the real-time data analysis, we observe a significant decrease in turbine power output across the entire system (steam turbine net power, HP, IP, and LP turbine power outputs). This is accompanied by a decrease in steam flow rates (main steam flow, HP/IP/LP turbine inlet steam flows) and a drop in steam temperatures and heat duties in the primary and secondary superheaters and reheaters. Conversely, there is an increase in both water flow rate and stack flue gas temperature, while evaporator and economizer parameters remain stable. This pattern suggests that steam is escaping from the superheater tubes due to a rupture or leak, which reduces the steam flow to the turbines and decreases the superheater heat duty. The increased water flow rate indicates an attempt to compensate for the lost fluid, while the unabsorbed heat in the flue gas results in an elevated stack flue gas temperature.",
      "recommendations": "1. Schedule an immediate inspection of the HRSG superheater section during the next planned or forced outage to locate the tube failure. 2. Perform non-destructive testing (NDT), such as ultrasonic testing, on superheater tube welds to detect thermal fatigue. 3. Inspect the external tube surfaces for localized flue gas erosion and install baffles or shields if necessary. 4. Run an internal tube deposit analysis to check for scaling and review feedwater chemistry to prevent localized overheating. 5. Assess the high-temperature sections for signs of creep rupture and replace compromised tube segments.",
      "fault_code": "FCRST-ME-007",
      "analysis_flag": true
    }
  ]
}
```

---

### 17. Vacuum Loss (R) (`FCRST-HY-003`)
- **Status**: **❌ FAILURE**
- **Induced Time**: `2026-06-22 13:09:32`
- **Resolved Time**: `2026-06-22 13:14:25`

#### Event Timeline
- [13:09:32] Induced fault 'Vacuum Loss (R)' (FCRST-HY-003).
- [13:09:43] Checked status. Active codes in state: [None]
- [13:09:53] Checked status. Active codes in state: [None]
- [13:10:03] Checked status. Active codes in state: [None]
- [13:10:13] Checked status. Active codes in state: [None]
- [13:10:23] Checked status. Active codes in state: [None]
- [13:10:33] Checked status. Active codes in state: [None]
- [13:10:43] Checked status. Active codes in state: [None]
- [13:10:53] Checked status. Active codes in state: [None]
- [13:11:03] Checked status. Active codes in state: [None]
- [13:11:13] Checked status. Active codes in state: [None]
- [13:11:23] Checked status. Active codes in state: [None]
- [13:11:33] Checked status. Active codes in state: [None]
- [13:11:33] Timeout reached. Played chime sound.
- [13:11:37] Reset dropdown to Normal.
- [13:14:25] Graphs successfully aligned back to Normal.

#### JSON Response Details
```json
N/A
```

---
