import { BrowserModule } from '@angular/platform-browser';
import { HttpModule } from '@angular/http';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { SuiSelectModule, SuiCheckboxModule } from 'ng2-semantic-ui';

import { AppComponent } from './app.component';
import { HttpService } from "./services/http.service";
import { TesterComponent } from './tester/tester.component';
import { routing } from "./app.routing";

@NgModule({
  declarations: [
    AppComponent,
    TesterComponent
  ],
  imports: [
    BrowserModule,
    HttpModule,
    FormsModule,
    ReactiveFormsModule,
    SuiSelectModule,
    SuiCheckboxModule,
    routing
  ],
  providers: [
    HttpService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
