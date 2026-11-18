# Issues When Attempting to Transpile C to Rust

**Date:** 11-17-2026
**Keywords:**
Research Paper, C-to-Rust, Syntax, Transpiling

[Researchers at the University of Science and Technology China](https://csslab-ustc.github.io/publications/2023/rust-transpiler.pdf) pointed out
some specific issues when it comes to transpiling C to Rust. The following 3 issues are issues that the researchers
found:

- Language Discrepencies
- Safety Guarantees
- Idiomatic writing styles of both languages.

## Language Discrepencies
This in short accounts for the languages' syntax, but I also propose that it should account for the idiomatic
writing styles as these two ideas are interconnected by principle of semantics. 

As mentioned in [my other notes on exploring lifetimes](./paper_lifetimes.md), there are a ton of
issues that arise when attempting to transliterate C to Rust due to the many, many ways to achieve
the same goal. However, one oversight I did not account for in that collection of notes was the idea 
of language specific behavior in C that just simply does not exist in Rust; 

### The go-to statement
Researchers particularly point out C's use of `goto` statements, which are specifically unique to the C/C++
languages. In Rust, there is no such thing as a `goto` statement; and for good reason. Rust wants to maintain 
the structured programming principles in it's philosophy of making code safe and maintainable. 

### Object Oriented Programming principles without being an OOP language
Both C and Rust write code in manners that are very specific to their design philosophy and principles of their
linguistic ecosystems. Rust in particular has object oriented-like syntax without actually being an OOP language. This is
because the language itself does not have inheritence or a lot of OOP based principles. It does provide it's own ways
to achieving polymorphism, abstractions, etc. However this is done through it's generics and traits system that works
independently of the OOP-based mechanics that most programmers are traditionally used to.

This makes it difficult for translating C, because this is unique to Rust; and provides a layer of abstraction that C would
not be able to handle well being it's a strictly a procedural language. Therefore, in order to make a successful 
transpilation that builds off of these specific idiomatic principles would require time and effort into trying to understand 
what are the key ideas and points that drive such abstractions to begin with.

Take the following code block in C for example: 

```c
int main(void) {
    const size_t buf_size = 16;
    const size_t init = 0;
    size_t buf[buf_size];
    // calculate perfect squares from 0-15
    for (size_t i = 0; i < buf_size; i++) {
      size_t value = init;
      value += i;
      value *= value;
      buf[i] = value;
    }
}
```

The equivalent code in Rust could look something like this:

```rust
fn main() {
    //! calculate perfect squares and store them into a statically
    //! sized buffer.
    const BUF_SIZE: usize = 16;
    let mut buf: [usize; BUF_SIZE] = [0; BUF_SIZE];
    /* iterate through and up to this point */
    for i in 0..BUF_SIZE{
      let mut value = buf[i];
      value += i;
      value *= value;
      buf[i] = value;
    }
}
```

Or alternatively (and how I would also personally write this) is by using the `into_iter()` method:

```rust 
fn main() {
  //! calculate perfect squares and store them into a statically
  //! sized buffer.
    const BUF_SIZE: usize = 16;
    let mut buf: [usize; BUF_SIZE] = [0; BUF_SIZE];
    /* use the iter method instead */
    buf.into_iter().enumerate().for_each(|(i, mut v)| {
        v += i;
        v *= v;
        buf[i] = v
    });
}
```
> The key point here is that there are multiple ways to essentially represent the same concepts with levels of abstraction in between.

Not to mention certain missing ideas such as the concept of `NULL`, which does not exist in Rust.
Although `NULL` is just a void pointer to 0, this does not exist in Rust. Instead, Rust uses the
`Option<T>` enum, which enumerates a value between `Some(T)` or `None`.

Lets look at how this might look in C:

```c
#include <stdlib.h>
// check if a pointer contains null. returns 1 if true,
// 0 if false.
int check_null(void *number) {
    if (number == NULL) {
      return 1;
    }
    return 0;
}

// create a pointer to null, and return the result
// of check_null.
int main(void) {
    void *x = NULL;
    int result = 0;
    result = check_null(x);
    return result;
}
```

Already this causes issues in Rust because there are no pointers to begin with, so there is no
direct way to make this work as intended, in addition we have to make the additional steps of
exiting with a value that represents the faulty return in the C version:

```rust
fn check_none(t: Option<usize>) -> bool {
    t != None
}

fn main(){
    let t: Option<usize> = None;
    let result= check_none(t);
    let mut exit_status=0;

    if !result {
      exit_status = 1;
    }
    std::process::exit(exit_status)
}
```
Which can be reduced to:
```rust
fn main(){
    let t: Option<usize> = None;
    let mut exit_status=0;
    if t.is_none() {
      exit_status = 1;
    }
    std::process::exit(exit_status)
}
```
So the question then becomes how do we deal with pointers? 
There is no safe way to do this in Rust without making calls to unsafe functions.

## Safety
C allows unsafe code to compile while Rust doesn't. However it is unknown how to make a safe guarantee that something
can compile going from one language to the other because of certain guarantees that either compilers make or lack. 
For example, Rust makes specific guarantees pre-compilation of static sized variables that cannot be made in C.

Take the example of the buffer I made earlier:

```c
int main(void) {
    const size_t buf_size = 16;
    const size_t init = 0;
    size_t buf[buf_size];
    // calculate perfect squares from 0-15
    for (size_t i = 0; i < buf_size; i++) {
      size_t value = init;
      value += i;
      value *= value;
      buf[i] = value;
    }
}
```

### Strings and buffers
In C (and all languages that inherit certain properties of C); C terminates all strings with byte 0-- denoted as `\0` and anthropically
labelled as the `NUL` terminator, which tells C where a string ends. In the code snippet above, we actually overflow the string buffer with 
the hidden `\0` at an address space that our buffer does not known.

This is known as an "off-by one" error and is [exploitable undefined behavior as defined by CWE-193](https://cwe.mitre.org/data/definitions/193.html).

While the code above is safe; the use of buffers generally can be a bit difficult for the unexperienced developer to navigate around.
This is most visible in strings which include the `Nul` terminator at the end of the string to indicate the termination of a string.

```c
#include <stddef.h>
#include <stdio.h>
#include <string.h>
int main(void) {
    char string[11]; //  hello world = 11 chars (12 if counting \0)

    char *to_copy = "Hello World"; // real len = 12
    for (size_t i = 0; i < strlen(to_copy); i++) {
        // copies the contents of to_copy into string
        string[i] = to_copy[i];
    }

    printf("%s\n", string);
}
```

This will print "Hello World", however what is not accounted for in the variable `to_copy` is the `\0` character at the very end that is
unseen. This won't cause the program to crash-- however whatever was at the address after the end of string[11] now
is filled with a `NUL` character.

Something like this is not possible in Rust; because of the extremely strong type system and specifically the multiple
different types of strings that are accessible just in the standard library alone.

```rust
fn main(){
    let mut string = String::new();
    let to_copy: &str ="Hello World";

    // split into character by character
    // and copy into string
    for i in to_copy.chars(){
      string.push(i);
    }
}
```
even more abstract:
```rust
fn main(){
    let to_copy: &str = "Hello World";
    let mut string = String::from(to_copy);
    println!("{string}")
}
```

# Conclusive thoughts
There are tons of extremely difficulties when translating C to Rust; and this has to do
with design choices that we are making-- and why many researchers opt to use AI for producing
the Rust code; because there are too many probable and correct ways to write C code into rust
that produce identical looking output, but operate completely differently the deeper we dive into 
their implementation details.

AI resolves this because it chooses based on training data from Rust developers, and feedback from
the compiler. (which is not covered yet, but is the next topic I will be writing about)
