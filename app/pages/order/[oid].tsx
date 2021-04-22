import { useRouter } from 'next/router';
import Layout from '../../components/layouts';
import Image from 'next/image'
import ReactStars from "react-rating-stars-component";
import React from "react";
import fetch from 'isomorphic-unfetch'




export default function Order({order_info}){
    const router=useRouter();
    
    //http://apiserver/api/product
    return (
        <Layout>
            <h1>{router.query.id}</h1>
            <p>Order info: {order_info}</p>
           
  

        </Layout>
    );
};



export async function getStaticPaths(){  //return an array of possible values for pid
    const res=await fetch("https://csci5828api.herokuapp.com/api/order") //will change in future
    const orders = await res.json()
    //console.log(`Show data fetched. Count: ${products}`);
    console.log(orders)
    const paths=orders.map((order)=>`/order/${order.oid}`)
     return {paths, fallback: false}
}

export async function getStaticProps({params}){//fetches necessary data for the product info w/ id
    const oid=params.oid
    const res = await fetch(`https://csci5828api.herokuapp.com/api/order/${oid}`)
    const order = await res.json()
    return {props:{order}}
}

// main/order/100