from tkinter import *
from tkinter import ttk
from fuctions import *


class ui:

    def __init__(self,master):



        self.scrollbar = Scrollbar(master)
        self.scrollbar.pack(side= RIGHT,fill = Y)
        

        self.caja_texto = Text(master,borderwidth=1,padx=10,pady=0,font=60,yscrollcommand=self.scrollbar.set,relief="flat")
        self.caja_texto.config(font=('Arial',12))
        self.caja_texto.place(x=10,y=30)

       

        self.scrollbar.config(command=self.caja_texto.yview)

        self.boton_guardar = Button(master,text="Guardar",command = lambda:guardar(self.caja_texto),relief="groove")
        self.boton_guardar.place(x=10,y=1)

        self.boton_personalizar = Button(master,text="Personalizar fondo",command=lambda:personalizar_fondo(master,self.caja_texto),relief="groove")
        self.boton_personalizar.place(x=60,y=1)

        self.boton_oscuro = Button(master,text="Noche",command=lambda :oscuro(self.caja_texto,master),relief="groove")
        self.boton_oscuro.place(x=130,y=1)

        self.boton_claro =Button(master,text = "claro",command=lambda:modo_claro(self.caja_texto,master),relief="groove")
        self.boton_claro.place(x=175,y=1)


        self.open_button = Button(master,text="Abrir",command=lambda:abrir_archivo(self.caja_texto),relief="groove")
        self.open_button.place(x=210,y=1)

        self.clipboard_button = Button(master,text="copiar",relief="groove",command=lambda:copiar_texto(self.caja_texto,master))
        self.clipboard_button.place(x=245,y=1)


        self.fecha_hora =Button(master,text="Fecha y hora",command=lambda:get_date(self.caja_texto),relief="groove")
        self.fecha_hora.place(x= 290,y=1)

        


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