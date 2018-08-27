#diction can't not be sorted
#Dictionaries are mappings and do not retain order! If you do want the capabilities of a dictionary but you would like ordering as well, check out the ordereddict object lecture later on in the course!
#diction is muttable

price_loopup = {'apple':2.99, 'oranges':1.99, 'milk': 5.80}

print (price_loopup['apple'])

d = {'k1': 123, 'k2': [0,1,2], 'k3': {'insideKey':100}}
print (d['k2'])
print (d['k3'])
print (d['k3']['insideKey'])
