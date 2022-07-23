n = int(input())
s = [input() for i in range(n)]
for i in range(n):
  for j in range(n):
    if s[i][j] == "-":continue
    if s[i][j] == "W" and s[j][i] == "W":exit(print("incorrect"))
    if s[i][j] == "L" and s[j][i] == "L":exit(print("incorrect"))
    if s[i][j] == "D" and s[j][i] is not "D":exit(print("incorrect"))
print("correct")