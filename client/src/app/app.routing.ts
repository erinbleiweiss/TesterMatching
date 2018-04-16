import { Routes, RouterModule } from "@angular/router";
import { AppComponent } from "./app.component";
import { TesterComponent } from "./tester/tester.component";

const APP_ROUTES: Routes = [
  {
    path: '',
    component: TesterComponent,
    pathMatch: 'full'
  }
];

export const routing = RouterModule.forRoot(APP_ROUTES);
