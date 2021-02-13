import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { FontAwesomeIcon } from '@fortawesome/fontawesome-free';
import { library } from '@fortawesome/fontawesome-svg-core';
import '../../static/css/index.scss';
import RoundedButton from './roundedButton';
import SideNav from './Sidenav';

export default class App extends Component {
   Constructor(props){
       Super(props);
   }

   render(){
       return(
         <div>
         <div id="banner">
         <h1>Rise Management System</h1>
         <p></p>
         </div>
         <div id="grid">
         <SideNav />
         <RoundedButton message="click me"/>
         </div>
         </div>
       )
   }
}

ReactDOM.render(<App />, document.getElementById('app'));