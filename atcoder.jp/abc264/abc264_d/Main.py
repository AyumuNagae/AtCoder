s = list(input())
atc = ["a","t","c","o","d","e","r"]
dic = {"a":0,"t":1,"c":2,"o":3,"d":4,"e":5,"r":6}
for i in range(7):
  s[i] = dic[s[i]]
cnt = 0
for i in range(7):
  for j in range(7 - i -1):
    if s[j] > s[j+1]: #左の方が大きい場合
      s[j], s[j+1] = s[j+1], s[j] #前後入れ替え
      cnt += 1
print(cnt)