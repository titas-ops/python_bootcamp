# ordered,mutable,heterogeneous,iterateable

# nested list

matrix1 = [[1,2],[3,4],[5,6]]
'''
1 2
3 4
5 6
'''
# method2
# using constructor
li = list("Hello")  #expects an iterable

print(type(matrix1))
print(type(li))

s = {10,20,30,15}
li2= list(s)

print(type(li2))

print(list(range(10)))

original_list = [3,4,2,111,4,'',3]
copy_list = list(original_list)

# list(1248584) : error 

#empty list
empty = []
# list of strings
string_list = ['kolkata','bangalore','chennai','fukusima']
#list of booleans
toss_binomial = [True,False,True,True,False]