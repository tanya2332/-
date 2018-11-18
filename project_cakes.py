print("Введите цену за тесто для 1 кекса")
dough = float(input())
while dough < 0:
    print("Цена не может быть отрицательной!")
    print("Введите цену за тесто для 1 кекса")
    dough = float(input())
print("Введите цену за крем для 1 кекса")
cream = float(input())
while cream < 0:
    print("Цена не может быть отрицательной!")
    print("Введите цену за крем для 1 кекса")
    cream = float(input())
print("Введите цену за посыпку для 1 кекса")
top = float(input())
while top < 0:
    print("Цена не может быть отрицательной!")
    print("Введите цену за посыпку для 1 кекса")
    top = float(input())

price1 = (dough + cream + top)

print("Введите необходимое количество кексиков")
n = float(input())
while n < 0:
    print("Не может быть отрицательного количества кексиков!")
    print("Введите необходимое количество кексиков")
    n = float(input())
while n*10 % 10 != 0:
    print("Не может быть нецелого количества кексиков!")
    print("Введите необходимое количество кексиков")
    n = float(input())

if n < 10:
    price = n * price1
if n < 20 and n > 9:
    price = 9 * price1 + (n-9) * price1 * 0.95
if n > 19:
    price = 9 * price1 + 10 * price1 * 0.95 + (n-19) * price1 * 0.9

if price*10 % 10 == 0:
    price = int(price)

print("Цена за кексики:",price)

  

