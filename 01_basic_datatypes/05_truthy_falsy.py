# boolean ==> True/False

a = True
# b = true    X
b = False

age = 17

is_adult = age > 18
print(is_adult)

print(bool(1))
print(bool(0))

# empty string,0,empty list,empty dict ==>all Falsy
# bool(None) == False
#All Other Values are Truthy


# bool is subclass of int ==> True

# every Boolean is an integer
print(isinstance(True,int)) # True
# every Integer is a boolean ==> False
print(isinstance(1,bool)) # False


a = 243
print(a.bit_length())

print(True.bit_length())  #1
print(False.bit_length()) #1


# Logical Operators
# Follow Usual Boolean Algebra , Short Circuit law for OR
# logial AND ==> and
# logial OR  ==> or
# logial NOT ==> not

has_money = False
if not has_money:
    print(f'This guy has money : {int(bool(not has_money))}')

