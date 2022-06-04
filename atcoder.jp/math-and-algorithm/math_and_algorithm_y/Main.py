n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = sum(a)+sum(b)*2
ans /= 3
print(ans)