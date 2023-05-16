import tokenL as t
from typing import List, Dict


class analisis:

    def __init__(self, nombre, estados, token):
        self.nombre: str = nombre
        self.inicio: Estado | None = None
        self.estados: List[Estado] = estados
        self.token: str = token

    def agregar_estado(self, estado):
        self.estados.append(estado)

    def alfabeto(self):
        alfabeto = []
        for estado in self.estados:
            for caracter in estado.transiciones:
                if caracter not in alfabeto:
                    alfabeto.append(caracter)

        return alfabeto

    def establecer_inicio(self, inicio):
        self.inicio = inicio

    def analizar(self, entrada):
        cadena_auxiliar = ''
        estado_actual = self.inicio

        for caracter in entrada:
            if caracter in estado_actual.transiciones:
                cadena_auxiliar += caracter
                estado_actual = estado_actual.transiciones.get(caracter)
            else:
                break

        if estado_actual.aceptacion and cadena_auxiliar == entrada:
            return t.LToken(self.token, cadena_auxiliar, 0, 0)
        else:
            return None


class Estado:

    def __init__(self, nombre, aceptacion) :
        self.nombre: str = nombre
        self.aceptacion: bool = aceptacion
        self.transiciones: Dict[str, Estado] = {}

    def transicion(self, caracter: str, destino):
        self.transiciones[caracter] = destino