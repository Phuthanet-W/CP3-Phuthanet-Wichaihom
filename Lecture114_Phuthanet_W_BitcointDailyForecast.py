from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
from tkinter import *
from datetime import datetime, timedelta

btc_rate = BtcConverter()
currency_rate = CurrencyRates()

def Left_click(event):
    btc_rate = BtcConverter()
    year = int(input_year.get())
    month = int(input_month.get())
    day = int(input_day.get())
    period = int(input_forecast_period.get()) #forecast จากกี่วันย้อนหลัง
    refer_date = datetime(year, month, day-2) #Current date ใส่ -2 เนื่องจากไม่สามารถดึงราคาปัจจุบันได้ bitcoin price deley 2 day
    sum_previous_price = 0
    for i in range(period):
        date = refer_date - timedelta(days=i)
        previous_price = btc_rate.get_previous_price('THB', date)
        sum_previous_price += previous_price
    sample_moving_average = sum_previous_price/period
    result.configure(text=sample_moving_average)

window = Tk()
window.title('Forecast Bitcoin Price')
window.minsize(width=230, height=200)

current_btc = btc_rate.get_latest_price('THB')
show_btc_current = "Current price BITCOIN = " + str(current_btc) + "  Baht"
button_current_btc_price = Label(window, text=show_btc_current, fg='Green', bg='White',
                                 font=("Helvetica", 12), anchor=W).grid(row=0, column=1)

ex_year_month_day = Label(window, text="ex: 1955/5/1 (year/month/day)").grid(row=1, column=1)
year = Label(window, text="Year",).grid(row=2, column=0)
input_year = Entry(window)
input_year.grid(row=2, column=1)

month = Label(window, text="Month").grid(row=3, column=0)
input_month = Entry(window)
input_month.grid(row=3, column=1)

day = Label(window, text="Day").grid(row=4, column=0)
input_day = Entry(window)
input_day.grid(row=4, column=1)

forecast_period = Label(window, text=" Period (Day)").grid(row=5, column=0)
input_forecast_period = Entry(window)
input_forecast_period.grid(row=5, column=1)

resultbutton = Button(window, text=" Next month price (THB)")
resultbutton.bind('<Button-1>', Left_click)
resultbutton.grid(row=6, column=0)
result = Label(window, text="Result")
result.grid(row=6, column=1)

window.mainloop()