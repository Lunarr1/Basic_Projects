def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main():
    while True:
        try:
            n = int(input(f"Input a number for factorial : "))
            if n >= 0:
                break
            else:
                print("That number cannot be factorialized!")
        except ValueError:
            print("That is not a value!")


    total = factorial(n)
    print(f"Your factorial total of {n} is {total}!")

main()

    
    