import { Component } from '@angular/core';
import { HospitalService } from '../services/hospital.service';
import { Hospital } from '../domain/hospital';
import { Router } from '@angular/router';

@Component({
  selector: 'app-suggestions',
  templateUrl: './suggestions.component.html',
  styleUrls: ['./suggestions.component.css']
})
export class SuggestionsComponent {

  local: string = '';
  transport: string = '';
  braceletColor: string = '';
  preference: string = '';
  bestAlternatives: Hospital[] = [];
  errorMessage: string = '';

  constructor(private hospitalService: HospitalService) {}

  convertSecondsToTime(seconds: number): string {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const remainingSeconds = seconds % 60;
  
    return `${this.padZero(hours)}:${this.padZero(minutes)}:${this.padZero(remainingSeconds)}`;
  }
  
  padZero(value: number): string {
    return value < 10 ? `0${value}` : `${value}`;
  }

  isFormDataValid(): boolean {
    return this.local && this.transport && this.braceletColor && this.preference ? true : false;
  }

  handleSuggestion() {
    if (!this.isFormDataValid()) {
      this.errorMessage = 'Por favor, preencha todos os campos antes de obter sugestões.';
      return;
    }

    let weights: string = "0.5,0.5";
  
    if (this.preference === 'shortest-wait-time') {
      weights = "0.75,0.25";
    } else if (this.preference === 'nearest-hospital') {
      weights = "0.25,0.75";
    }

    const jsonData = {
      origin: this.local,
      color: this.braceletColor,
      weights: weights,
      transport: this.transport
    };
  
    this.hospitalService.obtain_best_alternatives(jsonData).subscribe(
      (response) => {
        this.bestAlternatives = Object.values(response.best_alternatives).map(data => new Hospital(data));
        this.errorMessage = ''; // Limpa a mensagem de erro se a solicitação for bem-sucedida
      },
      (error) => {
        console.error('Erro ao obter melhores alternativas:', error);
        this.errorMessage = 'Erro ao obter melhores alternativas. Por favor, tente novamente mais tarde.';
      }
    );
  }
}
