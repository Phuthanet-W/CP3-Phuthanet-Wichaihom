menulist = []
pricelist = []
totalprice = int()


def bill():
  print("========FOOD DOG=======")
  for number in range(len(menulist)):
    print(menulist[number],"=",pricelist[number])
while True:
  menuName = input("Please Enter menu : ").capitalize()
  if (menuName == "Exit"):
    break
  else:
    menuprice = int(input("price :"))
    menulist.append(menuName)
    pricelist.append(menuprice)
    totalprice += menuprice

bill()
print("Totaprice is " ,totalprice, "Bth")