w=input()

a=[]

for i in range(len(w)):
    if w[i] in a:
        a.remove(w[i])
    else:
        a.append(w[i])

if a==[]:
    print("Yes")
else:
    print("No")