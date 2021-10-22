for n in range(2,100):
    for x in range(2,n):
        if n % x == 0:
            print(n, "不是一个素数")
            break
    else:
        print(n,"是一个素数")
