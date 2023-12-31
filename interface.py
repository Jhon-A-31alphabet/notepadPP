from tkinter import *
from tkinter import ttk
from basics import *
import password_gen


class UI:
    
    def __init__(self, master):
        self.password_window = password_gen.PasswordWindow(master)

        # Menu Bar
        self.menu_bar = Menu(master)
        master.config(menu=self.menu_bar)

        # File Menu
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=lambda: open_file(self.text_box))
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save", command=lambda: save_text_to_file(self.text_box))
        self.file_menu.add_command(label="Exit", command=master.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Edit Menu
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Copy", command=lambda: copy_text_to_clipboard(self.text_box, master))
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        # View Menu
        self.view_menu = Menu(self.menu_bar, tearoff=0)
        self.view_menu.add_command(label="Dark Mode", command=lambda: dark_mode(self.text_box, master))
        self.view_menu.add_command(label="Light Mode", command=lambda: light_mode(self.text_box, master))
        self.menu_bar.add_cascade(label="Themes", menu=self.view_menu)

        # Tools Menu
        self.tools_menu = Menu(self.menu_bar, tearoff=0)
        self.tools_menu.add_command(label="Date and Time", command=lambda: get_date(self.text_box))
        self.tools_menu.add_command(label="Random Password", command=lambda: self.password_window.run_password_window())
        self.menu_bar.add_cascade(label="Tools", menu=self.tools_menu)

        # Text Box
        self.scrollbar = Scrollbar(master)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.text_box = Text(master, borderwidth=1, padx=10, pady=0, font=60, yscrollcommand=self.scrollbar.set,
                             relief="flat")
        self.text_box.config(font=('Times New Roman', 12))
        self.text_box.place(x=10, y=10)

        self.scrollbar.config(command=self.text_box.yview)


try:
    root = Tk()

    root.title("Pynotepad")
    root.config(bg="white")
    root.geometry("690x470")
    root.resizable(False, False)
    ui_instance = UI(root)

except Exception as e:
    root.showerror("Invalid", f"There was an error: {e}")

finally:
    root.mainloop()
