import math

def main():
    num = int(input("Please enter an integer:"))
    if num < 2:
        print(f"{num} is not a prime number!")
        return

    is_prime = True

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % 2 == 0:
            is_prime = False
            break

    if is_prime == True:
        print(f"{num} is a prime number!")
    else:
        print(f"{num} is not a prime number!")
    
main()
