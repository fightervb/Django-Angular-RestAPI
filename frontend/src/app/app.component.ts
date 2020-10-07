import { Component ,Input} from '@angular/core';
import {HttpClient } from '@angular/common/http';
import {Observable} from 'rxjs';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'client';
 data:Observable<any>;
  constructor(private http:HttpClient){}
  url="http://localhost:8000/v1/projects/"

  display:Observable<any>;


  getData()
  {


    this.data =this.http.get(this.url);


  }
  postData(val)
  {
    this.http.post(this.url,{
    "name":val
  }).toPromise().then((data:any)=>{})

  }
}
