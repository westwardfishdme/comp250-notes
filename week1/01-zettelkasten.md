# Zettelkasten.md
**Date:** 09-03-2026

**Keywords**: Notetaking, Strategies, Tools

## Task
Ask a chatbot: "What are the advantages of the Zettelkasten method of note-taking for
university students?"

## Notes

Asked to get a chatbot's "opinion" on why it's so good.
 - Google Gemini's response:
 > The Zettelkasten method helps university students build long-term understanding, 
 connect ideas across different classes, and write research papers much faster.

However, a better source; doing actual research:

The word "Zettlekasten" stems from the German words 'Zettel' and 'kasten'
literally "Notes box". According to [a site dedicated to promoting the Zettelkasten method,](https://zettelkasten.de/introduction/)
you start an array of major points, and break it down into categories of subnotes, and those subnotes themselves recursively add
subnotes as they relate the ideas. Below is a sample diagram that explores the syntax:

```
[0] # some note denoted as 0.
[1]--> [1a] # (1 is a new note unrelated to 0, has subnote 1a)
[2]--> [2a]
   |-> [2b]-->[2b1] # (2b1 is now a subnote of 2b, along with 2b2) 
           |->[2b2]
[3]
```

The idea here is to connect notes to organize thoughts and ideas that allow a 
person to connect ideas between one another.

**__Ideas link by:__**
- main ideas
- keywords
- any relating idea

## Importance of handwriting
> Handwriting builds muscle memory that builds retention.

I like to think about it like this too, I used to be huge into eSports and playing
video games somewhat competitively. It's kind of like doing aim training, but with note-taking.
Although these notes are written on a keyboard, I like to think it still counts as "handwriting",
especially considering that AI could theoretically do this. Programming does something similar for
me too.

**Quote from class:**
> If something is hard to piece together; Try writing notes.

Breaking something down into small bite-sized pieces provides a "**divide and conquer**" strategy
to be able to understand information. Combine this with handwriting, and you build the muscle memory
for retention. 

## How do I practice Zettlekasten?
I kind of do already have a method of note taking; don't write everything; write the things I'll easily
forget; or write it like code documentation.

Maybe a CLI tool could be made in python or rust:

```rust
/// might look something like this:
struct Note{
  note: String,
  subnotes: Option<Vec<Note>>,
}
```

Or in python:

```py

class Note:
  def __init__(note:str):
    self.__note = note
    # subnotes could be a linked list or an list of `Note`s. 
    self.__subnotes = []
```

Of course implementations would be respective to each language with the usage:

```sh
zettlekast "some topic" --note "foobar"
zettlekast "topic-subnote" --topic "some topic" --note "fizzbuzz"
```

then to write to stdout:

```sh
# writes all and organizes them respectively.
zettlekast "some title" --write

# or if you want only the subnotes:
zettlekast "subnote topic" --write
```

would output something like:

```
some topic:
  - foobar
  topic-subnote:
    - fizzbuzz
```
Maybe some markdown integrations could be used. Like linking files and what not.

# Sources
“Getting Started • Zettelkasten Method.” Accessed September 3, 2026. https://zettelkasten.de/overview/
