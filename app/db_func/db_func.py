import sqlite3

def get_db():
    connection = sqlite3.connect('Website1/invoices.db')
    return connection


def check_db_exist():
    connection = sqlite3.connect('Website1/invoices.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    if not cursor.fetchall():
        script = open('Website1/schema.sql').read()
        connection.executescript(script)
        connection.close()


def run_query(sql):
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    connection.close()
    return results


def execute_sql(sql, *args):
    connection = get_db()
    cur = connection.cursor()
    cur.execute(sql, args)
    connection.commit()
    connection.close()


def validate_invoice_form(customername, customeraddress, date, description, invoiceno, invoicetotal):
    if len(customername) < 2:
        return 'Enter customer name'
        
    if len(customeraddress) < 3:
        return 'Address can\'t be less then 3 characters'
    
    if date is None or date == '':
        return 'Please add a date.'
            
    if len(description) < 1:
        return 'Please add a description'
    
    if len(invoiceno) < 1:
        return 'Enter invoice number'     
       
    if len(invoicetotal) < 1:
        return 'Enter invoice total.'
               
    return None     

