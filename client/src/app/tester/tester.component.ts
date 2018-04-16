import { Component, OnInit } from '@angular/core';
import { HttpService } from "../services/http.service";
import { Observable } from 'rxjs';

@Component({
  selector: 'tm-tester',
  templateUrl: './tester.component.html',
  styleUrls: ['./tester.component.css']
})
export class TesterComponent implements OnInit {

  public countries;
  public devices;

  constructor(private httpService: HttpService) {}

  ngOnInit() {
    this.httpService.getCountries().subscribe(data => {
      this.countries = data
    });
    this.httpService.getDevices().subscribe(data => {
      this.devices = data
    });
  }

}
