import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  constructor(private router: Router) {}

  // Método para redirecionar para a página de sugestões
  goToSuggestions(): void {
    this.router.navigate(['/suggestions']);
  }
}