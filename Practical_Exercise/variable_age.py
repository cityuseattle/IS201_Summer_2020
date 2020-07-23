print('How old are you?')
age = int(input())

if age < 2:
    print("He is a baby")
elif age < 4:
    print("He is a toddler")
elif age < 13:
    print("He is a kid")
elif age < 20:
    print("He is a teenager")
elif age < 65:
    print("He is an adult")
elif age >= 65:
    print("He is an elder")

