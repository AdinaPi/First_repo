# listele pot sa cuprinda elemente de tipuri diferite si au o dimensiune dinamica
fructe = ['mar', 'banana', 'portocala', 3, True]

#afisam fructe
print(fructe)

#afisam un element in functie de index
print(fructe[2])

#adaugam un element in lista
fructe.append('mango')

#suprascriem un element
fructe[4] = 'banana'

print(fructe)

#aflam dimensiunea unei liste
print(len(fructe))

#scoate/sterge si returneaza ultimul element
last = fructe.pop()
print(last)
print(fructe)

#de cate ori apare un element
print(fructe.count('banana'))
last = fructe.pop()
print(fructe)

#extinderea listei cu o alta lista
fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)

print(fructe.index(3))
fructe[3] = 'pomelo'
print(fructe)

