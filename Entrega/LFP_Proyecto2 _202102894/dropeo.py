class DropData:
    def __init__(self):
        self.eliminar= ""
        
    def creardropData(self):    
        self.eliminar = "db.dropDatabase();" 
        return self.eliminar 
        