from collections import Counter
n = int(input())
c = Counter(map(int, input().split()))
ans = n*(n-1)//2  -sum( v*(v-1)//2 for v in c.values() )
print(ans)