a,b,k = map(int, input().split())
r = range(a, b+1)
for i in sorted(set(range(a, b+1)[:k])|set(range(a, b+1)[-k:])): print(i)