#Welcome back from break
##So far we've worked with our file system via the terminal, next we'll write our first lines of Python!

## Use cd, ls, and touch to navigate to your day01 folder and create a file called 'hello.py' and give us a green check in the participants window when you have it.

## Next, let's go over how we run a python file with the terminal. In your 'hello.py' file, on line 1 type the code print("hello world"). Green check when you have that. *pause* Then, in our terminal let's write python3 hello.py and press enter. What do we see!

##In our code, the characters we see between the quotation marks (single or double) is called a "string"

##Let's touch another file called 'math.py' and open it. Let's add these two lines of code: print(4 + 3) print(4.0 + 3.0) . In the chat, type but don't send yet what exactly these two lines of code will produce. 

##Numbers without decimal points are called integers and numbers with decimal points are called floats. 

##Let's try out this line of code too: print('4' + '3') and make a prediction. In the chat, type but don't send yet what exactly will appear.

## When we use the + operator between strings, we get 'concatenation' which is a fancy word for stick together.

## For this next part, we're going to put our terrminal in REPL mode where we can type python directly and get it to print out. To do that, type 'python3' and enter.
## We have other operators and in breakout rooms, I want you to take 5 minutes and test them out using values of the three datatypes we know: integer, float, string. You'll try out +,-,*,/ and **
## Keep track of what you've discovered by using a slack DM to your breakout room partner.

### 5 min of Breakout rooms ###

# let's go over what the operators do first. To take notes for yourself, DM yourself in slack.
## + : add or concatenate
## - : subtract
## * : multiple or repeat a string
## / : divide
## ** : exponent


##### Variables and Concatenation ######

#Let's touch a new file in the day01 folder called 'greet.py'

#let's write these two lines of code 
name = "lauren"
print("Good morning " + name + "!")

##In the chat window, make a prediction on what statement will be printed. Write but don't send yet.

## So we call line 1 a variable. name is like a box that store information we can reference again later.

## As we heard this morning, what we did on line 2 is called concatenation and I'm really excited to show you another way to do it.
print(f"Good morning {name}!")
## In the chat, what do you notice is different with this approach? 

## Right now, we've just used the string stored in the variable as-is. What are some ways you might want to modify a word stored in a string? Let's chatstorm this so send as many as you can in the chat window starting now.

## I want to highlight capitalization. Python has built-in things called "string methods" that let us do a verb to the string. To get a list of these string methods, google w3schools python string methods and click the first link. When you get there, scroll through and see which method will let us capitalize the first letter of name.
## print(name.capitalize()) 

## So we're ready to do some lab time exploring string method. Have w3schools available for support. Here's the link to clone the lab: git clone https://github.com/upperlinecode/john-jacob-python-string-methods.git

## When you get into your breakout rooms, identify who will be the driver and who will be the navigator, share your favorite cereal, and have fun! Remember to use slack DMs to share code snippets back and forth and use the ask for help feature if you need it.
### Can have the additional string 
##### Time this out so lab time is done by 11:55am to 12pm. 

##User Input & Control Flow##

#Python gives us a way to ask the user for input and set it equal to a variable
name = input("What is your name?")

#Let's touch a new file called "greet1.py" and include this line of code too: 

#If we run this code, what would happen? Make a prediction in the chat

