import sys
sys.setrecursionlimit(10 ** 6)
def rec(v, p, depth, chs):
    if v == 0:
        depth[v] = 0
    else:
        depth[v] = depth[p] + 1
    for ch in chs[v]:
        rec(ch, v, depth, chs)

N = int(input())

P = list(map(int, input().split()))

for i in range(N-1):
  P[i]-=1

chs = [[] for v in range(N)]
for v in range(1, N):
    p = P[v - 1]
    chs[p].append(v)
depth = [0] * N
rec(0, -1, depth, chs)

print(depth[-1])