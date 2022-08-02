n, k = map(int,input().split())
 
ab = []
for _ in range(n):
    a, b = map(int,input().split())
    ab.append(a - b)
    ab.append(b)

ab.sort(reverse = True)
print(sum(ab[:k]))