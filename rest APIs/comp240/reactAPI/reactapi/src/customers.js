import React from 'react';


function Customers(props) {
    return (
        <p>
          Hello from customer !!
          
           {props.data[1].name}
        </p>
    );
}

export default Customers;