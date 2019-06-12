"""donors.users_ops: user operations module to create users or list users within the donors project package."""
import sqlite3,logging

from validate_email import validate_email
from prettytable import from_db_cursor
from donors.db import db_enabler

def users_ops(options):
    
    DB_PATH = db_enabler()
    
    conn = sqlite3.connect(DB_PATH)
    connect = conn.cursor()

    #Check table exist before creating a table to register a user.
    
    connect.execute('''CREATE TABLE IF NOT EXISTS USERS
             (username text, email text, zipcode integer)''')

    conn.commit()
    
    user_option = options
    
    if user_option=="create":
        
        fullname = input('Please enter your full mame: ')
        email = input('Please provide a valid email:')
        
        #Validate email id using validate_email module. We can also use py3DNS to check DNS availability.
        
        is_email_valid = validate_email(email)
        zipcode = input('Please provide a valid zip code to search a project near user:')
        
        #Check whether zipcode is a integer
        
        is_zipcode_valid=zipcode.isdigit()
        
        #If email is invalid don't proceed & if zipcode is invalid don't proceed.
        
        if is_email_valid == False:
            print("Please provide a valid email address")
        elif is_zipcode_valid == False:
            print("Please provide a valid zip code")
        else:
            connect.execute("INSERT INTO USERS VALUES(?, ?, ?)", (fullname,email,zipcode))
            conn.commit()
            print(f'Registering {fullname} as a Donor...')
        
    conn.close()
    
    if user_option=="list":
        
        DB_PATH = db_enabler()
        
        conn = sqlite3.connect(DB_PATH)
        connect = conn.cursor()
        
        connect.execute('''CREATE TABLE IF NOT EXISTS USERS
             (username text, email text, zipcode integer)''')

        conn.commit()
        
        #Using prettytable module to list users from database
        
        with conn:
            connect.execute('SELECT rowid as USERID,username as USERNAME,email as EMAIL,zipcode as ZIPCODE FROM USERS')   
            list_users = from_db_cursor(connect)   
        print(list_users)  
        
        conn.close()
    
