from tkinter import *
import datetime

root = Tk()
root.geometry("400x180")
root.title("Age Calculator")
root.resizable(0,0)
root.configure(background = 'orange')

def calculateage():
    birthdate = datetime.datetime(int(YearVariable.get()), int(MonthVariable.get()), int(DayVariable.get()))
    age = datetime.datetime.now() - birthdate
    convertdays = int(age.days)
    ageyears = round(convertdays/365, 2)
    Label(text =f"{NameVariable.get()} your age is {ageyears}").grid(row=7, column=1)

lb1 = Label(root, text = "Your Name", background = 'papayawhip').grid(row=2, column=1, padx=90, pady=5)
lb2 = Label(root, text = "Year", background = 'papayawhip').grid(row=3, column=1, padx=90,pady=5)
lb3 = Label(root, text = "Month", background = 'papayawhip').grid(row=4, column=1, padx=90,pady=5)
lb4 = Label(root, text = "Day", background = 'papayawhip').grid(row=5, column=1, padx=90,pady=5)

NameVariable = StringVar()
YearVariable = StringVar()
MonthVariable = StringVar()
DayVariable = StringVar()

EntryName = Entry(root, textvariable= NameVariable, background = 'lightgreen').grid(row=2, column=2, padx=0,pady=5)
EntryYear = Entry(root, textvariable= YearVariable, background = 'lightgreen').grid(row=3, column=2, padx=0,pady=5)
EntryMonth = Entry(root, textvariable= MonthVariable, background = 'lightgreen').grid(row=4, column=2, padx=0,pady=5)
EntryDay = Entry(root, textvariable= DayVariable, background = 'lightgreen').grid(row=5, column=2, padx=0,pady=5)

button1 = Button(root, text="Submit", command = calculateage, background = 'dodgerblue')
button1.grid(row=6, column=1,)
root.mainloop()

