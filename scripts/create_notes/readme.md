# Note creator;

My note creator written in Rust.

**Usage:** 
```sh
notes new "my_cool_notes" --keywords "Hamburger, Philosophy, Food" -t "The Philosophy of the Hamburger"

# creates the file:
# my_cool_notes.md
# and opens it with $EDITOR;
# if $EDITOR is not set; it will default to 
# using vim. 

```
Content of my_cool_notes.md

```md
# The Philosophy of the Hamburger

**Date:** (current date)
**Keywords:**
Hamburger, Philosophy, Food

```

Future editions may include a keyword search using a regular expression:

```sh
# search the current directory for all keywords.
notes keywords .
```
which would operate similarly to the script already included inside of [keywords.sh](../keywords.sh)
