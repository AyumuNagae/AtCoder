h, w = map(int, input().split())
s = [input() for _ in range(h)]
ans = 0
z =[]
for i in range(h):
    for j in range(w):
        if s[i][j] == 'o':
          z.append(i)
          z.append(j)
          if len(z) == 4:
            exit(print(abs(z[0]-z[2])+abs(z[1]-z[3])))