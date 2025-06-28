#strings are sequence of characters enclosed within quotes(single,double,triple)

str1 = "mike jordan" # string

print(str1[7]) 

print("12"+"3")

print(1==1)

msg = 'She said \'don\'t worry about errors\' '
print(msg) # \ is escape char

dialogue = "She said \"python is amazing\" "

print(dialogue)

poem = """ 
I tried to cook but burned the stew,
The smoke alarm yelled, “What'd I do to you?!”
My cat wore pants and judged my plate,
Then knocked it off — such twist of fate.

I joined a gym, felt strong and free,
Then tripped on air — oh, gravity!
My coffee talks, it says, “Not today.”
While bills pile up like papier-mâché.

Life's a mess, but that's my jam —
At least I nailed this Instagram.
"""
# ''' content ''' also works the samels
print(poem)

# how do you print C:Users\Nag\RCB\Trophy ?

direct = "C:\\Users\\Nag\\RCB\\Trophy"

print(direct)



# string concatination

a = "2"
b = "2"

print(a+b)
                                        
x = 'Titas'
y = 'Dey'

print(x+ " " +y)

age = 20
name = "Titas"

print("hi I am "+name + str(age))

# f string
new_str = f"Hello my name is {name} & my age is {age}"

print(new_str)
# ASCII & Unicode values & Comparision Operator ==> read from docs





#string indexing 

txt = "python"

print(txt[len(txt)-1]) 
# negative index txt[-1]==> n
print(txt[-3])

# slicing
# str[start:end:step] # step means how many char to jump/skip
# step == 1 means no jump, we can also skip writing this, 2 means skip one then print the next one , like if text = "hello" ==> print(text[::2]) : o/p ===> hlo
# start ==> inclusive , end ==>exclusive

txt = "Python Programmmming"

# normal,negative both works
print(txt[0:8])
print(txt[-11:-8])


# reverse a string 
text1 = "hello Everyone How are you all"
print(text1[::-1])


# string methods ==> almost same as function just calling is diff, we use .

print(txt)
print(txt.upper())
print(txt.lower())

txt2 = "the great gatsby"

print(txt2.title())

print(txt2.capitalize())

txt  = "     hello this is a  random poorly written string how to fix   ?      "

print(txt.strip())
print(txt.lstrip()) #moves left side wala white space
print(txt.rstrip())

# find("sub_string",start,end) returns the index of the string being found
new_str = 'Python is fun , Python is nice , python is easy to learn'
idx = new_str.find("Python")

print(idx)
print(new_str.find("ptty"))
print(new_str.find("python"))

print(new_str.count("Python"))


# .index(substring,start,end)
# this raises error if it can't find the intended string , unlike .find(), .find() returned -1

print(new_str.find("Java"))
# print(new_str.index("Java"))

# .replace() method
# .replace(old str, new str,count)

text = 'Hello World'

print(text.replace('Hello','Bye Bye'))

text ='potato potato potato'
print(text.replace("potato","vodka",2))

x1 = "2420402"
x2 ="23Pyt"

print(x1.isdigit())
print(x2.isdigit())

print(x1.isalnum())
print(x2.isalnum())


# other string methods
# islower(),isspace(), startswith(), endswith()

text ="one,two,three,four,five"
print(text.split(",")) #returns a list

li = [ 'apple', 'orange','banana','kiwi']

print(",".join(li))


# .format() method 
name = "Titas"
msg = "Hello my name is {0} & my age is {1}".format(name,19) # by default 0,1, so on it goes, but we can rearrange inside {} for different outputs
# also works with placeholder {p1},{p2}
print(msg)


# old formatting with % i.e format specifier

name = "Titas"

print("hello my name is %s" %name)

pi = 3.1415926

print("The value of pi is %.2f" %pi)

# Exactly like C , just not colon(comma)