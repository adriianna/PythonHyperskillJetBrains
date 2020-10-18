class CoffeeMachine:
    def __init__(self, money=550, water=400, milk=540, beans=120, cups=9):
        self.money = money
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.machine_state("start")

    def machine_state(self, state):
        if state == "start":
            machine_action = str(input('Write action (buy, fill, take, remaining, exit):'))
            self.machine_state(machine_action)
        elif state == "remaining":
            self.supplies_status()
        elif state == "take":
            self.take()
        elif state == "buy":
            flavour = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
            self.buy(flavour)
        elif state == "fill":
            add_water = int(input("Write how many ml of water do you want to add:"))
            add_milk = int(input("Write how many ml of milk do you want to add:"))
            add_beans = int(input("Write how many grams of coffee beans do you want to add:"))
            add_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
            self.fill(add_water, add_milk, add_beans, add_cups)
        elif state == "exit":
            pass

    def supplies_status(self):
        status = "The coffee machine has:\n{0} of water\n{1} of milk\n{2} " \
                 "of coffee beans\n{3} of disposable cups\n{4} of money".\
                 format(self.water, self.milk, self.beans, self.cups, self.money)
        print(status)
        self.machine_state("start")

    def take(self):
        print("I gave you $", self.money)
        self.money = 0
        self.machine_state("start")

    def fill(self, add_water, add_milk, add_beans, add_cups):
        self.water += add_water
        self.milk += add_milk
        self.beans += add_beans
        self.cups += add_cups
        self.machine_state("start")

    def buy(self, flavour):
        # espresso
        if flavour == "1":
            if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
                self.machine_state("start")
            else:
                print("Sorry, not enough water!")
                self.machine_state("start")
            # late
        elif flavour == "2":
            if self.water >= 350 and self.beans >= 20 and self.milk >= 75 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
                self.machine_state("start")
            else:
                print("Sorry, not enough water!")
                self.machine_state("start")
        # cappucino
        elif flavour == "3":
            if self.water >= 200 and self.beans >= 12 and self.milk >= 100 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
                self.machine_state("start")
            else:
                print("Sorry, not enough water!")
                self.machine_state("start")
        elif flavour == "back":
            #jesli back to zacznij od poczatku
            self.machine_state("start")
        else:
            print("Choose 1,2 or 3 :)")
            self.machine_state("buy")


testMachine = CoffeeMachine()

