# Count Digits: Write a program that counts how many digits are in a given positive integer.
#  For example, if the user enters 56789, the output should be 5.

def count(value):
    sum = 0
    for i in str(value):
        sum += 1
    return sum

def main():
    while True:
        try:
            value = int(input(f"Please enter an integer: "))
            if value > 0 :
                break
            else:
                print("Please print a value thats more than 0!")
        except ValueError:
            print("ValueError! This is not a number!")
    total = count(value)
    print(f"you have {total} digits in your integer!")

main()