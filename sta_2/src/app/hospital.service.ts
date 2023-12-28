import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { mergeMap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class HospitalService {
  private apiUrl = 'https://tempos.min-saude.pt/api.php/institution';

  constructor(private http: HttpClient) { }

  getHospitals(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/hospitals`);
  }

  prioritizeHospitals(origin: string): Observable<any[]> {
    const backendUrl = 'http://localhost:5000';  
  
    return this.http.get<any[]>(`${backendUrl}/get_hospitals`);
  }

  private sortHospitalsByPriority(hospitals: any[]): any[] {
    return hospitals;
  }
}