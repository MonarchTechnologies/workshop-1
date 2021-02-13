import React, { Component } from 'react';
import '../../static/css/index.scss';

export default class RoundedButton extends Component{
   Constructor(props){
       Super(props);
   }
   render(){
       return <button id="button-rounded-one">{this.props.message}</button>
   }
}
