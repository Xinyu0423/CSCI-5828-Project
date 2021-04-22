import Link from 'next/link';
import fetch from 'node-fetch'
import Layout from '../../components/layouts';
import { useRouter } from 'next/router';
 
 
const PostLink = props => (
    <li>
      <Link href="./order/[pid]" as={`./order/${props.oid}`}>
        <a>{props.pid}</a>
      </Link>
    </li>
  );



 export default function Order({orders_info}){
     const router=useRouter();
    return (
        <Layout>
        <h1>{router.query.title}</h1>
        <p>This is order page</p>
        <p>order list: {orders_info.map((order_info)=>(
            
            <li><PostLink pid={order_info.oid}/> </li>
        ))}</p>
        </Layout>
    )
}




export async function getServerSideProps(){
    const res= await fetch("https://csci5828api.herokuapp.com/api/order")
    const orders_info= await res.json()
    //console.log(products_info)
    return {props:{orders_info}}
}

// main/order