package main
import "fmt"

func main() {
  var n,x int
  fmt.Scan(&n,&x)
  
  ans := "No"
  
  var a int
  
  for i:=0;i<n;i++ {
    fmt.Scan(&a)
    if a == x {
      ans = "Yes"
    }
  }
  fmt.Println(ans)
}