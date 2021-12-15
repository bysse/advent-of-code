package main

import (
	"container/heap"
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
)

func readData(day int) ([]int, int) {
	data, err := ioutil.ReadFile("../input/input" + strconv.Itoa(day) + ".txt")
	//data, err := ioutil.ReadFile("../input/test.txt")
	if err != nil {
		panic(err)
	}

	var i = 0
	field := make([]int, 0)
	for _, ch := range data {
		if ch == ' ' || ch == '\n' || ch == '\r' {
			continue
		}
		field = append(field, int(ch)-int('0'))
		i++
	}
	return field, int(math.Sqrt(float64(len(field))))
}

func scale(tile []int, size, scale int) ([]int, int) {
	field := make([]int, (scale*size)*(scale*size))

	for i := 0; i < scale; i++ {
		for y := 0; y < size; y++ {
			write := y*(scale*size) + i*size
			read := y * size
			for j := 0; j < size; j++ {
				value := tile[read+j] + i
				if value > 9 {
					value -= 9
				}
				field[write+j] = value
			}
		}
	}

	chunk := (scale * size) * size

	for i := 1; i < scale; i++ {
		offset := i * chunk
		for j := 0; j < chunk; j++ {
			value := field[j] + i
			if value > 9 {
				value -= 9
			}
			field[offset+j] = value
		}
	}

	return field, size * scale
}

func dump(field []int, size int) {
	i := 0
	for y := 0; y < size; y++ {
		for x := 0; x < size; x++ {
			fmt.Print(field[i])
			i += 1
		}
		fmt.Println("")
	}
}

func search(field []int, size int) int {
	frontier := make(CoordHeap, 1, 1000000)
	visited := make(map[coord]int)

	heap.Push(&frontier, coord{0, 0, 0})
	visited[coord{0, 0, 0}] = 0

	delta := [4][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	for {
		if frontier.Len() == 0 {
			break
		}
		pos := heap.Pop(&frontier).(coord)

		if pos.x == size-1 && pos.y == size-1 {
			return pos.z
		}

		for _, d := range delta {
			x := pos.x + d[0]
			y := pos.y + d[1]
			if x < 0 || y < 0 || x >= size || y >= size {
				continue
			}

			r := field[x+y*size]
			np := coord{x, y, pos.z + r}

			if val, ok := visited[coord{x, y, 0}]; ok {
				if val <= np.z {
					continue
				}
			}
			visited[coord{x, y, 0}] = np.z
			heap.Push(&frontier, np)
		}

	}

	return 0
}

func main() {
	tile, tileSize := readData(15)
	fmt.Println("A:", search(tile, tileSize))

	field, size := scale(tile, tileSize, 5)
	fmt.Println("B:", search(field, size))
}

type coord struct {
	x int
	y int
	z int
}

type CoordHeap []coord

func (h CoordHeap) Len() int           { return len(h) }
func (h CoordHeap) Less(i, j int) bool { return h[i].z < h[j].z }
func (h CoordHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *CoordHeap) Push(x interface{}) {
	*h = append(*h, x.(coord))
}

func (h *CoordHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
