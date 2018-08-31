# utils for file operation

from pathlib import Path
import json
import re

def listado(ruta):
    """ devuelve una lista con los ficheros de tipo .py presentes en la ruta deseada y en directorios hijos """
    p=Path(ruta)
    return list(p.glob('**/*.json'))

def lee(fichero):
    """ lee fichero json y devuelve diccionario """
    with open(fichero, "r",encoding="utf-8") as read_file:
        objeto = json.load(read_file)
    
    read_file.close()
    #print(objeto)
    return objeto

def leeLineaAjustaPatron(fichero,patron):
    """ devuelve la primera linea del fichero que contiene el patron """
    linea = ''
    with open(fichero, "r",encoding="utf-8") as read_file:
        for line in read_file:
            #print(line,end='')
            match = re.search(patron,line)
            if match:
                linea = line
                break
            
        
    read_file.close()
    return linea

#lectura de entidades objetos['Entidades'][0]['nombre']
#lectura de atributos objetos['Entidades'][0]['atributos']    
#lectura de atributo 1 objetos['Entidades'][0]['atributos'][0] 
# entidades = [x for x in  objetos['Entidades']]
# shutil.copyfile(r'P:\mypython\rodorgen\resources\templates\ORACLE-DML-TEMPLATE.sql',r'P:\mypython\rodorgen\resources\outModelo\kk.sql')
# s = open(r'P:\mypython\rodorgen\resources\outModelo\kk.sql').read()
# s = s.replace(r'{nombre}', 'KKOperaciones')
# f = open(r'P:\mypython\rodorgen\resources\outModelo\kk.sql', 'w')
# f.write(s)

# f.close()
#with open(r'./rodorgen/resources/outModelo/kk.sql.sql',w) as f:   
