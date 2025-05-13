print("Welcome to Gadgets World")
gadget = input("Enter go to carry on")
if (gadget == "Go" or gadget == "go"):
    print("Here is two products for you")
    print("1 - Mobile")
    print("2 - Laptop")
    mo = input("Enter Your Gadgets Type")
    if (mo == "Mobile" or mo == "mobile"):
        print("Here is two choices")
        print("Vivo")
        print("Realme")
        brand = input("Enter your Brand")
        if (brand == "Vivo" or brand == "vivo"):
            print("Your Price is 20,000")
        elif (brand == "Realme" or brand == "realme"):
            print("Your Price is 30,000")
        else:
            print("Invalid Brand")
    elif (mo == "Laptop" or mo == "laptop"):
        print("Here is two choices for you")
        print("HP")
        print('Macbook Air')
        lap = input("Enter Your Laptop Brand")
        if (lap == "HP" or lap == "hp"):
            print("Your Price is 50.000")
        elif (lap == "Macbook Air" or lap == "macbook air"):
            print("Your Price is 1,00,000")
        else:
            print("Out Of Stock")
