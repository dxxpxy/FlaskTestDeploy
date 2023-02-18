from flask import Flask, Blueprint, render_template, request, flash, redirect
import sqlite3
from datetime import datetime
import db_func

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def home():
    return render_template("home.html")


@app.route('/addinvoice', methods = ['GET', 'POST'])
def addinvoice(): 
         
    if request.method == 'POST':
        
        customername = request.form.get('customername')
        customeraddress = request.form.get('customeraddress')
        date = request.form.get('date')       
        description = request.form.get('desp')
        invoiceno = request.form.get('invoiceno')
        invoicetotal = request.form.get('invoicetotal')
         
        error = db_func.validate_invoice_form(customername, customeraddress, date, description, invoiceno, invoicetotal)
        if error is not None:
            flash(error, category='redlight')
        else:
            date_obj = datetime.strptime(date, '%Y-%m-%d')  # Convert the string to a datetime object
            date_formatted = date_obj.strftime('%d/%m/%y')  # Convert the datetime object to a formatted string         
            db_func.check_db_exist()
            db_func.execute_sql('INSERT INTO invoice (customername, customeraddress, date, description, invoiceno, invoicetotal) VALUES (?, ?, ?, ?, ?, ?)', customername, customeraddress, date_formatted, description, invoiceno, invoicetotal)
            flash('Invoice added!', category='greenlight')
          
    return render_template("Form.html")


@app.route('/viewinvoice')
def viewinvoice():
    
    invoices = db_func.run_query('SELECT * FROM invoice')
    return render_template("invoice.html", invoices=invoices)        # Pass data to HTML template for display
          
          
@app.route('/editinvoice/<int:invoice_id>', methods=['GET', 'POST'])
def editinvoice(invoice_id):
    # Connect to database and retrieve invoice data
    connection = sqlite3.connect('invoices.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM invoice WHERE id = ?', (invoice_id,))
    invoice = cursor.fetchone()
    connection.close()

    if request.method == 'POST':
        # Retrieve new invoice total from form data
        new_invoicetotal = request.form['invoicetotal']
        db_func.execute_sql('UPDATE invoice SET invoicetotal = ? WHERE id = ?', new_invoicetotal, invoice_id)
        flash('Invoice updated!', category='greenlight')
        return redirect('/viewinvoice')

    # Render edit form with invoice data
    return render_template('editinvoice.html', invoice=invoice)
   
@app.route('/deleteinvoice/<int:invoice_id>', methods=['POST'])
def deleteinvoice(invoice_id):
    # Connect to database and delete invoice record
    db_func.execute_sql('DELETE FROM invoice WHERE id = ?', invoice_id,)
    flash('Invoice deleted!', category='greenlight')
    return redirect('/viewinvoice')   
 
if __name__ == '__main__':
    app.secret_key = 'asdasdasd'
    app.run(debug=True)
