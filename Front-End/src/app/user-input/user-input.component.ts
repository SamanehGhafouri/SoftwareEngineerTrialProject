import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup, Validators} from '@angular/forms';
import {StatisticsService} from '../statistics.service';
import {Router} from '@angular/router';
import {NgxSpinnerService} from 'ngx-spinner';

@Component({
  selector: 'app-user-input',
  templateUrl: './user-input.component.html',
  styleUrls: ['./user-input.component.css']
})
export class UserInputComponent implements OnInit {
  form: FormGroup;
  jsonString;
  responseData;

  constructor(private service: StatisticsService, public router: Router, private spinner: NgxSpinnerService) { }

  ngOnInit(): void {
    this.form = new FormGroup({
      inputData: new FormControl('', [Validators.required]),
      uploadFile: new FormControl('')
    });
  }
  get inputData() { return this.form.get('inputData'); }
  onFileSelected(event) {
    const fileReader = new FileReader();
    fileReader.readAsText(event.target.files[0], 'UTF-8');
    fileReader.onload = () => {
      if (typeof fileReader.result === 'string') {
        this.jsonString = fileReader.result;
        // console.log(JSON.parse(fileReader.result));
      }
    };
    fileReader.onerror = (error) => {
      console.log(error);
    };
  }

  onSubmit(){
    if (this.form.value.inputData) {
      this.spinner.show();
      const requestObserver = this.service.uploadJson(this.form.value.inputData);
      requestObserver.subscribe({
        next: data => {
          // remove spinner
          this.spinner.hide();
          this.router.navigate(['/results']);
          // route to next page and pass data
          this.responseData = data;
          console.log('## RESPONSE FROM BACK END ##', data);
        },
        error: error => {
          this.spinner.hide();
          const errorMessage = error.message;
          console.error('There was an error!', error);
        }
      });
    }
  }
}
