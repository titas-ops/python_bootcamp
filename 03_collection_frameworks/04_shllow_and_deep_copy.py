a = [1,2,3]
b = a
b.append(4)
print(f"a==={a} & b==={b}")


a =[1,2,3]

b = a[:] # slicing creates a shallow copy of flat list
# or b=list(a)
b.append(4)
print(f"a==={a} & b==={b}")

x = [[1,2],[3,4]]
y = x[:]
y[0][0] = 99
print(f"x={x},y={y}")

import copy

x = [[1,2,3],[4,5,6]]
y = copy.deepcopy(x)

print(id(x),id(y))


#list concatination works same as strings

a = [1,2,3,4,5]
b = [6,7]

c = a + b + [8]
print(c)

z = [0,1,2]
print(z*3)