import Link from 'next/link';
import Layout from '../components/layouts';
import React from "react"
import Async from 'react-promise'
import { resolve } from 'node:path';

const PostLink = props => (
    <li>
      <Link href="./product/[pid]" as={`./product/${props.pid}`}>
        <a>{props.pid}</a>
      </Link>
    </li>
  );


const PostLink = props => (
     <li>
      <Link href="./product/[pid]" as={`./product/${props.pid}`}>
        <a>{props.name}</a>
      </Link>
    </li>
   );


export default function Home({products_info}){

     products_info.sort(function(a,b){
      if(a.rating>b.rating) return -1;
        if(a.rating<b.rating) return 1;
        return 0

     }) //rank products based on ratings
    //console.log(trend_info)
    return(
      
        <Layout>
            <div>
            <p>top rating products:</p> 
            {products_info.map((product_info)=>(
            <PostLink pid={product_info.pid} name={product_info.name}/> 
        ))}
             
            </div>
           
            
        </Layout>
    );
}




 
  
export async function getServerSideProps(){
  const res= await fetch("https://csci5828api.herokuapp.com/api/product")
  const products_info= await res.json()
  //console.log(products_info)
  //console.log(typeof(products_info))
  return {props:{products_info}}
}

