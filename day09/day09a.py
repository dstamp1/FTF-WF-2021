Morning Session

### Morning Routine
# Stretch + Share 
## Question: If you could instantly learn how to do something new, what would it be and why?

# Microfeedback - 
## Got some microfeedback about codealongs and feeling like they don't want to interupt. We want to name that experiencing bugs is a key part of the process and its so helpful to us and your classmates if you do share your bugs as they arise. You're probably not the only one and we can learn so much from these errors.
## During CYOA Derek will be hosting a Flask review session that is open to all FinTech focus students, so you can get some additional instruction this afternoon too

## Agenda
 9:00 -  9:30 | Morning Routine 
 9:30 - 11:00 | Intro to Bootstrap + Components
11:00 - 11:30 | Bio Break + Game
11:30 - 12:30 | Bootstrap Grid Lab
12:30 -  1:30 | Lunch (Offline)
 1:30 -  2:30 | Bootstrap Mockup Match
 2:30 -  3:00 | Close
 3:00 -  4:00 | Choose Your Own Adventure


## Game
# Let's do a debugger


# Review of Design Manifesto
## On Tuesday we started class by talking about examples of good and not so good web design.
## Chat storm: What are some features of good web design? Send as many as you can think of

### Good web design is about putting the content at the center. The styling supports the content and doesn't distract.

# We have these key facets at our disposal: colors (text and background), font choice and size, and whitespace around elements (margins and padding)

#readbility, ease of focus, color scheme helps

### Oh and for fun, let's see what a "beautiful" website used to look like
# Apple in 1996 - https://web.archive.org/web/19961023165502/http://www.apple.com/
# Apple in 2001 - https://web.archive.org/web/20010822231227/http://www.apple.com/
# Apple in 2010 - https://web.archive.org/web/20100430204732/http://www.apple.com/

## Bootstrap Code-A-Long

### Styling a page with CSS can be very tedious and often requires creating many classes and IDs.
### Sometimes this styling doesn't quite work out and can have some visual inconsistencies.
### To solve this problem, groups of people collaborate on design frameworks. These frameworks give you a wide range of CSS classes you can use to consistently style your site.

### We'll start off together this morning seeing how to incorporate Bootstrap into your site.
### Then we'll look through the Bootstrap documentation to pull out the essential features https://getbootstrap.com/docs/5.0/getting-started/introduction/

## Then we'll be able to explore aspects of the bootstrap library and bring it back to the whole group to demo the code.

## Then we'll look at the Bootstrap Grid together

## Finally, we'll be able to revist a previous HTML project you've worked on and you'll restyle it with Bootstrap.

## We'll close out the afternoon with a design challenge!

### So what even is bootstrap?
# Let's look at a webpage I put together that does not use any CSS at all.
# And here's the same HTML file but with bootstrap included
# Bootstrap really lets us build beautiful websites quickly with design consistency

#### Using Bootstrap in our Website ####

## To use Bootstrap, we need to include a link to their CSS file & some JavaScript Files.

## Let's mkdir day09 and copy down this starter code: git clone https://github.com/dvoso/bootstrap-code-along.git

### Using https://getbootstrap.com/docs/5.0/getting-started/introduction/
### We're using Bootstrap 5.0.2 and when we search for support about how to use it, you need to be on this page and searching in this area.


# To add the CSS, we'll add
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

#And then we'll add the JavaScript links
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

## To view this page in cloudshell, we can right click on the file and select open with -> preview

## Let's start to add some content to our site!

### Take 3 minutes and add a list to your site with:
# An h1 header
# As many list items as you can


### To see how we use the Bootstrap classes, we're going to restyle the list using a List Group
# If we look at the documentation https://getbootstrap.com/docs/5.0/components/list-group/
# We see we need to add some classes
<ul class="list-group">
  <li class="list-group-item">Cras justo odio</li>
  <li class="list-group-item">Dapibus ac facilisis in</li>
  <li class="list-group-item">Morbi leo risus</li>
  <li class="list-group-item">Porta ac consectetur ac</li>
  <li class="list-group-item">Vestibulum at eros</li>
</ul>
# We also have some additional options to add .active or .disabled to change the appearance

## Take ~5 minutes in your breakout rooms to try out some more options of classes for list groups


### Showcase some code ###


# As you can see in the components section, there are alot of different components bootstrap pre-styled. Each breakout room will be designated to explore 1-2 of these components and to show it off for the group. 

Alerts & Badges
Buttons & Button Groups
Navbar 
Progress Bar
Dropdown 
Forms 
Card

Modal

#### 10 minutes in breakout room with ~1 minute for each group to demo ####



#### Crash course to Bootstrap Grid ####
# A key feature of modern web design is the responsive page. Web sites are accessed on screens of many widths and we want our sites to look good on all of them.
## Bootstrap gives us the tools to make this happen.
# The fundamental concept is that the page is constructed of rows and columns.
## In our bootstrap index.html, let's add
<div class="row">
  Contents of row.
</div>

## Nested inside of this div we can add our columns
<div class="row">
  <div class="col-1">contents of column 1</div>
  <div class="col-1">contents of column 2</div>
</div>
# Let's preview this file.

# A question you might ask next is how many columns are possible. Let's experiment to find out
<div class="row">
  <div class="col-1">contents of column 1</div>
  <div class="col-1">contents of column 2</div>
  <div class="col-1">contents of column 3</div>
  <div class="col-1">contents of column 4</div>
  <div class="col-1">contents of column 5</div>
  <div class="col-1">contents of column 6</div>
  <div class="col-1">contents of column 7</div>
  <div class="col-1">contents of column 8</div>
  <div class="col-1">contents of column 9</div>
  <div class="col-1">contents of column 10</div>
  <div class="col-1">contents of column 11</div>
  <div class="col-1">contents of column 12</div>
  <div class="col-1">contents of column 13 - note that this 13th column will wrap to start a second row, since we've exceeded the maximum of 12.</div>
</div>

## Having 12 columns available to us is very exciring, but it does seem like its way too much content to have side-by-side.

## Bootstrap gives us the ability to have a column span more than 1 column. To do that, we include a -x where x is a whole number from 1 to 12. 
# To ensure that the row is complete, we'll make sure each row adds up to 12.


#### Recreating the Spotify Footer ####
# Let's use what we just saw to try to recreate the spotify footer

<div class="container">
  <div class="row">
    <div class="col-lg-2">Logo content</div>
    <div class="col-lg-2">Company content</div>
    <div class="col-lg-2">Communities content</div>
    <div class="col-lg-2">Useful links content</div>
    <div class="col-lg-4">Social icons - this one is twice as wide as the other four.</div>
  </div>
</div>

## To make this site responsive on different viewports, we can specify the column sizes at different breakpoints.
