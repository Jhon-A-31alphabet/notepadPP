
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter.colorchooser import askcolor
from tkinter import messagebox
from tkinter import ttk


def guardar(x:None) ->None:
    a = filedialog.asksaveasfile(defaultextension=".txt",filetypes=[("textfile",".txt")]) # solamenta abrira archivos de text
    b = f"{a}.txt"
    file_Text =x.get(1.0,"END") # 1.0 PRINCIPIO
    a.write(file_Text)
    a.close()



def oscuro(x,y) -> None:
    ventana = y.config(bg="black")
    caja_texto = x.config(bg ="black",fg="white")
    
    barra_texto = x.config(insertbackground = "white")
   

def modo_claro(x,y):
    ventana = y.config(bg="white")
    caja_texto = x.config(bg ="white",fg="black")
    
    barra_texto = x.config(insertbackground = "black")


def personalizar_fondo(x,y):
    fondo_color =askcolor(title="color de fondo")
    caja_Texto_color =askcolor(title="caja de texto")
    fuente_caja_texto = askcolor(title="fuente")

    x.configure(bg=fondo_color[1])
    y.configure(bg=caja_Texto_color[1])
    y.configure(fg=fuente_caja_texto[1])



def abrir_archivo(text_widget):
    
        file_path = filedialog.askopenfilename()
        if file_path:
            if file_path.endswith(".txt"):
                with open(file_path, 'r') as file:
                    content = file.read()
                    text_widget.delete('1.0',END)  
                    text_widget.insert('1.0', content)
        


def copiar_texto(texto,master):
    contenido = texto.get("1.0", "end-1c")  # Obtiene el contenido de la caja de texto

    
    master.clipboard_clear()  # Limpia el portapapeles
    master.clipboard_append(contenido)  # Agrega el contenido al portapapeles
    master.update()
    
     


   

   


