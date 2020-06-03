# --------------------------- ОСТАТОК РЕСУРСОВ В МАШИНЕ ------------------------- #
water = 400
milk = 540
beans = 120
empty_cups = 9
money = 550

action = ''


# ----------------------------------- ФУНКЦИИ ----------------------------------- #
def remaining():  # функция показа остатков в кофе-машине
    print(f'''
    The coffee machine has:
    {water} of water
    {milk} of milk
    {beans} of coffee beans
    {empty_cups} of disposable cups
    ${money} of money''')


def espresso():  # функция приготовления еспрессо
    global water, beans, empty_cups, money
    if water >= 250 and beans >= 16 and empty_cups >= 1:
        print('I have enough resources, making you a coffee! \n')
        water -= 250
        beans -= 16
        money += 4
        empty_cups -= 1


def latte():  # функция приготовления латте
    global water, milk, beans, empty_cups, money
    if water >= 350 and milk >= 75 and beans >= 20 and empty_cups >= 1:
        print('I have enough resources, making you a coffee!')
        water -= 350
        milk -= 75
        beans -= 20
        money += 7
        empty_cups -= 1
    elif water < 350:
        print('Sorry, not enough water!')
    elif milk < 75:
        print('Sorry, not enough milk!')
    elif beans < 20:
        print('Sorry, not enough beans!')


def cappuccino():  # функция приготовления каппучино
    global water, milk, beans, empty_cups, money
    if water >= 200 and milk >= 100 and beans >= 12 and empty_cups >= 1:
        print('I have enough resources, making you a coffee!')
    water -= 200
    milk -= 100
    beans -= 12
    money += 6
    empty_cups -= 1


def buy():  # ФУНКЦИЯ ПОКУПКИ КОФЕ (BUY)
    coffee_type = input('\n What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n')
    if coffee_type == '1':
        espresso()
    elif coffee_type == '2':
        latte()
    elif coffee_type == '3':
        cappuccino()
    else:
        pass


def fill():  # ФУНКЦИЯ ПОПОЛНЕНИЯ ЗАПАСОВ (FILL)
    global water, milk, beans, empty_cups
    water += int(input('Write how many ml of water do you want to add:'))
    milk += int(input('Write how many ml of milk do you want to add:'))
    beans += int(input('Write how many grams of coffee beans do you want to add:'))
    empty_cups += int(input('Write how many disposable cups of coffee do you want to add:'))


def take():  # ФУНКЦИЯ ВЫДАЧИ ДЕНЕГ (TAKE)
    global money
    print('I gave you S', money)
    money = 0


def main_menu():
    global action
    action = input('\n Write action (buy, fill, take, remaining, exit): \n')
    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    elif action == 'remaining':
        remaining()

# -------------------------- КОД ПРОГРАММЫ ----------------------------------- #
while action != 'exit':
    main_menu()
