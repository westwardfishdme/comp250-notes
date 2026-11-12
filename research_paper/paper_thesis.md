# Thesis and Claim

**Date:** 11-11-2026
**Keywords:**
Research Paper, C-to-Rust, Thesis, Key Idea

## Thesis
In the 1970's C was the dominant language in the world of software development. It's high-level
semantics made accessing and manipulating memory accessible to many developers. This made it a strong choice 
over many of the other languages of the time in order to maximize both development speed and raw performance.
Although the language made it easier to develop software; developers often had to refer to dozens upon dozens
of chapters in the C standard in-order to develop without causing undefined behavior in their programs. 
This was due to the dangers that undefined behavior leaves in regards to the safety, security, and stability
of systems. This often took more time for developers to actually build stable software because of time that would
be spent debugging and ensuring that memory was managed effectively and efficiently.

This was addressed in other languages later on such as C++ and Java with methods such as RAII (Resource Acquistion Is Initialization)
and garbage collection respectively to name a few; However, C++ while being one of the few other languages that had a mixed 
approach when it comes to memory management still left room for undefined behavior to occur in critical infrastructure. 
Java being a garbage collected langauge on the other hand, leaves much performance overhead in order to ensure that memory is 
handled correctly within its JIT compiler (the JRE) although it a strong choice for many developers because of the language's
strengths in reliability and development time.

Today, the modern answer to balancing developer time, raw performance, and guaranteeing **memory safety** is 
Rust. Rust is a powerful general system's language that many other developers deem as *the* replacement for 
the C/C++ language for numerous reasons. The major reasons being the guaranteed memory safety with its 
zero-cost abstractions with the borrow-checker, it's strong standard library, and the easy-to-use build system 
and package manager `cargo`. The aim of this paper in particular is to demonstrate and explore possible methods 
in order to transpile C into safe Rust programmatically; with as minimal calls to unsafe Rust functions as possible.

