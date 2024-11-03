def main():
    a = 0
    b = 1
    value = int(input("Please enter an integer:"))

    print(a)
    print(b)

    for i in range(value - 2):
        total_sum = a + b
        print(total_sum)
        a = b #assign b to a, so that a will become the second number
        b = total_sum #assign total_sum to b, so that b will become the total number
        #using this formula, it will loop until it reaches the value, and add the total number and the last number.

main()