print("   Welcome to ABC shop   ")
print("-----Please login-----")
username = input("username : ")
password = input("password : ")
u1 = "123456"
p1 = "987654"
if username == u1 and p1 == password:
    print("Login complete")
    print(" >>> Please select menu <<< ")
    print("1.Fired rice = 35 Bth")
    print("2.Fired chicken = 50 Bth")
    print("3.Noodle soup = 45 Bth")
    print("4.Papaya salad = 30 Bth")
    print("5.Fired egg = 5 Bth")
    food = input("Please fill number or food name : ")
    if food == "1" or food == "Fired rice":
        print(">>> Fired rice: 35 bth")
        q1 = int(input("Order quantity: "))
        tt1 = q1*30
        print("Price is ", tt1, " Bth")
    elif food == "2" or food == "Fired chicken":
        print(">>> Fired chicken: 50 bth")
        q2 = int(input("Order quantity: "))
        tt2 = q2*50
        print("Price is ", tt2, " Bth")
    elif food == "3" or food == "Noodle soup":
        print(">>> Noodle soup: 45 bth")
        q3 = int(input("Order quantity: "))
        tt3 = q3*45
        print("Price is ", tt3, " Bth")
    elif food == "4" or food == "Papaya salad":
        print(">>> Papaya salad: 30 bth")
        q4 = int(input("Order quantity: "))
        tt4 = q4*30
        print("Price is ", tt4, " Bth")
    elif food == "5" or food == "Fired egg":
        print(">>> Fired egg: 5 bth")
        q5 = int(input("Order quantity: "))
        tt5 = q5*5
        print("Price is ", tt5, " Bth")
else:
    print("Login incomplete ;( ")


