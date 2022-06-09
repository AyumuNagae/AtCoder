n=int(input())
x,y=1,2
for i in range(n-1):
  x,y=y,x+y
print(x)