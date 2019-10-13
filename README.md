# Gallery App by Mediatrice  NKOTANYI KAMPIRE
## Description

Gallery web application to show different beautiful pictures. Users get can view photos uploaded by admin. Users can see photos based on the location, by clicking on the listed locations in the menu. They can also search for photos based on the categories. they can Copy a link to the photo to share with my friends.
## Features

* The home page allows users to see various images
* User can see all images per location they were taken
* Users can also search for images based categories
* Admin can upload images from a django dashboard

## Prerequisite
Gallery project requires a prerequisite understanding of the following:
* Django Framework
* Python3.6
* Postgres
* Python virtualenv

## Technologies Used
- Python (version3.6)
- HTML, CSS ,and Bootstrap
- Postgresql
## Setup and installation
- clone 
- Activate virtual environment
- Activate virtual environment using python3.6 as default handler virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate

### Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

### Create the Database
- psql
- CREATE DATABASE portfolio;

### Make & Run initial Migration
After add new attribute you should make and run migration so that you can update the database
- python3.6 manage.py makemigrations photos
- python3.6 manage.py migrate
### Run the app
- python3.6 manage.py runserver
- Open terminal on localhost:8000
## Lisence and Contact information
- Email: kampiremediatrice@gmail.com
- Tel: +25078561070
BY Mediatrice KAMPIRE
