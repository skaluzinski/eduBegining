"""a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [elem for elem in a if elem%2 == 0]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]
lam = [[row[i] for row in matrix] for i in range(4)]
p1 = ""
p2 = ""
decyzja = ""
while decyzja != "koniec":
    while p1 not in ['kamien','papier','nozyczki']:
        p1 =input("podaj").lower()
    while p2 not in ['kamien','papier','nozyczki']:
        p2 =input("podaj").lower()
    if (p1=="kamien" and p2=="papier")or(p1=="papier" and p2 =="kamien"):
        print("win papier")
    if (p1=="nozyczki" and p2=="papier")or(p1=="papier" and p2 =="nozyczki"):
        print("win nozyczki")
    if (p1=="kamien" and p2=="nozyczki")or(p1=="nozyczki" and p2=="kamien"):
        print("kamien")
    if(p1==p2):
        print('remis')
    decyzja = input("wpisz /'koniec/' aby wyjsc")
    p1,p2 = "",""

import random
a = str(random.randint(1,9))
count = 0
guess = ""
while guess != a:
    guess = str(input("guess number between 1 and 9"))
    count += 1
print("you have taken %d tries to guess number %s"%(count,a))

def fun():
    war = int(input("podaj"))
    a = [1,1]
    while len(a) != war:
        for x in range(2,war,1):
            d = a[x-2] + a[x-1]
            a.append(d)
    print(a)
fun()

a =[1,2,3,1,1,1,1]
b = [4,5,2,1]
c = a + b
print(c)

for elem in c:
    licz = c.count(elem)
    if licz != 1:
        c.remove(elem)
print(c)
"""

def funk():
    tekst = input()
    print(tekst)
    tekst = list(tekst.split())
    print(tekst)
    tekst = str(tekst[::-1])
    tekst = str(tekst)
    print (''.join(map(str, tekst)))
funk()