import {DeviceReport} from "./device-report";

export class Tester {
  public testerId: string;
  public totalBugs: number;
  public deviceReports: DeviceReport[] = [];

  constructor(testerId: string, deviceTotals: any){
    this.testerId = testerId;

    for (let report in deviceTotals) {
      if (report == "Total") {
        this.totalBugs = Number(deviceTotals[report]);
      } else {
        this.deviceReports.push(new DeviceReport(report, deviceTotals[report]));
      }
    }

  }
}
