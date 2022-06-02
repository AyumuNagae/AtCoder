a,b=map(int, input().split())
quotient=0;mod=0;
while a%b!=0:
  quotient = a/b
  mod      = a%b
  a        = b
  b        = mod
print(b)