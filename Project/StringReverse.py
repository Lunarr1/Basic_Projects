def main():
    user_input = input("Please enter a string to reverse: ")
    reversed_string = user_input[:: -1]
    print(f"The reverse string of {user_input} is {reversed_string}!")
main()