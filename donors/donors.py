"""donors.donors: provides entry point main()."""

import sys,click
from donors.users_ops import users_ops
from donors.getprojects import getprojectdetails
from donors.config_file_handler import config_check


@click.command()
@click.option("--user","-u",help='donors cli project users operations: Create Users or List Users',type=click.Choice(['create', 'list']))
@click.option("--getprojects","-gp",help='list all projects near user. Need valid USER ID as an argument which can be obtained by - donors --user list',type=int)


def main(user,getprojects):
    if user:
        
        #Verify if config file has been updated with keys.
        
        is_config = config_check()
        if is_config:
            users_ops(user)
        else:
            print("Please add valid keys in config.ini")
            #print("pycon India is awesome")
    if getprojects:
        
        #Verify if config file has been updated with keys.
        
        is_config = config_check()
        if is_config:
            getprojectdetails(getprojects)
        else:
            print("Please add valid keys in config.ini")
    
 
