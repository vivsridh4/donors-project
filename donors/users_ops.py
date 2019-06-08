# -*- coding: utf-8 -*-
"""donors.users: user operations module to create users or list users within the donors project package."""
import sqlite3

#from donors.list_users import *
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
        zipcode = int(input('We need your Zip Code to connect you to projects near you:'))
        
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
            c.execute('SELECT rowid,username,email,zipcode FROM USERS')   
            x = from_db_cursor(c)   
        print(x)  
        
        conn.close()
        #list_users()
        #print("list users")
    
