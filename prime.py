def div(a):
    list = []
    for x in range(1,a+1,1):
        if a % x == 0:
            list.append(x)
    print(list)
    if len(list)==2:
        print("prime number")

div(13)

