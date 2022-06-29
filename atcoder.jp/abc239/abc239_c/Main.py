dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
x1, y1, x2, y2 = map(int, input().split())
for i in range(8):
    for j in range(8):
        if x1 + dx[i] == x2 + dx[j] and y1 + dy[i] == y2 + dy[j]:
            exit(print('Yes'))
print('No')