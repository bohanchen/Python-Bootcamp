#tuple is inmmutable, this is the difference with the list

t = (1,2,3)
print (type(t))
print (t[-1])
print (t[0])
print (t[2])

t2 = ('a', 'b', 'c', 'd')
#tuple only has two methods
print (t2.count('a'))
print (t2.index('a'))

#this create an error, this is for to avoid assign values accidently 
#t[0] = 'New' #can't assign value



