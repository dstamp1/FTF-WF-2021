## Control Flow ##
# So far, when we run our Python programs, every single line of code takes place. At no point has the computer made a decision and done some lines, but not others.
# Let's imagine you had to write a program that determined what outfit to wear, what kind of information might you use to do that? Chatstorm in the chat window.
# Great, so I saw someone suggest if the event if formal or not.
# Let's write some code to ask the user if the event is formal. The prompt will be "Is the event formal?(y/n)" Type but don't send the line of code you would use to save the user's answer to this question as a variable
## is_formal = input("Is the event formal?(y/n)")

# For now, let's just print back to the user a message depending on their response. We can control the flow of our code by using an if statement.

if is_formal == 'y':
  print("A formal event, how fun!")
else:
  print("Casual clothes is better anyways")

# Take 30 seconds and jot down what you notice and what you wonder. 
# Let's run this code and try a few different inputs and see what happens. Chatstorm what you did with "input:___ output:_____" so we can see what happens

### Datatype Conversions ###
#Let's write another file that will check whether a user is old enough to vote. We'll touch a new file callled "ageCheck.py" and we'll copy and paste this coode into it (check slack code snippets)
age = input("How old are you?")
if age >= 18:
  print("You're old enough to vote!")
else:
  print("You're not old enough to vote.")

## Once you have this code, go ahead and run it. What do you notice?
## I see we got an error talking about '>=' not supported between instances of 'str' and 'int' 
### Error and errror message are an exciting and important part of coding! We learn so much from errors and debugging them.
## We can get a betterr sense of what's going on if we add a print(age) between lines 1 and lines 2. 
## It looks like we're trying to compare "18" with 18. How does that connect back to the error message?
## Python will give an error when we try to compare (>, ==, <) variables of different datypes. 
## So if we want to get our code to work, we need to convert (fancy term, coerce) our age variablel from a string to an integer.
## We can do that by reassigning the age variable
age = int(age)



### For Loops ###
# Computers are really good at repeating the same task over and over again without making any mistakes/typos
# Let's imagine we were having a competition to see who could type out "print('hello')" as many times as we could without using copy and paste.
# We might type out 
print('hello')
print('hello')
print('hello')
print('hello')
print('hello')
print('hello')
print('hello')
# and quickly get bored or maybe a typo!

## What kind of tasks do you often have to repeat or maybe a company might need to repeat? Let's chatstorm. annticipated responses: marketing emails, order emails, happy birthday emails, etc.

## the most basic way to complete a task multiple times is too use a for loop like so:
for i in range(10):
  print("Hello")

## Let's do a chat waterfall, so type but don't send yet, how many times "Hello" will print on the screen?

## let's examine what that i is doing by modifying our code
for i in range(10):
  print(f"i is currently {i}")
  print("Hello")

## The letter i is used as this placeholder (this placeholder frustratingly doesn't have a name, but is most commonly called the "iterator", "loop counter", "iteration variable" or "constant of iteration"), but the term i isn't special or reserved, it's just the most common. You might have seen it before in a math class during summations

## since it's a variable, we can call it anything we want so we can referennce it later.

### There are soooo many things you can do with loops. Let's talk about finding sums and you can think about other uses of the superpower.

## Lets say we want to find the sum of the numbers 5,6,7 and 8

## We could use this code:

sum = 0
for i in range(5,9):
  sum += i
  print(f"The sum is currently {sum}.")

print(f"The loop is over, and the total is {sum}!")

# What is the value of sum before the loop starts?
# What is the value of sum after the loop has gone one round?
# What is the value of sum after the loop has gone two rounds?

#### Let's skip over 'looping with a condition' in the teacherhub for time purposes ###### 
## I will mention it's something we can do

## Looping over strings ###
## So we've looked at looping over a range(), but we can loop over any 'iterable' like a string.
your_word = input("Give me a word and I'll spell it.")

print(f"Okay! I'll try to spell {your_word}.")
for letter in your_word:
  print(letter)

## Lab Time: we'll be working on the loopy math lab
# git clone https://github.com/upperlinecode/loopy-math-python-iteration.git
## You might want to explore the documentation for the range() function https://www.w3schools.com/python/ref_func_range.asp
## and if you might want to know more about the modulo function to find even numbers https://www.pythoncentral.io/using-python-to-check-for-odd-or-even-numbers/