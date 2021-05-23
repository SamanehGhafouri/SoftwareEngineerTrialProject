import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup, Validators} from '@angular/forms';

@Component({
  selector: 'app-user-input',
  templateUrl: './user-input.component.html',
  styleUrls: ['./user-input.component.css']
})
export class UserInputComponent implements OnInit {
  uploadForm: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.uploadForm = new FormGroup({
      inputData: new FormControl(''),
      uploadData: new FormControl('')
    });
  }
  onSubmit(){
    console.log('I uploaded', this.uploadForm.value);
  }

}
