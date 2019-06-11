"""donors.users_ops: user operations module to create users or list users within the donors project package."""
import sqlite3,logging

from validate_email import validate_email
from prettytable import from_db_cursor

def users_ops(options):
    
    conn = sqlite3.connect('donorsproject.db')
    connect = conn.cursor()

    connect.execute('''CREATE TABLE IF NOT EXISTS USERS
             (username text, email text, zipcode integer)''')

    conn.commit()
    
    user_option = options
    
    if user_option=="create":
        
        fullname = input('Please enter your full mame: ')
        email = input('Please provide a valid email:')
        is_email_valid = validate_email(email)
        zipcode = input('Please provide a valid zip code to search a project near user:')
        
        is_zipcode_valid=zipcode.isdigit()
        
        if is_email_valid == False:
            print("Please provide a valid email address")
        elif is_zipcode_valid == False:
            print("Please provide a valid zip code")
        else:
            connect.execute("INSERT INTO USERS VALUES(?, ?, ?)", (fullname,email,zipcode))
            conn.commit()
            print("Saving user details to a databases......")
        
    conn.close()
    
    if user_option=="list":
        
        conn = sqlite3.connect('donorsproject.db')
        connect = conn.cursor()
        
        connect.execute('''CREATE TABLE IF NOT EXISTS USERS
             (username text, email text, zipcode integer)''')

        conn.commit()
        
        with conn:
            connect.execute('SELECT rowid as USERID,username as USERNAME,email as EMAIL,zipcode as ZIPCODE FROM USERS')   
            list_users = from_db_cursor(connect)   
        print(list_users)  
        
        conn.close()
    
