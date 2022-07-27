from tkinter import *
face=Tk()
face.title("İnterface")
face.geometry('250x50')

labell=Label(face, text="Click")
labell.grid(column=1, row=0)

def click():
    global labell
    labell.configure(text='Clicked button!')

button=Button(face, text="Click button!", command=click)
button.grid(column=2,row=1)

face.mainloop()