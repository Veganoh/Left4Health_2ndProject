import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { GoogleMapsModule } from '@angular/google-maps';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SuggestionsComponent } from './suggestions/suggestions.component';
import { HomeComponent } from './home/home.component';
import { GoogleMapsComponent } from './google-maps/google-maps.component';
import { DiagnosisComponent } from './diagnosis/diagnosis.component';
import { ModalComponent } from './modal/modal.component'; // Renomeado para DiagnosisComponent

@NgModule({
  declarations: [
    AppComponent,
    SuggestionsComponent,
    HomeComponent,
    GoogleMapsComponent,
    DiagnosisComponent,
    ModalComponent // Adicionado o DiagnosisComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    GoogleMapsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
