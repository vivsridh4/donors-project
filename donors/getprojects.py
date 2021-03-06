import sqlite3,requests,configparser,logging,googlemaps
from prettytable import from_db_cursor
from donors.db import db_enabler

def getprojectdetails(getprojectszip):
    userid = getprojectszip
    
    logging.basicConfig(filename = 'app.log', level = logging.INFO)
    
    DB_PATH = db_enabler()
    
    conn = sqlite3.connect(DB_PATH)
    connect = conn.cursor()
    
    #Create a table if this is the first option used before creating database / tables.
        
    connect.execute('''CREATE TABLE IF NOT EXISTS USERS
             (username text, email text, zipcode integer)''')

    conn.commit()
    
    #Get zipcode of the user from database from user id provided by the user for --getprojects option.
    
    try:
        connect.execute('SELECT zipcode FROM USERS WHERE rowid=?', (userid,))
        get_zipcode = connect.fetchone()
        
    except TypeError as e:
        logging.exception(str(e))
        
    #List all users if user id doesn't match 
        
    if get_zipcode == None:
        print("Please choose a valid user id from below:",'\n')
        with conn:
            connect.execute('SELECT rowid as USERID,username as USERNAME,email as EMAIL,zipcode as ZIPCODE FROM USERS')   
            list_users = from_db_cursor(connect)   
        print(list_users)  
        
    #Connecting zipcode --> donors api --> get school details --> invoke google maps module to get place id using school details --> use place id to generate google maps url
    
    if get_zipcode != None:
        print("[Most Urgent] donors proposals near user",'\n')
        config = configparser.ConfigParser()
        config.read("config.ini")
        google_api_key = config['KEYS']['google_places_api_key']
        donors_api_key = config['KEYS']['donors_api_key']
    
        donors_api = "https://api.donorschoose.org/common/json_feed.html?zip=" + str(get_zipcode[0]) + "&" + "APIKey=" + donors_api_key
        
        request_donors_list = requests.get(donors_api)
        donors_json = request_donors_list.json()
        
        gmaps = googlemaps.Client(key=google_api_key)
        
        for field in donors_json["proposals"]:
            biglist=[]
            for key, value in field.items():
                if key=="schoolName":
                    biglist.append(value)
                if key=="city":
                    biglist.append(value)
                if key=="proposalURL":
                    biglist.append(value)
                else:
                    pass

            geocode_result = gmaps.geocode(biglist[1])
        
            print("#######",'\n')
            print("School Name:     ---",biglist[1])
            print("City:            ---",biglist[2])
            for distro in geocode_result:
                google_maps_integrated = "https://maps.googleapis.com/maps/api/place/details/json?placeid=" + distro['place_id'] + "&key=" + google_api_key
                
                get_google_maps = requests.get(google_maps_integrated)
                get_map_url = get_google_maps.json()
                
                print("Google Maps URL: ---",get_map_url['result']['url'])
                print("lat:             ---",get_map_url['result']['geometry']['location']['lat'])
                print("lng:             ---",get_map_url['result']['geometry']['location']['lng'])
            print("Proposal URL:    ---",biglist[0],'\n')
               
    
    conn.close()