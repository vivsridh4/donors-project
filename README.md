# donors-project

<a href="https://docs.python.org/3/index.html"><img src="https://img.shields.io/badge/python-3.7-blue.svg"/></a>

Teachers and students all over the U.S. need your help to bring their classroom dreams to life. This repo aims to find projects near a user so that he can contribute and find projects via google maps.

## Get started: Install the CLI

### Prerequisites

Before continuing with this tutorial, make sure you are logged in as a user with sudo privileges.

**Install & use [Python 3.7+](https://www.python.org/) before using donors-project CLI application**

```bash
$ python --version
Python 3.7.3
```
**Installing pip for Python 3**

Start by updating the package list and install pip for Python 3 using the following command if using Linux:

```bash
$ sudo apt update
$ sudo apt install python3-pip
```
**Install setuptools module using pip3**

```bash
$ pip3 install setuptools
```
**NOTE:** You can install and use virtualenv with Python 3, follow this [link for detailed documentation.](https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3)You can reference python3 as python if you're using virtualenv to install this app.

### Donors CLI installation steps

Create a copy of this repo using git clone command as below:

```bash
$ git clone https://github.com/vivsridh4/donors-project.git
$ cd donors-project
```

Update *config.ini* file with the following details:

* Google Place API Key - To generate a new key, follow this [documentation.](https://developers.google.com/places/web-service/get-api-key)
* Donors API Key - To generate a new key, follow this [documentation.](https://developers.google.com/places/web-service/get-api-key)
* Database Path  - Create a local data store or use default path "./db/donors.db".

For example, update *config.ini* file as below:

```bash
$ vi config.ini

[KEYS]
google_places_api_key = AIzaSyCBiC44AIzaSyCBiC44_AIzaSyCBiC44
donors_api_key = ef4uef4ujef4uj

[DATABASE]
db_path = ./db/test.db
```

Install app using the following command from donors-project directory:

```bash
$ python3 setup.py install
```
Verify installation using the following command:

```bash
$ donors --help

Usage: donors [OPTIONS]

Options:
  -u, --user [create|list]    donors cli project users operations: Create
                              Users or List Users
  -gp, --getprojects INTEGER  list all projects near user. Need valid USER ID
                              as an argument which can be obtained by "donors
                              --user list"
  --help                      Show this message and exit.
```

## Run the CLI

The main commands supported by the Donors CLI are:

* `donors --help`        - Get help on donors cli app.
* `donors --user create` - Create new user with name, email id & zip code to search projects near user.
* `donors --user list`   - Lists all users with name, email id & zip code to get USER ID for searching projects near user                              based on his zip code.
* `donors --getprojects <USERID>` - Lists all projects near a user selected via *donors --user list* with google maps link.

## Usage with examples

* Create new user with the following command:

```bash
$ donors --user create

Please enter your full mame: Vivek Sridhar
Please provide a valid email:vivsridh@gmail.com
Please provide a valid zip code to search a project near user:560055
Saving user details to a databases......
```

* List all valid users who are registered in the donors project:

```bash
$ donors --user list

+--------+---------------+--------------------+---------+
| USERID |    USERNAME   |       EMAIL        | ZIPCODE |
+--------+---------------+--------------------+---------+
|   1    | Vivek Sridhar | vivsridh@abcde.com |  560055 |
+--------+---------------+--------------------+---------+
```

* To find all projects near a user with google maps details use the following command:

```bash
$ donors --getprojects 1

[Most Urgent] donors proposals near user

#######

School Name:     --- Arrowpoint Elementary School
City:            --- Saint Louis
Google Maps URL: --- https://maps.google.com/?cid=5060762413414080472
lat:             --- 38.8122919
lng:             --- -90.22734349999999
Proposal URL:    --- https://www.donorschoose.org/project/creative-counting/4146977/?utm_source=api&utm_medium=feed&utm_content=bodylink&utm_campaign=ef4uju946azk

#######

School Name:     --- All City Leadership Secondary School
City:            --- Brooklyn
Google Maps URL: --- https://maps.google.com/?cid=5922384627807966959
lat:             --- 40.6975906
lng:             --- -73.91309729999999
Proposal URL:    --- https://www.donorschoose.org/project/penny-wars-fundraising-supplies/4134999/?utm_source=api&utm_medium=feed&utm_content=bodylink&utm_campaign=ef4uju946azk
```

**NOTE:** Connect to "./db/test.db" by updating *config.ini* for some test data to play it.

## Know issues in the app

* Packaging CLI app as a CLI command using shell script and even further packaging it in a docker.
* Handling empty or non availability of local data store.
* Handling google api failed scenarios - api fails to return a URL if school names not found.
* Handling donors api failed scenarios.
* Creating more functions for standard code like - connect to the database and more.
* Verifying school name before generating list.
* Add valid comments in the code for useablility.
* Handling in-valid google api or donors api keys and verifying validity before using the CLI app.
* Other option to get google place-id is to use gmaps.reverse_geocode((40.714224, -73.961452)) function and most effective only if Donors project data is accurate.
