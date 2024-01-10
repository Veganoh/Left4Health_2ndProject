import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Modal } from 'bootstrap';
import { BehaviorSubject } from 'rxjs';
import { Router } from '@angular/router';
import { Hospital } from '../domain/hospital';

@Component({
  selector: 'app-modal-suggestions',
  templateUrl: './modal-suggestions.component.html',
  styleUrls: ['./modal-suggestions.component.css']
})
export class ModalSuggestionsComponent {

  constructor(private router: Router) { }

  @Input() isShown: BehaviorSubject<boolean> = new BehaviorSubject(false);
  @Input() hospitals: Hospital[] = [];
  @Output() onSubmit = new EventEmitter<void>();

  currentHospitalIndex: number = 0;



  ngOnInit() {
    this.isShown.subscribe(
      {
        next: (b) => {
          const element = document.getElementById('myModal') as HTMLElement;
          const myModal = new Modal(element);

          if (b) {
            myModal.show();
            document.body.style.overflow = 'hidden';
          } else {
            element.classList.remove('show');
            element.style.display = 'none';
            document.body.style.overflow = '';
            const bd = document.getElementsByClassName('modal-backdrop')[0] as HTMLElement;
            bd?.remove();
            const body = document.getElementsByTagName('body');
            if (body[0].classList.contains('modal-open')) body[0].classList.remove('modal-open');
            myModal.hide();
          }
        }
      }
    )
  }
  
  showPreviousHospital() {
    if (this.currentHospitalIndex > 0) {
      this.currentHospitalIndex--;
    }
  }

  showNextHospital() {
    if (this.currentHospitalIndex < this.hospitals.length - 1) {
      this.currentHospitalIndex++;
    }
  }

  convertSecondsToTime(seconds: number): string {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const remainingSeconds = seconds % 60;
  
    return `${this.padZero(hours)}:${this.padZero(minutes)}:${this.padZero(remainingSeconds)}`;
  }
  
  padZero(value: number): string {
    return value < 10 ? `0${value}` : `${value}`;
  }

  close() {
    this.isShown.next(false);
    document.body.style.overflow = 'visible';
  }

  submit() {
    this.onSubmit.emit();
    this.isShown.next(false);
    this.router.navigate(['']);
  }


}
