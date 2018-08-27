#while some_boolean_condition:
#do something

x = 0
while x<5:
    print(f'The current value of x is:{x}')
    x=x+1
else:
    print ("X is not less than 5")
    
#the pass keyword
x = [1,2,3]
for item in x:
    #do nothing for now
    pass
print ('end of my script')

#continue keyword
mystring = 'SAMMMMY'
for letter in mystring:
    if letter == 'A':
        continue
    print(letter)

#break keyword
for letter in mystring:
    if letter == 'A':
        break
    print(letter)