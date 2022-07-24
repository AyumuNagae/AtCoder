from math import gcd
a,b,c = map(int, input().split())
s = gcd(a,b)
s = gcd(s,c)
print(a//s + b//s + c//s -3)