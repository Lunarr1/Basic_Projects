name = input("what is your name? : ")
#getting input from user
age = input("How old are you?: ")

# age = age + 1
#fundementally doesnt work because every user input received is always string
age = int(age)
age = age + 1
#type cast it into a int, so that you are able to add numbers into it

print(f"Hello {name}!")
print("Happy Birthday!")
print(f"You are {age} years old")