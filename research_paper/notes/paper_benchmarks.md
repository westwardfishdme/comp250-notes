# paper_benchmarks
**Date:** 11-17-2026
**Keywords:**
Research Paper, C-to-Rust, Benchmarking

For the bemchmarking portion of my analysis; I have broke it up into 3 distinct categories:

1. Analyzing run-time performance.
2. Analyzing time of compilation.
3. Analyzing Memory Safety

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

## How do we analyze memory safety?
In some research performed by Researchers in Shenzhen, China-- they measured how memory safe
a piece of code was depending on the count of unsafe Rust functions were necessary in a traditional
transpiler C2Rust. Something like this will be extremely useful in measuring how useful it really is
to translate a project written in C over to Rust using memory-safe guarantees provided with Rust's Compiler.

# Bibliography

- Lei Xia, Baojiian Hua, and Zhiyuan Peng. An Empirical Study of C to Rust Transpilers. April 27, 2023. https://doi.org/10.5281/ZENODO.7871547.
- NDSS Symposium. NDSS 2025 - Translating C To Rust: Lessons from a User Study. With guest Prateek Saxena. With Ruishi Li, Bo Wang, and Ashish Kundu. 2025. Presentation, 15:27. https://www.youtube.com/watch?v=ElQs8rNjFzk.
- Sirlanci, Melih, Carter Yagemann, and Zhiqiang Lin. “C2RUST-BENCH: A Minimized, Representative Dataset for C-to-Rust Transpilation Evaluation.” arXiv:2504.15144. Preprint, arXiv, April 21, 2025. https://doi.org/10.48550/arXiv.2504.15144.
- Yao, Junjie, Xiongzheng Guan, Jia Feng, Yujia Chen, Hongliang Tian, and Cuiyun Gao. “SpeC2Rust: Specification-Driven Repository-Level C-to-Rust Translation.” Version 1. Preprint, arXiv, October 27, 2026. https://doi.org/10.48550/ARXIV.2610.34141.
