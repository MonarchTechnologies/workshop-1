import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

export default class App extends Component {
   contstructor(props){
       Super(props);
   }

   render(){
       return(
         <div>
         <h1>Hello, Fullstack World</h1>
         <p>how are you?</p>
         </div>
       )
   }
}

ReactDOM.render(<App />, document.getElementById('app'));