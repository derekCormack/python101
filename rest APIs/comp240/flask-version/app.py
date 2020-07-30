# Create an API to send a JSON document to a React frontend (SPA)

import openpyxl
from openpyxl import load_workbook
from data_xl import customer_call, invoice_call,itemsold_call,product_call, loopdahdata_call
from flask import (Flask, render_template)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World v4!"

@app.route("/hello/<name>")
def hello2(name):
    return render_template("hello.html", name=name)

@app.route('/plain')
def plain():
    return render_template("index.html", data="Many many dinasouras.")

@app.route('/dump/customer')
def dumpcustomer():
     return render_template("dump.html", customer=customer_call())

@app.route('/dump/invoice')
def dumpinvoice():
       return render_template("dump.html", customer=invoice_call())

@app.route('/dump/itemsold')
def dumpitemsold():
       return render_template("dump.html", customer=itemsold_call())

@app.route('/dump/product')
def dumpproduct():
       return render_template("dump.html", customer=product_call())

@app.route('/loop')
def dumploop():
       return render_template("dump.html", customer=loopdahdata_call(product_call()))



# def invoice_printer():
#       date=invoices[x]['date']
#       invoiced_customer_id=invoices[x]['customer_id']
#       customer_name=customers[invoiced_customer_id]['name']
#       customer_email=customers[invoiced_customer_id]['email']
#       overall_price=0
#       print(CGREEN + f"Customer report for _{customer_name}_ regarding invoice #_{x}_ on {date} "+ CEND )
#       for y in itemsold: 
#             if (itemsold[y]['invoice_id'])==x:
#                   product_dict=itemsold[y]['product_id']
#                   product_name=productlist[product_dict]['product_name']
#                   price=productlist[product_dict]['price']
#                   # print(itemsold[y]['product_id'])
#                   sold=itemsold[y]['quantity_sold']
#                   total_price=round(sold*price,2)
#                   overall_price+=total_price
#                   print(f"Product:  {product_name} Quantity:  {sold} Price per unit:  ${price} Total Price:  ${total_price} ")
#       print(CRED + f"Total invoice pricing is: ${round(overall_price,2)}"+ CEND)


if __name__ == '__main__':
	print("--- Starting", __file__)
	app.run(debug=True, use_reloader=True)

    #if this is being executed then start flask, start in debug.