import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http'; // Importe o HttpClientModule
import { GoogleMapsModule } from '@angular/google-maps';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SuggestionsComponent } from './suggestions/suggestions.component';
import { HomeComponent } from './home/home.component';
import { DiagnosticoComponent } from './diagnostico/diagnostico.component';
import { FormsModule } from '@angular/forms';
import { GoogleMapsComponent } from './google-maps/google-maps.component';
import { DiagnosisComponent } from './diagnosis/diagnosis.component';


@NgModule({
  declarations: [
    AppComponent,
    SuggestionsComponent,
    HomeComponent,
    DiagnosticoComponent,
    GoogleMapsComponent,
    DiagnosisComponent
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
export class DiagnosticoModule { }
