import React from 'react';


function Customers(props) {
    console.log(props.data);
    return (
        <p>
          Hello from customer v3 !!
          
           {props.data.name}
           {props.data.address}
           {props.data.email}
        </p>
    );
}

export default Customers;