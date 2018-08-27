x = 25

def printer():
    x = 50
    return x

# x = 25
print (x)
# x = 50
print (printer())

'''
LEGB Rules
L:Local--name assigedn in any way within a function
E:Enclosing function locals
G:Global
B:Built in (python)

'''
#this is a local 
#lambda num:num**2

#This is a enclosing function locals
name = 'This is a global string'

def greet():
    name = 'Sammy' #enclosing function local
    def hello():
        name = 'Alice' #local
        print('Hello '+name)
    hello()
greet()