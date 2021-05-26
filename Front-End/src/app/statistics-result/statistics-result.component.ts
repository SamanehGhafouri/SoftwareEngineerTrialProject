import { Component, OnInit } from '@angular/core';
import {UserInputComponent} from '../user-input/user-input.component';
import {StatisticsService} from '../statistics.service';

@Component({
  selector: 'app-statistics-result',
  templateUrl: './statistics-result.component.html',
  styleUrls: ['./statistics-result.component.css']
})
export class StatisticsResultComponent implements OnInit {
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
  }

  ngOnInit(): void {

  }

  statOne(){
    this.statisticOne = this.statistics.percent_stat_1;
    return this.statisticOne;
  }

  statTwo(){
    this.statisticTwo = this.statistics.percent_stat_2;
    return this.statisticTwo;
  }
  statThree(){
    this.statisticThree = this.statistics.percent_stat_3;
    return this.statisticThree;
  }
  statFour(){
    this.statisticFour = this.statistics.percent_stat_4;
    return this.statisticFour;
  }
  statFive(){
    this.statisticFive = this.statistics.percent_stat_5;
    return this.statisticFive;
  }
  statSix(){
    this.statisticSix = this.statistics.percent_stat_6;
    return this.statisticSix;
  }
  statSeven(){
    this.statisticSeven = this.statistics.percent_stat_7;
    return this.statisticSeven;
  }


}
