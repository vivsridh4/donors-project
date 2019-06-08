#get project details 

import sqlite3
import requests
import configparser
import logging
import googlemaps
#from prettytable import from_db_cursor

def getprojectdetails(getprojectszip):
    #print(f'printing row id {getprojectszip}')
    userid = getprojectszip
    #print(userid)
    
    logging.basicConfig(filename = 'app.log', level = logging.INFO)
    
    conn = sqlite3.connect('donorsproject.db')
    c = conn.cursor()
        
    c.execute('''CREATE TABLE IF NOT EXISTS USERS
             (username text, email text, zipcode integer)''')

    conn.commit()
    
    try:
        c.execute('SELECT zipcode FROM USERS WHERE rowid=?', (userid,))
        get_zipcode = c.fetchone()
        #print(type(get_zipcode))
        #print(get_zipcode)
        
    except TypeError as e:
        #print("Please provide a valid user id")
        logging.exception(str(e))
        
    if get_zipcode == None:
        print("Please provide a valid user id")

    if get_zipcode != None:
        print("Donors Proposals near user")
        config = configparser.ConfigParser()
        config.read("config.ini")
        google_api_key = config['KEYS']['google_places_api_key']
        donors_api_key = config['KEYS']['donors_api_key']
    #print(donors_api_key)
        donors_api = "https://api.donorschoose.org/common/json_feed.html?zip=" + str(get_zipcode[0]) + "&" + "APIKey=" + donors_api_key
        #print(donors_api)
        r = requests.get(donors_api)
        jforson = r.json()
        
        gmaps = googlemaps.Client(key=google_api_key)
        
        for d in jforson["proposals"]:
            biglist=[]
            for k, v in d.items():
                if k=="schoolName":
                    biglist.append(v)
                if k=="city":
                    biglist.append(v)
                if k=="proposalURL":
                    biglist.append(v)
                else:
                    pass

            geocode_result = gmaps.geocode(biglist[1])
            googlemaps_var="https://www.google.com/maps/search/?api=1&query=Google&query_place_id="
   
            print("#######",'\n')
            print("School Name:     ---",biglist[1])
            print("City:            ---",biglist[2])
            for distro in geocode_result:
                googlemaps_intgrated = googlemaps_var + distro['place_id']
                print("Google MAps URL: ---",googlemaps_intgrated)
                print("lat:             ---",distro['geometry']['location']['lat'])
                print("lng:             ---",distro['geometry']['location']['lng'])
            print("Proposal URL:    ---",biglist[0],'\n')
               
    
    conn.close()