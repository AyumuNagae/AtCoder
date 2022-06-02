import functools
import math

def gcd(a,b):
  quotient=0;mod=0;
  while a%b!=0:
    quotient = a/b
    mod      = a%b
    a        = b
    b        = mod
  return(b)

n = int(input())
A_list = list(map(int, input().split()))
list_gcd = functools.reduce(gcd, A_list)
print(list_gcd)