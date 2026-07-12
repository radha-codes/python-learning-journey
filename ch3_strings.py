# String types
name = 'Radha' #Single line string
name = "Radha" #Double quotes string
name = '''Radha''' #Multi-line string

# String Slicing
nameshort = name[0:3] # starts from index 0 all the way till 3 (excluding 3)
print(nameshort)
character1 = name[1]
print(character1)

# Negative Slicing
name = "Harry"
print(name[-4:-1])
print(name[1:4])

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5]) 

# String Functions
name = "mohit are"
print(len(name))
print(name.endswith("hit"))
print(name.endswith("hits"))
print(name.startswith("mo"))
print(name.startswith("Mo"))
print(name.startswith("Hit"))
print(name.capitalize())

# Escape sequence characters
str1 = " Shiva is a good boy \nbut not a bad 'boy'"
str2 = " Shiva is a good boy \tbut not a bad boy "
print(str1)
print(str2)