#Opening
## Show the agenda
## Stretch and Share
### Directions - Let's get ourselves ready to code by warming up our bodies with a stretch and share. We'll go around the group and each person will (1) share a stretch or keep a previous stretch going and (2) answer the prompt for the day.
### What song is stuck in your head?
## Discuss Microfeedback
### A great day with almost all enjoyables!
### Definitely feeling a trend that we took on alot of new material and feeling a bit rushed
### Request for a reference document to look back on --- Julia is preparing it and its linked in the slack
### More break! Definitely, we'll chunk up the sessions to include some getting to know you breaks before launching into labs
### Talking about how to set up the window for zoom and cloudshell
### Mentioning some of the slack channels


## Intro to Lists ##
## mkdir a day02 folder
## Touch a file called introLists.py

#Let's start out by writing out some of our favorite foods in five separate variables.
first_favorite_foods = 'Pizza'
#take 90 seconds to write them out

# Chat Waterfall - Type but don't send yet: what was frustrating about this process with one word
# Ask 2-3 students to expand on their one word

# What is: Code Refactor (rewrite your code to have the same functionality)

# Let's create a *list*
fav_foods = ["Pizza", "Ice Cream", "tacos", "Tofu Pad Thai", "Chicken and Waffles"]

## Refactor your top five fav foods to make your list of fav_foods and print it

### Indexing Items ###

# Let's say we want to access a particular value of the list.

# print(fav_foods[2])

# Chat Waterfall - Type but don't send yet: which food would be printed?
# Ask a student with the wrong answer to explain their answer (it seems logical), have a student with the correct answer remind us that python is zero index, and have a third student correct the number in the print statement to access just the second favorite food.

#### CRUD ####
# When we interact with a new data structure, there are four basic operations: Create, Read, Update, Delete. For a list, it would how to add a new item in the list, how to access an item in the list, how to change an item in the list, and how to remove an item from a list.
# Python overlaps reading and updating with similar syntax
fav_foods[0] = "Spinach and Artichoke Pizza"

print(fav_foods[0])

#Mini-challenge: Update one of your favorite foods in your list

## The other CRUD operations are handled with list methods.

# I want to review the syntax of methods with a review example.
# Let's say I have a string stored in a variable
name = "kevin"
#and I want to capitalize all the letters with .upper()
#Let's get a volunteer to raise their hand and tell us how to define a new variable name_upper

### So to access a great list of list methods, google 'w3schools python list methods'

## Mini-break + game
# Let's go into breakout rooms and do a scavenger hunt challenge. Without leaving the room you're in, find an item you both have accessible.

## We'll work on the list methods lab now for ~30 minutes
git clone https://github.com/upperlinecode/list-methods-mini-lab-python.git

##### Quick direct teach on list iteration #####
# Yesterday we looked at for loops using the range function and over a string. Of course we can do this with a list.

# Let's write a loop that prints out my love for each of my favorite foods.

## Let's have a volunteer raise their hand and help me start with this loop like yesterday.

fav_foods = ["Pizza", "Ice Cream", "Okonomiyaki", "Tofu Pad Thai", "Chicken and Waffles"]

for food in fav_foods:
  print("I sure do love " + food + "!")

## A major pro tip is to have your list variable explicitly be a plural noun and your iteration variable be a connected, singular noun

## All the things we saw yesterday with loops we can do here too. We can use other control flow, we can use += to do an accumulator, and any other fun idea yoou can think of.

## Mini-break + game
# Let's go into breakout rooms and do a show and tell challenge. Use the 2 minutes of the breakout room to find an item cost <$5 that is worth much work. We'll do a whip around with the main group before going on to a lab.

## We'll work on the list iteration lab now
git clone https://github.com/upperlinecode/list-iteration-mini-lab-python.git
