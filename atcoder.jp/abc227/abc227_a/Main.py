n, k, a = map(int, input().split())
a -= 1
ans = (a + k - 1) % n + 1
print(ans)