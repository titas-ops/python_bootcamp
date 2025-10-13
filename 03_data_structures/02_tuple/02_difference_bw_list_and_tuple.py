t = (1,2,3,4)

# t[0] = 18 # error 
#  tuple is immutable

# tuple arengenerally faster and smaller compared to list


import sys

print(sys.getsizeof([1,2,3,4]))
print(sys.getsizeof((1,2,3,4)))

'''all will give attribute error 
t.append(8) -error
t.remove(19) - error
del t[9]
'''
del t # works fine 


# Immutability works on the tuple container but not to the objects inside it 


t = (1,[2,3])


t[1].append([6,9])
print(t)

org_tuple =(1,2,3,)

new_tuple = org_tuple + (4,5)
print(new_tuple)


org_tuple = org_tuple + (4,5,6,7)
print(org_tuple)


# Accessing tuple element 
# same as lists - +ve, -ve indexing both works
# slicing works same as str,lists
