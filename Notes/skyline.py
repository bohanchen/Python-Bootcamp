def myfunc(string):
    result = ''
    i = 0
    for letter in string:
        #print (i)
        if i%2 ==0:
            result += letter.lower()
        else:
            result+= letter.upper()
        i+=1
    print(result)

myfunc('mystring')

