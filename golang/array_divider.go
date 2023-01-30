package main

import "fmt"

func main() {
	arr := []string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"}
	fmt.Println(array_divider(5, arr))
}

func array_divider(count_sublist int, data []string) [][]string {
	var result [][]string
	var subres []string

	for i := 0; i < len(data); i++ {
		subres = append(subres, data[i])

		if (i+1)%count_sublist == 0 {
			result = append(result, subres)
			subres = subres[:0]
		}
	}

	if len(subres) > 0 {
		result = append(result, subres)
	}

	return result
}
