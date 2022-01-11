package main

import (
	"fmt"
	"os"
)

func main() {
	data, err := os.ReadFile("../input-09.txt")
	//data, err := os.ReadFile("../test.txt")
	if err != nil {
		panic(err)
	}

	total := 0
	score := 0
	i := 0
	garbage := false
	skip := false
	gcCount := 0
	for i < len(data) {
		ch := data[i]

		if garbage {
			if skip {
				skip = false
			} else {
				switch ch {
				case '>':
					garbage = false
					skip = false
					break
				case '!':
					skip = true
					break
				default:
					gcCount++
				}
			}
		} else {

			switch ch {
			case '{':
				score++
				break
			case '}':
				total += score
				score--
				break
			case '<':
				garbage = true
				break

			}
		}

		i++
	}

	fmt.Println("A:", total)
	fmt.Println("B:", gcCount)
}
