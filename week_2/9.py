password = input("Wpisz hasło: ")

strong_password = password.replace('a', '@')
strong_password = strong_password.replace('s', '$')

print('Silne hasło to: ', strong_password)
