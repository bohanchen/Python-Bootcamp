def myfunc(string):
    i = 0
    for letter in string:
        #print (i)
        if i%2 ==0:
            letter = letter.lower()
            print(string[i])
        else:
            letter = letter.upper()
            print(string[i])
        i+=1

myfunc("mystring")

