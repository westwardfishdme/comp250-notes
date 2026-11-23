# Note Collection overview #2

**Date:** 11-23-2026
**Keywords:**
Research Paper, Overview, Assignment


The notes that I have written for this overview can be directly found the [./notes](./notes) directory.

## What I got done
While I reduced the scope of my research, I am continuing analyzing what makes Rust difficult to transpile;
as well as looking into what linguistic features Rust has that makes it on-par with C with the added bonus
of memory safety.

In addition, I had written some very useful notes within (paper_lexical_analysis.md)[./notes/paper_lexical_analysis.md]
that describes how to directly translate certain primitive C types directly to Rust which will prove itself useful 
for future references in my own work. As it partially already has within the code I had written inside of 
[./src/mnemosyne/.../primitives.rs](./src/mnemosyne/src/modules/static_analyzer/typing/primitives.rs).

I had returned to writing my notes after running into a roadblock for 
[./src/mnemosyne/.../functions.rs](./src/mnemosyne/src/modules/static_analyzer/functions.rs),
only to find myself realizing some saddening truths that made it difficult for me to progress forward.


## Shortcomings
I was not able to reach the quota of 10 unique notes, however each note that I do argue that what I have 
in my collection accounts for 2-notes per note due to the quality of the analysis and research done in
each note. I have tried to give handwritten direct code examples of how I would write something in C, and
how I would write it in Rust, and then doing some analysis of my own that isn't really explored in any of 
the sources that I have found on the topic.

It's very hard to find papers on directly translating C-to-Rust without it speaking of AI-based capabilities,
and that's with good reason. As it would turn out, translating C-to-Rust without the use of AI will be extremely
difficult-- and that's because AI can partially reason out certain abstract principles that Rust provides that
simply just does not exist in the C language. While disheartening that it isn't possible to be able to just rely
on pure static analysis for transliteration comes with a silver-lining. The researchers looking to achieve memory-safe
Rust using AI are making tremendous progress in making already existing C-to-Rust transpilers more efficient using AI
to parse the outputted code and making it memory safe, particularly with SpeC2Rust, which has seen tremendous output
by reducing the amount of generated unsafe Rust to 0%. 

## Going Forward
From this point on, I think that my paper will solely focus on why the language is as powerful as it is-- what makes it
so powerful and disclose what contributions I have made towards finding a solution to translating C-to-Rust. While I am
saddened that I was not able to make a working transliteration process possible with it, I can at the very least discuss
what my initial approach was, and how I was planning on writing the process.

