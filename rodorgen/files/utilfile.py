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

def leeFicheroAString(ficheroPath):
    """ devuelve un fichero en una cadena """
    return open(ficheroPath).read()
