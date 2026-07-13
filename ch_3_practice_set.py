# Problem 1 : Write a python program to display a user entered name followed by Good Afternoon using input() function.
name = input(" Enter your name :  ")
print(f"Good Afternoon {name} ") 

# Problem 2 : Write a program to fill in a letter template given below with name and date.
letter = ''' Dear <|Name|>,
You are selected!
<|Date|> '''
print(letter.replace("<|Name|>", "Radha").replace("<|Date|>" , "24 September 2026"))  

# Problem 3 : Write a program to detect double space in a string.
name_str = "Radha is good   girl and"
print(name_str.find("  "))

# Problem 4 : Replace the double space from problem 3 with single spaces.
my_str = "Radha is good   girl and"
print(my_str.replace("  ", " "))
print(my_str) # Strings are immutable which means that you cannot change them by running functions on them 

# Problem 5 : Write a program to format the following letter using escape sequence characters.
letter_formatted = "Dear Radha , \n\tThis python course is nice. \nThanks!"
print(letter_formatted)
