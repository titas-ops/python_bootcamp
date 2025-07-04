f = open('myFile.txt','r')  #default mode is read i.e 'r'

text = f.read()
print(text)
f.close()

# 'w'=>deletes all the old stuff & writes freshly
# 'a':appends after the previous text

f2 = open('myFile2.txt','a')
f2.write("Okay,this will be appended on the last line of the text in the file previously saved after every run")
f2.close()

print(f2) 

# run the code multiple times

# another syntax, with statement

with open('file3.txt','w') as f3:
    f3.write("hey I am inside with")

print(f3)