mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print (mylist)

mylist2 = [letter for letter in 'word']
print (mylist2)

mylist3 = [num**2 for num in range(0,11)]
print(mylist3)

mylist4 = [x for x in range(0,11) if x%2 ==0]
print (mylist4)

results = [x if x%2==0 else'ODD' for x in range(0,11)]
print (results)

mylist5 = []
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist5.append(x*y)
print(mylist5)

mylist_unreadable = [x*y for x in [2,4,6] for y in [100,200,300]]
print (mylist_unreadable)