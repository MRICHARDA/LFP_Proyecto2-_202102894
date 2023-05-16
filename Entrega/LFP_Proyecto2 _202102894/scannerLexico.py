from prettytable import PrettyTable

def revisarErrores(informacion):
    listaErrores = []
    listaErrores = encontrarErrores(informacion,listaErrores)

    table=PrettyTable(['Tipo de Error','Linea','Columna','Token','Descripción'])
    for error in listaErrores:
        table.add_row([error.tipo, error.linea, error.columna, error.token, error.description])

    print(table)
    return table

def encontrarErrores(informacion, listaErrores:list):
    numeroFila=0

    lineas = informacion.split("\n")
    for linea in lineas:
        numeroColumna=0
        numeroFila+=1

        for c in linea:
            numeroColumna+=1

            if not(c.isdigit()|c.isalpha()or c==" " or c == "{" or c=="}" or c == ":" or c=="," or c == "(" or c==")" or c == "=" or c == "."or c == '"' or c == ";" or c=="$"):
                listaErrores.append(Error('lexico', numeroFila, numeroColumna, c, "Caracter no valido"))
    return listaErrores

class Error:

    def __init__(self, tipo, linea, columna, token, description) -> None:
        self.tipo=tipo
        self.linea=linea
        self.columna=columna
        self.token=token
        self.description=description
