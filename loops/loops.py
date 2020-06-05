
sin_numbers = [995883276, 227736222, 989333287, 229300928]

names = ["Tait", "Derek", "Justin"]

if __name__ == '__main__':
    print("using x in y")
    for x in sin_numbers:
        print(x)

    print("using range")    
    for x in range(10):
        print(x)

    print("Using range(len())")
    for x in range(len(sin_numbers)):
        print("[{0}]: {1}".format(x, sin_numbers[x]))

    while True:
        for name in names:
            print(name)
        ui = input("Add a new name (q to exit): ")
        if ui is "q":
            break
        names.append(ui)

    print("Thank you for adding names")
    print("Come again next time")
    for x in range(len(names)):
        print("[{0}]: {1}".format(x, names[x]))
