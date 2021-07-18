Morning Session

## Morning Routine
# Stretch and share....if you could make a website about anything, what would it be about?
## Share with students that websites aren't just about making money, they can be about important causes

# Microfeedback 
# People liked having the opportunity to choose what they wanted to work on in the afternoon based on their comfort level, and the chance to go over the lab with a teacher was really helpful 
# Getting the chance to work with the teachers has been helpful 
# Suggestion to pin important things in slack like julias document - #anchor-charts only has julias doc in there so if you want to see it, go there
# More time for games 
# Debugger is the current favorite game for many people in the class 
# Working with people at different levels - we are going to continue to push you to work with people more/less experienced with you.

## Show the agenda and then...

## Let's play debugger today!


## Today we're going to dive into HTML + CSS. By the end of today, we want to be able to understand how to place tags in an HTML file and how to style via classes and IDs. 
## While this might not be new to you, we want a strong foundation so we can learn how to use Bootstrap and, eventually, use Python to dynamically generate HTML.

# What Makes for a great website?

### Take a few minutes to search the web for sites you find to be particular beautiful and ones that could use some design tweaks. We'll go into breakout rooms after 2 minutes so you can screenshare.

### Now that we have a sense of what feels like good and not so good web design, let's collaborate on a document that encapsulates what we believe to be true about web design. Go to this google document and add 1-2 things you picked up from our conversations: 
# https://docs.google.com/document/d/1HG5pcbepLaeMr7gvmGoFRlfzNTc-Ql3mzIZYEHpt5Jg/edit?usp=sharing

### Into to HTML ###
#HTML is not a scripting language, it is a language that communicates structure and hierarchy within a document.
# We can go to any website (like https://www.wikipedia.org/) and do a right click + inspect to see this code that web browsers read to generate websites.
# HTML provides the structure and CSS provides the visual styling.

# The core construction in HTML is the tag.

## Tags consist of abbreviations or short words and have an opening and closing version.

#<tag> _content_ </tag>rep

# And a central premise of HTML tags is that they can be nested inside of one another. This relationship is known as a parent-child relationship.

<div>
  <p>Nested</p>
</div>

## Let's first make a template of a basic one page website https://github.com/dstamp1/html-website-template

## In the html file, we have a few tags that are "required" --- modern web browsers are expecting them
## The head and the body
## The head has information about the website (metadata) and can include links to outside resources --- like a stylesheet (internal or external)
## the body is where the content of the website goes. If you want it to show up on the webpage, it goes here

## Let's take a look at one tag together -- adding an image
# First, let's check out what w3 schools has on the topic
## https://www.w3schools.com/tags/tag_img.asp
<img src="img_girl.jpg" alt="Girl in a jacket" width="500" height="600">
## src = a link to the image itself
## alt = alternate text that shows if the image doesnt load -- also used by screen readers
## width = a measure in pixels
## height = a measure in pixles (both width and height are not required)
## measurements can also be set with percentages

## First, let's practice nesting and placing image tags (you'll look up documentation on how to do this) in the Boroughs Nesting Lab.  git clone https://github.com/upperlinecode/NYC_Boroughs_Lab.git

## To view this page, we need to spin up a simple server
## To do that, we'll run python3 -m http.server 8080 in the 

## 15 minutes of play time here ##
##################################################
# Now that we have some content on the page, we can start to style what we see.

# CSS gives us many ways to specify which elements we're going to apply style to. Let's start with one of the most specific ways, using an id.

# The boroughs lab already includes some styling. Take a look at it and how that code showed up on the screen. CSS consists of rules. Each rule connects a CSS property with a value. The rule has a : in the middle and rules are separated by ;. There are so many different rules you can construct and you have to consider how multiple rules would interact. It is so much fun!

# Take 10 minutes to google different CSS properties and make the borough lab your own. If you're unsure where to get started, changing colors is always fun.


### Class Selectors ####
# So far we've had to style each id on it's own. Not too bad when there's 5. But imagine we had this site to style. Make a copy into day07 folder git clone https://github.com/upperlinecode/css-classes-template.git

# We can see there's some overlap here between paragraphs and some paragraphs share some features.
# CSS gives us a way to style more than one element at a time with classes. We preface classes with a . in the CSS file. Let's write some css for these classes given to us.

# Another powerful feature of classes is that an element can have more than 1 class. This gives us a ton of flexability

### Bifurcation ###
# This was our crash course in HTML + CSS!
# You can start your mini-hackathon and begin constructing your website
# https://docs.google.com/document/d/19-rxeMOdC0ifGrivk63kSknTM1dZXRqNzASxTDeuHJY/edit?usp=sharing

## There's also a few more activities we have if you want to focus in on HTML + CSS
## https://flukeout.github.io/
## http://toolness.github.io/css-selector-game/
## https://cssbattle.dev/

