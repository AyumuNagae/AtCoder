n, q = map(int, input().split())
a = list(range(n))
index = list(range(n))
for _ in range(q):
    ax = int(input()) - 1
    ix = index[ax]
    iy = ix + 1 if ix + 1 < n else ix - 1
    ay = a[iy]
    a[ix], a[iy] = a[iy], a[ix]
    index[ax], index[ay] = index[ay], index[ax]
print(*(ax + 1 for ax in a))