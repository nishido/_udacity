## Synopsis

By running the entertainment_centre.py file, a webpage listing my (Jason Blee) favourite movies will be generated along with a movie poster for each movie. By clicking on the movie poster you can watch a youtube trailer for that movie. 

## Motivation

This project was created for an assignment on the Full-Stack Web Development nano-degree on udacity.com.

## Installation

Simply download and contain the three files, as follows, accompanying this README in teh same folder:

entertainment_centre.py
media.py
fresh_tomatoes.py



## Running the program

Once installed all you need to do is run the entertainment_center.py file and the fresh_tomatoes.html file will be created and placed in the same folder (it will also open automatically).


## Further Information

These files were created, by and large, by following the first module in the FSND on udacity.com.

The only real changes I made were the movies themselves and a slight change to fresh_tomatoes.py. That is, I created a style for the movie-title id, increasing the movie titles' heights to 60px. I made this change because any title long enough to need two lines would result in that movie taking up two whole movie tiles (itself and the one below it); Forcing some inconsistant white space. For example, in my movie selection, The Shawshank Redemption would force Finding Nemo and Forest Gump one tile to the right, and The Matrix onto a third line (leaving empty white space where Finding Nemo would have been), using the base fresh_tomatoes.py file. 

Of course, this still doesn't help for movie titles requiring three or more lines, but I felt that would be a rare enough occassion to not warrant the extra time investment required to accomodate (I would prefer to have the movie-title height change dynamically with the maximum title length on that particular row). 

I am hopeful, however, that by the end of the nano-degree, the time required of me to make such a change would be far smaller.
