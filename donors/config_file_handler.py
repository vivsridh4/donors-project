import configparser

def config_check():
    
    #Validate user has provided api key with valid details (check for empty string & integers)
    
    config = configparser.ConfigParser()
    config.read("config.ini")
    google_api_key = config['KEYS']['google_places_api_key']
    donors_api_key = config['KEYS']['donors_api_key']
    
    is_config_valid = False
    
    is_digit_check=google_api_key.isdigit()
    is_digit_check_donors_key = donors_api_key.isdigit()

    if is_digit_check:
        print("Not a valid google api key")
    elif is_digit_check_donors_key:
        print("Not a valid donors api key")
    elif google_api_key =="":
       print("Please provide a valid google api key")
    elif donors_api_key =="":
        print("Please provide a valid donors api key")
    else:
        is_config_valid = True
    
    return is_config_valid