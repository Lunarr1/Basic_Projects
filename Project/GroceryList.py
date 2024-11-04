def main():
    grocery_list = []
    #create an empty list
    budget = float(input("Enter Your Budget: "))
    while True:
        item = input("Enter the item name (or type 'stop' to finish): ")
        if item.lower() == "stop":
            break
        price = float(input("Enter the price for "+ item + ": "))

        grocery_list.append([item, price])

    total_sum = sum([price for item, price in grocery_list])
    #find the sum of all the prices, for both item and price in the grocery_list
    remainder = budget - total_sum

    if budget >= total_sum:
            print(f"You have {remainder} left in your budget!")
    else:
            print(f"You are over budget by {abs(remainder)}. Your total is {total_sum}, but your budget is {budget}.")
    #using abs()}on the input can change a negative number to a positive number
main()