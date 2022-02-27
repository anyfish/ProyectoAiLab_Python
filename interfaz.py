from tkinter import *
from venv.GAME.Juego import *

app = Tk()
app.geometry("800x600")
app.title("Aimon Game")
app.configure(bg='gray')
app.iconbitmap('pokeball.ico')

labelNombre = Label(app, text='Ingresa tu Nombre')
labelNombre.place(x=10, y=2)
labelNombre.config(bg='gray')

entryNombre = Entry(app)
entryNombre.place(x=10, y=25)

botonUsuarioNuevo = Button(app, text='Guardar', command=nuevoUsuario).place(x=10, y=50)

app.mainloop()