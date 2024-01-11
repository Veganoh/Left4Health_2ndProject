export class Hospital {
    id: number;
    name: string;
    address: string;
    latitude: number;
    longitude: number;
    wait_time: number;
    duration: number;
  
    constructor(data: any) {
      this.id = data.id;
      this.name = data.name;
      this.address = data.address;
      this.latitude = data.latitude;
      this.longitude = data.longitude;
      this.wait_time = data.wait_time;
      this.duration = data.duration;
    }
  }
  