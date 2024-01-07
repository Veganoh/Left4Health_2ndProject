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
  postHospitals(informacao: any): Observable<any[]> {
    console.log(informacao)
    return this.http.post<any[]>(`${this.apiUrl}/best_alternativas`, {informacao});
  }

  getChoises(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/best_alternativas`);
  }
  prioritizeHospitals(origin: string): Observable<any[]> {
    const backendUrl = 'http://127.0.0.1:5000';  
  
    return this.http.get<any[]>(`${backendUrl}/get_hospitals`);
  }

  private sortHospitalsByPriority(hospitals: any[]): any[] {
    return hospitals;
  }
  
}