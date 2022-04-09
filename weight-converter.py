from tkinter import *      #used to create GUI application (blank textbox type)
# Creating a GUI Window
window = Tk()
window.title("Weight converter")
def from_kg():              #function (in kg) start
    gram = float(e2_value.get())*1000     #get function is used to retrieve value from dictionary
    pound = float(e2_value.get())*2.20462
    ounce = float(e2_value.get())*35.274
    tonne = float(e2_value.get())/1000
    milligram = float(e2_value.get())*(1e+6)
    microgram = float(e2_value.get())*(1e+9)
    t1.delete("1.0",END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)
    t4.delete("1.0", END)
    t4.insert(END, tonne)
    t5.delete("1.0", END)
    t5.insert(END, milligram)
    t6.delete("1.0", END)
    t6.insert(END, microgram)

e1 = Label(window, text="Input the weight in KG",bg='light green')  #label: used for writing text
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text="Gram")
e4 = Label(window, text="Pound")
e5 = Label(window, text="Ounce")
e6 = Label(window, text="tonne")
e7 = Label(window, text="milligram")
e8 = Label(window, text="microgram")

t1 = Text(window, height=5, width=30,bg='sky blue')
t2 = Text(window, height=5, width=30,bg='pink')
t3 = Text(window, height=5, width=30,bg='sky blue')
t4 = Text(window, height=5, width=30,bg='pink')
t5 = Text(window, height=5, width=30,bg='sky blue')
t6 = Text(window, height=5, width=30,bg='pink')

b1 = Button(window, text="Convert", command=from_kg,bg='yellow')

e1.grid(row=0, column=0)    #grid: it is used to display the grid lines
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
e6.grid(row=1, column=3)
e7.grid(row=1, column=4)
e8.grid(row=1, column=5)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
t4.grid(row=2, column=3)
t5.grid(row=2, column=4)
t6.grid(row=2, column=5)
b1.grid(row=0, column=2)

window.mainloop()         #variety of GUI to build an interface like buttons and widgets



