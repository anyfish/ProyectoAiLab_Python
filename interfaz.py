from tkinter import *
from venv.GAME.Juego import *

def ventanaInicio():
    vn = Tk()
    vn.geometry("500x500")
    vn.title("Aimon Game")
    vn.configure(bg='gray')
    vn.iconbitmap('egg.ico')

    labelTitulo = Label(vn, text='La aventura te espera en Aimon')
    labelTitulo.place(x=10, y=2)
    labelTitulo.config(bg='gray')

    botonIniciarSesion = Button(vn, text='Iniciar Sesión', command=validarUsuario)
    botonIniciarSesion.place(x=25, y=50)

    botonUsuarioNuevo = Button(vn, text='Nuevo Usuario', command=nuevoUsuario)
    botonUsuarioNuevo.place(x=25, y=100)

    vn.mainloop()

def ventanaIniciarSesion():
    global vn
    vn.geometry("500x500")
    vn.title("Aimon Game")
    vn.configure(bg='gray')
    vn.iconbitmap('egg.ico')

    entryNombre = Entry(vn)
    entryNombre.place(x=10, y=25)

    vn.mainloop()
