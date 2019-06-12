import configparser

def db_enabler():
    
    #Get database path provided by the user.
    
    config = configparser.ConfigParser()
    config.read("config.ini")
    db_path = config['DATABASE']['db_path']
    
    return db_path