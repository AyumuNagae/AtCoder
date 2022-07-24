n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s= abs( sum(a) - sum(b) )
if s%2 != k%2:exit(print("No"))

ab = 0

for i in range(n): ab += abs(a[i]-b[i])

if ab <= k: print("Yes")
else:print("No")