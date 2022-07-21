n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = []
idx = list(range(n))
idx.sort(key=lambda i: (a[i], -i))
for _ in range(x):
    ans.append(idx.pop() + 1)
idx.sort(key=lambda i: (b[i], -i))
for _ in range(y):
    ans.append(idx.pop() + 1)
idx.sort(key=lambda i: (a[i] + b[i], -i))
for _ in range(z):
    ans.append(idx.pop() + 1)
ans.sort()
print(*ans)