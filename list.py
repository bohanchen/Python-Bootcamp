my_list = [1, 2,3]
my_list2 = ['string', 1, 2, 3.4]
print (my_list2)
print (len(my_list2))

my_list3 = ['one', 'two', 'three']
print (my_list3[2])

another_list = ['four', 'five']
print (my_list3+another_list)

new_list = my_list3 + another_list
print (new_list)

new_list[0] = 'ONE ALL CAPS'

print (new_list)

new_list.append('six')
print (new_list)

pop_item = new_list.pop()
print (new_list)
print (pop_item)


new_list4 = ['a', 'b', 'x', 'd', 'c']
new_list5  = [4,2,3,9,5,1,0,8]

new_list5.sort()
sorted_list  = new_list5
print (new_list5)
print(sorted_list)
