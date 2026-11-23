# Lexical Analysis
**Date:** 10-8-2026, revised 11-23-2026
**Keywords:**
Analysis, Lexer, Compiling, Research Writing, Research Paper

Lexical Analysis is the first step in compiling source code that takes in
a token stream and searches for keywords within source code. More on this later.

# Significance to Project:
The idea of using lexical analysis is to be able to essentially perform the process of rewriting 
C code to a language like Rust. Essentially creating bindings to Rust data structures from the C 
programming language.

## Type systems
In C there are only a few types in comparison to Rust. Sizes are implementation defined,
but are defined by using the GNU C Compiler @ 64-bits:
### Signed
- `char` (signed 8-bit integer)
- `short int` (signed 16-bit integer)
- `int` (signed 32-bit integer)
- `long int` (signed 64-bit integer)
- `long long int` (signed 64-bit integer)
### Unsigned
- `unsigned char` (unsigned 8-bit integer) 
- `unsigned short int` (unsigned 16-bit integer)
- `unsigned int` (unsigned 32-bit integer)
- `unsigned long int / unsigned long` (unsigned 64-bit integer)
- `unsigned long long int/ unsigned long long` (unsigned 64-bit integer)
- `size_t` (implementation defined)

### Floating Point integers 
- `float` (32-bit floating point number)
- `double` (64-bit floating point number)
- `long double` (128-bit floating point number)

In addition, C has pointer-based structures known as **buffers**, which can store
any value of the above types into a statically allocated array on the stack contiguously.
Alternatively, you can use the standard library `<stdlib.h>` to dynamically allocate values 
upon the heap using `malloc()`, `realloc()`, and `calloc()`.

# Rust Types
In contrast, Rust has many more types included in the Standard Library in comparison to the C programming
language. As a result, not all types can be directly translated over to Rust using the traditional methods 
due to the sheer 

Below is a list of primitive types that Rust uses along with their associated C types (C99 standard) if applicable:
## Scalar Types
### Signed Integers
- `i8`
> `char`/signed 8-bit integer
- `i16`
> `short int`/signed 16-bit integer
- `i32`
> `int`/signed 32-bit integer
- `i64`
> `long int`/`long long int`/signed 64-bit integer
- `i128`
- `isize` (architecture dependent)
### Unsigned Integers
- `u8`
> `unsigned char`/unsigned 8-bit integer
- `u16`
> `unsigned short int`/unsigned 16-bit integer
- `u32`
> `unsigned int`/unsigned 32-bit integer
- `u64`
> `unsigned long long int`/`unsigned long int`/unsigned 64-bit integer
- `u128`
- `usize` (architecture dependent)
> `size_t` (also architecture dependent)
### Character Type
- `char` (distinct from the C `char` type)
What makes char distinct from the C char type is that char must be defined
as a printable character in code and must be declared with single (`'`) quotation marks:

```rust
fn main(){
  let my_c:char = 'c';
  println!("{my_c}");
  let my_a:char = 'a';
  println!("{my_a}");
  let my_r:char = 'r';
  println!("{my_r}");
}
```
prints:
```
c
a
r
```
## Compound Types
- `Tuples`
- `Array`
> `Static Buffers in C`

## Collection Types
Below are a list of types that are defined as a part of the std::collections type which have no bindings in C,
and must be manually implemented
- `Vec<T>`
- `Hashmap<K,V>`


# Typecasting
Both languages allow type casting. Something interesting is that both languages support
casting into smaller types; However let us note some nuances:

I wrote the following code in Rust and annotated points of interest with comments:
```rust
/* main.rs */
fn test(a: u16) {
    let b: u16 = 12;

    let c = a + b;
    println!("value of c: {}", c) // POI 2
}

fn main() {
    let t: u64 = u64::MAX;
    println!("value of short cast: {}", t as u16); // POI 1
    test(t as u16);
}
```
> This will compile correctly, yet there is some incorrect behavior that exists,
Let's see how Rust handles it...

### POI 1: 
Let's start with casting to a smaller type within a `print` statement.
When we reach this point in execution, the program will just cast it to
the maximum of `u16`; which is 65535.

### POI 2:
This is where things get interesting, because the behavior changes depending on compiler options.
If you are compiling normally with the following compiler options:
```sh
rustc main.rs
```
The attempted addition into point c above this line will cause the program to crash.
However, if you are compiling with optimizations:
```sh
rustc -O main.rs #similar to gcc -O3 
```
The program will run and reach this point effortlessly. This is because the debug symbols when
compiling **without** the compiler option will detect that we are trying to fit a larger sized integer
(64 bits) into a smaller integer size (16-bits). However, with the optimizations enabled; Rust performs
two's compliment and wraps the number around to `u16::MAX`; giving the result 11 (number resets to 0).

We can view the exact same behavior in the C equivalent:
```c
#include <limits.h>
#include <stdio.h>

void test(unsigned short int a) {
  unsigned int b = 12;
  unsigned int c = a + b; // cast into smaller digit size...
  printf("value of c: %hu\n", c); // print the result
}

int main(void) {
  unsigned long long int x = ULLONG_MAX;
  printf("value of short cast: %hu\n", x);
  test(x);
}
```

With both programs outputting:

```
value of short cast: 65535
value of c: 11
```

# Rust specific complications
This section I talk about the specific complications that are difficult to deal with in transliterations,
particularly with the behavior of Rust.


## Variable mutability
Mutability just means that the variable can be changed. In Rust, we define a variable to be mutable with the
`mut` keyword, which allows a variable to change its value. In C, all variables are mutable.

An immutable variable differs from the `const` keyword in Rust because `const`s cannot be derived from 
variables, as these are compiled directly into the program.

For example:

```rust

const COOL_NUMBER: i32 = 123;
fn addcool(x:i32)-> i32{
    let y = x + 32;
    x + COOL_NUMBER + y
}
fn main(){
    let mut x = 2;
    x = addcool(x);
}
```
The number `123` is actually compiled into the program and cannot be changed at all; `const` keywords dictate a promise to the
compiler that the number will not be changed at any point during execution, and will remain the same value throughout.

## Implicit Returns
Unlike C, Rust does not require the `return` keyword when at the end of a function.
We can do this by just removing the semi-colon and returning an expression.

```rust
fn add2(x:i32)->i32{
    x + 2 // implicit return 
}

fn main(){
    let x = 21;
    let y = add2(x); // y = 23
}
```
A direct translation in C would be:
```c

int add2(int x){
    return x + 2;
}

int main(void){
    int x = 21;
    int y = add2(x); // y = 23
}
```
While this example is easy to understand, let's look at some more advanced Rust:
```rust
fn between_three_options(mut x:u8)-> u8{
    x += 1;
    match x{
        1=> 132,
        2=> 240,
        3=> 56,
        _=> 0,
    }
}

fn main(){
    let x = 2
    let y = 3
    let z = between_three_options(x); // z = 56
    let a = between_three_options(y); // a = 0
}
```
This code would be the equivalent of:

```C
#include <stdio.h>
unsigned char between_three_options(unsigned char x) {
    switch (x += 1) {
    case 1:
      return 132;
      break;
    case 2:
      return 240;
      break;
    case 3:
      return 56;
      break;
    default:
      return 0;
      break;
    }
}
int main(void) {
    unsigned char x = 2;
    unsigned char y = 3;
    unsigned char z = between_three_options(x);
    unsigned char a = between_three_options(y);
}
```

The code is nearly identical with the caveat of the implicit return type in Rust.
This is because the result of the match statement stores the value of the internal
enumeration after it has found it's 'match point' and it determines the value that is
returned; using a jump table to return the correct answer.

In C, we must use the `switch` statement which is the operates the exact same; however
we need to know when something is an explicit return because the answer must be enumerated within
that jump table-- or if the code needs to refer to the continuation of the program rather than explicitly
return an error-- which is where the problems arise.

### Explicit Errors
In C, you would have to determine what value is considered an "error value" and check externally from the function
whether that value is reached at any point. In Rust you can use the Result Enumeration:
```rust
use std::error::Error;

fn between_three_options(mut x:u8)-> Result<u8, &'static str>{
    x += 1;
    match x{
        1=> Err("Value is 3 numbers too low"),
        2=> Err("Value is 2 numbers too low"),
        3=> Err("Value is 1 numbers too low"),
        _=> Ok(0)
    }
}

fn main()-> Result<(), Box<dyn Error>>{
    let x: u8 = 0;
    let a = between_three_options(x)?; // would result in an error and exit with an error message.
    let b = between_three_options(5)?; // b would store Ok(0); but is unreachable.
    println!("b value= {}", b);
    
  Ok(())
}
```
Where as something like this in C would require more error handling:
```C
#include <stdio.h>
unsigned char between_three_options(unsigned char x) {
    switch (x += 1) {
    case 1:
      fprintf(stderr,"Value is 3 numbers too low")
      exit(1);
      break;
    case 2:
      fprintf(stderr,"Value is 2 numbers too low")
      exit(1);
      break;
    case 3:
      fprintf(stderr,"Value is 1 numbers too low")
      exit(1);
      break;
    default:
      return 0;
      break;
    }
}
int main(void) {
    unsigned char x = 0;
    unsigned char a = between_three_options(x);
    unsigned char b = between_three_options(5); // code is unreachable
}
```
Which is why implicit returns can be difficult to implement should we have to enumerate over
Result Types.
## Generics and Polymorphic Behavior
Generics are something that are exclusive to Rust, and are what allow it to perform polymorphic behavior.
The best way to exemplify this is with the `Vec<T>` type which create a struct of type `T` which is a generic.

For example, you can have `Vec<f64>`, or `Vec<u32>`, or even `Vec<Vec<u8>>`; This is because generics allow
different ways to implement the same functionality for different types, which is how Rust achieves 
**polymorphic behavior**. 

This is relevent to us mostly because it is way more difficult to implement polymorphic behavior in C,
but also because this is something that is unique to Rust and is something that cannot be determined how
to transliterate directly.

## Dealing with Structs
In both C and in Rust, you may define customized data structure types with the `struct`
keyword. Structs typically hold primitive types such as the all of the types above or another
`struct` value. However, a C struct and Rust struct both differ completely. The best way to
exemplify this is by analyzing how a struct works in Rust.

In Rust, structs demonstrate OOP-like principles in their design. As an example, I wrote
the following program to create a simple Cartesian Graph:
```rust 
use std::fmt::Display;
struct Point {
    pub x: f64,
    pub y: f64,
}
impl Point {
    pub fn new<T: Into<f64>, U: Into<f64>>(new_x: T, new_y: U) -> Point {
        //! creates a new point.
        Point {
            // we use generics to convert both x and y into f64 points.
            x: new_x.into(),
            y: new_y.into(),
        }
    }
    pub fn mid_point(&self, other_point: &Point) -> Point {
        //! calculate the mid point and return it as a new point.
        let mid_x = (self.x + other_point.x) / 2_f64;
        let mid_y = (self.y + other_point.y) / 2_f64;
        Point { x: mid_x, y: mid_y }
    }
}
/// Makes the point printable.
impl Display for Point {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}
fn main() {
    // since we use generics to convert it into an f64,
    // we can use integers instead of casting into 64-bit 
    // floating point numbers.
    let p1 = Point::new(-1, 2);
    let p2 = Point::new(3, 4);
    let p3 = p1.mid_point(&p2);

    println!("value of p1: {}", p1);
    println!("value of p2: {}", p2);
    println!("value of p3: {} # midpoint", p3);
}
```
We can see that this implementation does some relatively advanced things;
but what we're mostly focused on is the syntax used, particularly:
```rust
    //...
    let p3 = p1.mid_point(&p2);
    //...
```
This piece of code uses Rust's Object-Oriented like programming syntax to be able
to calculate and return the midpoint from the referenced 2nd point `p2` with the values
used for `p1` as defined in the function on line 15 (`mid_point(&self, other_point: &Point)-> Point`).

This type of syntax while possible in C, is extremely hard to reproduce-- as it would require using
pointers to functions in order to be able to call values. It would be much easier to write a function
that dictates how to calculate the midpoint as written in the my translated version below:
```c
#include <stdio.h>
#include <stdlib.h>
typedef struct Point {
  double x;
  double y;
} Point;

Point midpoint(Point *first_point, Point *second_point) {
  // calculate the midpoint
  double new_x = (first_point->x + second_point->x) / 2;
  double new_y = (first_point->y + second_point->y) / 2;
  Point midpoint = {new_x, new_y};
  return midpoint;
}

char *str_point(Point* point) {
  // print the string representation of a Point
  char *string = (char *)malloc(10 * sizeof(char));

  sprintf(string, "(%.2lf, %.2lf)", point->x, point->y);
  return string;
}

int main(void) {
  Point p1 = {-1, 2};
  Point p2 = {3, 4};
  Point p3 = midpoint(&p1, &p2);
  // get the string representations.
  char *p1_string = str_point(&p1);
  char *p2_string = str_point(&p2);
  char *p3_string = str_point(&p3);
  // print the values
  printf("value of p1: %s\n", p1_string);
  printf("value of p2: %s\n", p2_string);
  printf("value of p3: %s\n", p3_string);
  // free the strings...
  free(p1_string);
  free(p2_string);
  free(p3_string);

  return 0;
}
```
As we can observe in the code above, C doesn't really have much object-oriented principles implemented in the language;
with the exception of field accessors which were not implented in the program, but would look similar to:
```c
#include <stdio.h>
typedef struct Point {
    double x;
    double y;
} Point;
int main(void){
    Point p1 = {1, 2};
    printf("x: %lf, y: %lf", p1.x, p1.y);
}
```
## Unsafe Rust
Unsafe Rust is Rust that allows for the existence of contracts that the Rust compiler cannot check.
However, it does not mean that it can cause undefined behavior unlike C which will cause undefined behavior;
which is referred to by the Rust language as **soundness**.

Meaning that no matter what, we will always be able to remove undefined behavior.

## No pointers in Rust
As we see in the code above, pointers in C need to be translated into referenced variables
with types which defaulting to using a function is a little bit tedious when it comes to
heap allocated objects-- as we would need to perform unsafe Rust.

# Issues
This makes transliterating C to Rust difficult because of the following reasons:

1. Direct translations while correct, are just gross misrepresentations of the abstractions that Rust provides.
This is because `structs` in Rust are similar to C structs, but represent their own version of what a class is in object-oriented languages. 
The object-oriented like syntax of Rust makes it possible to have simplified versions of what C implementations define into their own object 
and thus deriving methods from derived functions can prove themselves to be difficult to translate.
2. Rust's generic system allows developers to build complex programs that exhibit polymorphic behavior that otherwise would be difficult to
translate from C.
3. Pointers make understanding what v

# Bibliography
- ISO/IEC. ISO/IEC 9899:1999. Second Edition. American National Standards Institute, Withdrawn 2004 December 1999. https://www.gwduan.com/web/computer/languages/c/c99.pdf.
- “Rust Reference for 1.95.” Accessed October 21, 2026. https://doc.rust-lang.org/1.95.0/reference/.
- Steve Klabnik, Carol Nichols, and Chris Krycho. The Rust Programming Language. 3rd ed. With Rust Community. No Starch Press, 2026. https://doc.rust-lang.org/stable/book/.
