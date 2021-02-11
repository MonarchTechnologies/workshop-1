import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import '../../static/css/index.scss';
import mui from '@material-ui/core';
import icons from '@material-ui/icons';
import roundedButton from './rounded-button';

export default class App extends Component {
   contstructor(props){
       Super(props);
   }

   render(){
       return(
         <div>
         <h1>Hello, Fullstack World</h1>
         <p>how are you?</p>
         <roundedButton message="click me" />
         </div>
       )
   }
}

ReactDOM.render(<App />, document.getElementById('app'));