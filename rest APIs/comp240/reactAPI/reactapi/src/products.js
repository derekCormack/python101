import React from 'react';


function Customers(props) {
return (
    <p>
        Hello from products 
        {props.data[1].product_name}
        {props.data[1].wieght}
        {props.data[1].price}
    </p>
);
}

export default Customers;