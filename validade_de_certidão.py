from tkinter import *
from datetime import datetime, timedelta

root = Tk()
root.title("Validade de certidão v1.3")

myLabel = Label(root, text="Qual a data de emissão dessa certidão? (no formato dd/mm/aaaa)")
myLabel.grid(row=0, column=5, columnspan=9)

e = Entry(root, width=35, borderwidth=3)
e.grid(row=1, column=5, columnspan=9)

myLabel2 = Label(root, text="Quantos dias de validade?")
myLabel2.grid(row=2, column=5, columnspan=9)

e2 = Entry(root, width=35, borderwidth=3)
e2.grid(row=3, column=5, columnspan=9)

def Calcular():
    date1 = e.get()
    days1 = int(e2.get())
    date2 = datetime.strptime(date1, '%d/%m/%Y')
    days2 = timedelta(days=days1)
    final_day = date2 + days2
    myLabel3 = Label(root, text=f"Essa certidão é valida até {final_day.day}/0{final_day.month}/{final_day.year}")
    myLabel3.grid(row=5, column=5, columnspan=9)
    e.delete(0, END)
    e2.delete(0, END)

myButton = Button(root, text="Calcular", command=Calcular, fg="green")
myButton.grid(row=4, column=3, columnspan=9)

exitButton = Button(root, text="Fechar", command=root.quit)
exitButton.grid(row=4, column=7, columnspan=9)

root.mainloop()
myLabel3.grid_forget()