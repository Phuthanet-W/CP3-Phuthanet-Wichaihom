menulist = []
totalprice = int()
print("========FOOD DOG=======")

def bill():
  print("========FOOD DOG=======")
  for number in range(len(menulist)):
    print(menulist[number][0],menulist[number][1])
  print("Total price is ", totalprice, "Bth")
while True:
  menuName = input("Please Enter menu : ").capitalize()
  if (menuName == "Exit"):
    break
  else:
    menuprice = int(input("price :"))
    menulist.append([menuName,menuprice])
    totalprice += menuprice


bill()
