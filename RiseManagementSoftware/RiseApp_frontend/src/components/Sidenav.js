import React, { Component } from 'react';
import '../../static/css/index.scss';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faHome, faFolder, faClipboardList, faCommentAlt, faSignOutAlt } from '@fortawesome/free-solid-svg-icons';

export default class SideNav extends Component{
    Constructor(props){
        Super(props);

    }

    render(){
        library.add(faHome, faFolder, faClipboardList, faCommentAlt, faSignOutAlt);
        return(
            <div id="nav">
            <ul id="nav.ul">
                <li><a href="#Dashboard"><FontAwesomeIcon icon="home"/>  Dashboard </a></li>
                <li><a href="#Projects"><FontAwesomeIcon icon="folder" />  Projects </a></li>
                <li><a href="#Schedule"><FontAwesomeIcon icon="clipboard-list" />  Schedule </a></li>
                <li><a href="#TeamChat"><FontAwesomeIcon icon="comment-alt" />  TeamChat </a></li>
                <li><a href="#Logout"><FontAwesomeIcon icon="sign-out-alt" />  Logout </a></li>
             </ul>
            </div>
        )
    }
}