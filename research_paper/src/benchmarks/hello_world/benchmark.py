#!/usr/bin/env python3
"""
Benchmarking script. Uses output from makefile
to build and deconstruct bin.

Built for x86_64 GNU Make 4.4.1;
tested on zsh
"""
import sys
import os
import subprocess
import threading
import numpy
MAX_ITER = 10
MAX_THREADS = 5


class Time:
    """
    Data class that stores the numeric
    representations of the time values to be used
    by the `Data` class
    """

    def __init__(self, fmtstring: str):

        hours = 0
        minutes = 0
        seconds = 0.0
        self.__hours:   int = hours
        self.__minutes: int = minutes
        self.__seconds: float = seconds
        self.__parse(fmtstring)

    @property
    def seconds(self) -> float:
        """
        Gets the total amount of seconds
        """
        t_seconds = self.__seconds
        if self.__hours != 0:
            t_seconds += self.__hours*3600
        if self.__minutes != 0:
            t_seconds += self.__minutes*3600

        return t_seconds

    def __parse(self, data_string: bytes):
        """
        Parses the inputted string to get an accurate reading of time data.
        """
        tmp_string = []
        string = data_string.decode("utf-8")
        # in theory, this should pick up the decimal point too.
        for character in string:

            if character.isdecimal() or character == ".":
                tmp_string.append(character)
            else:
                match character:
                    case 'h':
                        self.__hours = int("".join(tmp_string))
                    case 'm':
                        self.__minutes = int("".join(tmp_string))
                    case 's':
                        self.__seconds = float("".join(tmp_string))
                    case _:
                        pass
                tmp_string = []

    def __str__(self):
        return f"Time(\n\t{
            self.__hours} hours\n\t{
            self.__minutes} minutes\n\t{
            self.__seconds} seconds\n)"


class Data:
    """
    API that stores the time values
    of real, kernel, and user time parsed
    from the compilation process.
    """

    def __init__(self,
                 real: str,
                 krnl: str,
                 user: str):
        self.__real:  Time = Time(real)
        self.__kernel: Time = Time(krnl)
        self.__user:  Time = Time(user)

    def real(self) -> Time:
        """
        Get the real time it took for compilation
        """
        return self.__real

    def kernel(self) -> Time:
        """
        Get the time the process spent in kernel space
        """
        return self.__kernel

    def user(self) -> Time:
        """
        Get the time the process spent in user space
        """
        return self.__user

    def csv(self, name: str) -> str:
        """
        Prints the output in csv format
        """
        try:
            with open(f"{name}.csv", 'r') as file:
                pass
            with open(f"{name}.csv", 'a') as file:
                file.write(f"{self.kernel().seconds},{
                           self.real().seconds},{self.user().seconds}\n")
        except FileNotFoundError:
            with open(f"{name}.csv", 'w') as file:
                file.write("kernel,real,user\n")
            with open(f"{name}.csv", 'a') as file:
                file.write(f"{self.kernel().seconds},{
                           self.real().seconds},{self.user().seconds}\n")

    def __repr__(self) -> str:
        return f"Data(\n{self.__real},\n{self.__kernel},\n{self.__user})"


def parse_compiler_output(time_output: list[str]) -> (Data, Data):
    """
    Parses the inputted string to create a data point.
    Assumes output is the following format:

    ```
    # Rust compilation stats
    real: 0h0m12s
    user: 0h0m1s
    sys: 0h0m4s
                # <- newline gets parsed into: b''
    # C compilation stats
    real: 0m09s
    user: 0m1s
    sys: 0m4s
    ```

    Returns a tuple of data points (CARGO_STATS, C_STATS)
    """
    idx = 0
    while idx < time_output.__len__():
        # gets the string value @idx
        string_value = time_output[idx]
        # switch between rust and c compiler data
        # should we get to the null byte, we know
        # we are getting data for the C data point.
        if string_value != b'':
            time_details = string_value.split(b',')
            match time_details[0]:
                case b'real':
                    r = time_details[1]
                case b'sys':
                    k = time_details[1]
                case b'user':
                    u = time_details[1]
        else:
            cargo_stats = Data(r, k, u)
        idx += 1
    gcc_stats = Data(r, k, u)

    cargo_stats.csv("cargo_stats")
    gcc_stats.csv("gcc_stats")

    return (cargo_stats, gcc_stats)


def compile() -> bytes:
    """
    Begins compiling the program.
    """
    # start the compilation process of both programs
    try:
        makeprocess = subprocess.check_output(
            ["./build.sh"], stderr=subprocess.STDOUT)
    except Exception as e:
        print(f"make ran into a problem: ({e})")
        os._exit(1)

    # format output correctly.
    output = makeprocess.strip().replace(b"\t", b",").split(b"\n")
    return output


def average(nums: list[float]) -> float:
    """
    Calculates the average.
    """
    return sum(nums)/nums.__len__()


# used when threading to store the results


class Results:
    RUST_KERNEL_TIMES = []
    RUST_USER_TIMES = []
    RUST_REAL_TIMES = []

    RUST_K_AVG = 0
    RUST_U_AVG = 0
    RUST_R_AVG = 0

    GCC_KERNEL_TIMES = []
    GCC_USER_TIMES = []
    GCC_REAL_TIMES = []

    GCC_K_AVG = 0
    GCC_U_AVG = 0
    GCC_R_AVG = 0

    def __init__(self):
        # for calculating data on rust compilation
        self.rust_kernel_time: float = 0
        self.rust_user_time: float = 0
        self.rust_real_time: float = 0
        # for calculating data on c compilation
        self.gcc_kernel_time: float = 0
        self.gcc_user_time: float = 0
        self.gcc_real_time: float = 0

    def append_to_global(self):
        """
        Used when running in thread.
        """
        Results.RUST_KERNEL_TIMES.append(self.rust_kernel_time)
        Results.RUST_USER_TIMES.append(self.rust_user_time)
        Results.RUST_REAL_TIMES.append(self.rust_real_time)

        Results.GCC_KERNEL_TIMES.append(self.gcc_kernel_time)
        Results.GCC_USER_TIMES.append(self.gcc_user_time)
        Results.GCC_REAL_TIMES.append(self.gcc_real_time)

    def average() -> str:
        """
        returns the results in string representation forma
        """
        assert len(Results.RUST_KERNEL_TIMES) == MAX_ITER
        Results.RUST_K_AVG = average(Results.RUST_KERNEL_TIMES)
        Results.RUST_U_AVG = average(Results.RUST_USER_TIMES)
        Results.RUST_R_AVG = average(Results.RUST_REAL_TIMES)

        Results.GCC_K_AVG = average(Results.GCC_KERNEL_TIMES)
        Results.GCC_U_AVG = average(Results.GCC_USER_TIMES)
        Results.GCC_R_AVG = average(Results.GCC_REAL_TIMES)

        string = f"Rust avgs:\n\treal: {
            Results.RUST_R_AVG:.5f}\n\tkernel: {
            Results.RUST_K_AVG:.5f}\n\tuser: {
            Results.RUST_U_AVG:.5f}"

        string += f"\nGCC avgs:\n\treal: {
            Results.GCC_R_AVG:.5f}\n\tkernel: {
            Results.GCC_K_AVG:.5f}\n\tuser: {
            Results.GCC_U_AVG:.5f}"
        return string

    def average_csv() -> str:
        """
        prints the results in a csv format
        """
        string = "rust kernel avg. time,"\
            + "rust user avg. time,"\
            + "rust real avg. time,"\
            + f"{Results.RUST_K_AVG},{Results.RUST_U_AVG},{Results.RUST_R_AVG}"

        return string

    def __repr__(self):
        return f"Result(\n\t{
            self.gcc_kernel_time}\n\t{
            self.gcc_real_time}\n\t{
            self.gcc_user_time}\nRUST\n\t{
            self.rust_kernel_time}\n\t{
            self.rust_real_time}\n\t{
            self.rust_user_time} "


def main(total_iters: int, forked=True) -> Results:
    """
    Benchmarks the compilation time.
    """
    rust_kernel_times: list[float] = []
    rust_user_times: list[float] = []
    rust_real_times: list[float] = []
    gcc_kernel_times: list[float] = []
    gcc_user_times: list[float] = []
    gcc_real_times: list[float] = []
    result = Results()

    for i in range(total_iters):
        if not forked:
            print(f"running iteration: {i+1}/{total_iters}", file=sys.stderr)
        output = compile()
        # begin parsing output to get numeric data:
        (cargo_data, gcc_data) = parse_compiler_output(output)
        if forked:
            # for rust
            result.rust_kernel_time = cargo_data.kernel().seconds
            result.rust_user_time = cargo_data.user().seconds
            result.rust_real_time = cargo_data.real().seconds
            # for gcc
            result.gcc_kernel_time = gcc_data.kernel().seconds
            result.gcc_user_time = gcc_data.user().seconds
            result.gcc_real_time = gcc_data.real().seconds
            result.append_to_global()
            return result
        else:
            rust_kernel_times.append(cargo_data.kernel().seconds)
            rust_user_times.append(cargo_data.user().seconds)
            rust_real_times.append(cargo_data.real().seconds)
            gcc_kernel_times.append(gcc_data.kernel().seconds)
            gcc_user_times.append(gcc_data.user().seconds)
            gcc_real_times.append(gcc_data.real().seconds)
    # get the averages

    rust_r_avg = average(rust_real_times)
    rust_k_avg = average(rust_kernel_times)
    rust_u_avg = average(rust_user_times)
    gcc_r_avg = average(gcc_real_times)
    gcc_k_avg = average(gcc_kernel_times)
    gcc_u_avg = average(gcc_user_times)
    print(f"total runs: {total_iters}")
    print(f"Rust avgs:\n\treal: {
        rust_r_avg:.5f}\n\tuser: {
        rust_u_avg:.5f}\n\tkernel: {
        rust_k_avg:.5f}")
    print(f"gcc avgs:\n\treal: {
        gcc_r_avg:.5f}\n\tuser: {
        gcc_u_avg:.5f}\n\tkernel: {
        gcc_k_avg:.5f}")


if __name__ == "__main__":
    print("Starting benchmark...", file=sys.stderr)
    args = sys.argv
    if args.__len__() == 1:
        print("you can pass the argument 'thread' as ./benchmark.py thread",
              "to run this task in multithreading mode.")
        main(MAX_ITER, False)
    else:
        if args[1].lower() == "thread":
            total_threads = []
            for i in range(MAX_ITER):
                t = threading.Thread(target=main, args=(
                    1,), kwargs={"forked": True})
                total_threads.append(t)

            # split into even chunks of max threads
            chunk_threads = numpy.array_split(
                total_threads, numpy.ceil(MAX_ITER/MAX_THREADS))

            results = []

            for threads in chunk_threads:
                for thread in threads:
                    thread.start()
                for thread in threads:
                    thread.join()

            print(Results.average())
