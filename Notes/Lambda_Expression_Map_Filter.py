def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square, my_nums):
    print (item)

def splicer(mystring):
    if len(mystring)%2 == 0:
        print( 'EVEN')
    else:
        print( mystring[0])

names = ['Andy', 'EVe','Sally']

list(map(splicer, names))


def check_even(num):
    return (num%2 == 0)
    
mynums = [1,2,3,4,5,6]
print (list(filter(check_even, mynums)))

for n in filter(check_even, mynums):
    print(n)
    

square = lambda num: num **2

print (square(20))

print (list(map(lambda num:num**2, mynums)))