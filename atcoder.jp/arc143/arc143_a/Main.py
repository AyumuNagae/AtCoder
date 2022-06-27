a = sorted(map(int, input().split()))
cnt = a[2] - a[0] + a[2] - a[1]
if cnt > a[2]:
    print(-1)
else:
    print(a[2])