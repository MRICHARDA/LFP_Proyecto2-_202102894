import tkinter as t
import tkinter.ttk as ttk
import tkinter as tk
import tkinter.scrolledtext as s

class Ventana_Funciones:

    FONDO_VENTANA = 'lightcyan'
    FONDO_MENU = 'bg="EC7063"'
    FONDO_TABLA = '#white'
    ANCHO = '1000'
    FUENTE = 'Roboto'
    ALTO = '700'
    COLOR_FUENTE = 'black'

    def __init__(root, tabla_errores):
        root.marco = t.Tk()
        root.marco.title('Errores')
        root.marco['bg'] = root.FONDO_VENTANA
        root.marco.resizable(False, False)
        root.ruta_archivo_actual = ''

        root.ancho = 800
        root.alto = 500
        x = (int(root.marco.winfo_screenwidth()) - int(root.ancho))//2
        y = (int(root.marco.winfo_screenheight()) - int(root.alto))//2
        root.marco.geometry(f'{root.ancho}x{root.alto}+{x}+{y}')

        root.titulo = t.Label(root.marco, text='Errores', font=("Roboto", 30),bg="lightcyan", width=20).place(x=0, y=0)
        root.marco.errores = s.ScrolledText(root.marco)   
        root.marco.errores['height'] = 24
        root.marco.errores['width'] = 90
        root.marco.errores['wrap'] = t.NONE
        root.marco.errores.place(x=10, y=80)
        root.marco.errores.insert('1.0', tabla_errores)
        root.marco.mainloop()

    def volver(self):
        self.marco.destroy()
