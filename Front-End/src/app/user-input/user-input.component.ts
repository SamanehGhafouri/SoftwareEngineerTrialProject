import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup} from '@angular/forms';
import {StatisticsService} from '../statistics.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-user-input',
  templateUrl: './user-input.component.html',
  styleUrls: ['./user-input.component.css']
})
export class UserInputComponent implements OnInit {
  form: FormGroup;

  constructor(private service: StatisticsService, public router: Router) { }

  ngOnInit(): void {
    this.form = new FormGroup({
      inputData: new FormControl('{example_text:"example text value"}'),
      uploadFile: new FormControl('')
    });
  }
  onSubmit(){
    if (this.form.value.inputData) {
      console.log('this is coming from inputData');
      const requestObserver = this.service.uploadJson(this.form.value.inputData);
      requestObserver.subscribe({
        next: data => {
          console.log('## RESPONSE FROM BACK END ##', data);
        },
        error: error => {
          const errorMessage = error.message;
          console.error('There was an error!', error);
        }
      });
    }
    else {
      console.log('this is coming from uploadFile');
      const requestObserver = this.service.uploadJson(this.form.value.inputData);
      requestObserver.subscribe({
        next: data => {
          console.log('## RESPONSE FROM BACK END ##', data);
        },
        error: error => {
          const errorMessage = error.message;
          console.error('There was an error!', error);
        }
      });
    }
    // this.router.navigate(['/results']);
  }

}
