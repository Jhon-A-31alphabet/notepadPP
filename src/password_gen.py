import random
import string
from tkinter import *
from basics import read_config_file

class Passwords:


    def __init__(self, size) -> str:
        self.size: int = size
        self.characters: tuple = string.ascii_letters + string.punctuation
    
    def generate_password(self):
        password = random.sample(self.characters, k=self.size)
        code = "".join(password)
        return code




def insert_password(text, size):
    password_instance = Passwords(size)
    generated_code = password_instance.generate_password()
    text.insert("1.0", generated_code)

def copy_password(text_widget, master) -> None:
    content = text_widget.get("1.0", "end-1c")
    master.clipboard_clear()
    master.clipboard_append(content)
    master.update()




class PasswordWindow:
    def __init__(self, main) -> None:
        self.main = main

    def run_password_window(self):
        fg_text=read_config_file.data["FG"]
        bg_text=read_config_file.data["BG"]
        cursor_text = read_config_file.data["CURSOR"]
        # Window
        self.win_pass = Toplevel(self.main)
        self.win_pass.geometry("550x290")
        self.win_pass.resizable(False, False)
        self.win_pass.title("Password Generator")
        
        # Widgets
        self.label_size = Label(self.win_pass, text="Password Length", font=("Arial", 10))
        self.label_size.place(x=95, y=10)
        
        # List box
        self.list_box_numbers = Spinbox(self.win_pass,
                                        from_=4, to=84, increment=1,
                                        width=10)
        self.list_box_numbers.place(x=10, y=10)
        self.scroll_bar = Scrollbar(self.win_pass)
        self.scroll_bar.pack(side=RIGHT, fill=Y)  # Scrollbar
        
        # Text widget
        self.text_password = Text(self.win_pass, borderwidth=1, padx=5, pady=5, font=5, yscrollcommand=self.scroll_bar.set, height=10, width=70)
        self.text_password.config(font=("Helvetica", 9),fg=fg_text,bg=bg_text,insertbackground=cursor_text)  # Text font
        
        # Get button
        self.button_get_password = Button(self.win_pass, text="Generate", command=lambda: insert_password(self.text_password, int(self.list_box_numbers.get())))
        self.button_get_password.place(x=230, y=10)
        
        self.text_password.place(x=10, y=50)  # Text place
        
        # Copy button
        self.button_copy = Button(self.win_pass, text="Copy", command=lambda: copy_password(self.text_password, self.main))
        self.button_copy.place(x=300, y=10)
        self.scroll_bar.config(command=self.text_password.yview)
