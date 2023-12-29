import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SuggestionsComponent } from './suggestions/suggestions.component';
import { HomeComponent } from './home/home.component';
import { DiagnosticoComponent } from './diagnostico/diagnostico.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'diagnostico', component: DiagnosticoComponent },
  { path: 'suggestions', component: SuggestionsComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
