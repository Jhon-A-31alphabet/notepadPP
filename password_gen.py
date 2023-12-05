import random
import string
from tkinter import *

class passwords:
    def __init__(self,size) -> str:
        self.size: int = size
        self.character :tuple = string.ascii_letters + string.punctuation
    
    def generate_pass(self):
        pass__= random.sample(self.character,k=self.size)
        print(len(self.character))
        code ="".join(pass__)
        return code




class password_window:
    def __init__(self,main) -> None:
        self.main = main
    
    def run_password_window(self):
        #window
        self.win_pas= Toplevel(self.main)
        
        self.win_pas.geometry("550x290")
        self.win_pas.resizable(False,False)
        self.win_pas.title("codigo aleatorio")
        
        #widgets
         
        self.label__ = Label(self.win_pas,text="Tamaño del codigo",font=("Arial",10))
        self.label__.place(x=95,y=10)
        
        #list box
        self._list_box_numbers = Spinbox(self.win_pas,
                                        from_=4,to=84,increment=1,
                                        width=10)
        
        
        self._list_box_numbers.place(x=10,y=10)
        self.scroll__ = Scrollbar(self.win_pas)
        
        self.scroll__.pack(side=RIGHT, fill=Y) #scrollbar
        
        self.text_code =Text(self.win_pas,borderwidth=1,padx=5,pady=5,font=5,yscrollcommand=self.scroll__.set,height=10,width=70) #text widget
        
        self.text_code.config(font=("Helvetica",9)) #text font
        #get button
        self.button_get_code = Button(self.win_pas,text="Generar")
        self.button_get_code.place(x=250,y=10)
        
        self.text_code.place(x=10,y=50) #text place   
        
       #copy button
        self.button_copy = Button(self.win_pas,text="Copiar")
        self.button_copy.place(x=300,y=10)
        self.scroll__.config(command=self.text_code.yview)
        
        


        
        