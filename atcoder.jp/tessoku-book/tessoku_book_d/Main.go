package main
import "fmt"

func main() {
  var n int
  fmt.Scan(&n)
  for i:=9;i>=0;i--{fmt.Print(n / (1<<i) %2)}
}