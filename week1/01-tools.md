# Tools and personal use
**Date:** 09-08-2026

**Keywords:** Tools, Git, Notetaking, Markdown

## What are we using these tools for?
The tools that we are using for the course extend themselves beyond the actual coursework.
I already have used Zotero for another course (my COMP352 course) to generate a bibliography
for some information.

**The tools that we are using in the course**
- Git
- Zotero
- Pandoc
- Markdown

### Git
A .md file dedicated to the uses of git is already documented inside of [./01-git.md](./01-git.md).

While this document covers the usage in the course, I am strongly familiar with `git` as I use it
as a part of my daily workflow for courses and beyond. As an open-source developer, I have to use
`git` regularly to not only stage projects, but also to publish them to [GitHub](https://github.com/westwardfishdme).

### Zotero
Zotero is a Free and Open Source research tool that allows users to create and share research
collaboratively. I find use in this for creating bibliographies easily and exporting them to
LaTeX, which for other courses I use to write documents.

Additionally, we were instructed to watch a video by Steven Bradburn called [How to Use Zotero](https://www.youtube.com/watch?v=JG7Uq_JFDzE),
which I had briefly skimmed since Zotero itself was pretty intuitive to use regardless.

What I find cool about Zotero is that you can source things **directly from your browser**, which doesn't require much setup other than
logging into the account. I do kind of wish that I could self-host this, but if it works -- it works. Besides, my poor single repurposed server
is overloaded with so many services that I don't want to have to setup another service onto it.


## Markdown
Originally I intended to write the notes for this course purely in LaTeX.

I planned on using it for this course for notetaking, however this idea was scrapped once 
Dr.Thiruvathukal demonstrated the cool things about markdown-- which convinced me to use 
Markdown over LaTeX for notetaking. Below are reasons that convinced me that Markdown was 
more useful to use over LaTeX:

- GitHub's integration with MarkDown; Things look pretty.
- I can easily link other notes or information with relative ease.
- If I need to insert a snippet of code, I can do so with syntax highlighting:

```py
def foo(x:int)-> int:
  """
  Add 40 to x
  """
  return (40 + x)
```
> quotes also make adding subtext or quotations look nice.

However, the assignment given on **September 3rd** required us to look for a note-taking app that supported Markdown.
Neovim was not on this list, but it's what I'm using anyways.

#### Why Neovim?
- I have used Vim for the past 6 years, I am comfortable using it and have it configured to the way that I like it.
- I can't live without Vi keybindings.
- I can remotely edit files via SSH if I need to, although I already have an NFS configuration that allows me to share
my school work directory directly to my laptop over a VPN.

### Pandoc
Pandoc is actually something I find quite useful too outside of the course. A lot of the time,
I have to open LibreOffice to edit `.docx` files, and I personally hate leaving neovim which is
configured to my liking. Pandoc allows me to convert between a ton of different file formats with ease.

It also allows me to create scripts to convert my markdown into whatever format, as demonstrated by Dr. Thiruvathukal in class.

```bash
# this already can come in useful...
pandoc --from=markdown --to=latex some.md -o some.tex
```
I already used `pandoc` in this repository to convert some notes taken earlier from LaTeX to markdown so that I can actually use them to work on assignments. 

# Sources
Steven Bradburn. How To Use Zotero (A Complete Beginner’s Guide). 2021. https://www.youtube.com/watch?v=JG7Uq_JFDzE.
