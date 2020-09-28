while True:
    a = input()
    g = ('0' in a or '1' in a or '2' in a or '3' in a or '4' in a or '5' in a or '6' in a or '7' in a or '8' in a or '9' in a)
    if 'qwerty' in a:
        print("Слабый пароль")
        continue
    elif '1234' in a:
        print("Слабый пароль")
        continue
    elif len(a)<8:
        print("Короткий пароль")
        continue
    elif not g:
        print("Пароль должен содержать цифры")
        continue
    break
