def compilar(informacion: str):
    salida=''
    informacion=informacion.replace('\n','')
    informacion=informacion.replace('\t','')
    
    sentencias=informacion.split(';')
    sentencias=sentencias[0:len(sentencias)-1]

    for sentencia in sentencias:
        partesFuncion=sentencia.split('=')

        parte0=partesFuncion[0]
        parte1=partesFuncion[1]

        funcion=parte1[0:parte1.index('(')]
        funcion=funcion[funcion.index('nueva')+5:len(funcion)]
        funcion=funcion.strip()

        datos=parte1[parte1.index('('):parte1.index(')')+1]
        #print(datos)
        if datos=='()' or datos=='':
            dato=parte0.split(' ')[1]

            if funcion == 'CrearBD':
                salida=salida+"use('"+dato+"');\n"
            elif funcion == 'EliminarBD':
                salida=salida+"db.dropDatabase();\n"

        elif ',' in parte1:
            atributos=parte1.split(',')
            dato=atributos[0].strip().replace('"','')
            dato=dato.split('(')[1]

            json=atributos[1].strip()
            json=json[1:len(json)-1]

            if funcion=='InsertarUnico':
                salida=salida+"db."+dato+".insertOne("+json+");\n"
            elif funcion=='ActualizarUnico':
                salida=salida+"db."+dato+".updateOne("+json+");\n"
            elif funcion=='EliminarUnico':
                salida=salida+"db."+dato+".deleteOne("+json+");\n"

        else:
            dato=datos.replace('"','')
            if (')' in dato) and ('(' in dato):
                dato=dato[1:len(dato)+1]

            if funcion=='CrearColeccion':
                salida=salida+"db.createCollection('"+dato+"');\n"

            elif funcion=='EliminarColeccion':
                salida=salida+"db."+dato+".drop();\n"
    
    print(salida)
    return salida

prueba='InsertarUnico insertadoc = nueva InsertarUnico("NombreColeccion" ,\n"\n{\n"nombre" : "Obra Literaria",\n"autor" : "Jorge Luis"\n}\n");'    