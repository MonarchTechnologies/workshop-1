import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import '../../static/css/index.scss';

export default class roundedButton extends Component{
   constructor(props){
       Super(props)
   }
   render(){
       return(
        <button id="button-rounded-one">{this.props.message}</button>
       )
   }
}
