import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SuggestionsComponent } from './suggestions/suggestions.component';
import { HomeComponent } from './home/home.component';
import { DiagnosisComponent } from './diagnosis/diagnosis.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'suggestions', component: SuggestionsComponent },
  { path: 'diagnosis', component: DiagnosisComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
