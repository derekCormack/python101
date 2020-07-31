import React from 'react';
import Products from './products'
import './App.css';
import functions from './fetch'
import Customers from './customers'

const hardcode = {1: {'name': 'jack ', 'address': 2355, 'email': 'jack@bbb.com'}, 2: {'name': 'bob', 'address': 245, 'email': 'bob@tbs.com'}, 3: {'name': 'steve', 'address': 2566, 'email': 'steve@kdkd.com'}, 4: {'name': 'derek', 'address': 2456, 'email': 'derek@googs.com'}, 5: {'name': 'sean', 'address': 233, 'email': 'sean@fronk.ca'}, 6: {'name': 'randy', 'address': 2541, 'email': 'randy@glipper.uk'}, 7: {'name': 'phil', 'address': 12, 'email': 'phil@mcracken'}, 8: {'name': 'david', 'address': 2564, 'email': 'david@uptown.com'}, 9: {'name': 'mathew', 'address': 84562, 'email': 'mathew@sphlipf.com'}, 10: {'name': 'gronk', 'address': 6542, 'email': 'gronk@nsoup.uk'}, 11: {'name': 'flipper', 'address': 78452, 'email': 'flipper@fronkie.ca'}, 12: {'name': 'glutenhiemer', 'address': 521, 'email': 'gutenhiemer@bbq.com'}, 13: {'name': 'sizzlechest', 'address': 123, 'email': 'sizzlechest@frappo.nz'}, 14: {'name': 'srchronkinblitz', 'address': 654, 'email': 'srchronkinblitz@pancakemuch.com'}, 15: {'name': 'jon frappoboink', 'address': 85, 'email': 'frappo@sneezesnort.ca'}}
const url = 'http://localhost:5000/';
let customerdata ={1: {'product_name': 'gizmoschlonker', 'wieght': 1, 'name':"name not loaded"}}
let productdata={"1":{"price":"not loaded yet","product_name":"not loaded yet","wieght":"not loaded yet"}}
class App extends React.Component {

  constructor() {
      super();
      // this.community = new func.community()
      this.state = {
          counter: 0
      }
  }
    async componentDidMount() {
      customerdata={}
      customerdata = await functions.postData(url + 'json/customer');
      productdata={}
      productdata = await functions.postData(url + 'json/product');
      // this.community.fromserver(data);
      this.setState({ counter: 0 })
    }

  

render() {
  const customerArray =[];
  let keyCounter = 0;
  for(const row in customerdata) {
    keyCounter+=1;
    customerArray.push(<Customers 
      key={keyCounter}
      data = {row}
      
      />)
}; 


  return (
    <div className="App">
      <header className="App-header">
        <h1>
          Getting information from our invoice spreadsheet.
        </h1>
        <p>
          Table of customer information. <br/>
          {customerArray}
        </p>
        <Customers
          data={hardcode}
        />
        <Customers
          data={customerdata}
        />
        <Products
          data={productdata}
        />
      </header>
    </div>
  );
};
}
 



export default App;
