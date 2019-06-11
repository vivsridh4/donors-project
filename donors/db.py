import configparser

def db_enabler():
    config = configparser.ConfigParser()
    config.read("config.ini")
    db_path = config['DATABASE']['db_path']
    
    return db_path