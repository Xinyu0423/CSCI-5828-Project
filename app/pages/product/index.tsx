import Link from 'next/link';
import fetch from 'node-fetch'
import Layout from '../../components/layouts';
import { useRouter } from 'next/router';

import fetch from 'node-fetch'
import Layout from '../../components/layouts';
import { useRouter } from 'next/router';

const PostLink = props => (
    <li>
      <Link href="./product/[pid]" as={`./product/${props.pid}`}>
        <a>{props.name}</a>
      </Link>
    </li>
  );


export default function Product({products_info}){
    const router=useRouter();
    
    return (
        
        <Layout>
        <h1>{router.query.title}</h1>
        <p>This is product page</p>
        <p>Product list: {products_info.map((product_info)=>(
            
            <li><PostLink pid={product_info.pid} name={product_info.name}/> </li>
        ))}</p>
        </Layout>
    
    );
};

export async function getServerSideProps(){
    const res= await fetch("https://csci5828api.herokuapp.com/api/product")
    const products_info= await res.json()
    //console.log(products_info)
    console.log(typeof(products_info))
    return {props:{products_info}}
}

//main/product/
