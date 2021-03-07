print("Write how many cups of coffee you will need:")
how_many = int(input())
water = how_many * 200
milk = how_many * 50
beans = how_many * 15
if how_many == 1:
    print(f"For {how_many} cup of coffee you will need:")
else:
    print(f"For {how_many} cups of coffee you will need:")
print(f"{water} ml of water")
print(f"{milk} ml of milk")
print(f"{beans} g of coffee beans")
