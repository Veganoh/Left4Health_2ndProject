import { Component, OnInit } from '@angular/core';
import { HospitalService } from '../services/hospital.service';

@Component({
  selector: 'app-suggestions',
  templateUrl: './suggestions.component.html',
  styleUrls: ['./suggestions.component.css']
})
export class SuggestionsComponent implements OnInit {

  suggestedHospitals: any[] = []; 

  constructor(private hospitalService: HospitalService) { }

  ngOnInit(): void {
    this.getHospitals();
  }

  getHospitals(): void {
    this.hospitalService.getHospitals()
      .subscribe((data: any[]) => {
        this.suggestedHospitals = data; 
        console.log(this.suggestedHospitals);
      });
  }
}