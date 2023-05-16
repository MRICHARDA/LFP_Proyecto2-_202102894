
import tokenL as t
import automata as aal 
from typing import List

class AnalizadorLexico:

    def __init__(self):
        self.fila = 1
        self.columna = 1
        self.puntero = 0
        self.posicion_actual = 0
        self.entrada = ''
        self.automatas = aal.AutomatasAnalizadorLexico()
        self.tokens: List[t.LToken] = []
        self.alfanumericos = ['_']

        for i in range(65, 91):
            self.alfanumericos.append(chr(i))
        
        for i in range(97, 123):
            self.alfanumericos.append(chr(i))

        for i in range(0, 10):
            self.alfanumericos.append(str(i))

    def analizar(self, entrada):
        self.entrada = entrada
        cadena_auxiliar = ''

        while self.puntero < len(self.entrada):
            cadena_auxiliar += self.entrada[self.puntero]
            self.columna += 1

            if cadena_auxiliar == ' ':
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == '=':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                token = t.LToken("igual", cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == '\n' or cadena_auxiliar == '\r':
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
                self.fila += 1
                self.columna = 1
            elif cadena_auxiliar == ',':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                                    #cambiar nombre de Token_Coma
                token = t.LToken("coma", cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == ';':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                token = t.LToken(
                    "puntocoma", cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == ':':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                token = t.LToken(
                    "dospuntos", cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == '(':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                token = t.LToken("parentesisinicial",cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == ')':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                token = t.LToken("parentesisifinal",cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == '{':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                token = t.LToken(
                    "llaveinicio", cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == '}':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                token = t.LToken("llavecierra",cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == '[':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                token = t.LToken("corcheteinicio",cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == ']':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                token = t.LToken("corchetefinal",cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            else:
                self.columna -= 1

                resultado = self.crearbd()

                if resultado is None:
                    resultado = self.eliminarBD()

                if resultado is None:
                        resultado = self.crearcoleccion()

                if resultado is None:
                        resultado = self.eliminarcoleccion()

                if resultado is None:
                        resultado = self.insertarunico()

                if resultado is None:
                        resultado = self.actualizarunico()

                if resultado is None:
                        resultado = self.eliminarunico()

                if resultado is None:
                        resultado = self.buscartodo()

                if resultado is None:
                        resultado = self.buscarunico()

                if resultado is None:
                        resultado = self.analizarnueva()

                if resultado is None:
                        resultado = self.set()

                if resultado is None:
                        resultado = self.numero()

                if resultado is None:
                        resultado = self.cadena()

                if resultado is None:
                        resultado = self.identificador()

                if resultado is None:
                    print('Error Lexico: Simbolo no definido')
                    self.error = True
                    break
                else:
                    cadena_auxiliar = resultado[0]
                    token = resultado[1]
                    fila = self.fila
                    columna = self.columna - len(cadena_auxiliar)
                    token.fila = fila
                    token.columna = columna
                    self.tokens.append(token)
                    self.posicion_actual += len(cadena_auxiliar)
                    cadena_auxiliar = ''
                    self.puntero = self.posicion_actual

        
        print('\n----------------Tokens---------------- ')
        for token in self.tokens:
            print(token)
        
        return self.tokens    

        

    def crearbd(self):
        columna = self.columna
        puntero_inicial = self.puntero
 
        cadena = ''
        longitud = len(self.entrada)
     
        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_crear_bd.analizar(cadena)
            
            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.puntero = puntero_inicial
        self.columna = columna
        return resultado

    def eliminarBD(self):
        columna = self.columna
        puntero_inicial = self.puntero

        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_eliminar_bd.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def crearcoleccion(self):
        columna = self.columna
        puntero_inicial = self.puntero
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_crear_coleccion.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def eliminarcoleccion(self):
        columna = self.columna
        puntero_inicial = self.puntero
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_eliminar_coleccion.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def insertarunico(self):
        columna = self.columna
        puntero_inicial = self.puntero
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_insertar_unico.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def actualizarunico(self):
        columna = self.columna
        puntero_inicial = self.puntero
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_actualizar_unico.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def eliminarunico(self):
        columna = self.columna
        puntero_inicial = self.puntero
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_eliminar_unico.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def buscartodo(self):
        columna = self.columna
        puntero_inicial = self.puntero
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_buscar_todo.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def buscarunico(self):
        columna = self.columna
        puntero_inicial = self.puntero
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_buscar_unico.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def analizarnueva(self):
        columna = self.columna
        puntero_inicial = self.puntero
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_nueva.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def set(self):
        columna = self.columna
        puntero_inicial = self.puntero
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_set.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado
    
    def numero(self):
        columna = self.columna
        puntero_inicial = self.puntero
        caracter_actual = self.entrada[self.puntero]
        cadena = ''

        while caracter_actual != ' ' and caracter_actual != '\n' and caracter_actual != ',':
            cadena += caracter_actual
            self.columna += 1
            self.puntero += 1
            caracter_actual = self.entrada[self.puntero]

        resultado = self.automatas.aut_numero.analizar(cadena)

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return None

    def cadena(self):
    
        columna = self.columna
        puntero_inicial = self.puntero
     
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_cadena.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def identificador(self):
        columna = self.columna
        puntero_inicial = self.puntero
        caracter_actual = self.entrada[self.puntero]
        cadena = ''

        while caracter_actual in self.alfanumericos:
            cadena += caracter_actual
            self.columna += 1
            self.puntero += 1
            caracter_actual = self.entrada[self.puntero]

        resultado = self.automatas.aut_identificador.analizar(cadena)

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return None    