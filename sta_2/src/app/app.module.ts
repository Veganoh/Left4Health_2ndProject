import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DiagnosisComponent } from './diagnosis/diagnosis.component';
import { SuggestionsComponent } from './suggestions/suggestions.component';

@NgModule({
  declarations: [
    AppComponent,
    DiagnosisComponent,
    SuggestionsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
