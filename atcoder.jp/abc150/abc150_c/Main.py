from itertools import permutations
n=int(input())
p=tuple(input().split())
q=tuple(input().split())
a=sorted(list(permutations(p)))
print(abs(a.index(p)-a.index(q)))