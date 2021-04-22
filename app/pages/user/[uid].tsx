import { useRouter } from 'next/router';
import Layout from '../../components/layouts';
import Image from 'next/image'
import ReactStars from "react-rating-stars-component";
import React from "react";
import fetch from 'isomorphic-unfetch'



export default function User({user_info}){
    const router=useRouter();
    
    //http://apiserver/api/product
    return (
        <Layout>
            <h1>{router.query.id}</h1>
            <p>This is user info: {user_info}</p>
           
        </Layout>
    );
};

User.getInitialProps = async (ctx) => {
    const res = await fetch("https://csci5828api.herokuapp.com/api/login")
    const json = await res.json()
    return {product_info:json}
  }