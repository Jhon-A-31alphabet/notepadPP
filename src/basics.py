from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter.colorchooser import askcolor
from tkinter import messagebox
from tkinter import ttk
import time
import json


class read_config_file:
    
     with open('config.json', 'r') as archivo:
        datos = json.load(archivo)
    

class theme_conf:
    
    @staticmethod
    def darkmode(text,window):
        

        with open('config.json', 'r') as archivo:
            datos = json.load(archivo)
            datos['FG'] = 'white'
            datos['BG'] ='black'

        with open('config.json', 'w') as archivo:

            json.dump(datos, archivo, indent=4)
        
        text.config(bg=datos['BG'],fg=datos['FG'],insertbackground="white")
        window.config(bg=datos['BG'])

    @staticmethod
    def light_mode(text,window):
        

        with open('config.json', 'r') as archivo:
            datos = json.load(archivo)
            datos['FG'] = 'black'
            datos['BG'] ='white'

        with open('config.json', 'w') as archivo:

            json.dump(datos, archivo, indent=4)
        
        text.config(bg=datos['BG'],fg=datos['FG'],insertbackground="black")
        window.config(bg=datos['BG'])






            

    
    

    




def save_text_to_file(text_widget: None) -> None:
    file_dialog = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("textfile", ".txt")])
    file_path = f"{file_dialog}.txt"
    file_text = text_widget.get(1.0, "end-1c")
    file_dialog.write(file_text)
    file_dialog.close()




def open_file(text_widget) -> None:
    file_path = filedialog.askopenfilename()
    if file_path:
        if file_path.endswith(".txt"):
            with open(file_path, 'r') as file:
                content = file.read()
                text_widget.delete('1.0', END)
                text_widget.insert('1.0', content)


def copy_text_to_clipboard(text_widget, master) -> None:
    content = text_widget.get("1.0", "end-1c")

    master.clipboard_clear()
    master.clipboard_append(content)
    master.update()


def get_date(text_widget) -> None:
    date = time.strftime("%c")
    text_widget.insert('1.0', f"Date and Time: {date} ")
