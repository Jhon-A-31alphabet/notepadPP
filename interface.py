from tkinter import *

from fuctions import *

print("executing")



class ui:
    def __init__(self,master):
        self.caja_texto = Text(master,borderwidth=5,padx=10,pady=0,font=60)
       
        self.caja_texto.config(font=('Arial', 16))
        self.caja_texto.place(x=0,y=30)

        self.boton_guardar = Button(master,text="Guardar",command = lambda:guardar(self.caja_texto))
        self.boton_guardar.place(x=10,y=1)

        self.boton_personalizar = Button(master,text="Personalizar fondo",command=lambda:personalizar_fondo(master,self.caja_texto))
        self.boton_personalizar.place(x=60,y=1)

        self.boton_oscuro = Button(master,text="Noche",command=lambda :oscuro(self.caja_texto,master))
        self.boton_oscuro.place(x=130,y=1)

        self.boton_claro =Button(master,text = "claro",command=lambda:modo_claro(self.caja_texto,master))
        self.boton_claro.place(x=170,y=1)

        
#-----------------------------------------------------------------------------------------instancias---------------------


try:
    root = Tk()
    root.title("Pynotepad")
    root.config(bg="white")
    root.geometry("1080x700")
    ar = ui(root)
except:
    root.showerror("invalido","hubo un error")

finally:
    root.mainloop()
