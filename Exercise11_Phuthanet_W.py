numberstar = int(input("Number : "))
text = ""
qtyspace = numberstar
space = " "*qtyspace
for i in range(numberstar):
    if i == 0:
        qtyspace = qtyspace - 1
        space = " " * qtyspace
        text = "*"*(i+1)
        print(space + text)
    else:
        qtyspace = qtyspace - 1
        space = " " * qtyspace
        text = "*"*(i+1)+("*"*i)
        print(space + text)
