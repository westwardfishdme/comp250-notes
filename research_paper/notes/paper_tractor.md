# Notes on the TRACTOR project

**Date:** 10-26-2026
**Keywords:**
DARPA, TRACTOR, Rust


# Vision
- Translate C to Rust: permanently remove memory vulnerabilities.

## Gemini example provided; (with additional commentary by me on what it's doing)
Below are a few code blocks with additional annotations by me
containing information on [an early example of Rust's strengths compared to C 
written by the presenter](https://youtu.be/p-ktEmoKo78?si=7MJbLKhD_z29Q0-S&t=756):

```c

int main(int argc, char **argv){
  /* 
  there is already an off-by-one error
  since the string to be compared is
  's3cr8tpw\0' with a trailing NUL 
  terminator that will overflow the buffer
  even if the input is 'correct'.
  */
  char buff[8];
  int success = 0;

  // vulnerable code block
  strcpy(buff, argv[1]);
  /* 
  Vulnerable for 2 reasons:
  1: There is no guarantee that argv[1]
  will exist; therefore it will result

  2: strcpy is known for security vulnerabilities 
  violating several memory security principles.

  If a user provided a string that is longer than the 
  declared 8 bytes, then the buffer will
  overflow.
  */

  if (!strcmp(buff, "s3cr8tpw")) {
    
    success = 1;
  }

  if(success){
    printf("Welcome!\n");
  }
}
```
The code above is valid C and rather weakly protected. More
often than not, novice C developers will write code like this
because it is easy to understand what is going on; there is no
need to deal with dynamically allocated memory blocks, the code
is straight-forward, and despite it's flaws-- compile.

Although the code is rather that of just an example; there is a real
implication meant here that feels rather underestimated. In a real-world
developer environment; mistakes like these will inevitably happen. More
often than not, writing code like this will be done by tenured and experienced
developers for the sake of time efficiency. Code needs to be shipped and there
isn't much time to go back and fix every minute detail-- as Donald Knuth put it:

> "Premature optimization is the root of all evil."

While this applies to algorithmic optimization, the statement remains applicable to 
addressing memory safety. C developers already need to deal with a lot more complexities 
outside of just developing the program itself; they have to deal with the language *itself*. 
What I mean by this is that more time is usually spent linking header files, building Makefiles, 
writing tests in other scripting languages because the language itself just lacks modern features 
since it's a language developed out of the 1970's. The reality is that not all C developers will
have time to return to address bugs until they occur in a production environment.

```rust
fn main(){
  
  /* 
    vulnerability removed as there is no
    buffer to fill; if the argument isn't
    provided, then we immediately return.
    this is done through Rust's Option<T>
    type with .nth(1), which acts as a 
    standing enumeration between None and Some<T>.
  */
  // &str type annotation added for readability.
  let password: &str = if let Some(arg) =args().nth(1){
    arg
  } else {
    return;
  };
  /

  if password == "s3cr8tpw"{
    // translate printf to the println! macro.
    println!("Welcome!");
  }
}
```
Written above is a code block in Rust by gemini (from the presenter); 
already two major vulnerabilities get addressed:

1. The `Option<T>` enumeration of the `password` variable prevents any
input that is missing the argument from enumerating, and safely returns
should `argv[1]` not exist. 
2. the string slice (or `&str`) type [automatically allocates the exact space 
of the string](https://doc.rust-lang.org/nightly/reference/types/str.html) as dynamically sized
and prevents any off-by-one errors from occurring.
3. In addition Rust's type system is contracted by the borrow checker; meaning that a variable or 
symbol must remain as it's type for the remainder of it's lifetime-- or the compiler will throw 
an error at compile time.

At the end of the example, the presenter asks:
> "[*The code it provides is great*], but can we do this at scale?"

The answer provided is what this paper aims to achieve: 
> Achievement of successfully translating C to Rust by the use of static analysis.

While the AI portion is not of particular interest for this paper; It is highly probable that future
implementations will need to use generative AI to recreate the variable naming schema that Gemini created.
As the TRACTOR project proposes, a combination of generative AI and traditional static code analysis will be
necessary to recreate readable code as if it was naturally written. As for my implementation; symbols and variables
will either be directly transcribed, OR assigned a name dependent on variable lifetime.
