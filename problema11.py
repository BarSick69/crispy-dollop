import statistics
n=int(input('Dati numarul de elemente:'))
z=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
for i in range(0,n):
    x=int(input('Dati elementul {} = '.format(i+1)))
    z.extend([x])
print(z)

print('a: ',*z[0:5])

print('b: ',*z[::-1])
b=sorted(z)
b.sort(reverse=True)
print('c: ')
c=sorted(z)
c.sort(reverse=True)
print(c)

print('d: ')
d=[]
for i in range(0,len(z)):
    if z[i]%2==0:
        y=z[i]
        d.extend([y])
print(d)
print('e:')
e=statistics.mean(d)
print(e)
print('f:')
f=[]
for i in range(0,len(z)):
    if z[i]%2!=0:
        y=z[i]
        f.extend([y])
print(f)
print('g:')
x,y=eval(input('Introduceti x,y:'))
g=[]
for i in z:
    if(i>x) and (i%y!=0):
        g.extend([i])
        print(g)
print('h:')
h=[]
for j in z:
    if(j>x) and (j<y):
        h.extend([j])
        print(h)
print('i:')
i=[]
for v in z:
    if(v<0) and (v%2!=0):
        i.extend([z.index(v)])
        print(i)
print('j:')
j=[]

for b in z: 
    if ((abs(b) // 10) < 10) and ((abs(b) // 10) > 0):
        j.extend([z.index(b)])
print('k:')
zzx=z.copy()
zzx[0]=min(z)
print(zzx)
print('l: ')
zz=z.copy()
zz[zz.index(min(zz))]=zz[0]
print(zz)
print('m:')
zx=[]
for q in z:
    if (q % 2 == 0):
        zx.extend([q])
        print(zx)
print('n: ')
sz=[]
for w in z:
    if (w % 3 == 0):
        sz.extend([w])
        print(sz)
print('o: ')
zs=[]
for e in z:
    if len([r for r in range(1, e + 1) if e % r == 0]) <= 4:
        zs.append([e])
        print(zs)