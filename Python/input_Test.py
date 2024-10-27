#mission: build a system where the system gets the user name, date of birth and age, and whether if today is the user's birthday

#get the input first
name = input("whats your name? : ")
age =  input("whats your age?: ")
is_birthday = input("is today your birthday? : Yes/No  |  ")

age = int(age)

print(f"Hello {name}!")
if is_birthday.lower() == "yes":
    age = age + 1
    print("Happy Birthday!")
    print(f"Congratulations on your {age}th year old!")
else:
    print(f"You are {age} years old.")

