n = int(input())
a = list(map(int,input().split()))
ans = 0

ans = abs(max(a)- min(a))
print(ans)