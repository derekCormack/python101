# primitive way
ages = [10, 20, 30]
names = ["John", "Tait", "Justin"]
occupation = ["Student", "Student", "C++ Programmer"]

# OO (Object-Oriented) way
class Person:
    # all methods in a class must pass self as the first paramater
    def __init__(self, _age=0, _name="", _lname="", _occupation=""): # equiv. to constructor() in javascript
        self.age = _age
        self.name = _name
        self.lname = _lname
        self.occupation = _occupation
    
    def has_birthday(self):
        self.age += 1

    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def get_occupation(self):
        return self.occupation
    def get_lname(self):
        return self.lname
    
    def gets_married_to(self, other_person):
        if type(other_person) == Person: # as long as other_person is a Person object
            self.lname = other_person.get_lname() # set lastname equal to other_person's lastname
    
    def __str__(self):
        info = ""
        info += "First Name: " + self.name + "\n"
        info += "Last Name: " + self.lname + "\n"
        info += "Age: " + str(self.age) + "\n"
        info += "Job: " + self.occupation + "\n"
        return info

if __name__ == '__main__':
    p1 = Person(20, "Tait", "S.", "Tutor")
    print(p1)
    print("Tait has a brithday")
    p1.has_birthday()
    print(p1)

    p2 = Person(23, "Carly", "D.", "Student")
    print(p2)

    print("Carly married Tait")
    p2.gets_married_to(p1)
    print(p2)