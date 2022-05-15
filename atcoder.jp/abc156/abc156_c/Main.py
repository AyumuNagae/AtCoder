n = int(input()); x = [ int(i) for i in input().split() ];

avg = sum(x)//n; avg2 = avg + 1
ans = 0;         ans2 = 0;

for i in x:
  ans =  ans  + (i - avg )**2
  ans2 = ans2 + (i - avg2)**2

print(min(ans,ans2))