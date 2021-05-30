import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class StatisticsService {
  public responseData;
  constructor(private http: HttpClient) { }
  validateFileExtension(name: string) {
    const ext = name.substring(name.lastIndexOf('.') + 1);
    if (ext.toLowerCase() === 'json' || ext.toLowerCase() === 'txt') {
      return true;
    }
    else {
      return false;
    }
  }
  properJson(jsonString: string): boolean {
    try{
      JSON.parse(jsonString);
    }
    catch (e) {
      return false;
    }
    return true;
  }
  uploadJson(json: string){
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json'
      })
    };
    return this.http.post<any>('http://127.0.0.1:5000/results', json, httpOptions);
  }
}
