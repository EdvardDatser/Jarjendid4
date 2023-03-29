from modul import *


while True:
    print("Menuu:")
    print("0 - Sule menüü")
    print("1 - Täida tootenimekirjad")
    print("2 - Kustuta juba ostetud kauba nimekirjast")
    print("3 - Leia kõige kallim/odavam kaup")
    print("4 - Sorteerimine tähestikulises järjekorras")
    print("5 - Otsib etteantud kauba hinda")
    menu = int(input("Valige menüüpunkt: "))

    if menu == 0:
        break
    elif menu == 1:
        pood()
    elif menu==2:
        kutsuta()
    elif menu == 3:
        choice=str(input("Vale kallis või odav\n"))
        maks_min(choice)
    elif menu ==4:
        a_z()
    elif menu ==5:
        print(products)
        product=str(input("Valige product\n "))
        find(product)
    elif menu ==6:
        top3()
    else:
        print("Vale valik. Palun valige uuesti.")

#Напишите функцию pood(), при запуске которой происходит заполнение двух списков: покупки[], цены[]. Количество элементов в списках ограничивается пользователем (либо оговаривается сколько продуктов надо купить, либо в режиме online- данные вносятся пока не закончатся данные о покупках).
#После заполнения списков появляется меню с выбором действий:
#• Удалить из списка купленный товар и добавить в список купил[] и составить чек;
#• Отобразить в алфавитном порядке список покупок и их цены;
#• Найти самый дорогой/дешевый товар;
#• Найти цену запрашиваемого товара ;
#• Свой вариант.
#Для описания действий создайте необходимые функции.