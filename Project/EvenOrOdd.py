def main():
    value = input("Please enter the numbers you want:")
    list_of_values = value.split()

    #.split() functions to split the numbers in a string, for example:
    #if my value = 13 15 17 16 15,using list_value =  value.split(), my output will be ['13', '15', '17', '16', '15']

    int_list_of_values = [int(value) for value in list_of_values] #this is a list comprehension, which shortens the syntax

#     int_list = []
# for num in string_list:
#     int_list.append(int(num))
#^^^^^ this is the original way to append a loop, and a list comprehension is able to shorten the syntax.
#int() means changing the value to int, which means for every value thats contained in the list_of_values
#  it will be switched into an integer value, and will be stored as a function to int_list_of_values

    odd_count = 0
    even_count = 0
    #have 2 inputs to store values


    for number in int_list_of_values: #for loop
        if number % 2 == 0:
            even_count += 1 #if there is no remainder, then add one to even_count
        else:
            odd_count += 1 #if there is remainder, then add one to odd_count
    print(f"you have {odd_count} odd numbers and {even_count} even numbers!")
main()