amount_of_money = 550
amount_of_water = 400
amount_of_milk = 540
amount_of_beans = 120
amount_of_cups = 9

print("The coffee machine has:")
print(f"{amount_of_water} of water")
print(f"{amount_of_milk} of milk")
print(f"{amount_of_beans} of coffee beans")
print(f"{amount_of_cups} of disposable cups")
print(f"{amount_of_money} of money")

print("Write action (buy, fill, take):")
choice = input()

if choice.lower() == "buy":
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino")
    coffee_choice = int(input())
    if coffee_choice == 1:
        amount_of_water -= 250
        amount_of_beans -= 16
        amount_of_money += 4
        amount_of_cups -= 1
    elif coffee_choice == 2:
        amount_of_water -= 350
        amount_of_milk -= 75
        amount_of_beans -= 20
        amount_of_money += 7
        amount_of_cups -= 1
    elif coffee_choice == 3:
        amount_of_water -= 200
        amount_of_milk -= 100
        amount_of_beans -= 12
        amount_of_money += 6
        amount_of_cups -= 1
elif choice.lower() == "fill":
    print("Write how many ml of water do you want to add:")
    amount_of_water += int(input())
    print("Write how many ml of milk do you want to add:")
    amount_of_milk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    amount_of_beans += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    amount_of_cups += int(input())
elif choice.lower() == "take":
    print(f"I gave you ${amount_of_money}")
    amount_of_money = 0

print("")
print("The coffee machine has:")
print(f"{amount_of_water} of water")
print(f"{amount_of_milk} of milk")
print(f"{amount_of_beans} of coffee beans")
print(f"{amount_of_cups} of disposable cups")
print(f"{amount_of_money} of money")