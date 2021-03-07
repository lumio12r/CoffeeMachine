print("Write how many ml of water the coffee machine has: ")
water = int(input())
print("Write how many ml of milk the coffee machine has: ")
milk = int(input())
print("Write how many grams of coffee beans the coffee machine has: ")
beans = int(input())
print("Write how many cups of coffee you will need: ")
how_many = int(input())


maximally_water = water//200
maximally_milk = milk//50
maximally_beans = beans//15
how_maximally = min(maximally_water, maximally_milk, maximally_beans)
how_more = how_maximally - how_many

if how_maximally == how_many:
    print("Yes, I can make that amount of coffee ")
elif how_maximally < how_many:
    if how_maximally == 1:
        print("No, I can make only {} cup of coffee".format(how_maximally))
    else:
        print("No, I can make only {} cups of coffee".format(how_maximally))
elif how_maximally > how_many:
    print("Yes, I can make that amount of coffee (and even {} more than that)".format(how_more))

