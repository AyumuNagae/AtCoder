n = int(input())
c = sorted(list(map(int, input().split())))

ans = 1
mod = 1000000007

for i in range(n): ans = ans * max(0, c[i]-i) % mod

print(ans)