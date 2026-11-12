# Paper Storyboard

**Date:** 11-12-2026
**Keywords:**
Research Paper, C-to-Rust, Reference Points, Roadmap

This is just a simple roadmap to better organize how evidence and research will impact and pivot
through each section through my paper.


**Goal:** Prove why Rust is the strongest choice for replacing general purpose system's languages such as
C/C++ as opposed to other languages, and explore possible ways to transpile C to Rust; As well as see why
it is so difficult to translate C to a language like Rust.

> Keywords are in bold.

1. Introduce brief history of programming languages and proposed solutions
  - See what approaches previous developers have been taken to achieve memory safety. 
  - Explore how the **borrow checker** works in-depth, and display how easy it is
  to cause **undefined behavior** in C, and what makes it impossible to occur in Rust.
2. Summarize **__performance benchmarks__** between the languages.
3. Explore the linguistic differences between Rust and C that make **__transpiling difficult__**.
  - Summarize idiomatic features that make it difficult to transpile.
4. **Demonstrate** my theory and approach to implement a "working" transpiler.
