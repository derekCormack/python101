#https://evolveu.udemy.com/course/rest-api-flask-and-python/learn/lecture/15927742#overview
# --------------functions

# def functionname (parameters):
#     "function_docstring"
#     funciton_suite
#     return [expression]

# By default, parameters have a positional behavior and you need to inform them in the same order that they were defined.
# Dont REUSE names!

#-------------------functions arguments params

# def add(x, y):  #parameters      
#     pass             #do NOTHING

# add(5,3)  #arguments!  used when CALLING a function

# def say_hello():
#     print(f"hello!",{name})

# say_hello("bob")

# #*** use keyword arguments where ever possible.
# eg divide(dividend=15, divisor=0)



# def add(x,y=8):
#         print(x+y)


# add(x=5)
# add(x=5, 5) NO!  you cant put a positional agrument after a named argument


# default_y =3

# def add(x,y=default_y):k  keep default at end
#         sum = x + y
#         print(sum)

# -------------------Functions returning Values

# def add(x,y):
#         print(x + y)
#         add(5,8)
#         result = add(5,8)
#         print(result)

#----------lambda functions operate on inputs provide output....no other actions
# nameless, just returns values.
# eg 

# def add(x,y):
#         return x+y

# SAME AS;

# add = lambda x, y: x + y    (can be used without variable assignment, made to be shorthand!)

# def double(x):
#     return x * 2
# OR
# sequence = [1,3,5,9]
# doubled =  [ (lambda x: x * 2)(x) for x in sequence]
# OR 
# doubled = list(map(lambda x: x * 2, sequence)





# ----------------------tate tutorial: below
# def add10(i):
#     return i+10

# def bprint(name, var):
#     want_to_print_string = "{0} == {1}".foramt(name, var)
#     print(want_to_print_string)

# if __name__ == '__main__':
#     ui = int(input("Enter a number: "))
#     uip10 = add10(ui)
#     print(uip10)

#     bprint("uiP10", uip10)


#------------------------Dictionary comoprehensions

# users = [
#   (0, "bob", "password"),
#   (0, "rolf", "bob123"),
#   (0, "jose", "longpassword"),
#   (0, "username", "1234"),
# ]

# username_mapping = {user[1]: user for user in users}
# print(username_mapping)

#---------------------upacking arguments


#def multiply(*args):  #function has a set of arguments that will be collected
 #   print(args)


#unpacking keywords
# def named(**kwargs):  ** collects keyword arguements into a dictonary
#     print(kwargs)

# detatils = {"name": "bob","age": 25}
# named(**details)  ** can be used in a function call to unpack a dictonary into keyword arguements

# def both(*arg,**kwargs):    *collect all positional arg,  and all named arguements into kwargs.
























