class CoffeeMachine:
    ESPRESSO_WATER = 250
    ESPRESSO_BEANS = 16
    LATTE_WATER = 350
    LATTE_MILK = 75
    LATTE_BEANS = 20
    CAPPUCCINO_WATER = 200
    CAPPUCCINO_MILK = 100
    CAPPUCCINO_BEANS = 12

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def opening(self, action):
        while True:
            if action == "buy":
                num = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                self.buy(num)
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.status()
            elif action == "exit":
                exit()
            else:
                print("Please try again.")
                self.opening(input("Write action (buy, fill, take, remaining, exit):"))

    def status(self):
        print("The coffee machine has:")
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')
        self.opening(input("Write action (buy, fill, take, remaining, exit):"))

    def espresso(self):
        if self.water < self.ESPRESSO_WATER:
            print("Sorry, not enough water!")
        elif self.beans < self.ESPRESSO_BEANS:
            print("Sorry, not enough beans")
        else:
            self.water -= self.ESPRESSO_WATER
            self.beans -= self.ESPRESSO_BEANS
            self.cups -= 1
            self.money += 4
            print("I have enough resources, making you a coffee!")

    def latte(self):
        if self.water < self.LATTE_WATER:
            print("Sorry, not enough water!")
        elif self.milk < self.LATTE_MILK:
            print("Sorry, not enough milk")
        elif self.beans < self.LATTE_BEANS:
            print("Sorry, not enough beans")
        else:
            self.water -= self.LATTE_WATER
            self.milk -= self.LATTE_MILK
            self.beans -= self.LATTE_BEANS
            self.cups -= 1
            self.money += 7
            print("I have enough resources, making you a coffee!")

    def cappuccino(self):
        if self.water < self.CAPPUCCINO_WATER:
            print("Sorry, not enough water!")
        elif self.milk < self.CAPPUCCINO_MILK:
            print("Sorry, not enough milk")
        elif self.beans < self.CAPPUCCINO_BEANS:
            print("Sorry, not enough beans")
        else:
            self.water -= self.CAPPUCCINO_WATER
            self.milk -= self.CAPPUCCINO_MILK
            self.beans -= self.CAPPUCCINO_BEANS
            self.cups -= 1
            self.money += 6
            print("I have enough resources, making you a coffee!")

    def buy(self, num):
        if num == "1":
            self.espresso()
            self.opening(input("Write action (buy, fill, take, remaining, exit):"))
        elif num == "2":
            self.latte()
            self.opening(input("Write action (buy, fill, take, remaining, exit):"))
        elif num == "3":
            self.cappuccino()
            self.opening(input("Write action (buy, fill, take, remaining, exit):"))
        elif num == "back":
            self.opening(input("Write action (buy, fill, take, remaining, exit):"))

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grans of coffee beans do you want to add:")
        self.beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(input())
        self.opening(input("Write action (buy, fill, take, remaining, exit):"))

    def take(self):
        print(f'I gave you ${self.money}')
        self.money -= self.money
        self.opening(input("Write action (buy, fill, take, remaining, exit):"))


coffee_machine = CoffeeMachine()
coffee_machine.opening(input("Write action (buy, fill, take, remaining, exit):"))
