import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  constructor(private router: Router) {}

  iniciarDiagnostico(): void {
    // Aqui você pode redirecionar para a página do diagnóstico
    this.router.navigate(['/diagnostico']); // Certifique-se de criar essa rota no próximo passo
  }
}
