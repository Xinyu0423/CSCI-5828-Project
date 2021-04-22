import Link from 'next/link';
import Image from 'next/image'
import {Nav, PageBody} from "./styles"  //yarn add react react-dom next @emotion/core @emotion/styled
import React, {Button} from "react"
import fetch from 'node-fetch'
import { useRouter } from 'next/router';
import axios from 'axios';

import Search from './search'


export default class Header extends React.Component {

  constructor(props){
     super(props)
     this.state = {
       query : '',
       data : null,
       searchDone : false,
       found : false,
     }
  }


  //get data to send
  getData = (event) => {
    this.setState({
      query : event.target.value
    })
  }

  submit = () =>{
    if(this.state.query.length <= 0 ){
      alert('you must have text before searching')
    }
    console.log('send');
    this.apiCall()
  }

  apiCall = async() => {

    this.setState({
      searchDone:false,
      found: false
    })

    const proxyurl = "https://cors-anywhere.herokuapp.com/";
    axios.get(proxyurl + 'https://csci5828api.herokuapp.com/api/product')
    .then((response) => {
        for(var i = 0; i < response.data.length; i++){
          if(response.data[i].pid.toString() === this.state.query || response.data[i].name === this.state.query){
              this.setState({
                data : response.data[i],
                query:'',
                searchDone:true,
                found:true,
              })
          }
        }

        if(this.state.data ===  null ){
          this.setState({
            data : 'Search found nothing',
            searchDone:true,
            found: false
          })
        }
  
    });

    

   
  
  }

  render(){
    return (
        <React.Fragment>
          <Nav>
              <Link href="/about">
                  <Image
                      src="/QXAAD_title.png"
                      alt="Website name"
                      width={300}
                      height={100}
              />
              </Link>
              <Link href='/product'>
                  <a>Products</a>
              </Link>
              <Link href='/order'>
                  <a>Orders</a>
              </Link>
              {/* <Link href='/user'>
                  <a>User</a>
              </Link> */}
              <Link href='/about'>
                  <a>About the project</a>
                </Link>
                <Link href='/trends'>
                  <a>Github trending repos</a>
                </Link>
          </Nav>
          <PageBody>{this.props.children}</PageBody>
          <div>
            <div><h1>Search Products</h1></div>
            <input type="text" placeholder='products to search' onChange={this.getData}/>
            <button onClick={this.submit}>search</button>
            {
              this.state.searchDone? 
                this.state.found?
                <div>
                  <div><h1>id : {this.state.data.pid}</h1></div>
                  <div><h1>name: {this.state.data.name}</h1></div>
                  {/* <div><h1>price: ${this.state.data.price}</h1></div> */}
                  <div><h1>rating: {this.state.data.price}</h1></div> 
                </div>:
                  <div><h1> product not in our invetory </h1></div> :
                  null
            }
          </div>
          <style jsx>{`
          .container {
            margin: 50px;
          }
          p {
            color: blue;
          }
        `}</style>
          <style jsx global>{`
            p {
              font-size: 40px;
            }
          `}
          </style>
        </React.Fragment>
    )
  }
}


