CC= time gcc
RUSTC = time rustc
CC_FLAGS= -std=c99 -O3
SRC= ./src

clean:
	rm -f main
	rm -f rusty_main

benchmark:
	$(RUSTC) $(SRC)/main.rs -o rusty_main;
	$(CC) $(CC_FLAGS) $(SRC)/main.c -o main;
