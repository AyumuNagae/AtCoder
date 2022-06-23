package main
import "fmt"
func main() {
	 var a, b, c, d int
	 fmt.Scan(&a, &b, &c, &d)
	 result := "Aoki"
	 if a * 60 + b <= c * 60 + d {result = "Takahashi"}
	 fmt.Println(result)
}