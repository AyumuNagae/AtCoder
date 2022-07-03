n, q = map(int, input().split())
s = input()
base = 0
for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        base -= x
        base %= n
    else:
        print(s[(base + x - 1) % n])