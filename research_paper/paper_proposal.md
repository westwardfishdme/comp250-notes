# Paper Proposal

**Date:** 10-15-2026
**Keywords:**
Assignment, Research Paper, Research Writing, Overview

# Summary
This document outlines Finch's Research Project Proposal and serves as his introduction 
to what technology, and methodology was used in order to conduct the research.

# Part 1: Topic, Question, and Problem
Since the creation of C and the modern computing environment in the 1970's, a large issue 
that has plagued the world of system's level programming has been the process of manual 
memory management. While C provided a higher-level of abstraction and fulfilled the
growing desire for a more readable and portable language, the compiler lacks any regard
to memory safety. 

This has allowed code containing explicit undefined behavior to slip past the 
compiler. Such vulnerable code can cause massive disruption to systems including
security incidents, system outages, and buggy code; which can bring entire industries 
screeching to a halt.

## History
In 2025, the industry norm for memory vulnerabilities stood at a 
[70% of all reported vulnerabilities](https://blog.google/security/rust-in-android-move-fast-fix-things/)(Stoep, 2025).
In the same year, the Defense Advanced Research Projects Agency (DARPA) announced their **TRACTOR** project;
an acronym for "**Tr**anslating **A**ll **C TO R**ust. Their goal was to eliminate vulnerable C code by translating
it into Rust, which has stricter compile-time guidelines when it comes to memory safety.

## Goal
The goal of this paper is to conduct research into what makes Rust a strong replacement for 
C in comparison to other languages with built-in memory management systems, as well as address
some shortcomings of Rust that pose themselves as issues for creating direct C translations. 

In addition, this paper also aims to explore other research and projects seeking similar if not
the same goal of transpiling C to Rust. 

Since the scope of this project's development is limited by time constraints; Therefore it is likely
I will only to produce something that directly translates *very* rudimentary C
source code for a single file to get a functional prototype. Therefore, in order 
to maximize the effectiveness of the research conducted, the code will be published 
under the GNU Public License 2.0.

# Part 2: Process
For this project I will be writing the paper in markdown and LaTeX, pandoc will also be used to convert it to LaTeX, 
and the bibliography in Zotero. [All papers will be in this directory](./) and the source code will be inside [./src](./src).
The program will be written in Rust 1.95 with cargo, a sample program written in C will also be provided and tested against the 
generated Rust program using python 3.14. Other similar implementations will be tested in the same manner using the same valid
C program. Another C file containing undefined behavior will also be tested against with both my implementation and other
implementations to both refine my program and to test comparative metrics.

Below are some sources I will be using to perform my research:
- [Quick introduction to TRACTOR](https://www.youtube.com/watch?v=p-ktEmoKo78)
- [DARPA's official TRACTOR page](https://www.darpa.mil/research/programs/translating-all-c-to-rust)
- [MIT's Lincoln Labs' sample implementation of TRACTOR](https://www.ll.mit.edu/r-d/projects/translating-all-c-rust-tractor-benchmarks)
- [Github repository of TRACTOR](https://github.com/DARPA-TRACTOR-Program)
- [Rust-to-C transpiler (rs2c) library crate](https://docs.rs/rs2c/latest/rs2c/)
- [C-to Rust Transpiler (c2rust) library crate ](https://github.com/immunant/c2rust/blob/master/README.md)
- [ACM's research on a c2rust transpiler using LLM's + static analysis](https://cacm.acm.org/research/automatically-translating-c-to-rust/)
