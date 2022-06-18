n = int(input())
a = list(map(int, input().split()))
tmp = [0]*n
for i in range(n):
  tmp[i] = sum(a[i:])
print(len([i for i in tmp if i > 3]))