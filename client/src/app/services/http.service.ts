import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { Http, Response } from '@angular/http';
import 'rxjs/add/operator/map'

const HOSTNAME = "http://34.217.31.121:5000";

@Injectable()
export class HttpService {

  constructor(private http: Http) { }

  getCountries(): Observable<any[]>{
    return this.http.get(`${HOSTNAME}/countries`)
      .map(res => {
        return res.json()
      });
  }

  getDevices(): Observable<any[]>{
    return this.http.get(`${HOSTNAME}/devices`)
      .map(res => {
        return res.json()
      });
  }

  search(countryParam: string, deviceParam: string): Observable<any[]>{
    return this.http.get(`${HOSTNAME}/search?country=${countryParam}&device=${deviceParam}`)
      .map(res => {
        return res.json()
      });
  }

}
