day1: build/day1.o
	ld  -s build/day1.o -o day1

debug: build
	nasm -f elf64 -F dwarf -g -o build/debug.o day1.asm
	ld  build/debug.o -o debug

build/%.o: %.asm build
	nasm -f elf64 -o $@ $<

build:
	mkdir -p build

clean:
	rm -rf build day1
