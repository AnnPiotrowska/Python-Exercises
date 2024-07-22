#program do walidacji użytkownika i hasła

username = input("Podaj nazwę użytkownika: ")
password = input("Podaj hasło: ")
repeat_password = input("Powtórz hasło: ")

if len(username) <= 6 or len(username) >= 30:
    valid_username = False
    print("Nazwa użytkownika powinna mieć długość z zakresu (6,30)")
else:
    valid_username = True

if len(password) <= 6 or len(password) >= 30:
    valid_password = False
    print("Hasło powinno mieć długość z zakresu (6,30)")
else:
    valid_password = True

if password != repeat_password:
    valid_repeat = False
    print("Hasła nie są takie same!")
else:
    valid_repeat = True


if valid_username and valid_password and valid_repeat:
    print("Dziękuję!")
else:
    print("Popraw swoje dane!")




