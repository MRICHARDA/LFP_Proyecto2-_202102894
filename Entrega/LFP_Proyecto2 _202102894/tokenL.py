

TIPOS_FUNCIONES = ["CREAR_BD","ELIMINAR_BD","CREAR_COLECCION","ELIMINAR_COLECCION","INSERTAR_UNICO","ACTUALIZAR_UNICO","ELIMINAR_UNICO","BUSCAR_TODO","BUSCAR_UNICO"]

class LToken:

    def __init__(root, nombre:str, lexema:str, fila:int, columna:int):
        root.nombre = nombre
        root.lexema = lexema
        root.fila = fila
        root.columna = columna

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}    Fila: {self.fila}   Columna: {self.columna}    Lexema: {self.lexema}'