function initDigitalTwinManager(containerId) {
    let digitalTwinManager = new DigitalTwinManager();
    globalCache.addObject(containerId, digitalTwinManager);
    digitalTwinManager.init(containerId);
}
function showActiveAsset(containerId, assetObj) {
    let digitalTwinManager = globalCache.getObject(containerId);
    digitalTwinManager.showActiveAsset(assetObj);
}
function onDTWindowResize(containerId) {
    let digitalTwinManager = globalCache.getObject(containerId);
    if(!digitalTwinManager)return
    digitalTwinManager.onResize();
}
function onDTWindowClose(containerId) {
    let digitalTwinManager = globalCache.getObject(containerId);
//    digitalTwinManager.sendDemoRequest(false);
     clearInterval(digitalTwinManager.faultInterval);
     if(digitalTwinManager.startInterval){
 		clearInterval(digitalTwinManager.startInterval)
 	}
     if(digitalTwinManager.checkStatusInterval) {
    	 clearInterval(digitalTwinManager.checkStatusInterval)
     }
     digitalTwinManager.clearDemoRequestInterval();
     clearInterval(digitalTwinManager.digitalToolBar.currentFaultInterval);
     digitalTwinManager.screensList.forEach((screen) => {
         clearInterval(screen.startInterval);
     });
}
class DigitalTwinConstants {
	constructor() {
		this.DIGITALTWIN_CONSTANTS = {
			    views: {
			        OBSERVATION: "observationGraphs",
			        VIBRATION: "vibrationGraphs",
			    },
			    vibrationDirections: [
			        {
			            name: APP_SETTINGS.xfreqSpectrum,
			            direction: "x",
			        },
			        {
			            name: APP_SETTINGS.yfreqSpectrum,
			            direction: "y",
			        },
			        {
			            name: APP_SETTINGS.zfreqSpectrum,
			            direction: "z",
			        },
			    ],
			};
	}
}
class DigitalTwinManager {
    constructor() {
        this.firstAsset = true;
        this.DEMO_MODE = false;
        this.DEMO_REQUEST_INTERVAL = null;
        this.activeAsset = null;
        this.digitalToolBar = new DigitalToolBar();
        this.digitalToolBar.DEMO_MODE = this.DEMO_MODE;
        this.observationTypes = {
            EXPECTED: APP_SETTINGS.expected,
            ACTUAL: APP_SETTINGS.actual,
        };
        this.digitalTwinConstants = new DigitalTwinConstants();
        this.observationsConfig = {
            graphType: "timeseries",
            xAxisLabel: "time",
            xAxisLabelFormat: d3.timeFormat("%H:%M:%S"),
            autoRefreshTime: 1000 * 60 * 5 + 1000*10, //5m10s,
            screenType: this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.OBSERVATION,
            pathColors: ["rgb(255, 127, 14)", "rgb(31, 119, 180)"],
        };
        this.vibrationsConfig = {
            graphType: "linear",
            xAxisLabel: "Frequency(Hz)",
            xAxisFormat: d3.timeFormat(","),
            autoRefreshTime: 15 * 60 * 1000,
            screenType: this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.VIBRATION,
            pathColors: ["rgb(31, 119, 180)"],
        };
        this.analysisFaultCodes = {
            "dt-vibrationGraphs-analysis": null,
            "dt-observationGraphs-analysis": null,
        };
        this.checkStatusInterval = null;
        this.checkStatusFirstResponse = false;
        this.isScreensActive = false;
        this.faultInterval = null;
        this.loadedAssets = [];
        this.screensList = [];
        this.allFaults = [];
        this.faultsMap = {};
        this.websocket = new WebSocketHandler();
        this.setView = this.setView.bind(this);
        this.checkStatus = this.checkStatus.bind(this);
        this.removeStatus = this.removeStatus.bind(this);
        this.onChangeRefreshInterval = this.onChangeRefreshInterval.bind(this);
        this.changeDemoMode = this.changeDemoMode.bind(this);
        this.getDemoMode = this.getDemoMode.bind(this);
        this.sendDemoRequest = this.sendDemoRequest.bind(this);
        this.showAnalysis = this.showAnalysis.bind(this);
        this.showActiveAssetIssues = this.showActiveAssetIssues.bind(this);
    }
    init(containerId) {
    	this.containerId = containerId;
    	let height = d3.select("#" + containerId).node().getBoundingClientRect().height;
        this.container = d3
            .select("#" + containerId)
            .append("div")
            .attr("class", "digital-twin-wrapper").style("height",height+"px");
        this.buildDigitalLayout();
        this.digitalToolBar.initToolBar(this.toolBarContainer, containerId, {
            setView: this.setView,
            onClickStatus: this.checkStatus,
            removeStatus: this.removeStatus,
            onChangeRefreshInterval:this.onChangeRefreshInterval,
            changeDemoMode: this.changeDemoMode,
            sendDemoRequest: this.sendDemoRequest,
            showAnalysis: this.showAnalysis,
            showActiveAssetIssues:this.showActiveAssetIssues
        });
        this.initEventListeners();
    }
    initEventListeners() {
    	const debounce = (func, delay) => {
            let debounceTimer;
            return function () {
                const context = this;
                const args = arguments;
                clearTimeout(debounceTimer);
                debounceTimer = setTimeout(() => func.apply(context, args), delay);
            };
        }
//        window.addEventListener("resize", debounce((event) => {
//            this.onResize();
//        },1000));
    	window.addEventListener("resize", (event) => {
	          this.onResize();
	      });
        let timeoutInterval = null;
        document.addEventListener("visibilitychange", () => {
            if(d3.select('#'+this.containerId).empty() || !this.activeAsset)return
            if (document.visibilityState === "hidden") {
                //AFTER ONE 30SECONDS OF INACTIVE APPLICATION STOP SENDING REQUESTS
//                timeoutInterval = setTimeout(() => {
                    this.isScreensActive = false;
                    clearInterval(this.faultInterval);
                    this.screensList.forEach((screen) => {
                        clearInterval(screen.startInterval);
                    });
//                }, 30000);
            } else {
                clearTimeout(timeoutInterval);
                if (this.isScreensActive) {
                    return;
                }
                this.getInduceFaults();
                this.screensList.forEach((screen) => {
                    screen.firstRequest = true;
                    screen.autoRefresh();
                });
            }
        });
    }
    buildDigitalLayout() {
        this.toolBarContainer = this.container
            .append("div")
            .attr("class", "dt-toolbar-wrapper");
        this.screensContainer = this.container
            .append("div")
            .attr("class", "dt-screens-container");
        this.observationScreensWrapper = this.screensContainer
            .append("div")
            .attr("class", "dt-observations-wrapper");
        this.vibrationScreensWrapper = this.screensContainer
            .append("div")
            .attr("class", "dt-vibrations-wrapper");
        this.statusWrapper = this.screensContainer
            .append("div")
            .attr("class", "dt-analysis-wrapper");
        this.statusWrapper
            .append("div")
            .attr(
                "class",
                `dt-analysis dt-${this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.OBSERVATION}-analysis`
            );
        this.statusWrapper
            .append("div")
            .attr(
                "class",
                `dt-analysis dt-${this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.VIBRATION}-analysis`
            );
        this.statusWrapper
        	.append("div")
        	.attr("class", "dt-analysis dt-combined-analysis")
    }
    getInduceFaults() {
        // WRITE_API
        let filter = {
            assetType: {
                id: this.activeAsset.assetTypeId,
            },
        };
        invokeRestService(API_ROUTES.GET_FAULT_CODES, filter, {
        	handleMeasurements: (data) => {
                let faultCodes = data?.FaultCode ?? [];
                faultCodes.sort((a, b) => a.name.localeCompare(b.name));
                //ADD normal status at top
                let index = faultCodes.findIndex((d) => d.name == "Normal");
                if (index > -1) {
                    let normalFault = faultCodes.splice(index, 1)[0];
                    faultCodes.unshift(normalFault);
                }
                this.digitalToolBar.addFaults(faultCodes, this.activeAsset);
            },
        });
    }
    renderScreens(container, screens, screenInstance) {
        screens.forEach((screenInfo) => {
            let digitalScreen = new DigitalScreen();
            digitalScreen.setScreenDetails(screenInfo);
            digitalScreen.initScreen(
            	this.containerId,
                container,
                this.websocket,
                screenInstance,
                this.view,
                this.getDemoMode
            );
            this.screensList.push(digitalScreen);
        });
//        this.digitalToolBar.screensList = this.screensList;
    }
    renderSensors(sensors) {
        if (sensors.length == 0) {
        	this.vibrationScreensWrapper
	            .append("div")
	            .text(APP_SETTINGS.noSensors)
	            .attr("class", "dt-empty-screens-msg");
            return;
        }
        let sensorsWrapper = this.vibrationScreensWrapper
            .append("div")
            .attr("class", "vb-sensors-wrapper");
        let sensorsEl = sensorsWrapper
            .selectAll(".sensors")
            .data(sensors)
            .enter()
            .append("div")
            .attr("class", "vb-sensor")
            .on("click", (event, d) => {
            	if (d3.select(event.currentTarget).classed("active-vb-sensor")) return
                sensorsWrapper
                    .selectAll(".active-vb-sensor")
                    .classed("active-vb-sensor", false);
                d3.select(event.currentTarget).classed("active-vb-sensor", true);
                let screensList = this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.vibrationDirections.map(
                    (direction) => {
                        return {
                            screenName: direction.name,
                            screenId: d.sensorName + direction.direction,
                            unit: `${APP_SETTINGS.acceleration}(\u03bcm/s^2)`,
                            observationList: [
                                {
                                    code: direction.direction,
                                    id: direction.direction,
                                    name: direction.name,
                                    tagname: d.sensorName,
                                    type: this.observationTypes.ACTUAL,
                                },
                            ],
                        };
                    }
                );
                this.renderScreens(this.vibrationScreensWrapper, screensList, {
                    ...this.vibrationsConfig,
                    graphHeight: this.graphHeight,
                });
            });
        sensorsEl.append("label").text((d) => d.sensorName);
        sensorsWrapper.select(".vb-sensor").node().click();
    }
    clearDemoRequestInterval() {
        clearInterval(this.DEMO_REQUEST_INTERVAL);
    }
    setDemoRequestInterval() {
        clearInterval();
        const sendRequest = () => {
            invokeRestService(
                API_ROUTES.GET_DEMO_MODE_GENERATION,
                {
                    DemoModeFilter: {
                        assetCategoryId: this.activeAsset.assetCatId,
                        assetEcn: this.activeAsset.assetEcn,
                    },
                },
                {
                    handleMeasurements: (res) => {
                        let bool;
                        if (res && res.status != 404) {
                        	let data = res;
                            bool = data?.enabled_demo;
                            const timeLeft = data?.timeLeft;
//                            this.timeLeftForDemo = res?.timeLeft;
//                            if (bool != this.DEMO_MODE) {
                                this.digitalToolBar.toggleDemoMode(bool);
//                            }
                            if (timeLeft) {
                                clearTimeout(this.DEMO_REQUEST_INTERVAL);
                                this.DEMO_REQUEST_INTERVAL = setTimeout(() => {
                                    sendRequest();
                                }, timeLeft * 1000);
                            }
                        }
                    },
                }
            );
        };
        sendRequest();
    }
    loadIssues(issueType){
    	let filter = {
//			assetName:{
//				ecn:this.activeAsset.assetEcn,
//			},
    		assetName:this.activeAsset.assetEcn,
			dateRange:{
				fromDate:null,
				toDate:null
			},
			status:{
				id:1011
			},
			issueType:{
				id:issueType
			}
    	}
    	return new Promise((resolve,reject)=>{
    		invokeRestService(API_ROUTES.GET_ISSUE_MANAGEMENT_SERVICE_ISSUES, filter, {
                handleMeasurements: (res) => {
                    if(!res || !res.Issue){
                    	resolve([])
                    }else{
                    	if(!Array.isArray(res.Issue)){
                    		resolve([res.Issue])
                    		return;
                    	}
                    	resolve(res.Issue)
                    }
                },
            });
    	})
    }
    async showActiveAssetIssues(){
    	let issues = []
    	let conditionAIIssues = await this.loadIssues(6515);
    	let vibrationAIIssues = await this.loadIssues(6577);
    	issues = [...conditionAIIssues, ...vibrationAIIssues];
    	issues = issues.map((d)=>{
    		let format = `${APP_SETTINGS.dateFormat} ${APP_SETTINGS.timeFormat}`
	        let timeFormat = d3.timeFormat(convertToD3JsFormat(format));
    		return {
    			...d,
    			assetName:d.asset?.assetName,
				eventTime:timeFormat(new Date(d.eventTime).getTime()),
				severity:d.severity?.name,
				status:d.status?.name,
//				issueType:d.issueType.name,
				issueType: `
				    <div style="display:flex;align-items:center;gap:6px;">
				        <span>${d.issueType.name}</span>
				        <img 
				            src="client/images/markissue.png"
				            class="false-alarm-icon"
				            data-id="${d.id}"
				            style="width:16px;height:16px;cursor:pointer;"
				        />
				    </div>
				`,
				
    		}
    	})
    	let customDialog = new GWTDialog();
        customDialog.openDialog({
            container: this.container,
            width: "100%",
            maxWidth: "350",
            minHeight: "250px",
            title: "Issues",
        });
        let maxWidth = this.container.node().getBoundingClientRect().width;
        customDialog.dialog.style("max-width",`${maxWidth}px`)
        customDialog.dialogcontent.style("padding","10px");
        let columns = [
        	{
                title: "Id",
                data: "id",
                type: Number,
            },
            {
                title: "Issue Title",
                data: "name",
                type: String,
            },
//            {
//            	title:"Asset Name",
//            	data:"assetName",
//                type: String,
//            },
            {
            	title:"Event Time",
            	data:"eventTime",
                type: Date,
            },
            {
            	title:"Severity",
            	data:"severity",
                type: String,
            },
            {
            	title:"Status",
            	data:"status",
                type: String,
            },
            {
            	title:"Issue Type",
            	data:"issueType",
                type: String,
                html: true
            },
        ]
        let virtualTableGrid = new VirtualTableGrid();
        virtualTableGrid.init(
    		customDialog.dialogcontent,
            columns,
            issues,
            {
                tableResizing: false,
                colSorting: true,
                rowSelection: false,
                className: "issues-table",
                sortHeader: "eventTime",
                sortOrder: "desc",
            },
            {
            	
            }
        );
        customDialog.dialogcontent
        .selectAll(".false-alarm-icon")
        .on("click", (event) => {
            event.stopPropagation();
            const issueId = event.target.getAttribute("data-id");
            openFalseAlarmWindow(issueId);
        });
//        customDialog.dialogcontent.on("click", (event) => {
//            if (event.target.classList.contains("false-alarm-icon")) {
//                event.stopPropagation();
//                const issueId = event.target.getAttribute("data-id");
//                // this.onFalseAlarm(issueId);
//            }
//        });
        virtualTableGrid.tableWrapper.style(
            "max-height",
            `300px`
        );
    }
    showActiveAsset(asset) {
        if(this.activeAsset?.assetEcn == asset.assetEcn)return
    	if (this.activeAsset?.assetEcn) {
            this.activeAsset = null;
            this.screensList.forEach((screen) => {
                clearInterval(screen.startInterval);
            });
            if (this.checkStatusInterval) {
        	  clearInterval(this.checkStatusInterval);
        	  this.checkStatusInterval = null;
        	}
        }
        this.container.selectAll(".gwt-custom-dialog-wrapper")?.remove();
        this.screensList = [];
        this.allFaults = [];
        this.removeStatus();
        this.activeAsset = asset;
        if (this.firstAsset) {
            this.firstAsset = false;
        } else {
//            this.DEMO_MODE && this.sendDemoRequest(this.DEMO_MODE);
        }
        this.digitalToolBar.toggleDemoMode(false);
        this.setDemoRequestInterval();
        this.checkStatusFirstResponse = false;
        this.getInduceFaults();
        this.digitalToolBar.changeStatus("00-000");
        this.isScreensActive = true;
        this.setGraphHeight();
        this.getObservationScreensList((screensList) => {
        	this.observationScreensWrapper.selectAll("div").remove();
        	if (screensList.length == 0) {
                this.observationScreensWrapper
                    .append("div")
                    .text(APP_SETTINGS.noTags)
                    .attr("class", "dt-empty-screens-msg");
                return;
            }
            this.activeAsset.observationsList = screensList;
            this.renderScreens(this.observationScreensWrapper, screensList, {
                ...this.observationsConfig,
                graphHeight: this.graphHeight,
            });
            if (
                this.digitalToolBar.activeFault &&
                this.digitalToolBar.activeFault.faultCode.name.toLowerCase() != "normal" 
            ) {
            	setTimeout(() => {
//                    this.checkStatus(this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.OBSERVATION);
            		const view = this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.OBSERVATION;
            	    this.checkStatus(view);
            	    if (this.checkStatusInterval) {
            	        clearInterval(this.checkStatusInterval);
            	    }
            	    this.checkStatusInterval = setInterval(() => {
            	        this.checkStatus(view);
            	    }, 30 * 60 * 1000); 
                }, 1000);
            }
        });
        this.getVibrationSensors((sensors) => {
            this.vibrationScreensWrapper.selectAll("div").remove();
            this.activeAsset.sensors = sensors;
            this.renderSensors(sensors);
        });
    }
    getObservationScreensList(callback) {
        let filter = {
            TagFilterRest: {
                ecn: this.activeAsset.assetEcn,
                searchType: "equals"
            },
        };
        invokeRestService(API_ROUTES.GET_TAGS, filter, {
            handleMeasurements: async (response) => {
                if (!response.TagLight) return;
//                let tags = response.TagLight.filter((tag) => tag.type == 4300 && tag.assetId == this.activeAsset.assetId);
                let tags = response.TagLight.filter(
                	    (tag) => tag.type == 4300 && tag.tagStatus == 6132
                	);
                let resLength = tags.length;
                if (resLength == 0) {
                    callback([]);
                    return;
                }
                let resCount = 0;
                let obsList = [];
                let screensList = [];
                tags.forEach((tag, index) => {
                    invokeRestService(API_ROUTES.GET_FORM_ITEM+tag.obsCode, tag.obsCode, {
                        handleMeasurements: (res) => {
                            if (!res.FormItem) return;
                            resCount += 1;
                            let observation = res.FormItem;
                            observation.type = this.observationTypes.ACTUAL;
                            let tagname = tags.find(
                                (tag) => tag.obsCode == observation.id
                            ).tagName;
                            let screenId = observation.code;
                            let screenName = observation.name;
                            if (
                                res.FormItem.code.includes("EXP")
                            ) {
                                screenId = screenId.replace("EXP-", "");
                                observation.type = this.observationTypes.EXPECTED;
                                screenName = screenName.replace(
                                    this.observationTypes.EXPECTED + " ",
                                    ""
                                );
                            }
                            let index = screensList.findIndex(
                                (screen) => screen.screenId == screenId
                            );
                            if (index == -1) {
                                screensList.push({
                                    screenId,
                                    observationList: [
                                        {
                                            code: observation.code,
                                            id: observation.id,
                                            name: observation.name,
                                            tagname: tagname,
                                            type: observation.type,
                                        },
                                    ],
                                    screenName,
                                    unit: observation.measurementUnit?.name??"",
                                });
                            } else {
                                screensList[index].observationList.push({
                                    code: observation.code,
                                    id: observation.id,
                                    name: observation.name,
                                    tagname: tagname,
                                    type: observation.type,
                                });
                            }
                            if (resCount === resLength) {
                                callback(screensList);
                            }
                        },
                    });
                });
            },
        });
    }
    getVibrationSensors(callback) {
        let filter = {
            assetEcn: this.activeAsset.assetEcn,
            firstRequest: true,
            sensors: [],
            type: 4265,
            directions: ["x"],
            dateRange: {
                fromDate: null,
                toDate: null,
            },
        };
        invokeRestService(API_ROUTES.GET_HARMONICS, filter, {
            handleMeasurements: (res) => {
                if (!res || !res.VibConditionData.sensors) {
                    callback([]);
                    return;
                }
                let sensors = res.VibConditionData.sensors.filter(
                    (sensor) => sensor.type.name != "Temperature"
                );
                callback(sensors);
            },
        });
    }
    setView(view) {
        this.view = view;
        this.observationScreensWrapper.classed(
            "active-view",
            this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.OBSERVATION == this.view
        );
        this.vibrationScreensWrapper.classed(
            "active-view",
            this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.VIBRATION == this.view
        );
        this.checkStatusFirstResponse = false;
        this.statusWrapper.selectAll(`.active-view`).classed("active-view", false);
        this.statusWrapper
            .select(`.dt-${this.view}-analysis`)
            .classed("active-view", true);
        this.screensList.forEach((screen) => {
            screen.onChangeView(this.view);
        });
        if (
            this.digitalToolBar.activeFault &&
            this.digitalToolBar.activeFault.asset.ecn == this.activeAsset.assetEcn &&
            this.digitalToolBar.activeFault.faultCode.name.toLowerCase() != "normal"
        ) {
            this.checkStatus();
        }
    }
    onResize() {
        this.setGraphHeight();
        this.screensList.forEach((screen) => {
            screen.resizeScreen(this.graphHeight);
        });
    }
    setGraphHeight() {
        let screenConstrains = this.screensContainer.node().getBoundingClientRect();
        // SCREEN HEIGHT/2  - GRID GAP - SCREEN PADDING - LEGENDS HEIGHT
        let height = screenConstrains.height / 2 - 20 - 20 - 20;
        this.graphHeight = height;
    }
    updateAnalysisStatus() {
        if (
            this.analysisFaultCodes["dt-observationGraphs-analysis"] &&
            !this.analysisFaultCodes["dt-observationGraphs-analysis"]?.includes(
                "00-000"
            )
        ) {
            this.digitalToolBar.changeStatus(
                this.analysisFaultCodes["dt-observationGraphs-analysis"]
            );
//            this.analysisFaultCodes["dt-observationGraphs-analysis"] = null;
        } else {
            this.digitalToolBar.changeStatus(
                this.analysisFaultCodes["dt-vibrationGraphs-analysis"]
            );
//            this.analysisFaultCodes["dt-vibrationGraphs-analysis"] = null;
        }
    }
    checkStatus(view = this.view) {
		const sendRequest = (view)=>{
			let filter;
	        if (view == this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.OBSERVATION) {
	        	if (
	                !this.activeAsset?.observationsList ||
	                this.activeAsset?.observationsList?.length == 0
	            )
	                return;
	            let tags = [];
	            let obs = {};
	            this.activeAsset.observationsList.forEach((screen) => {
					screen.observationList.forEach((d)=>{
						tags.push(d.tagname)
						obs[d.tagname] = d.code
					})
				});
	            filter = {
	                msg_type: "DT_CHECK_CONDITION_STATUS",
	                time1: new Date().getTime() - 30 * 1000,
	                time2: new Date().getTime(),
	                assetType: String(this.activeAsset.assetTypeId),
	                uid: `dt-${view}-analysis/${this.activeAsset.assetEcn}`,
	                tags,
	                obs,
	            };
				
		        let wrapper = this.statusWrapper.select(`.dt-${view}-analysis`);
		        wrapper.selectAll("div").remove();
		        wrapper.append("div").html("<b>Loading Realtime Analysis...</b>");
	        } else {
				if(!this.activeAsset || !this.activeAsset.sensors || this.activeAsset?.sensors?.length==0)return
	            let sensorName = this.vibrationScreensWrapper
	                .select(".active-vb-sensor label")
	                .text();
	            let index = this.screensList.findIndex(
	                (screen) => screen.type == this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.VIBRATION
	            );
	            let time2 = this.screensList[index].toDate;
	            let time1 = this.screensList[index].fromDate;
	            filter = {
	                msg_type: "DT_CHECK_VIBRATION_STATUS",
	                time1,
	                time2,
	                assetType: String(this.activeAsset.assetTypeId),
	                assetEcn:this.activeAsset.assetEcn,
	                uid: `dt-${view}-analysis/${this.activeAsset.assetEcn}`,
	                sensorName,
	                digitalTwin: true,
	            };
		        let wrapper = this.statusWrapper.select(`.dt-${view}-analysis`);
		        wrapper.selectAll("div").remove();
		        wrapper.append("div").html("<b>Loading Vibration Analysis...</b>");
	        }
	        this.websocket.sendMessage(filter, (response) => {
	        	let uid = response.uid;
	        	let assetEcn = uid.split("/")[1];
	            if (this.activeAsset.assetEcn != assetEcn) return;
	            let view = uid.split("/")[0];
	            this.statusWrapper.select(`.${view}`).selectAll("div").remove();
	            
	            let details = JSON.parse(response.details);
	            this.statusAnalysis = JSON.parse(response.details);
	            let faultCodes = "";
	            this.faultsMap = {};
	            this.statusAnalysis.faults.forEach((fault, index) => {
	            	if (!fault?.fault_code) return; 
	            	faultCodes = faultCodes + fault.fault_code + " , ";	
	            	this.faultsMap[fault.fault_code] = fault;
	            })
	            this.analysisFaultCodes[view] = faultCodes;
	            this.removeStatus(view);
	            this.updateAnalysisStatus();
	            this.assetId = this.activeAsset.assetId;
//	            this.showAnalysis(this.statusWrapper.select(`.${view}`), view);
	            this.showAnalysis(this.statusWrapper.select(".dt-combined-analysis"), view);
	            if (!this.checkStatusFirstResponse) {
	                this.screensContainer.node().scrollTop =
	                    this.screensContainer.node().scrollHeight;
	                this.checkStatusFirstResponse = true;
	            }
	        });
		}
        this.analysisFaultCodes = {
            "dt-vibrationGraphs-analysis": null,
            "dt-observationGraphs-analysis": null,
        };
    	sendRequest(this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.OBSERVATION);
    	sendRequest(this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.VIBRATION);
    }
//    showAnalysis(container, view, analysis = this.statusAnalysis) {
//        if (!analysis || !analysis.analysis_flag || analysis.likely_fault.toLowerCase() == "no fault" || this.activeAsset.assetId !== this.assetId)
//            return;
//        if (view) {
//            let analysisType;
//            if (view == "dt-vibrationGraphs-analysis") {
//                analysisType = "Vibration Analysis";
//            } else {
//                analysisType = "Realtime Analysis";
//            }
//            if(container){
//				container.selectAll("h3").remove();
//			}
//            container
//                .append("h3")
//                .style("margin", "5px 0px")
//                .text(analysisType);
//        }
//        let contentKeys = Object.keys(analysis).filter((d)=> d != "analysis_flag");
//        let statusEl = container
//            .selectAll(".analysis")
//            .data(contentKeys)
//            .enter()
//            .append("div");
//        statusEl.append("label").text((d) => d.replace("_", " "));
//        statusEl.append("label").text(":");
////        statusEl.append("label").text((d) => analysis[d]);
//        statusEl.append("label")
//	        .text(d => {
//	            if (d === "likely_fault" && analysis.fault_code) {
//	                return `${analysis[d]} (${analysis.fault_code})`;
//	            }
//	            return analysis[d];
//	        });
//    }
    showAnalysis(container, view, analysis = this.statusAnalysis, faultCode) {
        if (!analysis || !analysis.faults[0].analysis_flag || analysis.faults[0]?.likely_fault?.toLowerCase() == "no fault" || this.activeAsset.assetId !== this.assetId)
            return;
        if (view) {
            let analysisType;
            if (view == "dt-vibrationGraphs-analysis") {
                analysisType = "Vibration Analysis";
            } else {
                analysisType = "Realtime Analysis";
            }
            let incomingFaults = analysis.faults.map(f => ({
                ...f,
                source: view   
            }));
            incomingFaults.forEach(fault => {
                if (!this.allFaults.some(f => f.fault_code === fault.fault_code)) {
                    this.allFaults.push(fault);
                }
            });
            this.allFaults.sort((a, b) => {
                if (a.source === b.source) return 0;
                return a.source === this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.VIBRATION ? 1 : -1;
            });
            if(container){
//				container.selectAll("h3").remove();
            	container.selectAll("*").remove();
			}
            container
                .append("h3")
                .style("margin", "5px 0px")
                .text("Fault Analysis");
            let contentKeys = Object.keys(analysis).filter((d)=> d != "analysis_flag");
            let fault_analysis = analysis;
            const tabHeader = container.append("div")
            	.style("margin-bottom", "10px");
            
            const tabs = tabHeader.selectAll(".fault-tab")
//    	        .data(fault_analysis.faults)
                .data(this.allFaults, d => d.fault_code)
    	        .enter()
    	        .append("span")
    	        .attr("class", "fault-tab")
    	        .classed("active", (d, i) => i === 0)
    	        .style("display", "inline-block")
    	        .style("padding", "6px 14px")
    	        .style("font-size", "13px")
    	        .style("border-radius", "3px")
    	        .style("font-weight", "500")
    	        .style("cursor", "pointer")
    	        .text(d => d.fault_code);
            
            this.content = container.append("div")
    	        .style("background", "#fff")
//    	        .style("border", "1px solid #3269a4")
    	        .style("border-radius", "4px")
    	        .style("padding", "10px")
    	        .style("display", "flex")
    	        .style("flex-direction", "column")

//            this.renderFaultDetails(fault_analysis.faults[0]);
    	     if (this.allFaults.length) {
	             this.renderFaultDetails(this.allFaults[0]);
			 }
            let curr = this;
            tabs.on("click", function (event, d) {

        	  tabs
        	    .classed("active", false)

        	  d3.select(this)
        	    .classed("active", true)

        	  curr.renderFaultDetails(d);
        	});
        } else {
        	let curr = this;
        	if (!curr.faultsMap || !curr.faultsMap[faultCode]) return;
        	let contentKeys = Object.keys(analysis.faults[0]).filter((d)=> d != "analysis_flag");
//	        let statusEl = container
//	              .selectAll(".analysis")
////	              .data(contentKeys)
////	              .enter()
//	              .append("div")
//	              .style("display", "flex")
//	              .style("flex-direction", "column");
        	let statusEl = container
	            .append("div")
	            .attr("class", "analysis")
	            .style("display", "flex")
	            .style("flex-direction", "column");
        	Object.entries(curr.faultsMap[faultCode]).forEach(([key, value], index) => {
        	    if (
        	      !value ||
        	      key === "analysis_flag" ||
        	      key === "fault_code"
        	    ) return;

        	    const label = key
        	      .replace(/_/g, " ")
        	      .replace(/\b\w/g, c => c.toUpperCase());

        	    const row = statusEl.append("div")
        	      .style("display", "grid")
        	      .style("grid-template-columns", "180px 1fr")
        	      .style("gap", "10px")
        	      .style("padding", "6px 0");

//        	    row.append("div")
//        	      .style("font-weight", "600")
//        	      .style("color", "#000")
//        	      .text(label + ":");

        	    const labelCell = row.append("div")
	    	        .style("display", "flex")
	    	        .style("align-items", "center")
	    	        .style("gap", "6px")
	    	        .style("font-weight", "600")
	    	        .style("color", "#000");
	    	
	    	    labelCell.append("span")
	    	        .html(ICONS[key] || "");
	    	
	    	    labelCell.append("span")
	    	        .text(label + ":");
        	    row.append("div")
        	      .style("color", "#333")
        	      .style("line-height", "1.4")
        	      .style("word-break", "break-word")
        	      .text(() => {
				        if (key === "likely_fault") {
				            return `${value} (${curr.faultsMap[faultCode].fault_code})`;
				        }
				        return value;
				   });
//        	      .text(value);
        	    statusEl.append("div")
        	      .style("border-bottom", "1px solid #ddd")
        	      .style("margin", "4px 0");
        	  });
        	
        }
        
        
    }
    
    renderFaultDetails(fault) {
    	this.content.selectAll("*").remove();

	  Object.entries(fault).forEach(([key, value], index) => {
	    if (
	      !value ||
	      key === "analysis_flag" ||
	      key === "fault_code" ||
	      key === "source"
	    ) return;

	    const label = key
	      .replace(/_/g, " ")
	      .replace(/\b\w/g, c => c.toUpperCase());

	    const row = this.content.append("div")
	      .style("display", "grid")
	      .style("grid-template-columns", "180px 1fr")
	      .style("gap", "10px")
	      .style("padding", "6px 0");

//	    row.append("div")
//	      .style("font-weight", "600")
//	      .style("color", "#000")
////	      .text(label + ":");
//	      .html(`${ICONS[key] || ""} ${label}:`);
	    const labelCell = row.append("div")
	        .style("display", "flex")
	        .style("align-items", "center")
	        .style("gap", "6px")
	        .style("font-weight", "600")
	        .style("color", "#000");
	
	    labelCell.append("span")
	        .html(ICONS[key] || "");
	
	    labelCell.append("span")
	        .text(label + ":");
	    row.append("div")
	      .style("color", "#333")
	      .style("line-height", "1.4")
	      .style("word-break", "break-word")
	      .text(() => {
		        if (key === "likely_fault") {
		            return `${value} (${fault.fault_code})`;
		        }
		        return value;
		   });
	    this.content.append("div")
	      .style("border-bottom", "1px solid #ddd")
	      .style("margin", "4px 0");
	  });
	}
    
    removeStatus(view) {
        if (view) {
        	const hasOtherFaults = Object.entries(this.analysisFaultCodes || {})
            	.some(([k, v]) => k !== view && v);

        	if (hasOtherFaults) return;
            this.statusWrapper.select(".dt-combined-analysis").selectAll("div").remove();
            return;
        }
        this.statusWrapper.selectAll(".dt-analysis").html("");
    }
    onChangeRefreshInterval(interval) {
    	if (!interval) {
            this.screensList.forEach((screen) => {
                screen.autoRefresh();
            });
            return;
        }
        let vibrationScreens = this.screensList.filter((screen) => {
            return (
                screen.screenInstance.screenType === this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.VIBRATION
            );
        });
        vibrationScreens.forEach((screen) => {
        	if(interval=="0"){
				clearInterval(screen.startInterval)
				return
			}
            screen.screenInstance.autoRefreshTime = interval;
            screen.autoRefresh();
        });
    }
    sendDemoRequest(bool) {
        if (this.activeAsset) {
        	let filter = {
                DemoModeFilter: {
                    assetCategoryId: this.activeAsset.assetCatId,
                    enabled_demo: bool,
                    assetEcn: this.activeAsset.assetEcn,
                },
            };
            invokeRestService(API_ROUTES.UPDATE_DEMO_MODE, filter, {
                handleMeasurements: (res) => {},
            });
        }
    }
    changeDemoMode(bool) {
        this.setDemoMode(bool);
        this.screensList.forEach((screen) => {
            screen.data = {
                Actual: [],
                Expected: [],
            };
            screen.firstRequest = true;
            screen.autoRefresh();
        });
        if (!bool) return;
        setTimeout(() => {
            this.screensList.forEach((screen) => {
                screen.firstRequest = true;
                screen.autoRefresh();
            });
        }, 3000);
    }
    setDemoMode(bool) {
        this.DEMO_MODE = bool;
    }
    getDemoMode() {
        return this.DEMO_MODE;
    }
}
class DigitalToolBar {
    constructor() {
        this.faultsWrapper = {};
        this.digitalTwinConstants = new DigitalTwinConstants();
        this.graphTypes = [
            {
                view: this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.OBSERVATION,
                label: APP_SETTINGS.realtime,
                default: true,
            },
            {
                view: this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.VIBRATION,
                label: APP_SETTINGS.vibration,
            },
        ];
        this.getAnalysis = true;
        this.activeFault = null;
        this.disableVibration = false;
        this.faults = [];
    }
    initToolBar(container, dashboardId, callbacks) {
        this.container = container;
        this.dashboardId = dashboardId;
        this.callbacks = callbacks;
        this.faultsWrapper = this.container
            .append("div")
            .attr("class", "dt-faults-wrapper");
        this.faultsWrapper.append("label").text("Induce Fault:");
        let resetBtn = this.faultsWrapper
	        .append("div")
	        .attr("class", "dt-svg-icon")
	        .on("click", (event) => {
	        	resetBtn
        	    	.classed("spin", false)
        	    void resetBtn.offsetWidth
        	    resetBtn
        	    	.classed("spin", true)
	            let faultCode = this.faults.find((fault) =>
	                fault.code.includes("00-000")
	            );
	            if (faultCode) {
	                this.saveFault(faultCode);
//	                let digitalTwinManager = globalCache.getObject(this.dashboardId);
//	                digitalTwinManager.allFaults = [];
	                this.getAnalysis = false;
	                setTimeout(() => {
	                    this.getAnalysis = true;
	                    this.callbacks.onChangeRefreshInterval();
	                    this.handleStatus();
	                    this.changeStatus("00-000");
	                }, 50000);
	            }
	        })
	        .html(ICONS.reset);
        let statusWrapper = this.container
            .append("div")
            .attr("class", "dt-status-wrapper")
            .on("mouseover", (event) => {
                if (this.activeFault?.faultCode?.code?.includes("00-000")) return;
                d3.select(statusHoverWrapper.node().parentNode).style(
                    "display",
                    "block"
                );
                statusHoverWrapper.selectAll("div").remove();
                this.callbacks.showAnalysis(statusHoverWrapper, null, this.statusAnalysis, event.target.innerText);
            })
            .on("mouseout", (event) => {
                d3.select(statusHoverWrapper.node().parentNode).style(
                    "display",
                    null
                );
                statusHoverWrapper.selectAll("div").remove();
            });
        statusWrapper.append("label").text("Status:");
        this.statusEl = statusWrapper.append("div").attr("class", "dt-normal-status");
        let statusHoverWrapper = this.container
	        .append("div")
	        .attr("class", "hover-wrapper")
	        .append("div")
	        .attr("class", "dt-hover-status-analysis dt-analysis");
//        this.container
//            .append("button")
//            .attr("class", "dt-check-status")
//            .text("Check Status")
//            .on("click", (event) => {
//                this.callbacks.onClickStatus();
//            });
        this.addGraphViews();
        this.renderRefreshWidget();
        let issuesWrapper = this.container
    		.append('div')
    		.attr('class','dt-issues-wrapper')
    		.on('click',(event)=>{
    			this.callbacks.showActiveAssetIssues();
    		})
    	issuesWrapper.append("img").attr("src","client/images/issue_management.png")
        this.addDemoMode();
        this.callbacks.setView(this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.OBSERVATION);
        this.setGraphView(this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.OBSERVATION);
    }
    renderRefreshWidget() {
    	let refrshWidgetscontainer = this.container
	        .append("div")
	        .attr("class", "dt-refreshwidgets-wrapper");
	    this.autoRefreshWrapper = refrshWidgetscontainer
	        .append("div")
	        .attr("class", "dt-autoRefresh-wrapper")
	        .style("display", "none");
	
	    this.refreshBtn = refrshWidgetscontainer
	        .append("button")
	        .attr("class", "dt-refresh-btn")
	        .text("Refresh")
	        .on("click", (event) => {
	            this.callbacks.onChangeRefreshInterval();
	        });
        let options = [
            {
                label: APP_SETTINGS.none,
                value: 0,
            },
            {
                label: "15",
                value: 15 * 60 * 1000,
                default: true,
            },
            {
                label: "30",
                value: 30 * 60 * 1000,
            },
            {
                label: "60",
                value: 60 * 60 * 1000,
            },
        ];
        this.autoRefreshWrapper.append("label").text("Auto Refresh(m):");
        let selectEl = this.autoRefreshWrapper
            .append("select")
            .on("change", (event) => {
                let { value } = event.target;
                this.callbacks.onChangeRefreshInterval(value);
            });
        selectEl
            .selectAll(".options")
            .data(options)
            .enter()
            .append("option")
            .attr("value", (d) => d.value)
            .property("selected", (d) => d.default)
            .text((d) => d.label);
//        this.autoRefreshWrapper
//            .append("span")
//            .html(ICONS.refreshIcon)
//            .on("click", () => {
//                this.callbacks.onChangeRefreshInterval(selectEl.node().value);
//            });
    }
    addDemoMode() {
        const onToggle = (checked) => {
            this.DEMO_MODE = checked;
            this.faultsWrapper.style("display", checked ? "flex" : "none");
            this.callbacks.changeDemoMode(checked);
        };
        let toggleWrapper = this.container
            .append("div")
            .attr("class", "dt-observations-toggle-wrapper");
        let toggleDiv = toggleWrapper.append("div");
        this.toggleInput = toggleDiv
            .append("input")
            .attr("type", "checkbox")
            .attr("id", "toggle-button")
            .attr("class", "toggle-input")
            .property("checked", this.DEMO_MODE)
            .on("change", (event) => {
                this.callbacks.sendDemoRequest(event.target.checked);
            	this.toggleDemoMode(event.target.checked);
            });
        toggleDiv
            .append("label")
            .attr("for", "toggle-button")
            .attr("class", "dt-observations-toggle toggle");
        toggleWrapper.append("label").text(APP_SETTINGS.demoMode);
        this.toggleDemoMode(this.DEMO_MODE);
    }
    toggleDemoMode(bool) {
        this.DEMO_MODE = bool;
        this.faultsWrapper.style("display", bool ? "flex" : "none");
        this.callbacks.changeDemoMode(bool);
        this.toggleInput.node().checked = bool;
//        setTimeout(()=>{
//        	this.screensList.forEach((screen) => {
//        		screen.loadMeasurements();
//        	})
//        },3 * 1000);
    }
    addFaults(faults, asset) {
        this.faults = faults;
        this.activeAsset = asset;
        this.faultsWrapper.selectAll("select")?.remove();
        let selectEl = this.faultsWrapper
        .insert("select", "div")
            .attr("class", "dt-fault-select")
            .on("change", (event) => {
                let faultCode = faults.find((fault) => fault.code == event.target.value);
                this.saveFault(faultCode);
                this.getAnalysis = false;
                setTimeout(() => {
                    this.getAnalysis = true;
                    this.callbacks.onChangeRefreshInterval();
                    this.handleStatus();
                    if(faultCode?.name === "Normal") {
                    	this.changeStatus("00-000");
                    }
                }, 50000);
            });
        selectEl
            .selectAll(".options")
            .data(faults)
            .enter()
            .append("option")
            .attr("value", (d) => d.code)
            .property("selected", (d) => d.code == this.activeFault?.faultCode?.code)
            .text((d) => d.name);
        if (this.currentFaultInterval) {
            clearTimeout(this.currentFaultInterval);
        }
        this.currentFaultInterval = setInterval(() => {
            this.setCurrentFault(faults, asset);
        }, 10000);
        this.setCurrentFault(faults, asset);
    }
    handleStatus(currentFault) {
        if (!this.getAnalysis) return;
        if (!currentFault) {
            this.callbacks.removeStatus();
            this.callbacks.onClickStatus();
            return;
        }
        if (
            this.activeFault &&
            this.activeFault?.faultCode?.code != currentFault?.faultCode?.code
        ) {
            this.callbacks.removeStatus();
            if (!currentFault?.faultCode?.code.includes("00-000")) {
                this.callbacks.onClickStatus();
            }
        }
    }

    setCurrentFault(faults, asset) {
        let filter = {
            DigitalTwinFilter: {
                ecn: asset.assetEcn,
            },
        };
        invokeRestService(API_ROUTES.GET_CURRENT_FAULT, filter, {
            handleMeasurements: (data) => {
                if (!data.DigitalTwin || data.DigitalTwin.length == 0){
                	this.activeFault = null;
                	return;
                }
                this.handleStatus(data.DigitalTwin[0]);
                this.activeFault = data.DigitalTwin[0];
                if (data.DigitalTwin.length == 0) {
                    this.activeFault = {
                        faultCode: {
                            code: faults[0]?.code,
                            name: faults[0]?.name,
                        },
                        asset: {
                            id: asset.assetId,
                        },
                    };
                }
                this.faultsWrapper
                    .select(".dt-fault-select")
                    .selectAll("option")
                    .property(
                        "selected",
                        (d) => d.code == this.activeFault.faultCode.code
                    );
//                this.changeStatus(this.activeFault.faultCode.code);
            },
        });
    }
    changeStatus(status) {
    	if (!status || status.includes("undefined")) return;
    	if (typeof status !== "string" || !status.trim()) {
            this.statusEl.selectAll("label,img").remove();
            this.statusEl.classed("dt-fault-status", false);
            this.statusEl
                .append("label")
                .text("Normal");
            let digitalTwinManager = globalCache.getObject(this.dashboardId);
            digitalTwinManager.allFaults = [];
            return;
        }
    	let isFaulty = true;
        if (status.includes("00-000")) {
            isFaulty = false;
            status = "Normal";
            let digitalTwinManager = globalCache.getObject(this.dashboardId);
            digitalTwinManager.allFaults = [];
        }
        this.statusEl.selectAll("label,img").remove();
        this.statusEl.classed("dt-fault-status", isFaulty);
//        this.statusEl.append("label").text(status);
        const statuses = isFaulty
        ? status
            .split(/\s*(?:or|,)\s*/i)
            .map(s => s.trim())
            .filter(Boolean)
        : [status.trim()];
	
	    statuses.forEach((s, i) => {
	        this.statusEl
	            .append("label")
	            .style("margin-right", "6px")
	            .text(s.trim());
	        if (i < statuses.length - 1) {
	            this.statusEl
	              .append("label")
	              .style("margin-right", "6px")
	              .text(",");
	        }
	    });
        if (isFaulty) {
            this.statusEl
                .append("img")
                .attr("class", "dt-fault-warning")
                .attr("src", "secure_client/images/warning-mage.png");
        }
    }
    addGraphViews() {
        this.graphSelectionWrapper = this.container
            .append("div")
            .attr("class", "hs-radiogroup");
        let radioBtn = this.graphSelectionWrapper
            .selectAll(".hs-radio")
            .data(this.graphTypes)
            .enter()
            .append("div")
            .attr("class", "hs-radio");
        radioBtn
            .append("input")
            .attr("type", "radio")
            .attr("name", (d) => `hs-radio${this.dashboardId}`)
            .attr("id", (d) => `hs-radio${d.view}${this.dashboardId}`)
            .on("change", (event, d) => {
            	if (d.view == this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.VIBRATION) {
	                this.autoRefreshWrapper.style("display", null);
	            } else {
	                this.autoRefreshWrapper.style("display", "none");
	            }
                this.callbacks.setView(d.view);
            });
        radioBtn
            .append("label")
            .attr("class", "hs-radio-label")
            .html((d) => d.label)
            .attr("for", (d) => `hs-radio${d.view}${this.dashboardId}`);
    }
    setGraphView(view) {
    	if (view == this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.VIBRATION) {
            this.autoRefreshWrapper.style("display", null);
        } else {
            this.autoRefreshWrapper.style("display", "none");
        }
        this.graphSelectionWrapper
            .select(`#hs-radio${view}${this.dashboardId}`)
            .property("checked", true);
    }
    saveFault(faultCode) {
        let filter = {
            DigitalTwin: {
                id: this.activeFault?.id ?? 0,
                faultCode,
                asset: {
                	id: this.activeFault?.asset?.id ?? this.activeAsset?.assetId
                },
            },
        };
        invokeRestService(API_ROUTES.SAVE_FAULT, filter, {
            handleMeasurements: (data) => {
            },
        });
    }
}
class DigitalScreen {
    constructor() {
    	this.VIB_CONSTANTS = new VibrationsConstants().VIB_CONSTANTS;
    	this.CONSTANTS = JSON.parse(JSON.stringify(this.VIB_CONSTANTS));
        this.screenId = null;
        this.observations = [];
        this.width = null;
        this.height = 300;
        this.firstRequest = true;
        this.socketObj = {};
        this.fromDate = null;
        this.toDate = null;
        this.activeView = null;
        this.data = {
            Actual: [],
            Expected: [],
        }; 
        this.changedUnits = {
    	    x: "hz",
    	    y: "ms2",
    	  };
		this.pathColors = {
			Expected:"rgb(31, 119, 180)",
			Actual:"rgb(255, 127, 14)",
		}
        this.inActiveGraphIndex = null;
        this.lineGraph = new CustomMultiLineGraph();
        this.handleMeasurements = this.handleMeasurements.bind(this);
        this.digitalTwinConstants = new DigitalTwinConstants();
    }
    initScreen(dashboardId,container, websocket, screenInstance, activeView, getDemoMode) {
        this.activeView = activeView;
        this.dashboardId = dashboardId;
        this.websocket = websocket;
        this.getDemoMode = getDemoMode;
        this.screenInstance = screenInstance;
        this.height = screenInstance.graphHeight ?? this.height;
        let screenBox = new DashboardBox();
        screenBox.createBox({ heading: this.screenName }, container, "dt");
        this.screencontent = screenBox.boxcontent;
        this.width = this.screencontent.node().getBoundingClientRect().width;
        this.addGraph(this.screenInstance.screenType);
        this.autoRefresh();
    }
    setScreenDetails(screenDetails) {
        this.screenId = screenDetails.screenId;
        this.screenName = screenDetails.screenName;
        this.units = screenDetails.unit;
        this.observations = screenDetails.observationList.sort((a, b) =>
	        a.type.localeCompare(b.type)
	    );
		this.observations = this.observations.map((d)=>{
			return {...d,color:this.pathColors[d.type]??this.pathColors.Expected}
		})
    }
    loadMeasurements() {
        this.observations.forEach((observation) => {
            let filter;
            if (
                this.screenInstance.screenType == this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.OBSERVATION
            ) {
            	let interval = 1000 * 60 * 10;
                let toDate = new Date().getTime();
                if (this.getDemoMode()) {
                    toDate = toDate;
                    interval = this.firstRequest ? 2 * 60 * 1000 : 5 * 1000;
                }
                filter = {
                    to_date: toDate,
                    from_date: toDate - interval,
                    msg_type: "CONDITION_DASHBOARD",
                    realtime: "true",
                    tag: observation.tagname,
                    uid: observation.code,
                };
                this.fromDate = filter.from_date;
                this.toDate = filter.to_date;
            } else {
                filter = {
                    msg_type: "GET_HARMONICS",
                    filter: {
                        firstRequest: false,
                        type: 4265,
                        sensors: [
                            {
                                sensorName: observation.tagname,
                            },
                        ],
                        directions: [observation.code],
                        dateRange: {
                            fromDate: new Date().getTime() - 3 * 60 * 60* 1000,
                            toDate: new Date().getTime(),
                        },
                        digitalTwin: true,
                    },
                    uid: observation.code,
                };
                this.fromDate = filter.filter.dateRange.fromDate;
                this.toDate = filter.filter.dateRange.toDate;
            }
            this.websocket.sendMessage(filter, this.handleMeasurements);
        });
        this.firstRequest = false;
    }
    handleMeasurements(response) {
        let index = this.observations.findIndex((obs) => response.uid == obs.code);
        let measurements;
        if (this.screenInstance.screenType == this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.OBSERVATION) {
            let prevMeasurements = !this.getDemoMode()?[]:this.data[this.observations[index].type];
            measurements = [];
            response.measurements.forEach((measurement) => {
                let index = prevMeasurements.findIndex(
                    (d) => d.x == measurement.x
                );
                if (index == -1) {
                    measurements.push({
                        x: measurement.time,
                        y: measurement.value,
                    });
                } else {
                    prevMeasurements[index].y = measurement.y;
                }
            });
            const newTimestamps = new Set(measurements.map(m => m.x));
            const prevTimestamps = new Set(prevMeasurements.map(m => m.x));
            const uniqueNewCount = measurements.filter(m => !prevTimestamps.has(m.x)).length;
            prevMeasurements = prevMeasurements.filter(m => !newTimestamps.has(m.x));
            const toRemove = Math.min(prevMeasurements.length, uniqueNewCount);
            measurements = [...prevMeasurements, ...measurements];
            measurements.sort((a, b) => a.x - b.x);
            if (this.getDemoMode() && measurements.length > 120) {
            	measurements.splice(0, toRemove);
            }
        } else {
            measurements = response.VibConditionData.harmonics?.map((d) => ({
                x: d.frequency,
                y: d.amplitude,
            }));
            measurements.sort((a, b) => a.x - b.x);
        }
        this.data[this.observations[index].type] = measurements;
        this.data.Expected = this.data.Expected.filter((d) => {
            return (
                this.data.Actual.length <= 0 || d.x >= this.data.Actual[0]?.x
            );
        });
        if(this.screenInstance.screenType !== this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.OBSERVATION) {
        	this.onSelectUnit(true);
        	return;
        }
        this.updateGraph([this.data.Actual, this.data.Expected]);
    }
    autoRefresh() {
        if (this.startInterval) {
            clearInterval(this.startInterval);
        }
        let interval = this.screenInstance.autoRefreshTime;
        if(this.getDemoMode()) {
        	if(this.screenInstance.screenType ==
                this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.OBSERVATION
            ) {
        		interval = 1000;
        	}
        	if(this.screenInstance.screenType ==
                this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.VIBRATION
            ) {
        		interval = 35000;
        	}
        }
        this.loadMeasurements();
        if (this.screenInstance.screenType != this.activeView || !d3.select(this.screencontent.node()).node()) return;
        this.startInterval = setInterval(() => {
            this.loadMeasurements();
        }, interval);
    }
    resizeScreen(height) {
        this.width = this.screencontent.node().getBoundingClientRect().width;
        this.height = height ?? this.height;
        this.lineInstance.graphWidth = this.width;
        this.lineInstance.graphHeight = this.height;
        this.lineGraph.resize(this.width, this.height);
        this.lineGraph.svgWrapper.getSVG().attr("width", "100%");	
    }
    
    getAxisLabel(label, id) {
    	let unitIndex = this.VIB_CONSTANTS[label].findIndex((type) => type.status);
        let labelWrapper = d3.create("g");
        this[`${this.screenId}-${id}label`] = label;
        let tagName = labelWrapper
          .append("text")
          .attr("id", `${this.screenId}-${id}-text-wrpper`)
          .text(label);
        let unitsWrapper = labelWrapper
          .append("g")
          .attr("id", `${this.screenId}-${id}-units-wrpper`)
          .attr("class", "units-wrpper");
        this[`${id}Unitslabel`] = this.CONSTANTS[label][unitIndex].title;
        let value1 = getLsItem(`${this.screenId}_${id === "x" ? "Frequency" : "DTAcc"}`);
        if(!value1 && id === "x"){
        	value1 = "hz"
        } 
        if(!value1 && id !== "x") {
        	value1 = "ms2"
        }
        let title = this.VIB_CONSTANTS[label]?.find(item => item.value === value1)?.title || null;
       unitsWrapper.append("text").text(title);
        unitsWrapper
          .append("g")
          .attr("class", `${this.screenId}-${id}-axis-down-arrow`)
          .html(ICONS.downArrow);
      
        unitsWrapper.attr("transform", "translate(" + label.length * 8 + ", 0)");
        setTimeout(() => {
          let unit = d3.select(`#${this.screenId}-${id}-units-wrpper`);
          let tag = d3.select(`#${this.screenId}-${id}-text-wrpper`);
          if(unit.empty())return
         this.changedUnits[`${id}`] = unit.selectAll("text").text().replace("/","").toLowerCase();
          unit
            .on("click", (event) => {
              event.stopPropagation();
              event.preventDefault()
              this.displayPopover(
                this.CONSTANTS[tag.text()],
                { x: event.clientX, y: event.clientY },
                unit,
                id
              );
            })
            .on("mouseover", function () {
              d3.select(this)
                .selectAll("text")
                .style("fill", "dodgerblue")
                .style("cursor", "pointer");
            })
            .on("mouseleave", function () {
              d3.select(this).selectAll("text").style("fill", "#000");
            });
        }, 2000);
        return labelWrapper.node().outerHTML;
    }
    displayPopover(list, position, unitsWrapper, axis) {
        d3.selectAll(".units-list").remove();
        const isFullscreen = d3.select(".vb-charts-wrapper").node() === document.fullscreenElement;
        let className ;
        if(isFullscreen){
        	className = ".digital-twin-wrapper"
        } else{
        	className = "body"
        }
        let containerSelector = isFullscreen
	        ? ".digital-twin-wrapper"
	        : "body";
	    const container = d3.select(containerSelector);
	
	    const containerNode = container.node();
	    const containerRect = containerNode.getBoundingClientRect();
	    const relativeX = position.x - containerRect.left;
	    const relativeY = position.y - containerRect.top;
        let unitswrapper = d3
          .select(className)
          .append("div")
          .attr("class", "units-list")
          .style("position", "absolute")
          .style("top", relativeY + "px")
          .style("left", relativeX + "px");

        let unitslist = unitswrapper.append("ul");

        let unit = unitslist
          .selectAll(".li-unit")
          .data(list)
          .enter()
          .append("li")
          .attr("class", "li-unit")
          .on("click", (event, d) => {
            event.stopPropagation()
            unitswrapper.remove();
            unitsWrapper.selectAll("text").html(`${d.title} `);
            this.changedUnits[axis] =  d.title.replace('/', '').toLowerCase();
            axis === "x" ? (this.xUnitslabel = d.title) : (this.yUnitslabel = d.title);
            this.xAxisUnits = this.changedUnits["x"];
            this.accUnits = this.changedUnits["y"];
            setLsItem(`${this.screenId}_Frequency`, this.xAxisUnits);
            setLsItem(`${this.screenId}_DTAcc`, this.accUnits);
            let yAxisUnits = this.accUnits;
//            let index = this.vbfilter.type === 4265 ? 0 : this.vbfilter.type === 4266 ? 1 : 2;
            this.VIB_CONSTANTS[this.VIB_CONSTANTS.avd[0].title].forEach(item => item.status = item.value === yAxisUnits);
            this.VIB_CONSTANTS[APP_SETTINGS.frequency].forEach(item => item.status = item.value === this.xAxisUnits);
////            if (this.xAxisUnits !== this.previousXAxisUnits || yAxisUnits !== this.previousYAxisUnits) {
////                this.unitsChanged = true;
////              }
            this.onSelectUnit();
          });

        unit.append("label").html((d) => d.title);
        function closePopover() {
          d3.selectAll(".units-list").remove();
          document.removeEventListener("click", closePopover);
        }
      document.addEventListener("click", closePopover);
       
    }
    clearDateRanges(){
        this.xmin=null,this.ymin=null, this.xmax=null,this.ymax=null;
    }
    onSelectUnit(bool) {
        let changedData = [];
        let data = [this.data.Actual, this.data.Expected];
        this.clearDateRanges()
        let unitIndex = this.VIB_CONSTANTS[this.VIB_CONSTANTS.avd[0].title].findIndex((type) => type.status);
        let yUnitValue = this.changedUnits["y"];
        changedData.push(
    		data[0].map((m) => ({
			  ...m,
			  x: m.x * this.CONSTANTS.formulas[this.changedUnits["x"]],
			  y: m.y * this.CONSTANTS.formulas[yUnitValue],
			}))
        );
        changedData[1] = this.data.Expected;
        this.updateGraph(changedData);  
    }
    addGraph(activeView) {
    	const isVibrationView =
            activeView === this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.VIBRATION;

        const xAxisLabel = isVibrationView
            ? this.getAxisLabel("Frequency", "x")
            : `<text>${this.screenInstance.xAxisLabel}</text>`;

        const yAxisLabel = isVibrationView
            ? this.getAxisLabel(this.CONSTANTS.avd[0].title, "y")
            : `<text>${this.units}</text>`;
        this.lineInstance = new LineGraphInstance(
            this.screencontent,
            [],
            this.screenInstance.graphType,
            xAxisLabel,
            yAxisLabel,
            this.screenInstance.xAxisLabelFormat,
            this.screenInstance.pathColors,
            this.width,
            this.height,
            0,
            0,
            0,
            0,
            true,
            6,
            false,
            false,
            this.screenId
        );
        this.lineGraph.init(this.lineInstance);
        this.lineGraph.svgWrapper.getSVG().style("height", null).attr("width", "100%");;
        if (this.screenInstance.screenType == this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.OBSERVATION) {
            this.addLegends();
        }
        this.lineGraph.svg.on("mousemove", (event) => {});
    }
    getExtremes(data) {
        let xmin = 0,
            xmax = 0,
            ymin = 0,
            ymax = 0;
        data = data.flat();
        if (data.length != 0) {
            xmin = d3.min(data, (d) => d.x);
            xmax = d3.max(data, (d) => d.x);
            ymin = d3.min(data, (d) => d.y);
            ymax = d3.max(data, (d) => d.y);
            ymax += ymax / 4;
            ymin -= Math.abs(ymin / 4);
        }
        return {
            xmin,
            xmax,
            ymin,
            ymax,
        };
    }
    updateGraph(data) {
        let graphData = [...data],
            pathColors = [...this.screenInstance.pathColors];
        if (this.inActiveGraphIndex != null) {
            graphData.splice(this.inActiveGraphIndex, 1);
            pathColors.splice(this.inActiveGraphIndex, 1);
        }
        let { xmin, xmax, ymin, ymax } = this.getExtremes(graphData);
        this.width = this.screencontent.node().getBoundingClientRect().width;
        this.lineInstance.graphWidth = this.width;
        this.lineGraph.updateGraph({
            data: graphData,
            xAxisLabelFormat: this.lineInstance.xAxisLabelFormat,
            pathcolors: pathColors,
            graphWidth: this.lineInstance.graphWidth,
            graphHeight: this.lineInstance.graphHeight,
            xmin,
            xmax,
            ymin,
            ymax,
        });
        this.lineGraph.svg
	        .selectAll("rect")
	        .attr("width", Math.max(this.lineGraph.graphWidth, 0));
    }
    addLegends() {
    	let legends = this.observations.map((obs, index) => {
            return {
                name: `${obs.type}(${obs.tagname})`,
                index,
                color: this.screenInstance.pathColors[index],
            };
        });
        this.legendsWrapper = this.screencontent
            .append("div")
            .attr("class", "dt-legends-wrapper");
        let legendsEl = this.legendsWrapper
            .selectAll(".legends")
            .data(legends)
            .enter()
            .append("div")
            .attr("class", (d) => `dt-legend`)
            .on("mouseover", (event, d) => {
                if (d3.select(event.currentTarget).classed("deactivate")) return;
                this.lineGraph.paths.forEach((graph, index) => {
                    if (index != d.index) {
                        graph.style("opacity", "0.3");
                    }
                });
            })
            .on("mouseout", (event, d) => {
                this.lineGraph.paths.forEach((graph) => {
                    graph.style("opacity", "1");
                });
            })
            .on("click", (event, d) => {
                legendsEl.classed("deactivate", false);
                if (this.inActiveGraphIndex == d.index) {
                    this.inActiveGraphIndex = null;
                }else{
	                d3.select(event.currentTarget).classed("deactivate", true);
	                this.inActiveGraphIndex = d.index;
				}
		        this.updateGraph([this.data.Actual, this.data.Expected]);
            });
        legendsEl
            .append("div")
            .attr("class", `dt-legend-line`)
            .style("background", (d) => d.color);
        legendsEl.append("div").text((d) => d.name);
    }
    onChangeView(view) {
        this.activeView = view;
        clearInterval(this.startInterval);
        this.resizeScreen();
        this.autoRefresh();
    }
}
