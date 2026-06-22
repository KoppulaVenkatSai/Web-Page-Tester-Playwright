class DigitalTwinPanel extends BaseGraphPanel {
  constructor(container, assetService, context) {
    super(container, context, "digital-twin-wrapper");
    this.container = container;
    this.container.select(".digital-twin-wrapper").style("height", "500px");
    this.handleMeasurements = this.handleMeasurements.bind(this);
  }
  loadMeasurements() {
    this.observations.forEach((observation) => {
      let filter;
      if (true) {
        let interval = 1000 * 60 * 10;
        let toDate = new Date().getTime();
        if (true) {
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
              fromDate: new Date().getTime() - 3 * 60 * 60 * 1000,
              toDate: new Date().getTime(),
            },
            digitalTwin: true,
          },
          uid: observation.code,
        };
        this.fromDate = filter.filter.dateRange.fromDate;
        this.toDate = filter.filter.dateRange.toDate;
      }
      this.workSpaceContext.websocket.sendMessage(
        filter,
        this.handleMeasurements,
      );
    });
    this.firstRequest = false;
  }
  handleMeasurements(response) {
    let index = this.observations.findIndex((obs) => response.uid == obs.code);
    let measurements;
    if (true) {
      let prevMeasurements = this.data[this.observations[index].type];
      measurements = [];
      response.measurements.forEach((measurement) => {
        let index = prevMeasurements.findIndex((d) => d.x == measurement.x);
        if (index == -1) {
          measurements.push({
            x: measurement.time,
            y: measurement.value,
          });
        } else {
          prevMeasurements[index].y = measurement.y;
        }
      });
      const newTimestamps = new Set(measurements.map((m) => m.x));
      const prevTimestamps = new Set(prevMeasurements.map((m) => m.x));
      const uniqueNewCount = measurements.filter(
        (m) => !prevTimestamps.has(m.x),
      ).length;
      prevMeasurements = prevMeasurements.filter(
        (m) => !newTimestamps.has(m.x),
      );
      const toRemove = Math.min(prevMeasurements.length, uniqueNewCount);
      measurements = [...prevMeasurements, ...measurements];
      measurements.sort((a, b) => a.x - b.x);
      if (true && measurements.length > 120) {
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
      return this.data.Actual.length <= 0 || d.x >= this.data.Actual[0]?.x;
    });
    // if (
    //   this.screenInstance.screenType !==
    //   this.digitalTwinConstants.DIGITALTWIN_CONSTANTS.views.OBSERVATION
    // ) {
    //   this.onSelectUnit(true);
    //   return;
    // }
    this.updateGraph([this.data.Actual, this.data.Expected]);
  }
  render(asset) {
    this.root.selectAll("*").remove();
    console.log(asset);
    this.asset = asset;
    if(!this.asset) return;
    initDigitalTwinManager("digital-twin-wrapper");
    showActiveAsset("digital-twin-wrapper", this.asset);
    // this.root.append("h3").text("This is digital-twin panel");
    // this.getObservationScreensList((screensList) => {
    //   screensList.forEach((screen) => {
    //     this.initScreen(screen, {
    //       graphType: "timeseries",
    //       xAxisLabel: "time",
    //       yAxisLabel: "bar-S",
    //       xAxisFormat: d3.timeFormat("%H:%M:%S"),
    //       graphHeight: 300,
    //       pathColors: ["rgb(255, 127, 14)", "rgb(31, 119, 180)"],
    //     });
    //   });
    // });
  }
  show() {
    this.root.style("display", "grid");
//    document.addEventListener("asset-data-loaded", () => {
//      this.show();
//    });
  }

  hide() {
    this.root.style("display", "none");
  }
  getObservationScreensList(callback) {
    let filter = {
      TagFilterRest: {
        ecn: this.asset,
        searchType: "equals",
      },
    };
    invokeRestService(API_ROUTES.GET_TAGS, filter, {
      handleMeasurements: async (response) => {
        if (!response.TagLight) return;
        let tags = response.TagLight.filter(
          (tag) => tag.type == 4300 && tag.tagStatus == 6132,
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
          invokeRestService(
            API_ROUTES.GET_FORM_ITEM + tag.obsCode,
            tag.obsCode,
            {
              handleMeasurements: (res) => {
                if (!res.FormItem) return;
                resCount += 1;
                let observation = res.FormItem;
                observation.type = "Actual";
                let tagname = tags.find(
                  (tag) => tag.obsCode == observation.id,
                ).tagName;
                let screenId = observation.code;
                let screenName = observation.name;
                if (res.FormItem.code.includes("EXP")) {
                  screenId = screenId.replace("EXP-", "");
                  observation.type = "Expected";
                  screenName = screenName.replace("Expected" + " ", "");
                }
                let index = screensList.findIndex(
                  (screen) => screen.screenId == screenId,
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
                    unit: observation.measurementUnit?.name ?? "",
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
            },
          );
        });
      },
    });
  }
  getDummyData() {
    return [5, 15, 2, 10, 4, 6, 18, 3, 20, 19, 8, 16];
  }
}
