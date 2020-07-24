# python OOP -  notes from https://evolveu.udemy.com/course/rest-api-flask-and-python/learn/lecture/5960090#overview

# class Student:
#     def __init__(self)     **function inside of a class = METHOD  eg init method.
#         self.name = "Rolf"  ** .name NAME PROPERTY
#         self.grades = (90,90,93,78,90)

#     def average(self):
#         return sum(self.gardes) /len(self.grades)



# student = Student()


# **using class throught the init method, to create an object to assign the name property inside object to the string "rolf".
# student will become a name for the 'self' object we have created.
# 1. call the class.
# 2. init method runs
# 3. you get back the object it has created.
# 4. in the init function you can set properties   self.name, self.grades...etc


# all methods inside a class MUST accept a parameter.....which is object that was originally created.

# def __init(self,name):

#     self.name = name
#     self.items = []

# def add_item(self,name,price):
#     #create a dcitionayr with keys name and price and append that to self.items
#     item = {'name':name, 'price":price'}
#     self.items.append(item)

# def stock_price(self):

# class ClassTest:
#     def instance_method(self):   # INSTANCE METHOD   #self=object  #when you want to perform the action by passing a param.
#         print(f"Called instance_method of {self}")  # using the object with a paremeter

#     @classmethod  #like a factory
#         def class_method(cls): #  method that uses class for something
#         print(f"called class_method of {cls}")


#     # @staticmethod  # seperate function that lives within the class....no info on class or object...
#     #     def static_method():  # method no param, cls or self, just a function inside a class, that doesnt use class or instance for anything.
#     #      print("called static method.")  # not used much.

# ClassTEst.class_method()   call the class method of this class 


# test= ClassTest()  # creates an object of the Class instance
# test.instance_method()
# ClassTest.instance_method() #


# ---class properties.

# class Book:
#     TYPES = ("hardcover", "paperback")      # put inside because you think only the Book class will use this var.

# def __init__(self, name, book_type, weight):  #create an init method,  will create an instance and give it back to you.
#     self.name = name
#     self.book_type = book_type
#     self.weight = weight

# def __repr__(self):
#     return f"<book {self.name},{self.book_type}, weighing {self.weight} g>"

#     @classmethod
#     def hardcover(cls,name,page_weight):
#         return cls(name, cls.TYPES[0], page_weight + 100)

#     @classmethod
#     def paperback(cls,name,page_weight):
#         return cls(name, cls.TYPES[0], page_weight)


# book = Book.hardcover("harryhardcover", 1500)
# light = Book.paperback("pyton 101", 600)

# print(book)
# print(light)

# -------classes and objects


# def __init__(self, name):  #create an init method,  will create an instance and give it back to you.
# #     self.name = name
# #     self.item = []
# #     
# def add item(self, name, price):
#     item = {'name:' name, 'price': price}
#     self.items.append(item)

# def stock_price(self):
#     total = 0  #start with zero
#     for item in self.items:  #go over each item
#         total += item['price']  #add to the total the price of the item
#     return total
    
    
# --------------static methods and Class methods

# class ClassTest:    #object of type ClassTest
#     def instance_method(self):               function(def),  uses self  = instance method
#         print(f"Caalled instance_method of {self}")

#     @classmethod
#     def class_method(cls):
#         print(f"Called class_method of {cls}")
#     ClassTEst.class_method(classtest)


#    # 2 ways of calling the above instance method:

#     test = ClassTest()  #creates a new object of type Classtest (an instance of Classtest)
#     test.instance_method()   #calls the instance method of the Classtest Object.
#     ClassTest.instance_method(test)  #calls the instance method of the Classtest Object.

# instance methods are used for MOST THINGS.....

# class methods are used often as factories.

# static method  used to place a method INSIDE a class....for code organisation.


    

# class Book:
#          TYPES = ("hardcover", "paperback")

# print(Book.TYPES)



# return cls(store.name +"- franchise")



# def store_details(store):
#     return '{}, total stock price: {}'  .format(store.name, int(store.stock_price()))


#-----------------------------------inheritence.

# class Device:
#         def __init__(self, name, connected_by):
#             self.name = name
#             self.connected_by = connected_by
#             self.connected = True

# def __str__(self):
#     return f"Device {self.name!r} ({self.econnected_by})"  !r calls the rpr method of self.name so it shows quotes already

# def disconnect(self):
#         self.connected = False
#         print("Dicsconnected.")

        

# class Printer(Device):   #  inherits Device METHODS!  printer is the child OF device
#     def __init__(self,anem,connected_by, capacity):
#         super().__init__(name, connected_by)  #gets the device(super class and call the init method.)
#         self.capacity = capacity
#         self.remaining_pages =capacity

#     def __str__(self):
#         return f"{super().__str__()} ({self.remaining_pages} pages reamining)"

#     def print (self,pages):
#         if not self.connected:
#             print("your printer is not connected!")
#             return
#         print ("printing {pages} pages.")
#         self.remaining_pages -= pages

 
#-----------------------COMPOSITION (used much more that inhereitence)
# # a book shelf is composed of many things....including books.
# class BookShelf:
#     def __init__(self,books):
#         self.books  = books 
#     def __str__(self):
#         return f"BookShelf with {self.books} books."

# shelf = BookShelf(300)

# class Book(BookShelf):
#     def __init__(self, name,)

# class Book(BookShelf):
#     def __init__(self,name,quantity):
#         super().__init__(quantity)
#         self.name = name
#     def __str__(self):
#         return f"Book {self.name}"


#------------------type hinting

def list_avg(sequence: list) -> float:
    return sum(sequences) / len (sequence)









