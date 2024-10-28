# Create a program that repeatedly asks the user for a number.
#  Each time the user enters a number, multiply it with the total product of all previous inputs.
#  The program should keep asking for a new number until the user types "stop."

def main():
    total = 1
    while True:
        try:
            value = input(f"Please enter an input to multiply(or type 'stop' to end):")
            if value.lower() == 'stop' :
                break
            value = int(value)
            total *= value
        except ValueError:
            print("ValueError! This is not a number!")
    print(f"your total is {total}!")
main()
    