def add10(i):
    return i+10

def bprint(name, var):
    want_to_print_string = "{0} == {1}".foramt(name, var)
    print(want_to_print_string)

if __name__ == '__main__':
    ui = int(input("Enter a number: "))
    uip10 = add10(ui)
    print(uip10)

    bprint("uiP10", uip10)


