n=int(input('Dati numarul de elemente din vector='))
a=[]
if 0<n<10:
    print('Introduceti ',n,' elemente pentru vectorul creat')
    for i in range(0,n):
        x=int(input('Dati elementul='))
        a.extend([x])
    print(a)
else:
    print("n trebuie sa fie mai mic ca 10 si mai mare ca 0")
print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii;')
print(a[0::5])
print('b) afişează pe ecran numerele în ordinea inversă a introducerii în calculator;')
b=a.copy()
b.sort(reverse=True)
print(b)
print('c)  sortează componentele tabloului în ordine descrescătoare;')
b=sorted(a)
print(b[::-1])
print('d)  afişează pe ecran doar componentele pare;')
b=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        b.extend([y])
print(b)
print("e)afişează pe ecran media aritmetică a componentelor pare")
suma=0
for i in range(0,len(b)):
    suma+=b[i]
if(suma!=0):
 print(suma/(len(b)))
else:
    print("nu exista numere impare")
b=[]
print('f)  afişează pe ecran doar componentele impare;')
for i in range(0,len(a)):
    s=a[i]
    if(s%2!=0):
        b.append(a[i])
print(b)
print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')
x=int(input("Introduceti x:"))
y=int(input("Introduceti y:"))
b=[]
for i in range(0,len(a)):
    x1=a[i]
    if(x<x1<y):
        b.append(a[i])
print(b)
b=[]
print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
for i in range(0,len(a)):
    x1=a[i]
    if(x1>x and x1%y!=0):
        b.append(a[i])
print(b)

print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative;')
print([i for i, e in enumerate(a) if  e & 0 and e<0])
print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
print([i for i, e in enumerate(a) if (e>9 and e<100)or(e<-9 and e>-100)])
print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
j=a
j[0]=min(j)
print(j)
print("l)înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;")
l=a.copy()
l[l.index(min(l))]=a[0]
print(l)
print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
m=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        kl=a[i]
        m.extend([kl])
print(m)
print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
n=[]
for i in range(0,len(a)):
    if a[i]%3==0:
        fea=a[i]
        n.extend([fea])
print(n)
print('o)  creează un tablou nou, format doar din acele componente ale tabloului in-trodus de la tastatură care au cel mult patru divizori:')
o=[]
for i in a:
    if i>0:
        nr=0
        for x in range(1,i+1):
            if i%x==0:
                nr+=1
        if nr<=4:
            o.append(i)
if i<0:
    print("Numar negativ")
print(o)









