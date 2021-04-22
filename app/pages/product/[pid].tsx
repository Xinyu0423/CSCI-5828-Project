import { useRouter } from 'next/router';
import Layout from '../../components/layouts';
import Image from 'next/image'
import ReactStars from "react-rating-stars-component";
import React from "react";
import fetch from 'isomorphic-unfetch'

const ratingChanged=(newRating)=>{
    console.log(newRating);
}




export default function Product({product}){
    const router=useRouter();
    
    //http://apiserver/api/product
    return (
        <Layout>
            <h1>{router.query.id}</h1>
            <p>Product name: {product.name} </p>
            <p>This is product info:  {product.intro}</p>
            <p>Product rating: </p>
            
            <ReactStars
                count={5}
                size={30}
                value={product.rating}  //{product.rating}
                edit={false}  //true==edit
                activeColor="#ffd700"
                onChange={ratingChanged}
                readOnly
            />
            <p>Product image:</p>
            <img src="https://source.unsplash.com/random/300×300" width="300" height="250"></img>
        </Layout>
    );
};



export async function getStaticPaths(){  //return an array of possible values for pid
    const res=await fetch("https://csci5828api.herokuapp.com/api/product")
    const products = await res.json()
    //console.log(`Show data fetched. Count: ${products}`);
    //console.log(products)
   // console.log(typeof(products))
    const paths=products.map((product)=>`/product/${product.pid}`)
     return {paths, fallback: false}
}

export async function getStaticProps({params}){//fetches necessary data for the product info w/ id
    const pid=params.pid
    const res = await fetch(`https://csci5828api.herokuapp.com/api/product/${pid}`)
    const product = await res.json()
    return {props:{product}}
}

  
//    Product.getInitialProps = async ({router}) => {
     
//      const res = await fetch(`https://csci5828dev.herokuapp.com/api/product`)
//      const json = await res.json()
//      const paths=json.map((product)=>`/product/${product.pid}`)
//      return {paths, fallback: false}
//    }
   //fallback : other route would be 404
  
