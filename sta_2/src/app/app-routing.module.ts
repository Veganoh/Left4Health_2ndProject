import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DiagnosisComponent } from './diagnosis/diagnosis.component'; // Importe o componente Diagnosis

const routes: Routes = [
  { path: 'diagnosis', component: DiagnosisComponent }, // Defina a rota para o componente Diagnosis
  // ... outras rotas
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
