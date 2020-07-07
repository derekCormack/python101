# python101
# my exploration and ground up introduction to Python.
# https://www.learnpython.org/

# LEARN THE BASIC-------------

# Hello, World!


# Variables and Types

# x = 15
# price = 9.99  floating point
# print(result)

# Lists
# Basic Operators
# -------------------------------String Formatting-----------------------------
# f-string allows us to embed variables in side of strings, 3.6 and later
# name = "BOB"
# print(f"Hello, {name}")
# name = "rolf"
# print(f"Hello, {name}")

# longer_phrase = "Hello, {}. Today is {}."
# formatted = longer_phrase.format("rolf", "monday")
# print(formatted)

# name = input("enter your name: ")  # input always gives you string

# print(name)

# size_input = input( "how big is your house in square feet?")
# square_feet = int(size_input)
# square_meters = square_feet / 10.8
# print (f"{square_feet} square feet is  {square_meters:.2f} square metres")

# user_age = int(input("Enter your age: "))
# months = user_age * 12
# print(f"Your age, {user_age}, is equal to {months} months. ")

# ---------LISTS TUPLES AND SETS
# l = ["Bob","Rolf","Anne"]  can add remove    standard
# t = ("Bob","Rolf","Anne")  #constant!  ant add or remove!
# s = {"Bob","Rolf","Anne"}   no duplicates! order not guarenteed

# print(l[0])  - subscript notation
# print(t())
# l[0] = "Smith"
# t[0] = Error cant add or delete
# s =  error cant do
#

# t.append("Smith")
# print(l)

# -------  Advanced set operations

# local = {"biff"}
# abroad ={"Bob","Anne"}

# friends = local.union(abroad)
# print(friends)

# .intersection  (items that are similar in both sets.)
# .union          (add two sets)
# .difference  ( deletes like pairs)
# -----------------------Booleans  created by creating comparisons

# print(5 == 5)
# print(5 > 5 )
# print (10 != 10)

# comparisons == != >, >=, <=

# ---is keyword
# print(friend == abroad) USE THIS!
# print(friend is abroad) DONT USE


# -----if statements
# day_of_week = input("What day of the week is it today?").lower()

# if day_of_week == "monday":
#     print("have a great start to the week")
# elif day_of_week == "tuesday":
#    print("Its Tuesday.") 
# else:
#     print("full speed ahead!")

# print("this always runs.!")

# ---------if statements with--- in keyword


# movies_watched = {"The Matrix", "Green Book", "Her"}
# user_movie =  input("Enter something:")

# if user_movie in movies_watched:
#      print(f"Iv watched {user_movie} too!")
# else:
#     print("I havent watched that yet.")     

# -----------------the IN keyword
# number = 7
# user_input = input("Enter 'y' if you would like to play:").lower()

# if user_input == ("y"):
#     user_number = int(input("Guess our number:"))
#     if user_number == number:
#         print ("you guessed correctly")
#     elif abs(number - user_number) == 1:
#         print("you were off by one")
#     else:
#         print("Sorry, its wrong!")

# ------------------loops in python


# number = 7

# while True:
#     user_input = input("Would you like to play?: (Y/n) ")

#     if user_input == "n":
#         break

#     user_number = int(input("Guess our number:"))
#     if user_number == number:
#         print ("you guessed correctly!!!!!!!!!!! YAY")
#     elif abs(number - user_number) == 1:
#         print("you were off by one")
#     else:
#         print("Sorry, its wrong!")

# # -------------------- if with  in
#  friends = ["rolf","Jen","Bob","Anne"]

#  for friend in friends:
#         print(f"{friend} is my friend")


# grades = [35,67,98,100,100]
# total = sum(grades)
# amount = len(grades)
# print(total/amount)


# numbers = [1,2,3,4,5,6,7,8,9]

# evens = []

# for number in numbers:
#    if number % 2 == 0:
#         evens.append(number)

# user_input = input("Enter your choice:")
# if user_input == "a":
#     print("ADD")
# elif user_input == "q":
#     print("QUIT")

# ---------------------LIST Comprehensions  (FOR, IN)



# for num in numbers:   #iteration
#         doubled.append(num*2)   

#         OR 

# numbers = [1,2,3]
# doubled = [x*2 for x in numbers]

# friends = ["Bob","Rolf","Anne","sally","salty"]
# starts_s = []

# for friend in friends:
#         if friend.startswith("s"):
#                 starts_s.append(friend)
# print(starts_s)

#  a NEW LIST IS CREATED WITH LIST COMPREHENSION!!!!!!!!!!

friends = ["Bob","Rolf","Anne","Sally","Salty"]
starts_s = [friend for friend in friends if friend.startswith("S")]  ##adding a conditional into list Compreshension!!!!

print(friends)
print(starts_s)
print(friends is starts_s)
print("frinds:", id(friends), "starts_s:", id(starts_s))







print(starts_s)










# Basic String Operations
# Conditions
# Loops
# Functions
# Classes and Objects
# Dictionaries
# Modules and Packages
#    - FLASK,
#    - Beautiful Soup,  (parsing html Docs)
#    - DB, Data visualisation.

# DATA SCIENCE TUTORIALS-------------

# Numpy Arrays
# Pandas Basics

# ADVANCE TUTORIALS---------------

# Generators
# List Comprehensions
# Multiple Function Arguments
# Regular Expressions
# Exception Handling
# Sets
# Serialization
# Partial functions
# Code Introspection
# Closures
# Decorators
# Map, Filter, Reduce