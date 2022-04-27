N = int(input())
T = list(map(int,input().split()))
T_sum = sum(T)
M = int(input())
for _ in range(M):
  P,X = list(map(int,input().split()))
  print(T_sum+X-T[P-1])