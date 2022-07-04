s = list(input())
n,m = map(int,input().split())
n -= 1
m -= 1
a = s[n]
s[n] = s[m]
s[m] = a
print("".join(s))