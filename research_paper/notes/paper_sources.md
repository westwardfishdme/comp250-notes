# Organization of Sources and Previous Research

**Date:** 11-3-2026
**Keywords:**
Research Paper, Sourcing, Synthesizing Information, Organization, C-to-Rust

While conducting further research, I have found more research not only related to my topic, but 
similar if not identical implementations of what I wish to achieve with my project, as well as
recent metrics related to the performance of converted C projects to Rust.
Further more, I have taken the extra step to separate the topics among 4 specific groups:

## 1. Papers that cover the linguistic and semantic issues that arise when translating to Rust.
- Hong, Jaemin, and Sukyoung Ryu. “Don’t Write, but Return: Replacing Output Parameters with Algebraic Data Types in C-to-Rust Translation.” Proc. ACM Program. Lang. 8, no. PLDI (2024): 176:716-176:740. https://doi.org/10.1145/3656406.
- Hong, Jaemin, and Sukyoung Ryu. “Automatically Translating C to Rust – Communications of the ACM.” Communications of the ACM 68, no. 11 (2025): 56–65. https://doi.org/10.1145/3737696.
- Lei Xia, Baojiian Hua, and Zhiyuan Peng. An Empirical Study of C to Rust Transpilers. April 27, 2023. https://doi.org/10.5281/ZENODO.7871547.
- NDSS Symposium. NDSS 2025 - Translating C To Rust: Lessons from a User Study. With guest Prateek Saxena. With Ruishi Li, Bo Wang, and Ashish Kundu. 2025. Presentation, 15:27. https://www.youtube.com/watch?v=ElQs8rNjFzk.

The research above covers all potential issues among the actual creation of valid Rust code and some tradeoffs that have to be made towards code 'correctness'; as in measurement of behaviorial changes
when converting C projects to Rust. The importance of this section is to precisely determine where issues may arise when attempting to deal with idiomatic C code and how that proves to be an issue when
translating to a language like Rust where these idiomatic styles fail the Borrow Checker.

## 2. Benchmark performance and impacts of translating C projects to Rust.
- “Translating All C To Rust (TRACTOR) Benchmarks | MIT Lincoln Laboratory.” Accessed October 21, 2026. https://www.ll.mit.edu/r-d/projects/translating-all-c-rust-tractor-benchmarks.
- Sirlanci, Melih, Carter Yagemann, and Zhiqiang Lin. “C2RUST-BENCH: A Minimized, Representative Dataset for C-to-Rust Transpilation Evaluation.” arXiv:2504.15144. Preprint, arXiv, April 21, 2025. https://doi.org/10.48550/arXiv.2504.15144.
- Yao, Junjie, Xiongzheng Guan, Jia Feng, Yujia Chen, Hongliang Tian, and Cuiyun Gao. “SpeC2Rust: Specification-Driven Repository-Level C-to-Rust Translation.” Version 1. Preprint, arXiv, October 27, 2026. https://doi.org/10.48550/ARXIV.2610.34141.

The research above explores empirical analysis of the raw performance of C to Rust translations; __however what is missing is compilation performance__ which does need further exploration.
These benchmarks will be useful in analyzing and understanding the runtime performance of direct C to Rust translations during tests.

## 3. Security implications of undefined behavior in C projects that pose real threats to the use of C in large codebases 
- Bob Lord. The Urgent Need for Memory Safety in Software Products | CISA. September 20, 2023. https://www.cisa.gov/news-events/news/urgent-need-memory-safety-software-products.
- DARPA. “TRACTOR | DARPA.” 2024. https://www.darpa.mil/research/programs/translating-all-c-to-rust.
- DARPAtv. TRACTOR Proposers Day Presentations. 2024. 01:13:52. https://www.youtube.com/watch?v=p-ktEmoKo78.
- Stoep, Jeff Vander. “Rust in Android: Move Fast and Fix Things.” Google, November 13, 2025. https://blog.google/security/rust-in-android-move-fast-fix-things/.

The reserarch and project proposals above explore why a language like Rust is necessary for systems level programming, and where the selection of languages C/C++
can prove to be a hazardous choice for software reliability. The importance of this section is to justify why a project needs to exist to
convert legacy C projects over to Rust in scale.

## 4. Open Source repositories and standards
- “Rust Reference for 1.95.” Accessed October 21, 2026. https://doc.rust-lang.org/1.95.0/reference/.
- “Immunant/C2rust: Migrate C Code to Rust.” Accessed October 21, 2026. https://github.com/immunant/c2rust/tree/master.
- “Rs2c - Rust.” Accessed October 21, 2026. https://docs.rs/rs2c/latest/rs2c/.
- Steve Klabnik, Carol Nichols, and Chris Krycho. The Rust Programming Language. 3rd ed. With Rust Community. No Starch Press, 2026. https://doc.rust-lang.org/stable/book/.
- ISO9899- C99 standard

The sources above are standards and open-source code repositories that are mentioned in some of the papers above; included for 
in-depth analysis and inspiration as I approach towards a working implementation, and to explore the semantical issues as described in
[section 1](#1.-Papers-that-cover-the-linguistic-and-semantic-issues-that-arise-when-translating-to-Rust.).
