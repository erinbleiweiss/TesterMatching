import { BrowserModule } from '@angular/platform-browser';
import { HttpModule } from '@angular/http';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { SuiSelectModule, SuiCheckboxModule } from 'ng2-semantic-ui';

import { AppComponent } from './app.component';
import { HttpService } from "./services/http.service";
import { TesterComponent } from './tester/tester.component';
import { routing } from "./app.routing";
import { KeyValuePipe } from './pipes/key-value.pipe';

@NgModule({
  declarations: [
    AppComponent,
    TesterComponent,
    KeyValuePipe
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
