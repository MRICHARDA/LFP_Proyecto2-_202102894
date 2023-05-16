import math
import subprocess
import os
import dropeo 
import funciones


class Analizador_sintactico: 
    
    def __init__(root,tokens):
        root.operaciones = []
        root.tokens = tokens
        root.atributo_lista =[]
        root.identificador= ""
        root.funcionesL = []
        root.textoJson =""
    
    def tenertoken(self):
        return self.tokens[0]

    def sacartoken(self):
        print("sacando:"+ self.tokens[0].lexema)
        return self.tokens.pop(0)

    def ejecutaranalizador(self):
        
        for f in self.tokens:
            print("son los tokens leidos" + f.nombre)
            
        
        
        
        comandos = ["CREAR_BD","ELIMINAR_BD","CREAR_COLECCION","ELIMINAR_COLECCION","INSERTAR_UNICO","TK_ACTUALIZAR_UNICO","TK_ELIMINAR_UNICO","TK_BUSCAR_TODO","TK_BUSCAR_UNICO"]


        tokenA = self.tenertoken()
        
        
            
            
        
        if tokenA.nombre in comandos:
            
            if tokenA.nombre == "CREAR_BD":
                
                self.crearbd()
                
            elif tokenA.nombre == "ELIMINAR_BD":

                self.eliminarbd()
                
                
            elif tokenA.nombre== "CREAR_COLECCION":
                self.crearcoleccion()
                
            elif tokenA.nombre == "ELIMINAR_COLECCION":        
                self.eliminarcoleccion()
                
            elif tokenA.nombre== "INSERTAR_UNICO":
                self.insertaruno()
                
                
            elif tokenA.nombre== "TK_ACTUALIZAR_UNICO":
                
                self.actualizarunico()
                
            elif tokenA.nombre == "TK_ELIMINAR_UNICO":    
                
                self.eliminarunico()
                
            elif tokenA.nombre == "TK_BUSCAR_TODO":
                
                self.buscartodo()
                
            elif tokenA.nombre == "TK_BUSCAR_UNICO":     

                self.buscaruno()
                

            if len(self.tokens) > 0:
                tokenA = self.tenertoken()

                if tokenA.nombre in comandos:
                    self.ejecutaranalizador()
                else:
                    print('')
                    

        return self.funcionesL    
    
    
    
    def crearbd(self):
        tokenA = self.tenertoken()

        if tokenA.nombre == "CREAR_BD":

            self.sacartoken()
            tokenA=self.tenertoken()

            if tokenA.nombre == "IDENTIFICADOR":
            
                self.sacartoken()
                tokenA=self.tenertoken()
                if tokenA.nombre == "TOKEN_IGUAL":
                    self.sacartoken()
                    tokenA=self.tenertoken()
                    if tokenA.nombre == "TK_NUEVA":
                        self.sacartoken()
                        tokenA=self.tenertoken()
                        if tokenA.nombre == "CREAR_BD":
                            self.sacartoken()

                            tokenA=self.tenertoken()
                            if tokenA.nombre == "TOKEN_PARENTESISABRE":
                                self.sacartoken()
                                tokenA=self.tenertoken()
                                if tokenA.nombre == "TK_CADENA":
                                    self.identificador = tokenA.lexema

                                    self.sacartoken()
                                    tokenA=self.tenertoken()
                                    if tokenA.nombre == "TOKEN_PARENTESISCIERRA":
                                        self.sacartoken()
                                        tokenA=self.tenertoken()
                                        if tokenA.nombre == "TOKEN_PUNTOCOMA":

                                            f_use= funciones.Use(self.identificador)
                                            use1=f_use.crearuse()
                                            self.funcionesL.append(use1)
                                            self.identificador= ""
                                            self.sacartoken()
                                            print(use1)
                                            
                                            
                                            
                                            
    def eliminarbd(self):
        
        tokenA = self.tenertoken()
        

        if tokenA.nombre == "ELIMINAR_BD":

            self.sacartoken()
            tokenA=self.tenertoken()

            if tokenA.nombre == "IDENTIFICADOR":
            
                self.sacartoken()
                tokenA=self.tenertoken()
                if tokenA.nombre == "TOKEN_IGUAL":
                    self.sacartoken()
                    tokenA=self.tenertoken()
                    if tokenA.nombre == "TK_NUEVA":
                        self.sacartoken()
                        tokenA=self.tenertoken()
                        if tokenA.nombre == "ELIMINAR_BD":
                            self.sacartoken()

                            tokenA=self.tenertoken()
                            if tokenA.nombre == "TOKEN_PARENTESISABRE":

                                self.sacartoken()
                                tokenA=self.tenertoken()

                                if tokenA.nombre == "TOKEN_PARENTESISCIERRA":
                                    self.sacartoken()
                                    tokenA=self.tenertoken()

                                    if tokenA.nombre == "TOKEN_PUNTOCOMA":
                                        self.sacartoken()
                                        f_drop= dropeo.DropData()
                                        drop1=f_drop.creardropData()
                                        self.funcionesL.append(drop1)
                                        self.identificador= ""
                                        print(drop1)

    def crearcoleccion(self):
        tokenA = self.tenertoken()
        if tokenA.nombre == "CREAR_COLECCION":

            self.sacartoken()
            tokenA=self.tenertoken()

            if tokenA.nombre == "IDENTIFICADOR":
            
                self.sacartoken()
                tokenA=self.tenertoken()
                if tokenA.nombre == "TOKEN_IGUAL":
                    self.sacartoken()
                    tokenA=self.tenertoken()
                    if tokenA.nombre == "TK_NUEVA":
                        self.sacartoken()
                        tokenA=self.tenertoken()
                        if tokenA.nombre == "CREAR_COLECCION":
                            self.sacartoken()

                            tokenA=self.tenertoken()
                            if tokenA.nombre == "TOKEN_PARENTESISABRE":
                                self.sacartoken()
                                tokenA=self.tenertoken()
                                if tokenA.nombre == "TK_CADENA":
                                    self.identificador = tokenA.lexema

                                    self.sacartoken()
                                    tokenA=self.tenertoken()
                                    if tokenA.nombre == "TOKEN_PARENTESISCIERRA":
                                        self.sacartoken()
                                        tokenA=self.tenertoken()
                                        if tokenA.nombre == "TOKEN_PUNTOCOMA":
                                            self.sacartoken()

                                            f_coleccion= funciones.Create_collection(self.identificador)
                                            col1=f_coleccion.crearcoleccion()
                                            self.funcionesL.append(col1)
                                            self.identificador= ""

                                    
    def eliminarcoleccion(self):
        tokenA = self.tenertoken()
        if tokenA.nombre == "ELIMINAR_COLECCION":

            self.sacartoken()
            tokenA=self.tenertoken()

            if tokenA.nombre == "IDENTIFICADOR":
            
                self.sacartoken()
                tokenA=self.tenertoken()
                if tokenA.nombre == "TOKEN_IGUAL":
                    self.sacartoken()
                    tokenA=self.tenertoken()
                    if tokenA.nombre == "TK_NUEVA":
                        self.sacartoken()
                        tokenA=self.tenertoken()
                        if tokenA.nombre == "ELIMINAR_COLECCION":
                            self.sacartoken()

                            tokenA=self.tenertoken()
                            if tokenA.nombre == "TOKEN_PARENTESISABRE":
                                self.sacartoken()
                                tokenA=self.tenertoken()
                                if tokenA.nombre == "TK_CADENA":
                                    self.identificador = tokenA.lexema

                                    self.sacartoken()
                                    tokenA=self.tenertoken()
                                    if tokenA.nombre == "TOKEN_PARENTESISCIERRA":
                                        self.sacartoken()
                                        tokenA=self.tenertoken()
                                        if tokenA.nombre == "TOKEN_PUNTOCOMA":
                                            self.sacartoken()

                                            f_coleccion= funciones.DropCollection(self.identificador)
                                            col1=f_coleccion.crear_dropCo()
                                            self.funcionesL.append(col1)
                                            self.identificador= ""
                                                                               

    def buscartodo(self):
        tokenA = self.tenertoken()
        if tokenA.nombre == "TK_BUSCAR_TODO":

            self.sacartoken()
            tokenA=self.tenertoken()

            if tokenA.nombre == "IDENTIFICADOR":
            
                self.sacartoken()
                tokenA=self.tenertoken()
                if tokenA.nombre == "TOKEN_IGUAL":
                    self.sacartoken()
                    tokenA=self.tenertoken()
                    if tokenA.nombre == "TK_NUEVA":
                        self.sacartoken()
                        tokenA=self.tenertoken()
                        if tokenA.nombre == "TK_BUSCAR_TODO":
                            self.sacartoken()

                            tokenA=self.tenertoken()
                            if tokenA.nombre == "TOKEN_PARENTESISABRE":
                                self.sacartoken()
                                tokenA=self.tenertoken()
                                if tokenA.nombre == "TK_CADENA":
                                    self.identificador = tokenA.lexema

                                    self.sacartoken()
                                    tokenA=self.tenertoken()
                                    if tokenA.nombre == "TOKEN_PARENTESISCIERRA":
                                        self.sacartoken()
                                        tokenA=self.tenertoken()
                                        if tokenA.nombre == "TOKEN_PUNTOCOMA":
                                            self.sacartoken()

                                            f_coleccion= funciones.Find(self.identificador)
                                            col1=f_coleccion.crearfind()
                                            self.funcionesL.append(col1)
                                            self.identificador= ""
                                          

    def buscaruno(self):
        tokenA = self.tenertoken()

        if tokenA.nombre == "TK_BUSCAR_UNICO":

            self.sacartoken()
            tokenA=self.tenertoken()

            if tokenA.nombre == "IDENTIFICADOR":
            
                self.sacartoken()
                tokenA=self.tenertoken()
                if tokenA.nombre == "TOKEN_IGUAL":
                    self.sacartoken()
                    tokenA=self.tenertoken()
                    if tokenA.nombre == "TK_NUEVA":
                        self.sacartoken()
                        tokenA=self.tenertoken()
                        if tokenA.nombre == "TK_BUSCAR_UNICO":
                            self.sacartoken()

                            tokenA=self.tenertoken()
                            if tokenA.nombre == "TOKEN_PARENTESISABRE":
                                self.sacartoken()
                                tokenA=self.tenertoken()
                                if tokenA.nombre == "TK_CADENA":
                                    self.identificador = tokenA.lexema

                                    self.sacartoken()
                                    tokenA=self.tenertoken()
                                    if tokenA.nombre == "TOKEN_PARENTESISCIERRA":
                                        self.sacartoken()
                                        tokenA=self.tenertoken()
                                        if tokenA.nombre == "TOKEN_PUNTOCOMA":
                                            self.sacartoken()

                                            f_coleccion= funciones.Find_one(self.identificador)
                                            col1=f_coleccion.crear_findOne()
                                            self.funcionesL.append(col1)
                                            self.identificador= ""
                                           
    def insertaruno(self):
        string_json=""
        tokenA = self.tenertoken()
       
        if tokenA.nombre == "INSERTAR_UNICO":

            self.sacartoken()
            tokenA=self.tenertoken()

            if tokenA.nombre == "IDENTIFICADOR":
            
                self.sacartoken()
                tokenA=self.tenertoken()
                if tokenA.nombre == "TOKEN_IGUAL":
                    self.sacartoken()
                    tokenA=self.tenertoken()
                    if tokenA.nombre == "TK_NUEVA":
                        self.sacartoken()
                        tokenA=self.tenertoken()
                        if tokenA.nombre == "INSERTAR_UNICO":
                            self.sacartoken()

                            tokenA=self.tenertoken()
                            if tokenA.nombre == "TOKEN_PARENTESISABRE":
                                self.sacartoken()
                                tokenA=self.tenertoken()
                                if tokenA.nombre == "TK_CADENA":
                                    self.identificador = tokenA.lexema

                                    self.sacartoken()
                                    tokenA=self.tenertoken()


                                    if tokenA.nombre == "TOKEN_COMA":
                                        self.sacartoken()
                                        tokenA=self.tenertoken()

                                        if tokenA.nombre == "TOKEN_LLAVEABRE":
                                            self.sacartoken()
                                            tokenA=self.tenertoken()
                                            string_json += "{\n"


                                            if tokenA.nombre == "TOKEN_LLAVEABRE":
                                                string_json += self.json()

                                                tokenA = self.tenertoken()
                                                if tokenA.nombre == "TOKEN_LLAVECIERRA":
                                                    string_json += "\n}"
                                                    self.sacartoken()

                                                    tokenA = self.tenertoken()
                                                    if tokenA.nombre == "TOKEN_PARENTESISCIERRA":
                                                        self.sacartoken()
                                                        tokenA=self.tenertoken()
                                                        if tokenA.nombre == "TOKEN_PUNTOCOMA":
                                                            self.sacartoken()
                                                            f_coleccion= funciones.InsertOne(self.identificador,string_json)
                                                            col1=f_coleccion.crearinsert()
                                                            self.funcionesL.append(col1)
                                                            self.identificador= ""
                                                            
                                                                                                                                                        
    def actualizarunico(self):
        string_json=""
        tokenA = self.tenertoken()
      
        if tokenA.nombre == "TK_ACTUALIZAR_UNICO":

            self.sacartoken()
            tokenA=self.tenertoken()

            if tokenA.nombre == "IDENTIFICADOR":
            
                self.sacartoken()
                tokenA=self.tenertoken()
                if tokenA.nombre == "TOKEN_IGUAL":
                    self.sacartoken()
                    tokenA=self.tenertoken()
                    if tokenA.nombre == "TK_NUEVA":
                        self.sacartoken()
                        tokenA=self.tenertoken()
                        if tokenA.nombre == "TK_ACTUALIZAR_UNICO":
                            self.sacartoken()

                            tokenA=self.tenertoken()
                            if tokenA.nombre == "TOKEN_PARENTESISABRE":
                                self.sacartoken()
                                tokenA=self.tenertoken()
                                if tokenA.nombre == "TK_CADENA":
                                    self.identificador = tokenA.lexema

                                    self.sacartoken()
                                    tokenA=self.tenertoken()


                                    if tokenA.nombre == "TOKEN_COMA":
                                        self.sacartoken()
                                        tokenA=self.tenertoken()

                                        if tokenA.nombre == "TOKEN_LLAVEABRE":
                                            self.sacartoken()
                                            tokenA=self.tenertoken()
                                            string_json += "{\n"


                                            if tokenA.nombre == "TOKEN_LLAVEABRE":
                                                string_json += self.json2()

                                                tokenA = self.tenertoken()
                                                if tokenA.nombre == "TOKEN_COMA":
                                                    
                                                    self.sacartoken()
                                                    string_json += " ,\n" + self.jsonset()
                                                    tokenA = self.tenertoken()
                                                    if tokenA.nombre == "TOKEN_LLAVECIERRA":
                                                        self.sacartoken()
                                                        string_json += "    \n}"
                                                elif tokenA.nombre == "TOKEN_LLAVECIERRA":
                                                    self.sacartoken()
                                                    string_json += "\n}"

                                                print(string_json)
                                                tokenA = self.tenertoken()
                                                if tokenA.nombre == "TOKEN_PARENTESISCIERRA":
                                                    self.sacartoken()
                                                    tokenA=self.tenertoken()
                                                    if tokenA.nombre == "TOKEN_PUNTOCOMA":
                                                        f_coleccion= funciones.ActualizaOne(self.identificador,string_json)
                                                        col1=f_coleccion.crear_actu1()
                                                        self.funcionesL.append(col1)
                                                        self.identificador= ""
                                        
    
#     
    def atribuset(self):
        clave = ""
        lexema = ""
        texto = ""

        tokenA = self.tenertoken()
        if tokenA.nombre == "TK_SET":
            clave = tokenA.lexema
            self.sacartoken()

            tokenA = self.tenertoken()
            if tokenA.nombre == "TOKEN_DOSPUNTOS":
                self.sacartoken()

                tokenA = self.tenertoken()

                if tokenA.nombre == "TOKEN_LLAVEABRE":
                    lexema = self.json2()
                    tokenA = self.tenertoken()
                    texto = clave + ":" + lexema
                    if tokenA.nombre == "TOKEN_LLAVECIERRA":
                        return texto
            
            
        
                                                         
    def json(self):
        texto = ""
        self.sacartoken()
        texto += "  {\n"

        tokenA = self.tenertoken()
        if tokenA.nombre == "TK_CADENA":
            texto += self.atributos()

            tokenA = self.tenertoken()
            if tokenA.nombre == "TOKEN_LLAVECIERRA":
                self.sacartoken()

                texto += "  \n}"

                tokenA = self.tenertoken()
                if tokenA.nombre == "TOKEN_LLAVECIERRA":
                    return texto

    def json2(self):
        texto = ""
        self.sacartoken()
        texto += "  {\n"

        tokenA = self.tenertoken()
        if tokenA.nombre == "TK_CADENA":
            texto += self.atributos()

            tokenA = self.tenertoken()
            if tokenA.nombre == "TOKEN_LLAVECIERRA":
                self.sacartoken()

                texto += "  \n}"
                return texto 

    def jsonset(self):
        texto = ""
        self.sacartoken()
        texto += "  {\n"

        tokenA = self.tenertoken()
        if tokenA.nombre == "TK_SET":
            texto += self.atribuset()

            tokenA = self.tenertoken()
            if tokenA.nombre == "TOKEN_LLAVECIERRA":
                self.sacartoken()

                texto += "  \n}"
                return texto                     
                                                                            
    def atributos(self):
        clave = ""
        lexema = ""
        texto = ""

        tokenA = self.tenertoken()
        if tokenA.nombre == "TK_CADENA":
            clave = tokenA.lexema
            self.sacartoken()

            tokenA = self.tenertoken()
            if tokenA.nombre == "TOKEN_DOSPUNTOS":
                self.sacartoken()

                tokenA = self.tenertoken()
               
                if tokenA.nombre == "TK_CADENA":
                    lexema = tokenA.lexema
                    self.sacartoken()

                    texto = clave + ":" + lexema
                    tokenA = self.tenertoken()
                  
                    if tokenA.nombre == "TOKEN_COMA":
                        self.sacartoken()
                        texto += ",\n"
                        texto += self.atributos()
                        return texto
                    elif tokenA.nombre == "TOKEN_LLAVECIERRA":
                        return texto

                                
                                                                            
    def eliminarunico(self):  
        string_json=""
        tokenA = self.tenertoken()
   
        if tokenA.nombre == "TK_ELIMINAR_UNICO":

            self.sacartoken()
            tokenA=self.tenertoken()

            if tokenA.nombre == "IDENTIFICADOR":
            
                self.sacartoken()
                tokenA=self.tenertoken()
                if tokenA.nombre == "TOKEN_IGUAL":
                    self.sacartoken()
                    tokenA=self.tenertoken()
                    if tokenA.nombre == "TK_NUEVA":
                        self.sacartoken()
                        tokenA=self.tenertoken()
                        if tokenA.nombre == "TK_ELIMINAR_UNICO":
                            self.sacartoken()

                            tokenA=self.tenertoken()
                            if tokenA.nombre == "TOKEN_PARENTESISABRE":
                                self.sacartoken()
                                tokenA=self.tenertoken()
                                if tokenA.nombre == "TK_CADENA":
                                    self.identificador = tokenA.lexema

                                    self.sacartoken()
                                    tokenA=self.tenertoken()


                                    if tokenA.nombre == "TOKEN_COMA":
                                        self.sacartoken()
                                        tokenA=self.tenertoken()

                                        if tokenA.nombre == "TOKEN_LLAVEABRE":
                                            self.sacartoken()
                                            tokenA=self.tenertoken()
                                            string_json += "{\n"


                                            if tokenA.nombre == "TOKEN_LLAVEABRE":
                                                string_json += self.json()

                                                tokenA = self.tenertoken()
                                                if tokenA.nombre == "TOKEN_LLAVECIERRA":
                                                    string_json += "\n}"
                                                    self.sacartoken()

                                                    tokenA = self.tenertoken()
                                                    if tokenA.nombre == "TOKEN_PARENTESISCIERRA":
                                                        self.sacartoken()
                                                        tokenA=self.tenertoken()
                                                        if tokenA.nombre == "TOKEN_PUNTOCOMA":
                                                        
                                                        
                                                            f_coleccion= funciones.DeleteOne(self.identificador,string_json)
                                                            col1=f_coleccion.crear_delete_one()
                                                            self.funcionesL.append(col1)
                                                            self.identificador= ""  





