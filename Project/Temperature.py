def main():
    while True:
        try:
            number = int(input("Enter a temperature in Celsius:"))
            break
        except ValueError:
            print ("That is not a valid number!")

    farenheit = (number * 9 / 5) + 32
    print(f"{number} convereted into Farenheit is {farenheit}!")

main()
            