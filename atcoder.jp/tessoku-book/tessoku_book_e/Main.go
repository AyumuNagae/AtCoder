package main
import "fmt"

func main(){
  var n,k int
  fmt.Scan(&n, &k)
  var c int
  ans := 0
  for a := 1;a<=n;a++ {
    for b := 1;b<=n;b++ {
      c = k - a - b
      if c >= 1 && c <= n {ans+=1}
    }
  }
  fmt.Print(ans)
}