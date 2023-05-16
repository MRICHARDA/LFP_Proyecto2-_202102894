import tkinter as t
import tkinter.ttk as ttk
import tkinter as tk

class Ventana_Token:

    FONDO_VENTANA = '#20147A'
    FONDO_MENU = '#EC7063'
    FONDO_TABLA = 'white'
    FUENTE = 'Roboto'
    COLOR_FUENTE = 'black'

    def __init__(root, lista_tokens):
        root.marco = t.Tk()
        root.marco.title('Tokens')
        root.marco.config(borderwidth=20, bg="lightcyan")
        root.marco.resizable(False, False)
        root.ruta_archivo_actual = ''

        root.ancho = 650
        root.alto = 500
        x = (int(root.marco.winfo_screenwidth()) - int(root.ancho))//2
        y = (int(root.marco.winfo_screenheight()) - int(root.alto))//2
        root.marco.geometry(f'{root.ancho}x{root.alto}+{x}+{y}')

        root.titulo = t.Label(root.marco, text='Tokens', font=("Roboto", 30),bg="lightcyan", width=20).place(x=0, y=0)
        
        '''self.lbl_titulo = t.Label(self.marco)
        self.lbl_titulo['text'] = 'TOKENS'
        self.lbl_titulo['font'] = (self.FUENTE, 30)
        self.lbl_titulo['bg'] = self.FONDO_VENTANA
        self.lbl_titulo.place(x=254, y=50)'''


        encabezados = ('No.', 'Token','Lexema')
        root.tabla = ttk.Treeview(root.marco, columns=encabezados,show='headings', height=20)

        root.tabla.heading('No.', text='No.')
        root.tabla.column('No.', anchor=t.CENTER, width=100)
        root.tabla.heading('Token', text='Token')
        
        root.tabla.heading('Lexema', text='Lexema')
        root.tabla.column('Lexema', anchor=t.CENTER, width=300)

        
        estilo = ttk.Style(root.tabla)
        estilo.configure('Treeview', background='#F2F2F2')
        estilo.theme_use('xpnative')
        estilo.configure(
            'Treeview.Heading',
            background=root.FONDO_TABLA,
            foreground=root.COLOR_FUENTE,
            font=(root.FUENTE, 12, 'bold'))
        estilo.configure('Treeview', font=(root.FUENTE, 10),
                        background=root.FONDO_TABLA)

        contador = 1
        for token in lista_tokens:
            datos = [str(contador), token.nombre, token.lexema]
            root.tabla.insert('', t.END, values=datos)
            contador += 1

        root.tabla.place(x=10, y=50)

        root.marco.mainloop()

    def volver(self):
        self.marco.destroy()