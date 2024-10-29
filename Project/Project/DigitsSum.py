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
    total_sum = 0

    for digit in value_str :  #create a variable digit, for the loop in value_str
        total_sum += int(digit)  #everytime it loops, for example 1234, the loop will go through the digits individually
                           #changing it to int so that the system can add integers together, which will be 1+2+3+4, and added into sum
    
    print(f"The sum of the digit in {value} is {total_sum}!")
main()
            