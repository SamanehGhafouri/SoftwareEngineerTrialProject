import {Component, OnInit, ViewChild} from '@angular/core';
import {UserInputComponent} from '../user-input/user-input.component';
import {StatisticsService} from '../statistics.service';
import {ApexChart, ApexNonAxisChartSeries, ApexResponsive, NgApexchartsModule} from 'ng-apexcharts';
import {Router} from '@angular/router';

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
export class StatisticsResultComponent implements OnInit {
  @ViewChild('chart-stats') chart: StatisticsResultComponent;
  public chartOptions: Partial<ChartOptions>;
  message;
  statistics;
  statDefinitions;
  statisticOne;
  statisticTwo;
  statisticThree;
  statisticFour;
  statisticFive;
  statisticSix;
  statisticSeven;

  constructor(private userInput: UserInputComponent, private service: StatisticsService, private router: Router) {
    if (this.service.responseData === undefined){
      this.router.navigate(['/home']);
    }
    this.statistics = this.service.responseData.stats;
    this.statDefinitions = this.service.responseData.definitions;

    this.chartOptions = {
      series: [],
      chart: {
        width: 600,
        type: 'pie'
      },
      labels: [],
      responsive: [
        {
          breakpoint: 480,
          options: {
            chart: {
              width: 400
            },
            legend: {
              position: 'bottom'
            }
          }
        }
      ]
    };
  }

  ngOnInit() {
    // StatOne
    this.statOne();
  }

  statOne() {
    this.statisticOne = this.statistics.percent_stat_1;
    this.chartOptions.series = [this.statisticOne, (100 - this.statisticOne)];
    this.chartOptions.labels = ['Female', 'Male'];
    this.message = '1.Percentage Female Versus Male';
  }

  statTwo() {
    this.statisticTwo = this.statistics.percent_stat_2;
    this.chartOptions.series = [this.statisticTwo, (100 - this.statisticTwo)];
    this.chartOptions.labels = ['First Name (A-M)', 'First Name (N-Z)'];
    this.message = '2.Percentage of First Names That Start With A-M Versus N-Z';
  }

  statThree() {
    this.statisticThree = this.statistics.percent_stat_3;
    this.chartOptions.series = [this.statisticThree, (100 - this.statisticThree)];
    this.chartOptions.labels = ['Last Name (A-M)', 'Last Name (N-Z)'];
    this.message = '3.Percentage of Last Names That Start With A-M Versus N-Z';
  }

  statFour() {
    this.statisticFour = this.statistics.percent_stat_4;
    const arrValues = [];
    const arrKeys = [];
    for (const key in this.statisticFour) {
      if (this.statisticFour.hasOwnProperty(key)) {
        arrValues.push(this.statisticFour[key]);
        arrKeys.push(key);
      }
    }
    this.chartOptions.series = arrValues;
    this.chartOptions.labels = arrKeys;
    this.message = '4.Percentage of People In Each State, Up To The Top 10 Most Populous States';
  }

  statFive() {
    this.statisticFive = this.statistics.percent_stat_5;
    const arrValues = [];
    const arrKeys = [];
    for (const key in this.statisticFive) {
      if (this.statisticFive.hasOwnProperty(key)) {
        arrValues.push(this.statisticFive[key]);
        arrKeys.push(key);
      }
    }
    this.chartOptions.series = arrValues;
    this.chartOptions.labels = arrKeys;
    this.message = '5.Percentage of Female In Each State, Up To The Top 10 Most Populous States';
  }

  statSix() {
    this.statisticSix = this.statistics.percent_stat_6;
    const arrValues = [];
    const arrKeys = [];
    for (const key in this.statisticSix) {
      if (this.statisticSix.hasOwnProperty(key)) {
        arrValues.push(this.statisticSix[key]);
        arrKeys.push(key);
      }
    }
    this.chartOptions.series = arrValues;
    this.chartOptions.labels = arrKeys;
    this.message = '6.Percentage of Male In Each State, Up To The Top 10 Most Populous States';
  }

  statSeven() {
    this.statisticSeven = this.statistics.percent_stat_7;
    const arrValues = [];
    const arrKeys = [];
    for (const key in this.statisticSeven) {
      if (this.statisticSeven.hasOwnProperty(key)) {
        arrValues.push(this.statisticSeven[key]);
        arrKeys.push(key);
      }
    }
    this.chartOptions.series = arrValues;
    this.chartOptions.labels = arrKeys;
    this.message = '7.Percentage of People In The Following Age Ranges: 0-20, 21-40, 41-60, 61-80, 81-100, 100+';
  }

}
