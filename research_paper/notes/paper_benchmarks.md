# paper_benchmarks
**Date:** 11-17-2026
**Keywords:**
Research Paper, C-to-Rust, Benchmarking

For the bemchmarking portion of my analysis; I have broke it up into 3 distinct categories:

1. Analyzing run-time performance.
2. Analyzing time of compilation.

## Why does compilation time matter?
Although it is not as important as the run-time performance of the actual software,
the compilation process is an underrated metric in most of the papers that I have sourced.

The reason why I wish to include metrics on this is because Rust is notorious for having
excessively long compile times because everything is statically built. Most C projects
rely on dynamic linking-- meaning that code libraries are called rather than be built
into the binary since it can cause unnecessary bloating of the outputted binary.

While this might not matter for projects that are using 'one-shot' functions,
code that is dependent on DRY principles will prefer to use dynamic linking since
these particular functions serve purpose across several different programs.

