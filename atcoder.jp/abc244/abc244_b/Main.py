d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
n = input()
x = y = 0
i = 0
for c in input():
    if c == 'S':
        x += d[i][0]
        y += d[i][1]
    else:
        i = (i + 1) % 4
print(x, y)