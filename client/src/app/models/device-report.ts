export class DeviceReport {

  public device: string;
  public bugCount: number;

  constructor(public deviceName: string, public deviceTotal: string){
    this.device = deviceName;
    this.bugCount = Number(deviceTotal);
  }

}
