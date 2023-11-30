from tkinter import *
from tkinter import ttk
from fuctions import *


class ui:

    def __init__(self, master):

        # Barra de menú
        self.menu_bar = Menu(master)
        master.config(menu=self.menu_bar)

        # Menú Archivo
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Abrir", command=lambda: abrir_archivo(self.caja_texto))
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Guardar", command=lambda: guardar(self.caja_texto))
        self.file_menu.add_command(label="Salir", command=master.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)

        # Menú Editar
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Copiar", command=lambda: copiar_texto(self.caja_texto, master))
        self.menu_bar.add_cascade(label="Editar", menu=self.edit_menu)

        # Menú temas
        self.view_menu = Menu(self.menu_bar, tearoff=0)
        self.view_menu.add_command(label="Modo Noche", command=lambda: oscuro(self.caja_texto, master))
        self.view_menu.add_command(label="Modo Claro", command=lambda: modo_claro(self.caja_texto, master))
        self.menu_bar.add_cascade(label="Temas", menu=self.view_menu)

        # Menú Herramientas
        self.tools_menu = Menu(self.menu_bar, tearoff=0)
        self.tools_menu.add_command(label="Fecha y hora", command=lambda:get_date(self.caja_texto))
        self.menu_bar.add_cascade(label="Herramientas", menu=self.tools_menu)

        # Caja de texto
        self.scrollbar = Scrollbar(master)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.caja_texto = Text(master, borderwidth=1, padx=10, pady=0, font=60, yscrollcommand=self.scrollbar.set,
                               relief="flat")
        self.caja_texto.config(font=('Times New Roman', 12))
        self.caja_texto.place(x=10, y=10)

        self.scrollbar.config(command=self.caja_texto.yview)
        
        

        #---------------------------------------------------------------------instancias---------------------

try:
    root = Tk()

    root.title("Pynotepad")
    root.config(bg="white")
    root.geometry("690x470")
    root.resizable(False, False)
    ar = ui(root)

except Exception as e:
    root.showerror("Invalido", f"Hubo un error: {e}")

finally:
    root.mainloop()
