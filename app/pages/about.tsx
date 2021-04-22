import Link from 'next/link';

import Layout from '../components/layouts';



export default function About({repos}){
    //console.log(repos)
    return (
        <Layout>
        <div>
        <h1>About the Project </h1>
        
        <p>This is CSCI5828 Team Project, we are building a website for merchants to sell products. <br/>
        On this website, users would be able to search, <br/>
        view and purchase products, the merchant would be able to post products, <br/>
        accept orders, and monitor sales. The website would support user management, <br/>
        merchant management, product management and administration.<br/>
        For more information, please visit our 
        <Link href="https://github.com/Xinyu0423/CSCI-5828-Project">
            <a> Github</a>
            </Link>
        </p>
        </div>
        {/* <div>
            {repos.map(function(d,idx){
                return (<li key={idx}>{d.name}</li>)

            })}
        </div> */}
        </Layout>
    )
}


// const trending=require('trending-github');

// function get_trends(){
//   return trending().then(repos => {return repos}).catch(err=>console.log(err));
// }





// async function asyncget_trends() {
//   let result = await get_trends()
//  // console.log(result)
//   return result
// }


// export async function getServerSideProps(){
//     let result = await get_trends()
//     const repos= await result
//     //console.log(products_info)
    
//     return {props:{repos}}
// }
