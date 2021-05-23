import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UserInputComponent } from './user-input/user-input.component';
import {ReactiveFormsModule} from '@angular/forms';
import {HttpClientModule} from '@angular/common/http';
import { StatisticsResultComponent } from './statistics-result/statistics-result.component';
import {StatisticsService} from './statistics.service';


@NgModule({
  declarations: [
    AppComponent,
    UserInputComponent,
    StatisticsResultComponent
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [StatisticsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
