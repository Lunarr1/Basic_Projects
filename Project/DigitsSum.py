def main():
    while True:
        try:
            value = int(input(f"Please input a positive integer: "))
            if value > 0:
                break
            else:
                print("Please input a positive integer!")
        except ValueError:
            print("ValueError! This is not a Digit!")

    value_str = str(value)
    sum = 0

    for digit in value_str :
        sum += int(digit)
    
    print(f"The sum of the digit in {value} is {sum}!")


main()
            