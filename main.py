from tkinter import *
from tkinter import messagebox
from time import gmtime, strftime
import time
from playsound import playsound
from datetime import timedelta
import schedule





def show_message():
    playsound("file.mp3")
    messagebox.showinfo("Напоминалка","Напоминание!")

def go():
    playtime = message.get()
    schedule.every().day.at(playtime).do(show_message)
    while 1:
        schedule.run_pending()
        time.sleep(1)


 
root = Tk()
root.title("Напоминалка")
root.geometry("300x250")
 
message = StringVar()
textt = StringVar()

lbl = Label(root, text="1 поле - время")
lbl.grid(column=1, row=2)

txt1 = Entry(textvariable=message)
txt1.place(relx=.5, rely=.1, anchor="c")

txt2 = Entry(textvariable=message)
txt2.place(relx=.5, rely=.1, anchor="c")
 
message_button = Button(text="Создать", command=go)
message_button.place(relx=.5, rely=.5, anchor="c")


 
root.mainloop() 
