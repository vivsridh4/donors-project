"""donors.users_ops: user operations module to create users or list users within the donors project package."""
import sqlite3


from validate_email import validate_email
from prettytable import from_db_cursor

def users_ops(options):
    
    conn = sqlite3.connect('donorsproject.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS USERS
             (username text, email text, zipcode integer)''')

    conn.commit()
    
    user_option = options
    
    if user_option=="create":
        
        fullname = input('Please enter your Full Name: ')
        email = input('Please provide a valid Email:')
        zipcode = int(input('Please provide a valid Zip Code to search a project near user:'))
        
        is_valid = validate_email(email)
        
        if is_valid == True:
            c.execute("INSERT INTO USERS VALUES(?, ?, ?)", (fullname,email,zipcode))
            conn.commit()
            print("Saving user details to a databases......")
        else:
            print("Please provide a valid email address")
    
    conn.close()
    
    if user_option=="list":
        
        conn = sqlite3.connect('donorsproject.db')
        c = conn.cursor()
        
        c.execute('''CREATE TABLE IF NOT EXISTS USERS
             (username text, email text, zipcode integer)''')

        conn.commit()
        
        with conn:
            c.execute('SELECT rowid as userid,username,email,zipcode FROM USERS')   
            x = from_db_cursor(c)   
        print(x)  
        
        conn.close()
    
