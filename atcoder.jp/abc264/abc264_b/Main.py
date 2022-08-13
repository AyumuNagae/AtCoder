r,c = map(int, input().split())
r-=1
c-=1
s = ["1"*8,
     "10000000",
     "10111111",
     "10100000",
     "10101111",
     "10101000",
     "10101011",
     "10101010",
    ]
if r > 7:
  r = 14-r
if c > 7:
  c = 14 -c
if s[r][c] == "1":
  print("black")
else:
  print("white")