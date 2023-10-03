from tkinter import *
from fuctions import *

class ui:

    def __init__(self,master):

        self.scrollbar = Scrollbar(master)
        self.scrollbar.pack(side= RIGHT,fill = Y)

        self.caja_texto = Text(master,borderwidth=5,padx=10,pady=0,font=60,yscrollcommand=self.scrollbar.set,relief="groove")
       
        self.caja_texto.config(font=('Arial', 12))
        self.caja_texto.place(x=10,y=30)

        self.scrollbar.config(command=self.caja_texto.yview)

        self.boton_guardar = Button(master,text="Guardar",command = lambda:guardar(self.caja_texto),relief="ridge")
        self.boton_guardar.place(x=10,y=1)

        self.boton_personalizar = Button(master,text="Personalizar fondo",command=lambda:personalizar_fondo(master,self.caja_texto),relief="ridge")
        self.boton_personalizar.place(x=60,y=1)

        self.boton_oscuro = Button(master,text="Noche",command=lambda :oscuro(self.caja_texto,master),relief="ridge")
        self.boton_oscuro.place(x=130,y=1)

        self.boton_claro =Button(master,text = "claro",command=lambda:modo_claro(self.caja_texto,master),relief="ridge")
        self.boton_claro.place(x=175,y=1)


        self.open_button = Button(master,text="Abrir",command=lambda:abrir_archivo(self.caja_texto),relief="ridge")
        self.open_button.place(x=210,y=1)
        
#---------------------------------------------------------------------instancias---------------------

try:
    root = Tk()
    
    root.title("Pynotepad")
    root.config(bg="white")
    root.geometry("790x470")
    root.resizable(False,False)
    ar = ui(root)
    
except:
    root.showerror("invalido","hubo un error")

finally:
    root.mainloop()
