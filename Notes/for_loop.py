my_list = [1,2,3,4,5,6,7,8,9,10]
for num in my_list:
    print (num)
    print ('hello')

for num in my_list:
    #check for even
    if num % 2 == 0:
        print (num)
    else:
        print(f'Odd Number:{num}')

list_sum = 0

for num in my_list:
    list_sum = list_sum+num
print ('the sum is:')    
print (list_sum)

mystring = 'Hello World'


print ('Letters are here:')
for letter in mystring:
    print (letter)
    
print("for loop with tuple")
tup = (1,2,3)
for item in tup:
    print (item)
    
print ('for loop with tuple inside list')
my_list2 = [(1,2),(3,4),(5,6),(7,8)]
print (len(my_list2))
for tup in my_list2:
    print (tup)
print ('tuple unpacking:')
for a, b in my_list2:
    print (a)
    print (b)
    


dic = {'k1':1, 'k2':2, 'k3':3}
for key in dic.keys():
    print (key)
for value in dic.values():
    print (key)
for key, value in dic.items():
    print (key)
    print (value)

    