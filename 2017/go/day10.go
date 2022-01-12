package main

import (
	"encoding/hex"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const bufferSize = 256

func hash(buffer *[]int, index int, length int) {
	if bufferSize == 256 {
		for i := 0; i < length/2; i++ {
			source := (index + i) & 0xff
			dest := (index + length - i - 1) & 0xff
			(*buffer)[dest], (*buffer)[source] = (*buffer)[source], (*buffer)[dest]
		}

	} else {
		for i := 0; i < length/2; i++ {
			source := (index + i) % bufferSize
			dest := (index + length - i - 1) % bufferSize
			(*buffer)[dest], (*buffer)[source] = (*buffer)[source], (*buffer)[dest]
		}
	}
}

func partA(data []byte) {
	selector := 0
	buffer := make([]int, bufferSize)

	for i := 0; i < bufferSize; i++ {
		buffer[i] = i
	}

	index := 0
	skip := 0

	for _, snum := range strings.Split(string(data), ",") {
		selector = 1 - selector
		length, _ := strconv.Atoi(snum)
		hash(&buffer, index, length)
		index = (index + length + skip) % bufferSize
		skip++
	}

	fmt.Println("A:", buffer[0]*buffer[1])
}

func partB(data []byte) {
	selector := 0
	buffer := make([]int, bufferSize)

	for i := 0; i < bufferSize; i++ {
		buffer[i] = i
	}

	sequences := data[:]
	sequences = append(sequences, []byte{17, 31, 73, 47, 23}...)

	index := 0
	skip := 0

	for round := 0; round < 64; round++ {
		for _, byteLen := range sequences {
			selector = 1 - selector
			length := int(byteLen)
			hash(&buffer, index, length)
			index = (index + length + skip) % bufferSize
			skip++
		}
	}

	output := make([]byte, 16)
	index = 0
	for i := 0; i < 16; i++ {
		value := buffer[index]
		index++
		for chunk := 1; chunk < 16; chunk++ {
			value = (value ^ buffer[index]) & 0xff
			index++
		}
		output[i] = byte(value)
	}

	fmt.Println("B:", hex.EncodeToString(output))
}

func main() {
	//data, err := os.ReadFile("../test.txt")
	data, err := os.ReadFile("../input-10.txt")
	if err != nil {
		panic(err)
	}

	partA(data)
	partB(data)
}
