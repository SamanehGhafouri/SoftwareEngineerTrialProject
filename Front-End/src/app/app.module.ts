import { BrowserModule } from '@angular/platform-browser';
import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UserInputComponent } from './user-input/user-input.component';
import {ReactiveFormsModule} from '@angular/forms';
import {HttpClientModule} from '@angular/common/http';
import { StatisticsResultComponent } from './statistics-result/statistics-result.component';
import {StatisticsService} from './statistics.service';
import {NgxSpinnerModule} from 'ngx-spinner';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {NgApexchartsModule} from 'ng-apexcharts';
import {SidebarModule} from 'ng-sidebar';


@NgModule({
  declarations: [
    AppComponent,
    UserInputComponent,
    StatisticsResultComponent,
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    HttpClientModule,
    AppRoutingModule,
    NgxSpinnerModule,
    NgApexchartsModule,
    SidebarModule.forRoot(),
    BrowserAnimationsModule
  ],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  providers: [StatisticsService, UserInputComponent],
  bootstrap: [AppComponent]
})
export class AppModule { }
