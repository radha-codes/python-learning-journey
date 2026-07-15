# Dictionary 

marks = {
    "Harry" : 100,
    "Shubham" : 56,
    "Rohan" : 23
}

# print(marks, type(marks))
# print(marks["Harry"])

# Dict_methods
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry":99 , "Shushmita":97})
# print(marks)

# print(marks.get("Harry")) 
# print(marks.get("Radha")) #Prints None
# print(marks["Radha"]) # Returns an error

# Sets
# s = { 1, 5, 32 }
# e = set() # Don't use s = {} as it will create an empty dictionary
# p = {1, 4, 6, 6, 6, 7, 7, 8, 8}
# print(p)

# Set_methods
# s = {1, 89, 0, 78, "Harry"}
# print(s, type(s))
# s.add(566)


# print(s, type(s))
# s.remove(1)
# print(s, type(s))

# Set_union_intersection

s1 = {1, 45, 6, 78, 78}
s2 = {7, 8, 1, 78}
print(s1.union(s2))
print(s1.intersection(s2))
