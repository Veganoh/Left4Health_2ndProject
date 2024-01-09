import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DiagnosisService {

  private apiUrl = '';


  constructor(private http: HttpClient) { }


  public obtain_triage(jsonData: any): Observable<any> {
    return this.http.post(this.apiUrl, jsonData);
  }
}
