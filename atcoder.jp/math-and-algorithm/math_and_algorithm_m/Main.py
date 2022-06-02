import math
n = int(input())
a = int(math.sqrt(n))
b=[]
for i in range(1,a+1):
  if n%i==0:
    b.append(int(i))
    b.append(int(n/i))
for i in b:
  print(i)