from tkinter import *

def Left_click(event):
    x = textbox2.get()
    y = textbox1.get()
    z = int(x) / (int(y)/100)**2
    #result.configure(text=int(x) / (int(y)/100)**2)
    if z < 18.5:
        result.configure(text ="ผอมเกินไป")
    elif 18.6 < z < 24:
        result.configure(text="เหมาะสม")
    elif 25 < z < 29.9:
        result.configure(text ="อ้วน")
    elif z > 30:
        result.configure(text ="อ้วนเกินไปนะ")


window = Tk()
window.title('BMI Calculator')

Height = Label(window,text = "Height(cm)").grid(row= 0,column =0)
textbox1 = Entry(window)
textbox1.grid(row=0,column=1)
weight = Label(window,text = "weight(kg)").grid(row =1,column =0)
textbox2 = Entry(window)
textbox2.grid(row = 1,column =1)
resultbutton = Button(window,text =" Calculate")
resultbutton.bind('<Button-1>', Left_click)
resultbutton.grid(row=3,column =0)
result = Label(window,text = "Result")
result.grid(row=3,column =1)

window.mainloop()