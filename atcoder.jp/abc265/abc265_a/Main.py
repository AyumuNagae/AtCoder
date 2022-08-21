x,y,n = map(int, input().split())
cnt = 0;
flag = True
if x*3 > y:
  print( ((n//3)*y + (n%3)*x)     )
else:
  print(   n*x    )
  