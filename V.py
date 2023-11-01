from tkinter import *
from tkinter import filedialog
import tkinter as tk
from C import Controller
from tkinter import messagebox
from PIL import ImageTk, Image


class View:
    def __init__(self):
        self.root = Tk()
        self.c = Controller()

        self.mainScreen()
        self.root.mainloop()


    def mainScreen(self):

        self.root.geometry("600x700")
        self.root.title("MainD")
        self.root.configure(bg="black")
        self.root.bind('<Escape>', self.c.exit)
        self.mainFrame = tk.Frame(self.root, height=600, width=700, bg="black")
        self.mainFrame.grid(row=0, column=0, columnspan=2,padx=150)

        self.create_label(self.mainFrame,"MainD", ('Calibri', 40), 10, 10, "pack")

        self.create_label(self.mainFrame, "Product Name:", ('Calibri', 15), 10, 10, "pack")
        self.entryName = self.create_entry(self.mainFrame, 'center', 'grey', 1, 50)
        
               
        self.create_label(self.mainFrame, "Stock:", ('Calibri', 15), 10, 10, "pack")
        self.entryEstoque = self.create_entry(self.mainFrame, 'center', 'grey', 1, 50)
           
        self.create_button(self.mainFrame, "Cadastrar", ('Calibri', 10), '#121313', 'white', 10, 20, lambda:[self.cadastrar(self.entryName.get(),self.entryEstoque.get(), self.c.getFile()), self.clearFields()], "pack")
        
        self.create_button(self.mainFrame, "Limpar Campos", ('Calibri', 10), '#121313', 'white', 10, 10, lambda:[self.clearFields()], "pack")     


    def create_label(self, frame, text, font, pady, padx, metod):
        label = Label(frame, text=text, font=font, justify='center', bg='black', fg='white', pady=pady, padx=padx)
        if metod == "pack": 
            label.pack()
        elif metod == "grid":
             label.grid()

    def create_entry(self, frame, justify, bg, borderwidth, width):
        entry = Entry(frame, justify=justify, bg=bg, borderwidth=borderwidth, width=width)
        entry.pack()
        return entry


    def create_button(self, frame, text, font, bg, fg, pady, padx, command, metodo):
        button = Button(frame, borderwidth=0, text=text, font=font, justify='center', bg=bg, fg=fg, pady=pady, padx=padx, command=command)
        
        if metodo == "pack":
             button.pack(pady=10)
        elif metodo == "grid":
             button.grid(pady=10)


    def alert(self, Name):
        alert = messagebox
        id = self.c.bd.find(Name, "Ident")
        alert.showwarning('Salvo', "ID: "+str(id))


    def clearFields(self):
        self.entryName.delete(0, tk.END)
        self.entryEstoque.delete(0, tk.END)

    
    def cadastrar(self, nome, estoque, getfile):
        self.confirm = self.c.cadastrar(nome, estoque, getfile)

        if self.confirm == False:
              messagebox.showwarning('Falha','Preencha todos os campos')
              self.clearFields()
        else:
            self.alert(self.entryName.get())

if __name__ == "__main__":
        view = View()