import { Component } from '@angular/core';
import { Router } from '@angular/router';

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

  constructor(private router: Router) {}

  selecionarResposta(questao: string, valor: number) {
    if (this.respostas[questao]) {
      this.respostas[questao].valor = valor;
    }
  }

  submeterRespostas(): void {
    this.router.navigate(['/suggestions'], { state: { respostas: this.respostas } });
  }
}







