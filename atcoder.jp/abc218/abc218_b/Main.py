p  = list(map(int, input().split()))
ans = [chr(p[i]+96) for i in range(len(p))]
print("".join(ans))