s = list(input())
if s[0] == "1":exit(print("No"))
a = [ s[6], s[3], s[4], s[5], s[9] ] 
if s[8] == "1" or s[2] == "1":a.insert(3,"1")
else: a.insert(3,"0")
if s[1] == "1" or s[7] == "1":a.insert(2,"1")
else:a.insert(2,"0")
for i in range(5):
  if a[i] == "1" and a[i+1] == "0":
    for j in range(i,5):
      if a[j+2] == "1":
        exit(print("Yes"))
      
print("No")