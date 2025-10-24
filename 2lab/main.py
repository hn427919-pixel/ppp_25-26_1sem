i,z=map(str,input("").split())
p=[]
o=[]
y=[]
u=[]
for x in 'qwertyuiopasdfghjklzxcvbnm':
    if x in i:
        p.append(x)
        o.append(i.count(x))
for x in 'qwertyuiopasdfghjklzxcvbnm':
    if x in z:
        y.append(x)
        u.append(z.count(x))


for x in range(len(o)):
    for e in range(len(o)):
        if o[x]==u[e]:
             print(f'{p[x]}={y[e]}')