

        # Создать меню со следующими пунктами
        # 1 - Создать аккаунт 
        # 2 - Войти в аккаунт
        # 3 - Посмотреть список созданных почт аккаунтов отсортированных по алфавиту
        # 4 - Удалить аккаунт
        # 5 - Изменить пароль 
        # 6 - Выйти

        # Пункт 1
        # Запрашивает логин и пароль и создает аккаунт из этих данных и сохраняет где-то
        # после пишит - аккаунт создан
        
        # Пункт 2
        # Запрасить логин и пароль и проверить, если ли созданный аккаунт с такими значениями - если есть, 
        # пишет имя добро пожаловать. Если нет - пишет ошибка логин или пароль

        # Пункт 3
        # Алгоритм выводить только логины всех созданных аккаунтов

        # Пункт 4
        # Алгоритм запрашивает логин и пароль от аккаунта который нужно Удалить
        # Если такого аккаунта нет - пишет об этом
        # Если мы указали верный логин и пароль, то текущий аккаунт удаляется

        # Пункт 5
        # Запрашиваем логин и пароль от аккаунте где хотим поменять пароль
        # Если данные от аккаунта ввели корректноm, то тогда запрашиваем новый пароль
        # Если ввели некорректные логин или пароль - выдаем ошибку

        # Пункт 6
        # Останавливает работу алгоритма

import os

accounts = [
    ['Dima@gmail.com','pass124','Dima'],
    ['Pasha@gmail.com','pashok228','Pasha'],
    ['Kolya@gmail.com','koll','Kolya'],
]

while True:
    os.system('cls')

    print("Меню игры:")
    print("1 - Создать аккаунт")
    print("2 - Войти в аккаунт")
    print("3 - Посмотреть список созданных почт аккаунтов отсортированных по алфавиту")
    print("4 - Удалить аккаунт")
    print("5 - Изменить пароль")
    print("6 - Выйти")

    menu = int(input("Enter: "))

    if menu == 1:
        mail = input("Введите почту: ")
        password = input("Введите пароль: ")
        name = input("Введи свое имя: ")
        a = [mail, password, name]
        accounts.append(a)
        print("Аккаунт создан")

    if menu == 2:
        mail_entered = input("Введите почту: ")
        password_entered = input("Введите пароль: ")

        is_auth = False
        for user in accounts:
            [mail, password, name] = user

            if mail_entered == mail and password_entered == password:
                is_auth = True 
                print(f"{name}, добро пожаловать")
            
        if is_auth == False:
            print("Неверный логин или пароль")
    if menu == 3:
        for account in accounts:
            print(account[0])
        input("Нажмите enter, чтобы вернуться в меню")
    if menu == 4:
        mail_to_delete = input("Введите почту: ")
        password_to_delete = input("Введите пароль: ")

        is_deleted = False
        for user in accounts:
            if user[0] == mail_to_delete and user[1] == password_to_delete:
                accounts.remove(user)
                is_deleted = True
                print("Аккаунт удален.")
                break

        if not is_deleted:
            print("Аккаунт с такими данными не найден.")
        input("Нажмите Enter для продолжения.")
    if menu == 5:
        mail_entered = input("Введите почту: ")
        password_entered = input("Введите пароль: ")

        is_auth = False
        for user in accounts:
            [mail, password, name] = user

            if mail_entered == mail and password_entered == password:
                is_auth = True 
                new_password = input("Введи новый пароль: ")
                user[1] = new_password
                print(f"{name},success change")
            
        if is_auth == False:
            print("Неверный логин или пароль")
        input("Нажмите Enter для продолжения.")
    if menu == 6:
        print("До скорых встреч!")
        break