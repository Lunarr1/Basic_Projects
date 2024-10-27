def square():
    while True:
        try:
            number = int(input(f"Please enter a number: "))
            if number > 1 :
                break
            else:
                print(f"Please enter a number thats more than 1!")
        except ValueError:
            print("That is not a number. Please Try Again.")

    squared = number * number
    print(f"The square of {number} is {squared}!")

    if number % 2 == 0 :
        print(f"{number} is an even number")
    else :
        print(f"{number} is an odd number")

while True:
    square()
    second_input = input(f"Do you want to square another number? (Yes/No): ").strip().lower()
    if second_input != "yes":
        break