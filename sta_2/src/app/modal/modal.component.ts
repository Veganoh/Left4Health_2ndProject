import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Modal } from 'bootstrap';
import { BehaviorSubject } from 'rxjs';
import { Router } from '@angular/router';



@Component({
  selector: 'app-modal',
  templateUrl: './modal.component.html',
  styleUrls: ['./modal.component.css']
})

//Todo: api call in transfer  to service
export class ModalComponent {

  @Input() isShown: BehaviorSubject<boolean> = new BehaviorSubject(false);
  @Input() title: string = '';
  @Input() triage: number = 0;
  @Output() onSubmit = new EventEmitter<void>();

  constructor(private router: Router) { }

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

  close() {
    this.isShown.next(false);
    document.body.style.overflow = 'visible';
  }

  submit() {
    this.onSubmit.emit();
    this.isShown.next(false);
    this.router.navigate(['/suggestions']);
  }
}