# nested tuple


ns_tuple = ((1,2),(2,3),(3,4),("Alex","Hales"),{'key':'value'})


# tuple unpacking

a,b,c = 1,2,3 


t = 3,4,5

a,b,c = t

a,*b = 1,2,3,4,5,6,7,8,9,11, 

print (a)
print (b)


x,*y = "Hello World"
print(f"x = {x} , y = {y}")


data = ("Alex",35,"Data Engineer",400000,"California")


# iterating tuple
# same as list, enumarate works too

color = ('red','green','yellow')

print(enumerate(color))
for c in enumerate(color,start = 11):
    print(c)


# Concatination 

t1 = ('a','b','c')
t2 = ('d','e','f')

t1 = t1 + t2

print(t1)


#  Repetitiion

tuple111 = (1,2)

tuple222 = tuple111*4

print(tuple222)

# Methods - count , index 

