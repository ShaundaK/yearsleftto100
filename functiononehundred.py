def users_age(years_left):
    if years_left >= 99:
        number = 100 - years_left
        print("You will be 100 years old in", number, "year!")
        quit()
    else:
        remainingyears = 100 - years_left
        return remainingyears
name = input("What is your name?  ")
age = input("How old are you?  ")
nage = int(age)
users_age(nage)
remainingyears = 100 - nage
print("You will be 100 years old in", remainingyears, "years!")
