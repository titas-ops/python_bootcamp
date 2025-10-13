# sum(listName) returns sum of the list
# slicing & indexing

fruits =['apple','banana','guava']

print(fruits[0])

for i in fruits:
    print(i)

print()

for i in range(0,len(fruits)):
    print(fruits[i])

# slicing variable[start:end:step],
#  always returns new list > does not modify the org list 
# going out of range does not give error in list
num = [2,3,21,45,63,66,73,25,75,24,626,21]

print(num[0:10:+2])
print({num[len(num)-1]})
print(f" reverse the list {num} => {num[::-1]}")
print(num[-8::])

# Modifying lists 

fruits =['apple','banana','guava']
fruits[1]= 'blueberry'
fruits.append('cherry')
print(fruits) # ['apple','blueberry','guava','cherry']

fruits.insert(3,'banana')
print(fruits) # ['apple','blueberry','guava','banana','cherry']

fruits_2 = ['grapes','kiwi']

print(fruits.extend(fruits_2)) # returns none, don't use append . why though??

print(fruits) # change in original list

fruits.remove('banana')
print(fruits)
fruits.pop('4')
print(fruits)
fruits.pop() # returns the thing it popped , just like the stack operation
print(fruits)

del fruits[1:3]
print(fruits) # returns None

fruits.clear()
print(fruits)

