n = int(input())
b = list(map(int, input().split()))
r = list(map(int, input().split()))
ans = sum(b)/n + sum(r)/n
print(ans)