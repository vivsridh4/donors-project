# -*- coding: utf-8 -*-


"""donors.donors: provides entry point main()."""

import sys
import click
from donors.users_ops import users_ops
from donors.getprojects import getprojectdetails


@click.command()
@click.option("--user","-u",help='donors cli project users operations: Create Users or List Users',type=click.Choice(['create', 'list']))
@click.option("--getprojects","-gp",help='list all projects based on user id(Row-ID from Table), get user id details from --user list',type=int)


def main(user,getprojects):
    if user:
        users_ops(user)
    if getprojects:
        getprojectdetails(getprojects)
    
    
 
