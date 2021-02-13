def vatCalculator(price):
    price = int(input("Please enter price: "))
    result = price+(price*0.07)
    return result
print(vatCalculator(int()))