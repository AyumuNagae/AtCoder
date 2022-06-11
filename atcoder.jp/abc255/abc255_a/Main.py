r,c  = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if r==1 and c ==1:
  print(a[0])
elif r==1 and c ==2:
  print(a[1])
elif r==2 and c ==1:
  print(b[0])
elif r==2 and c ==2:
  print(b[1])