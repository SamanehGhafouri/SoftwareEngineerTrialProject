import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class StatisticsService {
  public responseData;
  constructor(private http: HttpClient) { }

  uploadJson(json: string){
    console.log('** HERE **');
    return this.http.post<any>('http://127.0.0.1:5000/results?format=xml', json);
  }
}
