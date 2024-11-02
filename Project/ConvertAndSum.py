def main():
    value = input("Please input a series of numbers seperated by commas: ")
    listValue = value.split(",")

    intListValue = [int(num.strip()) for num in listValue] #list compehrension
    #we'll be using num.strip() so that it strips off the extra value to check for integers
    #we do that is because:
    # 1. if you only use int(num), you can only accept specific input from users such as 1,2,3,4
    # if the user inputs: 1 2 3 4 , the system will show an error

    #can add try catch error with this code:
    # try:
    #     intListValue = {int(value.strip() for num in listValue)}
    # except ValueError
    #     print("One or more inputs are not valid numbers. Please try again!")
    #     return

    total_sum = 0
    #avoid using sum as a name as it might conflict with the function "sum"

    for num in intListValue :
        total_sum += num
    
    print(f"the sum of {value} is {total_sum}!")
main()