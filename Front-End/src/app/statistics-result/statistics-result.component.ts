import {Component, ViewChild} from '@angular/core';
import {UserInputComponent} from '../user-input/user-input.component';
import {StatisticsService} from '../statistics.service';
import {ApexChart, ApexNonAxisChartSeries, ApexResponsive, NgApexchartsModule} from 'ng-apexcharts';

export type ChartOptions = {
  series: ApexNonAxisChartSeries;
  chart: ApexChart;
  responsive: ApexResponsive[];
  labels: any;
};

@Component({
  selector: 'app-statistics-result',
  templateUrl: './statistics-result.component.html',
  styleUrls: ['./statistics-result.component.css']
})
export class StatisticsResultComponent{
  @ViewChild('chart-stats') chart: StatisticsResultComponent;
  public chartOptions: Partial<ChartOptions>;
  statistics;
  definitionsD;
  statisticOne;
  statisticTwo;
  statisticThree;
  statisticFour;
  statisticFive;
  statisticSix;
  statisticSeven;
  constructor(private userInput: UserInputComponent, private service: StatisticsService) {
    this.statistics = this.service.responseData.stats;
    this.definitionsD = this.service.responseData.definitions;

    this.chartOptions = {
      series: [],
      chart: {
        width: 500,
        type: 'pie'
      },
      labels: [],
      responsive: [
        {
          breakpoint: 480,
          options: {
            chart: {
              width: 200
            },
            legend: {
              position: 'bottom'
            }
          }
        }
      ]
    };
  }
  statOne(){
    this.statisticOne = this.statistics.percent_stat_1;
    this.chartOptions.series = [this.statisticOne, (100 - this.statisticOne)];
  }
  statTwo(){
    this.statisticTwo = this.statistics.percent_stat_2;
    this.chartOptions.series = [this.statisticTwo, (100 - this.statisticTwo)];
  }
  statThree(){
    this.statisticThree = this.statistics.percent_stat_3;
    this.chartOptions.series = [this.statisticThree, (100 - this.statisticThree)];
  }
  statFour(){
    this.statisticFour = this.statistics.percent_stat_4;
    const arr = [];
    for (const key in this.statisticFour){
      if (this.statisticFour.hasOwnProperty(key)){
        arr.push(this.statisticFour[key]);
      }
    }
    this.chartOptions.series = arr;
  }
  statFive(){
    this.statisticFive = this.statistics.percent_stat_5;
    const arr = [];
    for (const key in this.statisticFive){
      if (this.statisticFive.hasOwnProperty(key)){
        arr.push(this.statisticFive[key]);
      }
    }
    this.chartOptions.series = arr;
  }
  statSix(){
    this.statisticSix = this.statistics.percent_stat_6;
    const arr = [];
    for (const key in this.statisticSix){
      if (this.statisticSix.hasOwnProperty(key)){
        arr.push(this.statisticSix[key]);
      }
    }
    this.chartOptions.series = arr;
  }
  statSeven(){
    this.statisticSeven = this.statistics.percent_stat_7;
    const arr = [];
    for (const key in this.statisticSeven){
      if (this.statisticSeven.hasOwnProperty(key)){
        arr.push(this.statisticSeven[key]);
      }
    }
    this.chartOptions.series = arr;
  }

}
