n = int(input())
SP = []
for i in range(n):
    s, p = input().split()
    p = int(p)
    SP.append([s, p, i + 1])

SP.sort(key=lambda x: (x[0], -x[1]))

for _, _, i in SP:
    print(i)
