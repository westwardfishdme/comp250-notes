#!/usr/bin/env bash

time rustc -O ./src/main.rs -o rs_main && rm -f rs_main
time gcc -std=c99 -O3 ./src/main.c -o c_main && rm -f c_main
