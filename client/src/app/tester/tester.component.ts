import { Component, OnInit } from '@angular/core';
import { HttpService } from "../services/http.service";
import { Observable } from 'rxjs';
import { FormGroup, FormControl, FormArray, FormBuilder } from '@angular/forms';

@Component({
  selector: 'tm-tester',
  templateUrl: './tester.component.html',
  styleUrls: ['./tester.component.css']
})
export class TesterComponent implements OnInit {

  public searchForm;
  public countries;
  public devices;

  public selectedCountries = [];

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
    console.log(selectedCountries);
  }

}
