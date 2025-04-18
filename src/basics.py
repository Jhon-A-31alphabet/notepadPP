from tkinter import messagebox
from tkinter import Tk
from tkinter import END, filedialog
import time
import json
import os
import base64
import string

save_current_file = None   #  this variable read the current file


class read_config_file:
    
     with open('config.json', 'r') as file:
        data = json.load(file)
    

class theme_conf:
    
    @staticmethod
    def darkmode(text,window):
        

        with open('config.json', 'r') as file:
            data = json.load(file)
            data['FG'] = 'white'
            data['BG'] ='black'
            data["CURSOR"]='white'
            


        with open('config.json', 'w') as file:

            json.dump(data, file, indent=4)
        
        text.config(bg=data['BG'],fg=data['FG'],insertbackground=data['CURSOR'])
        window.config(bg=data['BG'])
        


       


    @staticmethod
    def light_mode(text,window):

        with open('config.json', 'r') as file:
            data = json.load(file)
            data['FG'] = 'black'
            data['BG'] ='white'
            data["CURSOR"]='black'
            

        with open('config.json', 'w') as file:

            json.dump(data, file, indent=4)
        
        text.config(bg=data['BG'],fg=data['FG'],insertbackground=data['CURSOR'])
        window.config(bg=data['BG'])
        






def save_text_to_file(text_widget: None) -> None:
    #save as  name.txt  the current file
    try:
        
        file_dialog = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("textfile", ".txt")])
        file_text = text_widget.get(1.0, "end-1c")
        file_dialog.write(file_text)
        file_dialog.close()

    except:
        messagebox.showinfo("Iformation", "you did not save anything") 
    
    

def save(text_widget:None):
    #aplied changes for the current file
    if save_current_file:
        content = text_widget.get(1.0,END)
        with open(save_current_file,"w") as file:
            file.write(str(content))
    else:
        save_text_to_file(text_widget)    # else save as
    
        
    



def open_file(text_widget,master) -> None:
    
    global save_current_file
    file_path = filedialog.askopenfilename()
    
    if file_path:
        if file_path.endswith(".txt"):
            
            save_current_file = str(os.path.abspath(file_path))  #current file value if the user selected a file........
            
            
            with open(file_path, 'r') as file:
                content = file.read()
                text_widget.delete('1.0', END)
                text_widget.insert('1.0', content)
    master.title(str(save_current_file))


def copy_text_to_clipboard(text_widget, master) -> None:
    content = text_widget.get("1.0", "end-1c")

    master.clipboard_clear()
    master.clipboard_append(content)
    master.update()



def get_date(text_widget) -> None:
    date = time.strftime("%c")
    text_widget.insert('1.0', f"Date and Time: {date} ")




class enconding_base_64:

    @staticmethod
    def encode_text(text_on_widget: None) -> None:
        text = text_on_widget.get(1.0,END)
        encoded = base64.b64encode(text.encode("ascii"))
        text_on_widget.delete("1.0","end")
        text_on_widget.insert(1.0,encoded)

    @staticmethod
    def decode_text(text_on_widget: None) -> None:
        text = text_on_widget.get(1.0,END)
        decoded = base64.b64decode(text.encode("ascii"))
        text_on_widget.delete("1.0","end")
        text_on_widget.insert(1.0,decoded)
    
    



