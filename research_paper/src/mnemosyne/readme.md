# Mnemosyne
Mnemosyne is a C-to-Rust translator named after the Greek goddess
of memory. Mnemosyne can do basic static analysis of any given valid C 
file and an optional header file should you provide one.

## How it works
The way Mnemosyne works is by searching for keywords and symbols
to translate into Rust for example, the following function in C

```c
int main(int argc, char** argv){
  buff[10];

  for (int i=0; i<10; i++){
    printf("iteration %d", i);
    buff[i] = argc+i;
    printf("buff[%d] -> %d\n", i, argc+i);
  }
  
  return 0;
}
```

roughly translates to:

```rust
// import if main has 2 parameters for argc and argv
use std::env::args;
fn main(){

  // retain static buffer size.
  let mut buff:[usize; 10] = [0;10];

  // retain variable naming.
  let argc = args().len();
  //retain loop logic.
  for i in 0..10{
    print!("iteration {i}");
    buff[i] = argc+i;
    println!("buff{i} -> {}", argc+i);
  }
}

```

