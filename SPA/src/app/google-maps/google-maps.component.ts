import { Component, Input, OnInit  } from '@angular/core';
import { environment } from 'src/environments/environment';


@Component({
  selector: 'app-google-maps',
  templateUrl: './google-maps.component.html',
  styleUrls: ['./google-maps.component.css']
})
export class GoogleMapsComponent implements OnInit{
  @Input() latitude!: number;
  @Input() longitude!: number;
  googleMapsApiKey: string = '';


  ngOnInit(): void {
    this.googleMapsApiKey = environment.googleMapsApiKey;
  }
}
