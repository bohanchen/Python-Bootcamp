def say_hello(name):
    '''
    docstring:information about the function
    input:no input..
    output: Hello
    '''
    print('hello '+name)
    
say_hello('Jose')


def say_hello2 (name ="NAME"): #assign default value
    print ('print '+name)

say_hello2()

def add(n1,n2):
    print (n1+n2)
add(20,20)

#find our if the word "dog" is in a string?
#----------------------------------------------------------------------
def dog_check(mystring):
    """"""
    if 'dog' in mystring:
        return True
    else:
        return False
print (dog_check('dog ran away'))


#pig latin
def pig_latin(word):
    first_letter = word[0]
    #check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter +'ay'
    
    return pig_word

print(pig_latin('apple'))
    