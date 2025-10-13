# tuple is an ordered, immutable collection of items

my_tuple = 1,2,3
another_tuple = (1,2,3,4,5,6)

single_ele_tuple = 6900,

print(f"{type(my_tuple)}........{type(another_tuple)}.....{type(single_ele_tuple)}")


new_tuple = tuple("HELLO PEOPLE") # tuple constractor, expects  iterable

print(new_tuple)


# tuples are created using comma not parentheis 
# parenthesis is used for readability

# t = tuple(19)  --- error, cause constructor expect iterable
t = tuple([18])
empty = () # exception # or write empty = tuple()

print(type(empty)) # class tuple
