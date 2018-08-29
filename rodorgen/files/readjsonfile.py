# read json file to object ( dict)
import json
def lee(fichero):
    """ lee fichero json y devuelve diccionario """
    with open(fichero, "r",encoding="utf-8") as read_file:
        objeto = json.load(read_file)
    
    read_file.close()
    return objeto

    