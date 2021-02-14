menu = []
dictfood = {'Chicken' : 39, 'Beef':89, 'Meal':59, 'Egg':10}
totalprice = int()
def showprice():
    print("=" * 30)
    for i in range(len(menu)):
        food = menu[i]
        print(food,dictfood[food])
    print("="*30)
    print("Total Price is ", totalprice, " Bth")

while True:
  menuName = input("Please Enter menu : ").capitalize()
  if menuName == "Exit" :
      break
  else:
      menu.append(menuName)
      print(dictfood[menuName])
      totalprice += dictfood[menuName]


showprice()