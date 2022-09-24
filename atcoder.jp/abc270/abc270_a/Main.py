a,b = map(int,input().split())
l = []
if a == 1:l.append(1)
if a == 2:l.append(2)
if a == 3:
  l.append(1)
  l.append(2)
if a == 4:l.append(4) 
if a == 5:
  l.append(1)
  l.append(4)
if a == 6:
  l.append(2)
  l.append(4)
if a == 7:
  l.append(1)
  l.append(2)
  l.append(4)

  

if b == 1:l.append(1)
if b == 2:l.append(2)
if b == 3:
  l.append(1)
  l.append(2)
if b == 4:l.append(4) 
if b == 5:
  l.append(1)
  l.append(4)
if b == 6:
  l.append(2)
  l.append(4)
if b == 7:
  l.append(1)
  l.append(2)
  l.append(4)

l = list(set(l))
print(sum(l))