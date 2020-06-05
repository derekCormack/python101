
num = 10

name = 10

cars = ["Tesla", "BMW", "Ferrari", "Toyota"]
street_illegal_cars = ["Fast Cars"]

if __name__ == '__main__':
    ui = int(input("Please enter a number ")) # will always return a string type :)
    if ui is num:
        print("Good job!")
    else:
        print("You failed")

    car = input("Please enter a car name: ")
    if car in cars:
        print("Valid car!")
    elif car in street_illegal_cars:
        print("Valid car; not street legal!")
    else:
        print("Not a valid car!")
    
    '''
    Javascript -> Python
    ==/=== -> is
    x.contains(y) -> y in x
    '''