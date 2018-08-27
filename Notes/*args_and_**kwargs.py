def myfunc(a,b, c=0, d=0, e=0):
    #Returns 5% of the sum of a and b
    return sum((a, b, c, d, e)) * 0.05

print (myfunc(40,60,100))

def myfunc2(*args): #*args can be taken as many as variables in, taken as a tuple in the function
    return sum(args)*0.05

print (myfunc2(40,60,70,80))
print (myfunc2(40,77, 79, 8070,80))
print (myfunc2(40,70,80))
print (myfunc2(40,60,70,80,100,110,230,340,50))

def myfunc3(**kwargs):
    if 'fruit' in kwargs:
        print ('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print ('I did not find any fruit here')
myfunc3(fruit = "apple", veggie = "lettuce")

def myfunc4(*args, **kwargs):
    print (args)
    print (kwargs)
    print ('I would like {} {}'. format(args[0], kwargs['food']))
    
myfunc4(10,20,30, fruit='orange', food = 'eggs')
    
