package main
import "fmt"

func main() {
  a := make([]int, 10)
  for i:=0; i<10; i++ {
    fmt.Scan(&a[i])
  }
  fmt.Println(a[a[a[0]]])
}