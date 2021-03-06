Mid-Morning Session

#### finish setting up the collection on MongoDB
#Name the database 'test and the collection' 'events'


### How to connect a Flask App to a MongoDB database

## Let's make a template of the community board app from this morning
https://github.com/dstamp1/flask-and-mongodb-code-a-long


## To connect your database,
from flask_pymongo import PyMongo

MONGO_DBNAME = ''
MONGO_DB_USERNAME = ''
MONGO_DB_PASSWORD = ''

app.config['MONGO_DBNAME'] = MONGO_DBNAME
app.config['MONGO_URI'] = f'mongodb+srv://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@cluster0-kxrbn.mongodb.net/{MONGO_DBNAME}?retryWrites=true'

mongo = PyMongo(app)

# The proper way to store this information is with an environment variable. To use an environment variable, we need to include sudo pip3 install python-dotenv

sudo pip3 install python-dotenv

#and import the package
import os
from dotenv import load_dotenv
load_dotenv()

## and we'll include
MONGO_DBNAME = os.getenv("MONGO_DBNAME")
MONGO_DB_USERNAME = os.getenv("MONGO_DB_USERNAME")
MONGO_DB_PASSWORD = os.getenv("MONGO_DB_PASSWORD")

## So where does the data live? We put it in a file inside the directory called .env This file will not be uploaded into github and the information is kept secret.

# In the .env file, we would put
MONGO_DBNAME =
MONGO_DB_USERNAME =
MONGO_DB_PASSWORD =

## right now, this route requires us to hard code the event to add it.
# Let's connect it to the form.

### Now we want to add new documents to our database
events_db = mongo.db.events
event = {
'name':'',
'date':''
}
events_db.insert(event)

### Have students go to breakout rooms on how they would view all of the events in the route
events = events_db.find({})

## Playtime -- Continue to work on this flask app and add some styling, add additional fields to the form about the event, etc.
