import tkinter as tk
import tkinter as t
import tkinter.scrolledtext as s
import tkinter.filedialog as fd
import sys
import os
from tkinter.messagebox import showinfo
import lexi
import listokens
import sintac as sint
import tabfunciones as tfunciones
import customtkinter
from tkdocviewer import *
from tkinter import messagebox
import webbrowser as wb
import compilador
import scannerLexico

class Ventana:

    
    def __init__(root,inicio):
        root.inicio = inicio
        root.inicio.title('LFP Proyecto 2')
        root.inicio.config(borderwidth=20, bg="lightcyan")
        root.inicio.resizable(False, False)
        root.ruta_archivo_actual = ''
        root.lista_tokens_actual = []
        root.lista_funciones =None
        root.lista_tokens_usar =None
        
        root.ancho = 800
        root.alto = 500


        x = (int(root.inicio.winfo_screenwidth()) - int(root.ancho))//2
        y = (int(root.inicio.winfo_screenheight()) - int(root.alto))//2
        root.inicio.geometry(f'{root.ancho}x{root.alto}+{x}+{y}')
        
        root.titulo = t.Label(root.inicio, text="Escribe tu codigo en esta area", font=("Roboto", 10, "bold"), bg = "cadetblue")
        root.titulo.grid(row=0,column=0)
        
        btn_Generar = customtkinter.CTkButton(root.inicio, text="Analizar", command=root.analizar, fg_color="cadetblue")
        btn_Generar.place(x=10, y=30)
        
        '''self.boton2 = tk.Button(self.PP, text='Tokens', command=self.ver_tokens, font=("Arial Black", 15), fg="black", bg="#8373FB", width=10).place(x=500, y=620)
        self.boton3 = tk.Button(self.PP, text='Errores',command=self.llenar_funcion , font=("Arial Black", 15), fg="black", bg="#8373FB", width=10).place(x=800, y=620)
         '''
        
        # Menú superior
        menubar = tk.Menu(root.inicio)
        root.inicio.config(menu=menubar)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Abrir", command=root.cargar_archivo)
        filemenu.add_command(label="Guardar", command=root.guardar)
        filemenu.add_command(label="Guardar Como", command=root.guardar_como)
        filemenu.add_command(label="Salir", command=root.salir)
        
        menubar.add_cascade(label="Archivo", menu=filemenu)
        
        filemenu = tk.Menu(menubar, tearoff=0)
        root.inicio.config(menu=menubar)
        filemenu.add_command(label="Análisis", command=root.analizar)
        filemenu.add_command(label="Tokens", command=root.ver_tokens)
        filemenu.add_command(label="Errores", command=root.llenar_funcion)

        menubar.add_cascade(label="Opciones", menu=filemenu)

        filemenu = tk.Menu(menubar, tearoff=0)
        root.inicio.config(menu=menubar)
        filemenu.add_command(label="Ayuda", command=root.ayuda)

        menubar.add_cascade(label="Ayuda", menu=filemenu)

        root.area_texto = s.ScrolledText(root.inicio)   
        root.area_texto['height'] = 12
        root.area_texto['width'] = 90
        root.area_texto['wrap'] = t.NONE
        root.area_texto.place(x=10, y=70)
        root.consola = s.ScrolledText(root.inicio)   
        root.consola['height'] = 12
        root.consola['width'] = 90
        root.consola['wrap'] = t.NONE
        root.consola.place(x=10, y=275)
    

    def cargar_archivo(root):
        extensiones = (('Todos los archivos', '*.*'),)

        root.ruta_archivo_actual = str(
            fd.askopenfilename(filetypes=extensiones))

        try:
            with open(root.ruta_archivo_actual, 'r') as archivo:
                texto = archivo.read()
                root.area_texto.delete('1.0', t.END)
                root.area_texto.insert('1.0', texto)
        except IOError:
            print('Error de Carga')

    def analizar(root):
        #error.lista_errores.clear()
        analizador = lexi.AnalizadorLexico()
        texto = root.area_texto.get('1.0', t.END)
        root.lista_tokens_usar = analizador.analizar(texto)
        root.lista_tokens_actual = root.lista_tokens_usar.copy()
        
        analizador_sint = sint.Analizador_sintactico(root.lista_tokens_actual)
        root.lista_funciones =analizador_sint.ejecutaranalizador()

        print('------Sentencias en MongoDB-----')
        info=root.area_texto.get("1.0", "end")
        salida= compilador.compilar(info)
        root.consola.delete('1.0', t.END)
        root.consola.insert('1.0', "Salida:\n"+salida)
    
    def ver_funciones(root):

        tfunciones.Ventana_Funciones(root.lista_funciones) 
        

    def borrar(root):
        root.area_texto.delete('1.0', t.END)
        
    def llenar_funcion(root):
        info=root.area_texto.get("1.0", "end")
        print('Errores: ')
        info=info.replace('\t','')  #is
        salida=scannerLexico.revisarErrores(info)
        tfunciones.Ventana_Funciones(salida)


    def guardar(root):
        if root.ruta_archivo_actual == '':
            root.ruta_archivo_actual = root.guardar_como()
        else:
            texto = root.area_texto.get('1.0', t.END)
            with open(root.ruta_archivo_actual, 'w', encoding='utf-8') as archivo:
                archivo.write(texto)
            showinfo('Guardado', 'Archivo guardado')

    def guardar_como(root):
        extensiones = (('Todos los archivos', '*.*'),)

        ruta_archivo = str(
            fd.asksaveasfilename(filetypes=extensiones))

        texto = root.area_texto.get('1.0', t.END)
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(texto)

        return ruta_archivo

    def salir(root):
        sys.exit(0)


    def ver_tokens(root):
        ventana = listokens.Ventana_Token(root.lista_tokens_actual)

    def ayuda(root):
        messagebox.showinfo(message='''
    
        USAC, LFP B+, 1er Semestre 2023

        Nombre: Richard Alexandro Marroquin Arana
        Carnet: 202102894''',
                        
                        title="Datos")   

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Datos")
    root.config(bg="lightcyan")
    root.geometry("300x200+300+300")
    root.resizable(width=False, height=False)
    app = Ventana(root)
    root.mainloop()
