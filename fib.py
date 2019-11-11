def fib():
    war = int(input("podaj"))
    a = [1,1]
    while len(a) != war:
        for x in range(2,war,1):
            d = a[x-2] + a[x-1]
            a.append(d)
    print(a)
fib()