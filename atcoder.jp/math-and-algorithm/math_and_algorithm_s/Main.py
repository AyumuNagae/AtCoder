n = int(input())
a = list(map(int, input().split()))
a1 = a.count(1)
a2 = a.count(2)
a3 = a.count(3)
ans = a1 * (a1-1)/2 + a2 * (a2-1)/2 + a3 * (a3-1)/2
print(int(ans))