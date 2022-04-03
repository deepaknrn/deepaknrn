MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
            }

money=[2.5]
menu=True

def check_cost(total_cost,choice):
  change=round(total_cost-MENU[choice]["cost"],2)
  if change<=0:
    print("Sorry that's not enough money ,money refunded")
    return 0
  elif change==0:
    money[0]=round(money[0]+MENU[choice]["cost"],1)
    return 1
  else:
    money[0]=round(money[0]-change+MENU[choice]["cost"],1)
    print(f"\n Here is {change} $ in change")
    return 1

def update_resources(water,milk,coffee):
  resources["water"]=resources["water"]-water
  resources["milk"]=resources["milk"]-milk
  resources["coffee"]=resources["coffee"]-coffee

while menu:

  def check_resources(input_water,input_milk,input_coffee):
    available_water= resources["water"]
    available_milk=resources["milk"]
    available_coffee=resources["coffee"]
    if input_water>available_water:
      print("Sorry there is not enough water")
      return 0
    elif input_milk>available_milk:
      print("Sorry there is not enough milk")
      return 0
    elif input_coffee>available_coffee:
      print("Sorry there is not enough coffee")
      return 0
    else:
      update_resources(input_water,input_milk,input_coffee)
      return 1

  choice=input("\n What would you like : espresso/latte/cappuccino: ")
  if choice=="report":
    water=resources["water"]
    milk=resources["milk"]
    coffee=resources["coffee"]

    print(f"\n Water: {water} ml \n Milk : {milk} ml \n Coffee : {coffee} g \n Money : ${money[0]}")
    
  if choice=="latte":
    print("\n Report Before Purchasing Latte")
    water=resources["water"]
    milk=resources["milk"]
    coffee=resources["coffee"]
    print(f"\n Water: {water} ml \n Milk : {milk} ml \n Coffee : {coffee} g \n Money : ${money[0]}")
    resource_check=check_resources(200,150,24)
    if resource_check==0:
      pass
    else:
      print("\n Please insert coins")
      quarters=float(int(input("\n How many quarters?"))*0.25)
      dimes=float(int(input("\n How many dimes?:"))*0.10)
      nickles=float(int(input("\n How many nickles?:"))*0.05)
      pennies=float(int(input("\n How many pennies?:"))*0.01)
      total_cost=round(quarters+dimes+nickles+pennies,1)
      print(f"\n Total Cost Paid is {total_cost}")
      cost_check=check_cost(total_cost,choice)
      if cost_check==0:
        pass
      else:
        print("\n Report After Purchasing Latte")
        water=resources["water"]
        milk=resources["milk"]
        coffee=resources["coffee"]
        print(f"\n Water: {water} ml \n Milk : {milk} ml \n Coffee : {coffee} g \n Money : ${money[0]} ")
  elif choice=="espresso":
    print("\n Report Before Purchasing Espresso")
    water=resources["water"]
    milk=resources["milk"]
    coffee=resources["coffee"]
    print(f"\n Water: {water} ml \n Milk : {milk} ml \n Coffee : {coffee} g \n Money : ${money[0]}")
    resource_check=check_resources(50,0,18)
    if resource_check==0:
      pass
    else:
      print("\n Please insert coins")
      quarters=float(int(input("\n How many quarters?"))*0.25)
      dimes=float(int(input("\n How many dimes?:"))*0.10)
      nickles=float(int(input("\n How many nickles?:"))*0.05)
      pennies=float(int(input("\n How many pennies?:"))*0.01)
      total_cost=round(quarters+dimes+nickles+pennies,1)
      print(f"\n Total Cost Paid is {total_cost}")
      cost_check=check_cost(total_cost,choice)
      if cost_check==0:
        pass
      else:
        print("\n Report After Purchasing Espresso")
        water=resources["water"]
        milk=resources["milk"]
        coffee=resources["coffee"]
        print(f"\n Water: {water} ml \n Milk : {milk} ml \n Coffee : {coffee} g \n Money : ${money[0]} ")
  elif choice=="cappuccino":
    print("\n Report Before Purchasing Cappucino")
    water=resources["water"]
    milk=resources["milk"]
    coffee=resources["coffee"]
    print(f"\n Water: {water} ml \n Milk : {milk} ml \n Coffee : {coffee} g \n Money : ${money[0]}")
    resource_check=check_resources(250,100,24)
    if resource_check==0:
      pass
    else:
      print("\n Please insert coins")
      quarters=float(int(input("\n How many quarters?"))*0.25)
      dimes=float(int(input("\n How many dimes?:"))*0.10)
      nickles=float(int(input("\n How many nickles?:"))*0.05)
      pennies=float(int(input("\n How many pennies?:"))*0.01)
      total_cost=round(quarters+dimes+nickles+pennies,1)
      print(f"\n Total Cost Paid is {total_cost}")
      cost_check=check_cost(total_cost,choice)
      if cost_check==0:
        pass
      else:
        print("\n Report After Purchasing Cappuccino")
        water=resources["water"]
        milk=resources["milk"]
        coffee=resources["coffee"]
        print(f"\n Water: {water} ml \n Milk : {milk} ml \n Coffee : {coffee} g \n Money : ${money[0]} ") 
  elif choice=="off":
    menu=False
    exit
