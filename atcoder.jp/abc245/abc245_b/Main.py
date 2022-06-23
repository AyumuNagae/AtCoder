n = int(input())
a = set(map(int, input().split()))
for i in range(len(a)+1):
  if i not in a:
    print(i)
    break