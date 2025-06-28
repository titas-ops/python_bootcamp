# integers
a = 10
b = -22
print(f"{a},{b}")
print(f"type of a = {type(a)} , type of b = {type(b)}")
# integers have unlimited precision , as per system memory
salary = 1_00_00_00_00 # can use _ for readability just like commas
print(salary)

print(bin(a)) # to see binary value
binary_num = 0b10111001010101000111
print(binary_num)
hex_num = 0xAAFF928830
print(hex_num)
# basic arithmetic operators

a=3
b=10

print(a+b)
print(a-b)
print(f"division {a/b}") # will convert to float unlike C and give proper answers
print(f"modulo operator {b%a}")
print(f"multiplication {a*b}")
print(f"power => {b**a}")
print(f"negation of a => {-a}") # negation
print(f"absolute value of -28 => {abs(-28)}")

# precedence of operators

# () > ** > *,/,//,% > +,-
# same level precedence we go L to R



# bitwise operator
x = 10 # 1010
y = 6  # 0110
# &, bitwise AND

print(bin(x&y)) # o/p == 0b10 or 2 in decimal

# | , bitwise OR
# ^ , bitwise XOR
# ~ , bitwise NOT ==> only 1 operand needed


#left shift
print(f"original value of x = {bin(x)}")
left_shift = x << 1
print(f"after the shift {bin(left_shift)}")

#right shift
print(f"original value of x = {x}, in binary x= {bin(x)}")

right_shift = x>>1
print(f"after right shift x {right_shift}, and in binary = {bin(right_shift)}")


# / operator does division
# // does integer division

print(-10//3) # why ans -4? cause answer is GIF ed or floored so: [-3.3333] = -4



