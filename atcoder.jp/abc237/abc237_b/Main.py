h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
for p in zip(*a):
    print(*p)