# raw strings: treat escape characters as normal part of string

rs = r"okay th\is how it works\\okay\f"
print(rs)

address = r"C:\user\titas\desktop\python_notes"
print(address)

# examples of disadvantages of raw str

r"she said,\"Hello \"" # fine
# r"She said , "Hello"" # syntax error
r"This ends with \\" # fine 
# r"This ends with \" # syntax error

# for revision
'''
https://youtu.be/MDZ4y-GgZ8k?si=Ucja05i2gesVILQs
'''
