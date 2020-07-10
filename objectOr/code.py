class Student:
    def __init__(self)     **function inside of a class = METHOD  eg init method.
        self.name = "Rolf"  ** .name NAME PROPERTY
        self.grades = (90,90,93,78,90)

    def average(self):
        return sum(self.gardes) /len(self.grades)



student = Student()


**using class throught the init method, to create an object to assign the name property inside object to the string "rolf".
student will become a name for the 'self' object we have created.
1. call the class.
2. init method runs
3. you get back the object it has created.
4. in the init function you can set properties   self.name, self.grades...etc


# all methods inside a class MUST accept a parameter.....which is object that was originally created.

# def __init(self,name):

#     self.name = name
#     self.items = []

# def add_item(self,name,price):
#     #create a dcitionayr with keys name and price and append that to self.items
#     item = {'name':name, 'price":price'}
#     self.items.append(item)

# def stock_price(self):

class ClassTest:
    def instance_method(self):   # INSTANCE METHOD   #self=object
        print(f"Called instance_method of {self}")

    @classmethod  #like a factory
        def class_method(cls):
        print(f"called class_method of {cls}")
    @staticmethod  # seperate function that lives within the class....no info on class or object...
        def static_method():
         print("called static method.")

ClassTEst.class_method()   calls it


