import { Component, OnInit } from '@angular/core';
import { HospitalService } from '../services/hospital.service';
import { Router } from '@angular/router';
import { AnonymousSubject } from 'rxjs/internal/Subject';

@Component({
  selector: 'app-suggestions',
  templateUrl: './suggestions.component.html',
  styleUrls: ['./suggestions.component.css']
})
export class SuggestionsComponent implements OnInit {

  suggestedHospitals: any[] = []; 

  opcColor: any;


  opc: any;

  local: any;

  opcTransporte: any;
   
  textoresposta: any;
  click: any;


  constructor(private hospitalService: HospitalService,private router: Router) { }


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

  atualizarlocal(event: Event): void {
    const valorSelecionado = (event.target as HTMLSelectElement).value;
    this.local = valorSelecionado;
    console.log('Opção selecionada:', valorSelecionado);
  }

  selecionarOpcaoColor(event: Event): void {
    const valorSelecionado = (event.target as HTMLSelectElement).value;
    this.opcColor = valorSelecionado;
    console.log('Opção selecionada:', valorSelecionado);
  }
  selecionarOpcaoTransporte(event: Event): void {
    const valorSelecionado = (event.target as HTMLSelectElement).value;
    this.opcTransporte = valorSelecionado;
    console.log('Opção selecionada:', valorSelecionado);
  }

  selecionarOpcao(event: Event, value: any): void {
    if(value == '0.5,0.5'){
     this.opc = '0.5,0.5';
    }else {
     this.opc == '0.75,0.25'; 
    }
    console.log('Opção selecionada:', this.opc);
  }

 
  getHospitais(): any {
    this.textoresposta = this.hospitalService.getChoises();
    return this.textoresposta.best_alternatives
      ? Object.values(this.textoresposta.best_alternatives)
      : [];
  }

  submeterRespostas(): void {

    const respostas: any = {
      origin: this.local,
      color: this.opcColor,
      weights: this.opc,
      transport: this.opcTransporte,
    };


  
    this.hospitalService.postHospitals(respostas);
    this.click = true;
    if(this.click){
      this.getHospitais();
    }
   }

}