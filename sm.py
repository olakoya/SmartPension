request = 5

while request > 0:
    with open('cred.txt', 'r') as file:
        passwords = file.readlines()
        # print(passwords)
        userpromt = input('Enter a password: ')
        passwordlenght = len(userpromt)

        for password in passwords:
            # print(password)
            pswd = password.rstrip('\n')
            # print(pswd)
            if passwordlenght < 8:
                print('password is weak')
                break
            elif pswd == userpromt:
                print('commonly use password')
                break
            elif userpromt != pswd and passwordlenght > 8:
                print('password is valid')
                break
    if request > 5:
        break