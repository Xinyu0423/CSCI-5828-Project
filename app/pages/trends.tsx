import { ArrowUpwardSharp, ReportSharp } from '@material-ui/icons';
import Link from 'next/link';
import ReactStars from "react-rating-stars-component";
import Layout from '../components/layouts';

const PostLink = props => (
    <li>
     <Link href={props.href}>
       <a>{props.name}</a>
     </Link>
     &nbsp;&nbsp;&nbsp;&nbsp;
     {props.stars}
   </li>
  );


export default function topRepos({repos}){
    repos.sort(function(a,b){
        if(a.stars>b.stars) return -1;
        if(a.stars<b.stars) return 1;
        return 0
    })
    return(
        <Layout>
            <p>Github trending repos</p>
            <div>
            {repos.map(function(d,idx){
                return (<PostLink href={d.href} name={d.name} stars={d.stars} />)

            })}
        </div>



        </Layout>



    )


}


const trending=require('trending-github');

function get_trends(){
  return trending().then(repos => {return repos}).catch(err=>console.log(err));
}





async function asyncget_trends() {
  let result = await get_trends()
 // console.log(result)
  return result
}


export async function getServerSideProps(){
    let result = await get_trends()
    const repos= await result
    //console.log(products_info)
    
    return {props:{repos}}
}