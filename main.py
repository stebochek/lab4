from tkinter import *
from tkinter import ttk
from generator import key
from pygame import mixer

def show_message():
    label["text"] = key(entry.get())

root = Tk()    
root.title("Приложение на Tkinter")     
root.geometry("1920x1080")

bg = PhotoImage(file='bg.png')
label_bg = Label( root, image = bg)
label_bg.place(x = -10, y = -10)

entry = ttk.Entry()
entry.pack(anchor=CENTER, padx=6, pady=6)

btn = Button(text="Сгенерировать ключ", command=show_message) 
btn.pack(anchor=CENTER)    

label = ttk.Label()
label.pack(anchor=CENTER, padx=0, pady=0)

mixer.init()
mixer.music.load('123.mp3')
mixer.music.play()

c = Canvas( width=100, height=100, bg='green')
c.pack()
oval = c.create_oval(0, 0, 25, 25, fill='red')

def moveBall():
    c.move(oval, 1, 1)
    c.after(100, moveBall)
    c.move(oval, 1, 1)

c.after(100, moveBall)


root.mainloop()