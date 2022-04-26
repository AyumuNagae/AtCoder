n = int(input())
a = list(map(int, input().split()))
average = round(sum(a)/len(a))
ans = 0
for i in range(n):
    ans += (a[i] - average) ** 2
print(ans)