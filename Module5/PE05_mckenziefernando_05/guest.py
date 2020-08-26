file = 'guest_Book1'
with open('guest_Book1','a') as f:
    while True:
        name = input ('Hello, what is your name?')
        if name == 'q':
            break
        f.write(name + '\n')
        print(f"Hello, {name} you are now added")
