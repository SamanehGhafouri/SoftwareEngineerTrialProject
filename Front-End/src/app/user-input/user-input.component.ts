import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup} from '@angular/forms';
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

  constructor(private service: StatisticsService, public router: Router, private spinner: NgxSpinnerService) { }

  ngOnInit(): void {
    this.form = new FormGroup({
      inputData: new FormControl(''),
      uploadFile: new FormControl('')
    });
  }
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
    this.form.reset();
    this.spinner.show();
    setTimeout(() => {
      this.spinner.hide();
      this.router.navigate(['/results']);
    }, 5000);
  }
}
