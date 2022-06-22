package main
import "fmt"
func main() {
	var a, b, k, c int
	fmt.Scan(&a, &b, &k)
	for a < b {
		a *= k
		c++
	}
	fmt.Println(c)
}