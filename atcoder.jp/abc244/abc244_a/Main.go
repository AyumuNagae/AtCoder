package main
import "fmt"

func main() {
	var n int
	var s string
	fmt.Scan(&n, &s)
	fmt.Println(s[n-1:])
}
