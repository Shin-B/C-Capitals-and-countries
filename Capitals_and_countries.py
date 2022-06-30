from tkinter import *
import random

root=Tk()
root.title("Random Countries and Capitals")
root.geometry("500x500")

enter_country = Entry(root)
enter_country.place(relx=0.5,rely=0.1,anchor=CENTER)

enter_capital = Entry(root)
enter_capital.place(relx=0.5,rely=0.2,anchor=CENTER)

label_country_list = Label(root)
label_capital_list = Label(root)
random_country = Label(root)
random_capital = Label(root)

capital_list=[]
country_list=[]

def add():
    country = enter_country.get()
    country_list.append(country)
    label_country_list["text"] = "Country List: " + str(country_list)
    capital = enter_capital.get()
    capital_list.append(capital)
    label_capital_list["text"] = "Capital List: " + str(capital_list)
    
def randomcc():
    length = len(country_list)
    random_no = random.randint(0, length-1)
    generated_random_number = country_list[random_no]
    random_country["text"] = " Random Country: " + str(generated_random_number)  
    
    length1 = len(capital_list)
    random_no1 = random.randint(0, length1-1)
    generated_random_number1 = capital_list[random_no1]
    random_capital["text"] = " Random Capital: " + str(generated_random_number1)
    
btn = Button(root,text="Add to the Country and Capital List", command = add)
btn.place(relx=0.5,rely=0.3,anchor=CENTER)

btn1 = Button(root,text="Random Pick", command = randomcc)
btn1.place(relx=0.5,rely=0.7,anchor=CENTER)

label_country_list.place(relx=0.5,rely=0.4,anchor=CENTER)
label_capital_list.place(relx=0.5,rely=0.5,anchor=CENTER)
random_country.place(relx=0.5,rely=0.8,anchor=CENTER)
random_capital.place(relx=0.5,rely=0.9,anchor=CENTER)




















root.mainloop()