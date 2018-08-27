def myfunc(*args):
    mylist = []
    for num in args:
        if num%2 == 0:
            mylist.append(num)
    print(mylist)

myfunc(2,3,4,5,6,7,8,9)
    