import Header from './header';
import React from "react"
import {Nav, PageBody} from "./styles"

const layoutStyle = {
    margin : 20,
    padding : 20,
    border : '1px solid #DDD'

};

const Layout = props =>(
    <div style={layoutStyle}>
        <Header />
        {props.children}
    </div>

);



export default Layout