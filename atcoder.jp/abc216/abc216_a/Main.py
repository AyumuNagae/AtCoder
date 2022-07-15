x, y = map(int, input().split('.'))
ans = str(x) + ('-' if 0 <= y <= 2 else '' if 3 <= y <= 6 else '+')
print(ans)