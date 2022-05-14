import itertools
n,w = map(int,input().split()); a = list(map(int,input().split()));
lis = [];

for n in range(1,4):
  for conb in itertools.combinations(a, n):
    if sum(list(conb)) <= w:
      lis.append(sum(list(conb)))
lis = set(lis)
print(len(lis))