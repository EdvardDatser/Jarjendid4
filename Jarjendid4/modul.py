

products = ["b", "c", "a"]
prices = [30,50,40]

def pood():
    c = int(input("Kui palju toodet te tahate?\n"))
   

    for i in range(c):
        product_name = input("Täida, mida soovid osta\n")
        product_price = float(input("Mis on toote hind?(EU)\n"))
        products.append(product_name)
        prices.append(product_price) 

    print("Ostetud tooted:", products)
    print("Toodete hinnad:", prices)


def kutsuta():
    purchased_products = []

    while True:
        print("Valikus olevad tooted:", products)
        product_name = input("Mida soovite osta?\n")

        if product_name in products:
            product_index = products.index(product_name)
            product_price = prices[product_index]
            purchased_products.append(product_name) 
            products.pop(product_index)
            prices.pop(product_index) 
            print(f"Teie ostukorvi lisati {product_name} hinnaga {product_price} EUR")
        elif product_name == "stop":
            break
        else:
            print("Sellist toodet ei ole saadaval. Palun valige midagi muud.")

    print("Ostetud tooted:", purchased_products)


def a_z():
    sorted_products = sorted(products, key=lambda x: x)
    sorted_prices = sorted(prices, key=lambda x: x)
    for i in range(len(sorted_products) - 1):
        print(f"{sorted_products[i]}: {sorted_prices[i]}")





def maks_min(choice):
    if choice == 'kallis':
        max_price = max(prices)
        max_price_index = prices.index(max_price)
        print(max_price_index, max_price)
    elif choice == 'odav':
        min_price = min(prices)
        min_price_index = prices.index(min_price)
        print(min_price_index, min_price)
    else:
        print("Palun vali <kallis> või <odav>")


def find(product):
    if product in products:
        index = products.index(product)
        print(prices[index])
    else:
        return "Siin ei ole toode mis sa validsid"

#last top 3 hind

def top3():
    copy=prices.copy()
    for i in range(3):
        ind=copy.index(max(copy))
        print(f"{products[ind]}: {prices[ind]}")
        copy.pop(ind)
        copy.insert(ind, min(copy) - 1)

#Напишите функцию pood(), при запуске которой происходит заполнение двух списков: покупки[], цены[]. Количество элементов в списках ограничивается пользователем (либо оговаривается сколько продуктов надо купить, либо в режиме online- данные вносятся пока не закончатся данные о покупках).
#После заполнения списков появляется меню с выбором действий:
#• Удалить из списка купленный товар и добавить в список купил[] и составить чек;
#• Отобразить в алфавитном порядке список покупок и их цены;
#• Найти самый дорогой/дешевый товар;
#• Найти цену запрашиваемого товара ;
#• Свой вариант.
#Для описания действий создайте необходимые функции.