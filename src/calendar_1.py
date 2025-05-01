import tkinter
from tkcalendar import Calendar

class calendar__:

    def __init__(self,main):
        self.main = main

    def calendarwindow(self):
        self.calendar_window =tkinter.Toplevel(self.main)


        self.calendar = Calendar(self.calendar_window)
        self.calendar.pack(padx=1,pady=1)


        self.calendar_window.title("Calendar")

        
    

        
        

        
