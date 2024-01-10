import { Component, OnInit } from '@angular/core';
import { DiagnosisService } from '../services/diagnosis.service';
import { BehaviorSubject } from 'rxjs';


@Component({
  selector: 'app-diagnosis',
  templateUrl: './diagnosis.component.html',
  styleUrls: ['./diagnosis.component.css']
})
export class DiagnosisComponent implements OnInit {

  isModalShown: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false);


  showPainField: boolean = false;

  model: string = '1'
  sex: string = '';
  injured: string = '';
  hasPain: string = '';
  painLevel: string = '';
  age: string = '';
  heartRate: string = '';
  respiratoryRate: string = '';
  saturation: string = '';
  bloodPressure: string = '';
  mentalState: string = '';
  arrivalMode: string = '';
  symptoms: string = '';
  temperature: string = '';

  triage: number = 0;


  constructor(private diagnosisService : DiagnosisService) { }

  ngOnInit(): void {
  }

  updatePainField(hasPain: boolean): void {
    this.showPainField = hasPain;
  }


  onSubmit(): void {

    if (this.hasPain === "0") this.painLevel = "0";
    
    const formData = {
      model: this.model,
      sex: this.sex.toString(),
      age: this.age,
      injured: this.injured.toString(),
      pain: this.hasPain.toString(),
      nrs_pain: this.hasPain ? this.painLevel.toString() : '0',
      heart_rate: this.heartRate,
      respiratory_rate: this.respiratoryRate,
      blood_pressure: this.bloodPressure,
      saturation: this.saturation,
      mental_state: this.mentalState,
      arrival_mode: this.arrivalMode,
      symptom: this.symptoms,
      temperature: this.temperature,
    };

    this.diagnosisService.obtain_triage(formData).subscribe(
      (response) => {
        this.triage = response.triage;
      },
      (error) => {
        console.log(error);
      }
    );

    this.triage = 1;
    this.isModalShown.next(true);

    console.log(formData);
  };

  areAllFieldsFilled(): boolean {
    const basicFieldsFilled =
      this.age.trim() !== '' &&
      this.heartRate.trim() !== '' &&
      this.respiratoryRate.trim() !== '' &&
      this.saturation.trim() !== '' &&
      this.symptoms.trim() !== '' &&
      this.sex.trim() !== '' &&
      this.injured.trim() !== '' &&
      this.hasPain.trim() !== '' &&
      this.bloodPressure.trim() !== '' &&
      this.mentalState.trim() !== '' &&
      this.arrivalMode.trim() !== '' &&
      this.temperature.trim() !== '';

  
    return basicFieldsFilled;
  }

  changeModel(): void {
    if (this.model === '1') {
      this.model = '2';
    } else if (this.model === '2'){
      this.model = '3';
    } else this.model = '1';
  }
}
