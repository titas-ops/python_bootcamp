print('lists in python')

# 3TYPES OF COLLECTION

# sequence => string,list,tuple
# mappings =>dictionary
# sets =>set,frozenset

#EG
temp = [18,22,21,17,16]
avg_temp = (sum(temp)/len(temp))

# string : ordered ,immutable sequence of characters enclosed within quotes

# list : ordered,mutable collecton that can contain mixed data types
#   [2,6,7,2,4,'hello',True]

# tuple Ordered, immutable collections similar to lists
#   -(1,"hello",3.1415,True)

# dictionary : Unordered(pre 3.7)/insertion-ordered(3.7+),key value pairs
#   {'name': "Titas", "age": 25, "city": 'Ne w York'}


d =  {'name': "Titas", #eg of dictionary
      "age": 25, 
      "city": 'New York'}

print(d["name"])


# set : unordered mutable collection of unique elements
# -{1,2,3,4,11}

# frozenset : immutable set 