from tkinter import *
from tkinter import messagebox
from random import *
from pandas import *
from json import *
from json import decoder

password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '#', '$', '%', '&', '(', ')', '*', '+']

class Gui:

    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width = 250, height = 250)
        self.check = ['0', '0', '0']

    def screen_settings(self):
        self.window.minsize(650, 550)
        self.window.title("password manager".title())

    def img_settings(self):
        self.img = PhotoImage(file = "logo.png")
        self.canvas.create_image(125, 125, image = self.img)
        self.canvas.place(x = 200, y = 20)

    def info_label(self):
        self.web = Label(text = "Website:").place(x = 65, y = 275)
        self.mail = Label(text = "Email:").place(x = 65, y = 325)
        self.pas = Label(text = "Password:").place(x = 65, y = 375)
 
    def info_entry(self):
        self.e_web = Entry(width = 20)
        self.e_web.place(x = 165, y = 275)
        self.e_web.focus()
        self.e_mail = Entry(width = 38)
        self.e_mail.place(x = 165, y = 325)
        self.e_pas = Entry(width = 20)
        self.e_pas.place(x = 165, y = 375)

    def info_buttons(self):
        self.gen_pas = Button(text = "Generate Password", width = 14)
        self.gen_pas.place(x = 408, y = 371)
        self.add = Button(text = "Add", width = 45)
        self.add.place(x = 65, y = 425)
        self.search = Button(text = "Search", width = 14)
        self.search.place(x = 408, y = 271)
    
    def hold_screen(self):
        self.window.mainloop()

    def generate(self):
        a = ""
        self.e_pas.delete(0,END)
        for _ in range(10):
            a += choice(password)
        return a 

    def add_inf(self):
        self.check = [self.e_web.get(), self.e_mail.get(), self.e_pas.get()]

        dict = {
            self.check[0].title():{
                "email": self.check[1],
                "password": self.check[2]
            }
        }

        if self.check[0] != '' and self.check[1] != '' and self.check[1] != '':
            try:
                a = load(open("My_Passwords.json"))
            except decoder.JSONDecodeError:
                dump(dict, open("My_Passwords.json", "w"), indent = 5)
                messagebox.showinfo(message = "Your data was added succefully")
            else:
                if self.check[0].title() not in a:
                    a.update(dict)
                    dump(a, open("My_Passwords.json", "w") ,indent = 5)
                else:
                    messagebox.showerror("Oops", "You already have data for this website")
                self.e_mail.delete(0,END)
                self.e_web.delete(0,END)
                self.e_pas.delete(0,END)
                messagebox.showinfo(message = "Your data was added succefully")
        else:
            messagebox.showerror("Oops", "Please don't leave any of the fields empty")

    def search_file(self):
        web = self.e_web.get().title()
        try:
            a = load(open("My_Passwords.json"))
        except decoder.JSONDecodeError:
            messagebox.showerror("Oops", "No such file")
        else:
            if web in a:
                messagebox.showinfo("Info", f"email: {a[web]['email']}\npas: {a[web]['password']}")
            else:    
                messagebox.showerror("Oops", "No such file")

