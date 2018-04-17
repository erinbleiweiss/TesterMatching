import { Component, OnInit } from '@angular/core';
import { HttpService } from "../services/http.service";
import { Observable } from 'rxjs';
import { FormGroup, FormControl, FormArray, FormBuilder } from '@angular/forms';
import { Tester } from "../models/tester";

@Component({
  selector: 'tm-tester',
  templateUrl: './tester.component.html',
  styleUrls: ['./tester.component.css']
})
export class TesterComponent implements OnInit {

  public searchForm;
  public countries;
  public devices;

  public searchResult: Tester[] = [];

  constructor(
    private httpService: HttpService,
    private formBuilder: FormBuilder
  ) {}

  ngOnInit() {
    this.httpService.getCountries().subscribe(data => {
      this.countries = data
    });
    this.httpService.getDevices().subscribe(data => {
      this.devices = data
    });

    this.searchForm = this.formBuilder.group({
      countrySelect:[],
      deviceSelect:[]
    })

  }

  onSubmit(){
    let selectedCountries = this.searchForm.controls['countrySelect'].value;
    let countryParam = selectedCountries ? selectedCountries.join('|') : "all";
    let selectedDevices = this.searchForm.controls['deviceSelect'].value;
    let deviceParam = selectedDevices ? selectedDevices.join('|') : "all";

    this.httpService.search(countryParam, deviceParam).subscribe(data => {
      this.searchResult = [];

      for (let testerId in data) {
        this.searchResult.push(new Tester(testerId, data[testerId]));
      }

      this.searchResult.sort(function(t1, t2){
        return t2.totalBugs - t1.totalBugs;
      });

      console.log(this.searchResult);

    })

  }

}
