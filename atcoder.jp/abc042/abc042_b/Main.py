n,l = map(int, input().split())
ans = [input() for _ in range(n)]
ans.sort()
print(''.join(ans))