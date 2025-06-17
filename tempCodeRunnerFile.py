def celsius_to_fahrenheit(celsius_list):
    fahrenheit_list = list(map(lambda c: (c * 9/5) + 32, celsius_list))
    print("Temperatures in Fahrenheit:", fahrenheit_list)