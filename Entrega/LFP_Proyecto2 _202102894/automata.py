import tokenL as t
import analizardor 

class AutomatasAnalizadorLexico:

    def __init__(self):
        self.aut_crear_bd = self.CrearDB()
        self.aut_eliminar_bd = self.eliminarBD()
        self.aut_crear_coleccion = self.crearcoleccion()
        self.aut_eliminar_coleccion = self.eliminarcoleccion()
        self.aut_insertar_unico = self.insertarunico()
        self.aut_actualizar_unico = self.autoactualizar()
        self.aut_eliminar_unico = self.eliminar()
        self.aut_buscar_todo = self.buscar()
        self.aut_buscar_unico = self.automatabuscar()
        self.aut_nueva = self.nueva()
        self.aut_numero = self.numero()
        self.aut_cadena = self.cadena()
        self.aut_identificador = self.identificador()
        self.aut_set = self.set()
      
    def CrearDB(self) :
        
        #Cambiar variables X1, X2 , etc
        a0 = analizardor.Estado('a0', False)
        b1 = analizardor.Estado('b1', False)
        c2 = analizardor.Estado('c2', False)
        d3 = analizardor.Estado('d3', False)
        e4 = analizardor.Estado('e4', False)
        f5 = analizardor.Estado('f5', False)
        g6 = analizardor.Estado('g6', False)
        h7 = analizardor.Estado('h7', True)

        a0.transicion('C', b1)
        b1.transicion('r', c2)
        c2.transicion('e', d3)
        d3.transicion('a', e4)
        e4.transicion('r', f5)
        f5.transicion('B', g6)
        g6.transicion('D', h7)

        token = "CrearBD" 

        estados = [a0, b1, c2, d3, e4, f5, g6, h7]
        inicio = a0

        automata = analizardor.analisis("Crear BD", estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def eliminarBD(self) :
        

        a0 = analizardor.Estado('a0', False)
        b1 = analizardor.Estado('b1', False)
        c2 = analizardor.Estado('c2', False)
        d3 = analizardor.Estado('d3', False)
        e4 = analizardor.Estado('e4', False)
        f5 = analizardor.Estado('f5', False)
        g6 = analizardor.Estado('g6', False)
        h7 = analizardor.Estado('h7', False)
        i8 = analizardor.Estado('i8', False)
        g9 = analizardor.Estado('g9', False)
        k10 = analizardor.Estado('k10', True)
           
        a0.transicion('E', b1)
        b1.transicion('l', c2)
        c2.transicion('i', d3)
        d3.transicion('m', e4)
        e4.transicion('i', f5)
        f5.transicion('n', g6)
        g6.transicion('a', h7)
        h7.transicion('r', i8)
        i8.transicion('B', g9)
        g9.transicion('D', k10)
       
        token = "eliminarBD"

        estados = [a0, b1, c2, d3, e4, f5, g6, h7, i8, g9, k10]
        inicio = a0

        automata = analizardor.analisis('Automata Eliminar BD', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def crearcoleccion(self) :
        
        nombre = 'Automata Crear Coleccion'

        a0 = analizardor.Estado('a0', False)
        b1 = analizardor.Estado('b1', False)
        c2 = analizardor.Estado('c2', False)
        d3 = analizardor.Estado('d3', False)
        e4 = analizardor.Estado('e4', False)
        f5 = analizardor.Estado('f5', False)
        g6 = analizardor.Estado('g6', False)
        h7 = analizardor.Estado('h7', False)
        i8 = analizardor.Estado('i8', False)
        j9 = analizardor.Estado('j9', False)
        k10 = analizardor.Estado('k10', False)
        m11 = analizardor.Estado('m11', False)
        n12 = analizardor.Estado('n12', False)
        p13 = analizardor.Estado('p13', False)
        q14 = analizardor.Estado('q14', True)

        a0.transicion('C', b1)
        b1.transicion('r', c2)
        c2.transicion('e', d3)
        d3.transicion('a', e4)
        e4.transicion('r', f5)
        f5.transicion('C', g6)
        g6.transicion('o', h7)
        h7.transicion('l', i8)
        i8.transicion('e', j9)
        j9.transicion('c', k10)
        k10.transicion('c', m11)
        m11.transicion('i', n12)
        n12.transicion('o', p13)
        p13.transicion('n', q14)

        token = "crearColeccion"

        estados = [a0, b1, c2, d3, e4, f5, g6,
                   h7, i8, j9, k10, m11, n12, p13, q14]
        inicio = a0

        automata = analizardor.analisis('Automata Crear Coleccion', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def eliminarcoleccion(self):
        
        
            #Cambiar al nombre que puse
        a0 = analizardor.Estado('a0', False)
        b1 = analizardor.Estado('b1', False)
        c2 = analizardor.Estado('c2', False)
        d3 = analizardor.Estado('d3', False)
        e4 = analizardor.Estado('e4', False)
        f5 = analizardor.Estado('f5', False)
        g6 = analizardor.Estado('g6', False)
        h7 = analizardor.Estado('h7', False)
        i8 = analizardor.Estado('i8', False)
        j9 = analizardor.Estado('j9', False)
        k10 = analizardor.Estado('k10', False)
        m11 = analizardor.Estado('m11', False)
        n12 = analizardor.Estado('n12', False)
        p13 = analizardor.Estado('p13', False)
        q14 = analizardor.Estado('q14', False)
        r15 = analizardor.Estado('r15', False)
        s16 = analizardor.Estado('s16', False)
        t17 = analizardor.Estado('t17', True)

        a0.transicion('E', b1)
        b1.transicion('l', c2)
        c2.transicion('i', d3)
        d3.transicion('m', e4)
        e4.transicion('i', f5)
        f5.transicion('n', g6)
        g6.transicion('a', h7)
        h7.transicion('r', i8)
        i8.transicion('C', j9)
        j9.transicion('o', k10)
        k10.transicion('l', m11)
        m11.transicion('e', n12)
        n12.transicion('c', p13)
        p13.transicion('c', q14)
        q14.transicion('i', r15)
        r15.transicion('o', s16)
        s16.transicion('n', t17)

        token = "EliminarColeccion"

        estados = [a0, b1, c2, d3, e4, f5, g6, h7, i8,
                   j9, k10, m11, n12, p13, q14, r15, s16, t17]
        inicio = a0

        automata = analizardor.analisis('Automata Eliminar Coleccion', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def insertarunico(self) :
        
        

        a0 = analizardor.Estado('a0', False)
        b1 = analizardor.Estado('b1', False)
        c2 = analizardor.Estado('c2', False)
        d3 = analizardor.Estado('d3', False)
        e4 = analizardor.Estado('e4', False)
        f5 = analizardor.Estado('f5', False)
        g6 = analizardor.Estado('g6', False)
        h7 = analizardor.Estado('h7', False)
        i8 = analizardor.Estado('i8', False)
        j9 = analizardor.Estado('j9', False)
        k10 = analizardor.Estado('k10', False)
        m11 = analizardor.Estado('m11', False)
        n12 = analizardor.Estado('n12', False)
        p13 = analizardor.Estado('p13', True)

        a0.transicion('I', b1)
        b1.transicion('n', c2)
        c2.transicion('s', d3)
        d3.transicion('e', e4)
        e4.transicion('r', f5)
        f5.transicion('t', g6)
        g6.transicion('a', h7)
        h7.transicion('r', i8)
        i8.transicion('U', j9)
        j9.transicion('n', k10)
        k10.transicion('i', m11)
        m11.transicion('c', n12)
        n12.transicion('o', p13)

        token = "inserte"

        estados = [a0, b1, c2, d3, e4, f5, g6, h7, i8, j9, k10, m11, n12, p13]
        inicio = a0

        automata = analizardor.analisis('Automata Insertar Unico', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def autoactualizar(self) :
        
        

        a0 = analizardor.Estado('a0', False)
        b1 = analizardor.Estado('b1', False)
        c2 = analizardor.Estado('c2', False)
        d3 = analizardor.Estado('d3', False)
        e4 = analizardor.Estado('e4', False)
        f5 = analizardor.Estado('f5', False)
        g6 = analizardor.Estado('g6', False)
        h7 = analizardor.Estado('h7', False)
        i8 = analizardor.Estado('i8', False)
        j9 = analizardor.Estado('j9', False)
        k10 = analizardor.Estado('k10', False)
        m11 = analizardor.Estado('m11', False)
        n12 = analizardor.Estado('n12', False)
        p13 = analizardor.Estado('p13', False)
        q14 = analizardor.Estado('q14', False)
        r15 = analizardor.Estado('r15', True)

        a0.transicion('A', b1)
        b1.transicion('c', c2)
        c2.transicion('t', d3)
        d3.transicion('u', e4)
        e4.transicion('a', f5)
        f5.transicion('l', g6)
        g6.transicion('i', h7)
        h7.transicion('z', i8)
        i8.transicion('a', j9)
        j9.transicion('r', k10)
        k10.transicion('U', m11)
        m11.transicion('n', n12)
        n12.transicion('i', p13)
        p13.transicion('c', q14)
        q14.transicion('o', r15)

        token = "actualizar"

        estados = [a0, b1, c2, d3, e4, f5, g6, h7,
                   i8, j9, k10, m11, n12, p13, q14, r15]
        inicio = a0

        automata = analizardor.analisis('Automata Actualizar Unico', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def eliminar(self) :
        
        

        a0 = analizardor.Estado('a0', False)
        b1 = analizardor.Estado('b1', False)
        c2 = analizardor.Estado('c2', False)
        d3 = analizardor.Estado('d3', False)
        e4 = analizardor.Estado('e4', False)
        f5 = analizardor.Estado('f5', False)
        g6 = analizardor.Estado('g6', False)
        h7 = analizardor.Estado('h7', False)
        i8 = analizardor.Estado('i8', False)
        j9 = analizardor.Estado('j9', False)
        k10 = analizardor.Estado('k10', False)
        m11 = analizardor.Estado('m11', False)
        n12 = analizardor.Estado('n12', False)
        p13 = analizardor.Estado('p13', True)

        a0.transicion('E', b1)
        b1.transicion('l', c2)
        c2.transicion('i', d3)
        d3.transicion('m', e4)
        e4.transicion('i', f5)
        f5.transicion('n', g6)
        g6.transicion('a', h7)
        h7.transicion('r', i8)
        i8.transicion('U', j9)
        j9.transicion('n', k10)
        k10.transicion('i', m11)
        m11.transicion('c', n12)
        n12.transicion('o', p13)

        token = "eliminar"

        estados = [a0, b1, c2, d3, e4, f5, g6, h7, i8, j9, k10, m11, n12, p13]
        inicio = a0

        automata = analizardor.analisis('Automata Eliminar Unico', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def buscar(self) :
        
        

        a0 = analizardor.Estado('a0', False)
        b1 = analizardor.Estado('b1', False)
        c2 = analizardor.Estado('c2', False)
        d3 = analizardor.Estado('d3', False)
        e4 = analizardor.Estado('e4', False)
        f5 = analizardor.Estado('f5', False)
        g6 = analizardor.Estado('g6', False)
        h7 = analizardor.Estado('h7', False)
        i8 = analizardor.Estado('i8', False)
        j9 = analizardor.Estado('j9', False)
        k10 = analizardor.Estado('k10', True)

        a0.transicion('B', b1)
        b1.transicion('u', c2)
        c2.transicion('s', d3)
        d3.transicion('c', e4)
        e4.transicion('a', f5)
        f5.transicion('r', g6)
        g6.transicion('T', h7)
        h7.transicion('o', i8)
        i8.transicion('d', j9)
        j9.transicion('o', k10)

        token = "buscar"

        estados = [a0, b1, c2, d3, e4, f5, g6, h7, i8, j9, k10]
        inicio = a0

        automata = analizardor.analisis('Automata Buscar Todo', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def automatabuscar(self):
        
        

        a0 = analizardor.Estado('a0', False)
        b1 = analizardor.Estado('b1', False)
        c2 = analizardor.Estado('c2', False)
        d3 = analizardor.Estado('d3', False)
        e4 = analizardor.Estado('e4', False)
        f5 = analizardor.Estado('f5', False)
        g6 = analizardor.Estado('g6', False)
        h7 = analizardor.Estado('h7', False)
        i8 = analizardor.Estado('i8', False)
        j9 = analizardor.Estado('j9', False)
        k10 = analizardor.Estado('k10', False)
        m11 = analizardor.Estado('m11', True)

        a0.transicion('B', b1)
        b1.transicion('u', c2)
        c2.transicion('s', d3)
        d3.transicion('c', e4)
        e4.transicion('a', f5)
        f5.transicion('r', g6)
        g6.transicion('U', h7)
        h7.transicion('n', i8)
        i8.transicion('i', j9)
        j9.transicion('c', k10)
        k10.transicion('o', m11)

        token = "buscar"

        estados = [a0, b1, c2, d3, e4, f5, g6, h7, i8, j9, k10, m11]
        inicio = a0

        automata = analizardor.analisis('Automata Buscar Unico', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def nueva(self) :
        
    

        a0 = analizardor.Estado('a0', False)
        b1 = analizardor.Estado('b1', False)
        c2 = analizardor.Estado('c2', False)
        d3 = analizardor.Estado('d3', False)
        e4 = analizardor.Estado('e4', False)
        f5 = analizardor.Estado('f5', True)

        a0.transicion('n', b1)
        b1.transicion('u', c2)
        c2.transicion('e', d3)
        d3.transicion('v', e4)
        e4.transicion('a', f5)

        token = "nueva"

        estados = [a0, b1, c2, d3, e4, f5]
        inicio = a0

        automata = analizardor.analisis('Automata Nueva', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def numero(self) :
        
        

        a0 = analizardor.Estado('a0', False)
        b1 = analizardor.Estado('b1', False)
        c2 = analizardor.Estado('c2', True)
        d3 = analizardor.Estado('d3', False)
        e4 = analizardor.Estado('e4', True)

        a0.transicion('-', b1)
        c2.transicion('.', d3)
        for i in range(0, 10):
            a0.transicion(str(i), c2)
            b1.transicion(str(i), c2)
            c2.transicion(str(i), c2)
            d3.transicion(str(i), e4)
            e4.transicion(str(i), e4)

        token = "numero"

        estados = [a0, b1, c2, d3, e4]
        inicio = a0

        automata = analizardor.analisis('Automata Numero', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def identificador(self) :
        token = "Identificador"
        

        a0 = analizardor.Estado('a0', False)
        b1 = analizardor.Estado('b1', True)

        for i in range(65, 91):
            a0.transicion(chr(i), b1)
            b1.transicion(chr(i), b1)

        for i in range(97, 123):
            a0.transicion(chr(i), b1)
            b1.transicion(chr(i), b1)

        for i in range(0, 10):
            b1.transicion(str(i), b1)

        b1.transicion('_', b1)

        estados = [a0, b1]
        inicio = a0

        automata = analizardor.analisis('Automata Identificador', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def cadena(self) :
        token = "cadena"
        

        a0 = analizardor.Estado('a0', False)
        b1 = analizardor.Estado('b1', False)
        c2 = analizardor.Estado('c2', False)
        d3 = analizardor.Estado('d3', True)

        a0.transicion('"', b1)
        for i in range(32, 127):
            if i != 34:
                b1.transicion(chr(i), c2)
                c2.transicion(chr(i), c2)
        b1.transicion('"', d3)
        c2.transicion('"', d3)

        estados = [a0, b1, c2, d3]
        inicio = a0

        automata = analizardor.analisis('Automata Cadena', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def set(self) :
        
        

        a0 = analizardor.Estado('a0', False)
        b1 = analizardor.Estado('b1', False)
        c2 = analizardor.Estado('c2', False)
        d3 = analizardor.Estado('d3', False)
        e4 = analizardor.Estado('e4', True)

        a0.transicion('$', b1)
        b1.transicion('s', c2)
        c2.transicion('e', d3)
        d3.transicion('t', e4)
        
        token = "set"
        
        estados = [a0, b1, c2, d3, e4]
        inicio = a0

        automata = analizardor.analisis('Automata Set', estados, token)
        automata.establecer_inicio(inicio)

        return automata