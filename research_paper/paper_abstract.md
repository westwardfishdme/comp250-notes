# Central Idea of Paper

**Date:** 10-12-2026
**Keywords:**
Research Paper, AI, Code Analysis, Objectives

The independent research that I wish to engage in for Comp250 is to perform
research on converting C to Rust by creating a lexer to perform basic syntax
conversions.

This file contains the central idea, abstract, and general ideas I have for testing
and implementing a direct translator from C to Rust.

# Abstract
In 2023, the Defense Advanced Research Projects Agency began research on a project
known as TRACTOR; short form for **TR**anslate **A**ll *(legacy)* **C** **To** 
**R**ust. The idea was to eliminate memory vulnerabilities overall in all software
using system's level languages, such as C, by utilizing Rust's Borrow Checker 
in order to catch memory bugs and vulnerabilities at compile-time. The general
idea was to use **large language models** to produce Rust source code similar of
that to a 'skilled Rust developer'.

While other transpilers currently exist in 2026 for Rust to C, and vice versa, 
the goal of this paper is to not only research on transpiling C to Rust, but 
testing proposed forms of static analysis as put forth by MIT researchers at
Lincoln Labs, researchers at the ACM, and other open source developers.

# Sources to Look At:
- https://www.youtube.com/watch?v=p-ktEmoKo78
- https://www.darpa.mil/research/programs/translating-all-c-to-rust
- https://www.ll.mit.edu/r-d/projects/translating-all-c-rust-tractor-benchmarks
- https://github.com/DARPA-TRACTOR-Program
- https://docs.rs/rs2c/latest/rs2c/
- https://github.com/immunant/c2rust/blob/master/README.md
- https://cacm.acm.org/research/automatically-translating-c-to-rust/
