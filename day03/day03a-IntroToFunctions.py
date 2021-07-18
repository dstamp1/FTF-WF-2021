Morning Session-- Intro to Functions
turn off autosave
# Opening Circle
## Show the agenda
## Stretch and Share
### Directions - Let's get ourselves ready to code by warming up our bodies with a stretch and share. We'll go around the group and each person will (1) share a stretch or keep a previous stretch going and (2) answer the prompt for the day.
### If you could have a superpower, what would it be?
## Discuss Microfeedback
### People feeling more comfortable with coding with lots of enjoyables
### People wanting more time to work on labs
### And so many great ideas for digi-murals --- so stay tuned
## Play a Game
### https://garticphone.com/

# Introducing Functions

# Let's mkdir day03 and touch a file functions.py

## Let's examine these outputs and see if we can come up with a rule
2 => 5
3 => 10
5 => 26
10 => 101

#Once you have an idea of what the rule is, come up with a name. Chat Waterfall: Type but don't send yet; what would be a good name for this function?

def square_plus_one():

## So far, we've seen two types of python built-in functions
variable.method_name() => return_value
function_name(argument) => return_value

## Chat storm: write as many example as you can of the first example. Repeat for the second example


## Of course, what if we want to define our own functions

#The general form is...
def function_name(parameters, separated, by, commas):
    ## business_logic
    return return_value

#Here's a function we might define
def shout(name):
    name = name.upper()
    return f"Hello {name}!"

#Lightning round
## 1) what is the name of this function?
## 2) how many parameters?
## 3) What is the datatype of the parameter?
## 4) What is the datatype of the return value?

# Let's actually use this function
shout("julia")

## let's put in an integer too and see the error, model by putting in slack channel

#Chat waterfall: Type but don't send yet; what will print to the terminal if we run this code?

## Functions with multiple arguments
# Of course we can have multiple arguments/parameter in our custom functions
# Let's write a function that takes in a name and age and returrns a customized message
def personalized_age_check(name, age):
  if age >= 18:
    return f"Congratulations {name}! You're old enough to vote."
  else:
    time_left = 18 - age
    return f"Congratulations {name}!. You can't vote for another {time_left} years."

# Call the function
print(personalized_age_check("Jeff", 28))
print(personalized_age_check("Zara", 14))


### BREAK FOR LAB HERE
budget buddy -- git clone https://github.com/upperlinecode/budget-buddy-python-functions.git

activity planner -- git clone https://github.com/upperlinecode/activity-planner-python-functions.git

string theory -- git clone https://github.com/upperlinecode/string-theory-python-methods.git

cookie monster -- git clone https://github.com/upperlinecode/cookie-monster-python-functions.git
