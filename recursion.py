"""
recursion - when program is called again within itself,it's much faster than linear way of solving a problem
Each copy of a program is consuming more RAM memory.We can define two parts of a recursive algoritm:
basic part - which is needed to be fullfiled so the program knows when it needs to go back and stop calling itself (when N== 0)
complex part - the part which involves calling the program again with some change.For example, substracting 1 from N
11.11.2019
"""


#   Sum of a list of numbers https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-1.php
def sumList(numList):
    if len(numList) == 1:  # if length of list is one,return the only member as the value of sumList upwards
        return numList[0]  # jezeli dlugosc listy to 1 ,zwroc element ktory jest w liscie jako wartosc funkcji sumlist
    else:  # else add first element to the function of list without the first element until there's only one element in the list
        return numList[0] + sumList(numList[
                                    1:])  # inacze dodaj pierwszy element do funkcji od listy z slice od indexu 1 wlacznie do momentu kiedy lista ma dlugosc 1 wted zwroc num[0]


lista = [60, 20, 10, 10, 10, 10, 10, 10, 10]


def fib(n):  # fib(n) = fib(n-2)+fib(n-1)
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


"""" do naprawy rozwiazanie pod spodem,needs review after better understanding of recursion solved below
def sop(n, x=0):  # sum(n)= n+(n-2)+(n-4)  until n - x <= 0
    if n - (2 * x) <= 0:
        return 2 * x
    else:
        return sop(n, x + 1)


print(sop(6))
"""


def sum_series(n):
    if n < 1:
        return 0
    else:
        return n + sum_series(n - 2)


print(sum_series(6))
print(sum_series(10))

"""Write a Python program to get the sum of a non-negative integer. Go to the editor
Test Data:
sumDigits(345) -> 12
sumDigits(45) -> 9
"""

""" brak pomyslu jak zrobic,dobry trop rozwiazanie pod spodem
def sum(liczba):
    if liczba % 10 == 0:
        return liczba
    else:
        liczba + sum(liczba)


if 1 == 1:
    print(182 // 10)
"""
def sumDigits(n):
  if n == 0:
    return 0
  else:
    return n % 10 + sumDigits(int(n / 10)) # dodajemy ostatnia liczbe z ciagu N uzywajac reszty z dzielenia modulo
#                                            zmmniejszamy liczbe o 1 miejsce od prawej dzielac przez 10 i tworzac float a potem robimy z float inta ktory ignoruje miajsca po przecinku
#                                              345/10 = 34.5    int(34.5)=34
print(sumDigits(345))
print(sumDigits(45))
def potega(a,b):
    if b==0:
        return 1
    else:
        return a * potega(a,b-1)

print(potega(3,6))
print(potega(20,1))
print(potega(3,3))