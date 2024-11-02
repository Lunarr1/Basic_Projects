def factorial(n):
    result = 1
    for i in range (1, n + 1):
        result *= i
    return result

def main():
    while True:
        try:
            integer = int(input(f"Please enter an integer:"))
            if integer >= 0 :
                break
        except ValueError:
            print("This is not a integer! Please try again!")

    n = 1
    factorial_n = factorial(n)

    while factorial_n <= integer:
        n += 1
        factorial_n = factorial(n)

    closest_factorial = factorial(n - 1)
    remainder = integer - closest_factorial

    if remainder == 0:
        print(f"The factorial for {integer} is {n-1}!")
    else:
        print(f"The factorial for {integer} is {n-1}, and will have a remainder of {remainder}!")
main()