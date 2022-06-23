package main

import "fmt"

func main() {
	var h1, h2, h3, w1, w2, w3 int
	fmt.Scan(&h1, &h2, &h3, &w1, &w2, &w3)

	ans := 0
	if h1+h2+h3 != w1+w2+w3 {
		fmt.Println(ans)
	} else {
		for i := 1; i <= h1-2; i++ {
			for j := 1; i+j <= h1-1; j++ {
				for k := 1; i+k <= w1-1; k++ {
					for l := 1; j+l <= w2-1 && k+l <= h2-1; l++ {
						if h1-i-j+h2-k-l < w3 && w1+w2-i-j-k-l < h3 {
							ans++
						}
					}
				}
			}
		}
		fmt.Println(ans)
	}
}
