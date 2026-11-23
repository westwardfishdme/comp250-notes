# Memory Safety

**Date:** 11-18-2026
**Keywords:**
Memory Safety, Purpose

The idea of key purpose of translating C projects into Rust is purely reasoned to
eliminating all C-related vulnerabilities in regards to manual memory management.

While C demonstrates the ability to write code with raw performance metrics in mind;
it is able to achieve this by optimizing itself to work directly with memory and provide
the programmer with a full kit of utilities to manage memory within their software as they see fit.

## Why memory safety is important

Memory safety is important because in the long history of industrialized computing, the power of C allowed
failures to occur in critical systems that require a baseline level of stability in order to functionally 
operate. Manual memory management allows users to recklessly write code without much thought put into their
implementations and thus creates this lack of awareness to any deeper understanding of what the code 
is actually doing. 

The consequences of this allows for what is called **undefined behavior** to slip into production codebases
and can cause any of the following vulnerabilities and problems to occur:

- Program crashes due to essential memory addresses.
- Potential leaks of sensitive information through mishandled user input.
- Remote code execution that provides threat actors leverage over a computer system.
- Inefficient memory allocation through memory leaks.
- Incorrect implementations that produce arbitrary/garbage information because of misread memory.

## How easy is it to fail manual memory management?

As described in my other notes on translating C to Rust; it is implicit within the context of writing
C that the user is confident that their implementations are correct, and that what ever code they write
abides by the set standard that the compiler is using. However; it is notoriously easy to provide bad
code to the compiler and still have a binary compile (bad in the sense that memory is handled improperly).

In the context of industry level software development; it is well-known that developers are expected to
develop products and features at fast speeds that allows for bad code to slip past experienced professional 
engineers and make their way into production. This can happen for any number of reasons, but likely 
because there are certain edge cases are not tested against that cause the undefined behavior to appear until
the given context happens. 

# Proposed Solutions
According to Bob Lord, a Senior Technical Advisor to the U.S. Cybersecurity & Infrastructure Security Agency (CISA),
one of the mitigations to violations on memory safety is to apply CISA's secure by design principles at the software
level. This means that instead of using a language that is prone to such memory vulnerabilities, companies and developers
should opt towards languages that implement this by abstracting memory management away.

This can be achieved in 2 different ways:

- Opt for using a language that handles memory though garbage collection.
- Opt for using Rust.

## Garbage collected languages
The process of garbage collection usually involves translating source code into byte code through an interpreter
which has to run separately on invocation. A great example of this is actually with Java as it uses the JVM 
(Java Virtual Machine) to check when an object was last used and then deallocates it after it is no longer needed.

## What makes Rust different
Rust allegedly operates at the same speed as C/C++ and abstracts the concept of managing memory away.
It achieves this in contrast to other garbage collected languages by implementing **zero-cost abstractions**
through the borrow checker rather than an additional garbage collector which adds additional performance overhead.

Rust hasn't seen widespread adoption, but has been adopted into several FAANG companies and even into the Linux
Kernel in version 6.8; Linux prior was solely written in C/C++ up until this point.

### How Rust has already fixed vulnerabilities and changed the game
In 2025, Google released a report that explored how Rust **decreased memory based vulnerabilities by a 1000x; or a relative 100,000%**
as well as a **4x lower rollback rate** and **25% reduction in time spent on code review**. Not only does it solve the original
problem of memory vulnerabilities, but we see it fits well into the **software development life cycle**. It is also notable that
the language has brought the industry norm of 70% memory-safety vulnerabilities down to 20%.


<!--
NOTE:
Personal Anecdote:
I have been writing Rust for the past 3 years, prior to which I would write projects in C, Bash, or python.
Rust is the only language with a comfortable enough ecosystem that makes developing performant software easy
without having to deal with manual memory management; or having to make arcane optimizations to my codebase
to shave off milliseconds of runtime (python specifically annoys me with this).
-->
# Bibliography
- “Rust Reference for 1.95.” Accessed October 21, 2026. https://doc.rust-lang.org/1.95.0/reference/.
- Steve Klabnik, Carol Nichols, and Chris Krycho. The Rust Programming Language. 3rd ed. With Rust Community. No Starch Press, 2026. https://doc.rust-lang.org/stable/book/.
- Stoep, Jeff Vander. “Rust in Android: Move Fast and Fix Things.” Google, November 13, 2025. https://blog.google/security/rust-in-android-move-fast-fix-things/.
