# Benchmarking
This directory covers the benchmarking of both C and Rust programs.

## Setup Details
This was tested on the following setup:
| CPU Model                         | Kernel      | Memory               |
|-----------------------------------|-------------|----------------------|
|AMD Ryzen 9 5900X 12-Core Processor|7.3.4-arch1-2|62.70 GiB DDR4-3200mhz|

 
## What is Tested
I tested for the following:
- Compilation Time
- Runtime benchmarks

These benchmarks are done in `benchmark.py` within each directory; which
use a subcommand call to **gnu-make**. I tested and wrote these scripts to
be specifically run on amd64 Linux/Unix based systems so be wary.

```sh 
time make -s benchmark
```

|Test Name              | written? | completed? | compile bench | runtime bench |
|-----------------------|----------|------------|---------------|---------------|
| Hello World           | yes      | partial    | yes           | no            |
| Headers and modules   | no       | no         | no            | no            |

# NOTE/KNOWN ISSUES
- `./benchmark.py thread` does not account for the CPU time increase for running each particular threads; This causes
the 'real' time to spike dramatically when running for each thread as it is accounting for CPU time and not the real time
elapsed.
