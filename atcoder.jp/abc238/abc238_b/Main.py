n = int(input())
c = [False] * 360
now = 0
c[now] = True
for x in map(int, input().split()):
    now = (now + x) % 360
    c[now] = True
ans = 0
last = 0
for i in range(360):
    if c[i]:
        ans = max(ans, i - last)
        last = i
ans = max(ans, 360-last)
print(ans)