def times_3(a_num):
    print(a_num * 3)

def pow(num, exp):
    return num ** exp

cars = ["Volvo", "BMW", "Honda", "Toyota", "Lambo"]
names = ["Tait", "Josiah", "Carly", "Derek"]
format_string = "My name is {0}, I am {1} years old, and I like {2}"

if __name__ == '__main__':
    print("Hello World!")
    times_3("Hello") # "Hello" * 3 = "HelloHelloHello"
    print(pow(15, 5)) # will run
    print(cars[0])
    print(cars[1])
    print(len(cars))
    print(cars[len(cars)-1])
    print(cars[-1]) # same as above
    # times = *
    print(10 * 20) # 200
    # add = +
    print(20 + 20) # 40
    # minus = -
    print(10 - 5) # 5
    # divide = /
    print(22 / 11) # 2
    # exp = **
    print(10 ** 5) # 100000

    # times
    print("Hi" * 10) # HiHiHiHiHiHiHiHiHiHi
    # plus
    print("Hello" + " World") # Hello World
    # minus, divide, exp do not work

    ## https://docs.python.org/3/library/string.html#formatstrings
    st = "{0} lived to be {1} years old".format("Wilbur", 22)
    print(st) # Wilbur lives to be 22 years old

    st2_5 = "{1} lived to be {0} years old".format(22, "Wilbur")
    st2_5 += " more text"
    print(type(st2_5)) # str/string/String

    st2 = "I have {0:.2f} dollars in my bank account".format(55.436752) # 55.43 as the value

    st3 = format_string.format(names[0], 20, "programming") # "My name is Tait, I am 20 years old, and I like programming"
