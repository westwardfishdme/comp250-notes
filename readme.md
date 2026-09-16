# My Collective Notes for Comp 250
This repository is the collection of notes and assignments for COMP250 
(*Research Writing: Open Source Tools and Techniques*)
All notes are written in markdown, and will be written to be best fit for GitHub's Markdown parser and formatter.

This repository was originally created by [Finch](https://github.com/westwardfishdme/comp250-notes) and serves as a template
for students taking COMP250.

## Navigation and Formatting
The directory is broken up by weeks; starting at enum 0, and proceeds sequentially all the way up to the end of the semester.
Notes are not named by days, but rather overarching topics. Each note contains the following format:

#### Example
```md
# Title/Topic

**Date:** mm-dd-yyyy
**Keywords:** 
Foo, Bar, Biz, Baz

## Subtitle/subtopic
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
culpa qui officia deserunt mollit anim id est laborum.

# Sources 
(if applicable in MLA18)
```
**Content will be fit based on readability on whatever machine I am using.** In other words, don't
expect the notes to be uniform to end at a specific column, but they will be nearly uniform based on
relativity to the previous line.

## Tools used
- [Zotero](https://github.com/zotero/zotero)
~This will be hosted on my home network and still accessible through school from my VPN.~ 

(Turns out I can't self-host this one)

- [pandoc](https://github.com/jgm/pandoc)
- [neovim](https://github.com/neovim/neovim)
- `git` of course.

### Custom tooling
Any programs, or scripts that I may use to complete assignments will also be included here under [./scripts](./scripts).
Below is a following list of tools that I have created for this course:

-`note`: CLI-tool written in Rust that currently only creates notes with the format I have described in the [example markdown](#Example)
-`keyword.sh`: Just a quick shell-script that counts keywords with grep/regex and prints them in an markdown table format. Planned to be merged
into notes.

**NOTICE!!!:** `note` requires you to compile it from source with Rust. To do so follow the instructions below;
1. Get and [install Rust from the official site](https://rust-lang.org/tools/install/)
2. Inside of [./scripts/create_notes/](./scripts/create_notes/), run
```sh
cargo build --release
```
3. Retrieve the binary from `./scripts/create_notes/target/release/note` by either manually moving it to this directory; OR install it locally by
copying/moving it to some directory within your `$PATH`

#### Usages
Below is a few examples of how to use my custom tools:

```sh
# create new note
note new --keywords "foo, bar, biz, baz" --title "my new note" new_notes.md
```
```sh
# from the project root directory...
./scripts/keywords.sh >> ./keywords.md
# then delete the old keywords manually;
# I haven't wrote a better form of the script yet-- sorry ;P
```

## Keywords
All keywords and their occurrences can be found in [keywords.md](./keywords.md)

## Licensing
**All software published are licensed under the GnuPublicLicense v3.0**; all text and published content is licensed by the CC-BY license.
Please see both licenses linked below:
- [GPL-v3](./LICENSE)
- [CC-BY](./LICENSE-CC-BY)

*This directory has now been renamed to comp250-notes to better suit naming conventions of the git
repositories as requested by the professors of the course.*
