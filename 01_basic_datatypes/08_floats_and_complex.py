# Usually precision till 15-17 digits
salary = 39932.39

print(f"salary = {salary}")
print(f"type of salary = {type(salary)}")

x =float("290") # typecasting to float
print(f"x = {x}")

print(8/5)

res = 0.1+0.2
print(res) 
# that age old interview question, ans ==> IEEE Floating Point Number Storage thingy


# method to write exponents
# eg.
electron_mass = 9.11e-31 # 9.11 * 10^-31

random_num = 1e5  # 10^5
print(random_num)

a = 1.2e3
b = 1200

print(a==b) #True

positive_infinity = float('inf')
negative_infinity = float('-inf')
print(positive_infinity)

pi = 3.141592

print(f"value of pi upto 2 digit = {pi:.2f}")




# COMPLEX NUMBERS 
Z1 = 3 + 5j # in python j is used instead of i
Z2 = 2 - 8j

print(Z1)
print(Z1.real)
print(Z1.imag)

sum_z = Z1+Z2
diff_z = Z1-Z2
prod_z = Z1*Z2
quot_z = Z1/Z2
mag_z1 = abs(Z1)
mag_z2 = abs(Z2) # magnitude of complex number

#another method to create complex num

z3 = complex(2,45)

print(z3)

