a, b, c, d = map(int, input().split())
if b >= c * d:exit(print(-1))
x = c * d - b
print((a + x - 1) // x)