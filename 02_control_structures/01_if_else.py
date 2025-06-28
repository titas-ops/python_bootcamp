name = "Titas"
age = 19

if age>=18:
    print(f"{name} is an adult aged {age}")
else:
    print(f"{name} is not an adult aged {age}")

# syntax
'''
if condition:
   code Block
else:
    codeBlock
   
'''

# elif
#Syntax

'''
if cond1:
    code
elif cond2:
    code
elif cond3:
    code
else:
    code
'''

#Ternary Operator
age = int(input("Enter your age : "))
###
isRetired = "Retired" if age>=65 else "Working"
###
print(f"Titas is {isRetired} at age {age}")


number = 17
divisor = 7

ans = (number/divisor) if divisor != 0 else "can't be divided"
print(f"ans ={ans:.4f}")
