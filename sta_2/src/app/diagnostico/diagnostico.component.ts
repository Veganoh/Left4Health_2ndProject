import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AnonymousSubject } from 'rxjs/internal/Subject';

interface RespostasModel {
  [key: string]: { valor: number | null; observacoes: string };
}



@Component({
  selector: 'app-diagnostico',
  templateUrl: './diagnostico.component.html',
  styleUrls: ['./diagnostico.component.css']
})
export class DiagnosticoComponent {
  respostas: RespostasModel = {
    questao1: { valor: null, observacoes: '' },
    questao2: { valor: null, observacoes: '' },
    questao3: { valor: null, observacoes: '' },
    questao4: { valor: null, observacoes: '' },
    questao5: { valor: null, observacoes: '' },
    questao6: { valor: null, observacoes: '' },
    questao7: { valor: null, observacoes: '' },
  };

  idade: any;
  sexo: any;

  resposta3 = {
    key: {
      valor: '',
      observacoes: ''
    }
  };

  opcFerido: any;
  obsFerido: any;

  opcSexo: any;


  opcEstadoMental: any;
  obsEstadoMental: any;

  
  opcDores: any;
  obsDores: any;

  opcNivelDores: any;
  obsNivelDores: any;

  opcBtCard: any;
  obsBtCard: any;

  opcTaxaResp: any;
  obsTaxaResp: any;

  opcTemp:any;
  obsTemp: any;

  opcSat: any;
  obsSat: any;

  opcArt: any;
  obsArt: any;

  opcIdade: any;

  resposta1: any = {questao2: { valor: null, observacoes: '' }};
  resposta2: any = {questao2: { valor: null, observacoes: '' }};
  resposta4: any = {questao4: { valor: null, observacoes: '' }};
  resposta5: any = {questao5: { valor: null, observacoes: '' }};
  resposta6: any = {questao6: { valor: null, observacoes: '' }};
  resposta7: any = {questao7: { valor: null, observacoes: '' }};
  resposta8: any = {questao8: { valor: null, observacoes: '' }};
  resposta9: any = {questao9: { valor: null, observacoes: '' }};
  resposta10: any = {questao10: { valor: null, observacoes: '' }};
  resposta11: any = {questao111: { valor: null, observacoes: '' }};



  //construir modelo do this.respostas com todas as respostas,
  //vamos fazer uma a uma e logo apos isso inserimos no objeto de objetos
  



  constructor(private router: Router) {}

  opcaoSelecionada: string = ''; 

  selecionarOpcaoFerido(event: Event): void {
    const valorSelecionado = (event.target as HTMLSelectElement).value;
    this.opcFerido = valorSelecionado;
    console.log('Opção selecionada:', valorSelecionado);
  }
  atualizarObservacoesFerido(event: Event): void {
    const novaObservacao = (event.target as HTMLTextAreaElement).value;
    this.obsFerido = novaObservacao;
    console.log(novaObservacao);
  }

  selecionarOpcaoSexo(event: Event, value: any): void {
    if(value == '1'){
     this.opcSexo = '1';
    }else {
     this.opcSexo == '0'; 
    }
    console.log('Opção selecionada:', this.opcSexo);
  }

  selecionarOpcaoEstadoMental(event: Event): void {
    const valorSelecionado = (event.target as HTMLSelectElement).value;
    this.opcEstadoMental = valorSelecionado;
    console.log('Opção selecionada:', valorSelecionado);
  }
  atualizarObservacoesEstadoMental(event: Event): void {
    const novaObservacao = (event.target as HTMLTextAreaElement).value;
    this.obsEstadoMental = novaObservacao;
    console.log(novaObservacao);
  }


  selecionarOpcaoDores(event: Event): void {
    const valorSelecionado = (event.target as HTMLSelectElement).value;
    this.opcDores = valorSelecionado;
    console.log('Opção selecionada:', valorSelecionado);
  }
  atualizarObservacoesDores(event: Event): void {
    const novaObservacao = (event.target as HTMLTextAreaElement).value;
    this.obsDores = novaObservacao;
    console.log(novaObservacao);
  }

  selecionarOpcaoNivelDores(event: Event): void {
    const valorSelecionado = (event.target as HTMLSelectElement).value;
    this.opcNivelDores = valorSelecionado;
    console.log('Opção selecionada:', valorSelecionado);
  }
  atualizarObservacoesNivelDores(event: Event): void {
    const novaObservacao = (event.target as HTMLTextAreaElement).value;
    this.obsNivelDores = novaObservacao;
    console.log(novaObservacao);
  }

  selecionarOpcaoBtCard(event: Event): void {
    const valorSelecionado = (event.target as HTMLSelectElement).value;
    this.opcBtCard = valorSelecionado;
    console.log('Opção selecionada:', valorSelecionado);
  }
  atualizarObservacoesBtCard(event: Event): void {
    const novaObservacao = (event.target as HTMLTextAreaElement).value;
    this.obsBtCard = novaObservacao;
    console.log(novaObservacao);
  }

  selecionarOpcaoTaxaResp(event: Event): void {
    const valorSelecionado = (event.target as HTMLSelectElement).value;
    this.opcTaxaResp = valorSelecionado;
    console.log('Opção selecionada:', valorSelecionado);
  }
  atualizarObservacoesTaxaResp(event: Event): void {
    const novaObservacao = (event.target as HTMLTextAreaElement).value;
    this.obsTaxaResp = novaObservacao;
    console.log(novaObservacao);
  }

  selecionarOpcaoTemp(event: Event): void {
    const valorSelecionado = (event.target as HTMLSelectElement).value;
    this.opcTemp = valorSelecionado;
    console.log('Opção selecionada:', valorSelecionado);
  }
  atualizarObservacoesTemp(event: Event): void {
    const novaObservacao = (event.target as HTMLTextAreaElement).value;
    this.obsTemp = novaObservacao;
    console.log(novaObservacao);
  }

  selecionarOpcaoSat(event: Event): void {
    const valorSelecionado = (event.target as HTMLSelectElement).value;
    this.opcSat = valorSelecionado;
    console.log('Opção selecionada:', valorSelecionado);
  }
  atualizarObservacoesSat(event: Event): void {
    const novaObservacao = (event.target as HTMLTextAreaElement).value;
    this.obsSat = novaObservacao;
    console.log(novaObservacao);
  }

  selecionarOpcaoArt(event: Event): void {
    const valorSelecionado = (event.target as HTMLSelectElement).value;
    this.opcArt = valorSelecionado;
    console.log('Opção selecionada:', valorSelecionado);
  }
  atualizarObservacoesArt(event: Event): void {
    const novaObservacao = (event.target as HTMLTextAreaElement).value;
    this.obsArt = novaObservacao;
    console.log(novaObservacao);
  }

  atualizarIdade(event: Event): void {
    const valorSelecionado = (event.target as HTMLSelectElement).value;
    this.opcIdade = valorSelecionado;
    console.log('Opção selecionada:', valorSelecionado);
  }
  
  submeterRespostas(): void {
   const respostas: any = {
      questao1: { valor: this.opcFerido || null, observacoes: this.obsFerido || null },
      questao2: { valor: this.opcSexo, observacoes: null },
      questao3: { valor: this.opcEstadoMental || null, observacoes: this.obsEstadoMental || null },
      questao4: { valor: this.opcDores, observacoes: this.obsDores },
      questao5: { valor: this.obsNivelDores || null, observacoes: this.obsNivelDores || null },
      questao6: { valor: this.opcBtCard || null, observacoes: this.obsBtCard || null },
      questao7: { valor: this.opcTaxaResp || null, observacoes: this.obsTaxaResp || null },
      questao8: { valor: this.opcTemp || null, observacoes: this.obsTemp || null },
      questao9: { valor: this.opcSat || null, observacoes: this.obsSat || null },
      questao10: { valor: this.opcArt || null, observacoes: this.obsArt || null },
      questao11: { valor: null || null, observacoes: this.opcIdade || null },
    };
    this.router.navigate(['/suggestions'], { state: { respostas: respostas } });
  }
}







