from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter.colorchooser import askcolor
from tkinter import messagebox
from tkinter import ttk
import time


def save_text_to_file(text_widget: None) -> None:
    file_dialog = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("textfile", ".txt")])
    file_path = f"{file_dialog}.txt"
    file_text = text_widget.get(1.0, "end-1c")
    file_dialog.write(file_text)
    file_dialog.close()


def dark_mode(text_widget, window) -> None:
    window.config(bg="black")
    text_widget.config(bg="black", fg="white")
    text_widget.config(insertbackground="white")


def light_mode(text_widget, window) -> None:
    window.config(bg="white")
    text_widget.config(bg="white", fg="black")
    text_widget.config(insertbackground="black")


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
