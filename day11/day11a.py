### Morning Routine
# Stretch + Share
## Question: If you could move anywhere, where would you live and why?

### A game...we'll go to breakout rooms of 2 people and find an item you both have in common.

### Share out of items by each group

### Midcourse survey --- Folks are feeling great about making it halfway through the program! We'll continue our strategies of reteaching and differentiation in the afternoon session to meet students where they are. Also know that youj have all learned an incredible amount of programming in just 8 class days! While you may or may not persue programming in college or continue as a hobby you have all proven you have a place in computer science. 

### Agenda in the slack channel

### What is an API? ####

## Chats Storm: Send as many responses as you can...what kind of data/data sources have you seen integrated into a google search? For example, if you searched for a restaurant near you.

## APIs provide a way for two different pieces of software to interact with one another. Most APIs rely on an exchange of information via a GET request to a specific API url (called an endpoint).

## To ask for data from an API, we would construct the API request URL with the search parameters and get back the data as a complex data structure.

# We'll explore the Jeopardy API together and then we'll do a mini-project in the morning on coding a jeopardy CLI game. https://jservice.io/ or an API of your choosing.

## Let's visit jservice.io/api/random and do a quick "what do you notice, what do yo uwodner"

# Let's open up our cloudshell and mkdir day11 and touch jeopardy.py

# To send our data via the HTTP GET request, we'll use the requests library in Python so on line 1 we'll add
import requests

# Next step, we need to construct the request URL from the API endpoint and any query variables we want to include.
API_prefix = 'https://jservice.io/api/clues'
# To determine the query, we'll look over the documentation. Let's say we want to get back just the 1000 clues
API_query = 'value=1000'
#To build the URL, we'll use string concatenation
## Example: API_endpoint = API_prefix+'?'+API_query + '&' + API_query_2
API_endpoint = API_prefix+'?'+API_query

# And finally, we can make the request
r = requests.get(API_endpoint)
## If we print the request, Let's print it
print(r)
## We get back a Response object. The [200] is the HTTP code for success and so our data is living inside of the Response object. To get it out,
data = r.json()

# Looking at the data we just got back can be difficult in the terminal...so let's try out a tool in our web browser with a JSON viewer.

# What we see is that we're getting back a list of dictionaries. Each dictionary represents a clue.

### In your breakout rooms, explore the data object you get back and print information with labels for the first clue. You'll work with your partner to write a function that takes in a clue (as a dictionary) and prints the clue category title, clue value, and question.
### Starter code
def display_clue(clue):
    clue_category = clue
    clue_value = clue
    clue_question = clue
    print(f"Category: {clue_category} ")
    print(f"Value: {clue_value}")
    print(f"Question: {clue_question}")

clue_one = data[0]
display_clue(clue_one)


## One of the trickest parts of working with an API is parsing through the returned data. You might have to switch back and forth between indexing a list and reading valus from a dictionary. The JSON viewer can be very helpful.


### You'll spend the rest of the morning designing and implementing a Jeopardy command line interface game. Clone this git respository https://github.com/upperlinecode/jeopardy-cli-python-apis.git to give you ideas of what to implement and in what order. By writing your display_clue function, you already have a great start. Level 4 has some really awesome stretch challenges in it, including printing the board so have lots of fun!
