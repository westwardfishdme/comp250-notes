# Reworking of the notes program

**Date:** 9-23-2026
**Keywords:**
Tools, Software Development, Notetaking, Automation, Synthesizing Information

As a part of my note collection, I had created the `note` program to enhance
my workflow as a part of my coursework. At first I had wrote it to be a template
creator for the notes, but now it has also replaced the script I used to search
for keywords and generate the table. Despite already having a script to generate
the table; I felt as if the script ran too slow and too inefficiently, so that's
why I just wrote the functionality directly.

The cool thing about it is that I can actually use the program to search within
any given directory in this project; So I can actually see the keyword count
**per week** in my note collection which is pretty awesome!

## Future features
Since I already wrote the functionality for doing a keyword search, I was thinking
that I should actually create a way to actually index and search for which notes
have the keywords. So it makes it easier for someone to actually look at where these
keywords are being used. I mean I already have the functions to perform the search,
but if I were to search in that manner (recursively regex each file) it would be
DRASTICALLY inefficient. So I gave it some thought and I think what I want to do
is mimic something like the gnu `locate` tool. 

### Search like `locate`
If you aren't familiar with [locate](https://en.wikipedia.org/wiki/Locate_(Unix)) tool,
it allows you to search for files based on their name by performing a regex over a 
generated database of files. While this note collection is rather small-- I do think
that I would find use in my tool for other classes.
> (which I actually started using it for some other courses already!) 

Essentially the idea is to generate a database of keywords and then from this database, grab
which files have this keyword and then direct the user to a menu of these items 
(preferably, in a TUI/curses like menu).

But maybe that's a bit too much for such a small collection of works, I think there
is a better solution for search indexing that is just escaping my mind right now and
I'll have to do more thinking before I begin working on an implementation. 
