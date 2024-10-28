def main():
    while True:
        try:
            number = int(input(f"Enter a temperature in Celsius:"))
            break
        except ValueError:
            print ("That is not a valid number!")

    farhrenheit = (number * 9 / 5) + 32
    print(f"{number} converted into Fahrenheit is {farhrenheit}!")

main()
            