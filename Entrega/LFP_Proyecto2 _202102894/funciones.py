class ActualizaOne:
    def __init__(self,identificador,json):
        self.identificador = identificador
        self.use= ""
        self.json=json
        
    def crear_actu1(self):    
        self.insert = "db."+self.identificador +".updateOne("+ self.json + ");" 
        return self.insert


class Create_collection:
    def __init__(self,identificador) :
        self.identificador = identificador
        self.coleccion= ""
        
    def crearcoleccion(self):    
        self.coleccion = 'db.createCollection('+ self.identificador +');'
        return self.coleccion

class DeleteOne:
    def __init__(self,identificador,json):
        self.identificador = identificador
        self.delete= ""
        self.json= json
        
    def crear_delete_one(self):    
        self.delete_one = "db."+self.identificador+".deleteOne("+self.json+");" 
        return self.delete_one

class DropCollection:
    def __init__(self,identificador):
        self.identificador = identificador
        self.drop= ""
        
    def crear_dropCo(self):    
        self.drop = "db."+self.identificador +".drop();"

        return self.drop

class DropData:
    def __init__(self):
        self.eliminar= ""
        
    def crear_dropData(self):    
        self.eliminar = "db.dropDatabase();" 
        return self.eliminar 
        
        
        
class Find:
    def __init__(self,identificador):
        self.identificador = identificador
        self.find= ""
        
    def crearfind(self):    
        self.find = "db.self."+self.identificador +".find();" 
        return self.find

class Find_one:
    def __init__(self,identificador):
        self.identificador = identificador
        self.find= ""
        
    def crear_findOne(self):    
        self.find = "db."+self.identificador+".findOne();" 
        return self.find

class InsertOne:
    def __init__(self,identificador,json):
        self.identificador = identificador
        self.use= ""
        self.json=json
        
    def crearinsert(self):    
        self.insert = "db."+self.identificador +".insertOne("+ self.json + ");" 
        return self.insert


class Json:
    def __init__(self,identificador):
        self.identificador = identificador
        self.json= ""
        
    def crear_json(self):    
        self.json = "use("+ self.identificador.strip('"') +");" 
        return self.json


class Use:
    def __init__(self,identificador):
        self.identificador = identificador
        self.use= ""
        
    def crearuse(self):    
        self.use = "use("+ self.identificador.strip() +");" 
        return self.use                                      