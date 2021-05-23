import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {UserInputComponent} from './user-input/user-input.component';
import {StatisticsResultComponent} from './statistics-result/statistics-result.component';


const routes: Routes = [
  {path: '', component: UserInputComponent},
  {path: 'results', component: StatisticsResultComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
