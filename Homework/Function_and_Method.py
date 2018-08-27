

# write a function of the volume of a sphere
def volume(rad):
    return (4/3)*3.14*rad**3
print(volume(3))

#write a function that checks weather a number is in a given range(nclusive of high and low)
def check_num(num, low, high):
    if (num > low & num < high):
        return "the number is in the range"
    else:
        return "the number is out of bound"
print(check_num(2,1,10))

#write a python function that accepts a string and calculate the number of upper case letter and lower case leeter

string = 'Hello Mr. Rogers, how are you this fine Tuesday?'
def up_low(string):
    num_up = 0
    num_low = 0 
    for letter in string:
        if letter.islower():
            #print(letter)
            num_low += 1
        elif letter.isupper():
            #print(letter)
            num_up += 1
    print (f'No. of Uppwer case characters : {num_up}')
    print (f'No. of Lowwer case characters : {num_low}')

up_low(string)   

#write a python function that takes a list and returns a new list
l = [1,1,1,1,2,2,3,3,3,3,4,5]
def unique_list(sample_list):
    new_list = []
    for i in sample_list:
        #print (i)
        if i not in new_list:
            new_list.append(i)
            #print(i)
    return new_list

print(unique_list(l))
    

#multiply all the number in a list
def multiply(number):
    result = 1
    for num in number:
        result = result*num
    return(result)
print(multiply([1,2,3,-4]))
        

#checks whether a passed string is palindrome or not
def palindrome(s):
    return s == s[::-1]

print(palindrome('abcdefg'))

#Hard level: check whether a string is a pangram or not
import string
def pangram(str1, alphabet=string.ascii_lowercase):
    alphabet = set(alphabet)
    return alphabet<=set(str1.lower())
    
print(pangram("The quick brown fox jumps over the lazy dog"))