n, m = map(int, input().split())
a = list(map(int, input().split()))
s1 = [0] * (n + 1)
s2 = [0] * (n + 1)
for i in range(n):
    s1[i+1] = s1[i] + a[i]
    s2[i+1] = s2[i] + i * a[i]
ans = -10 ** 18
for i in range(n - m + 1):
    ans = max(ans, s2[i+m] - s2[i] - (i - 1) * (s1[i+m] - s1[i]))
print(ans)