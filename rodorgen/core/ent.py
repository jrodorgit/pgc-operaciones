# util para tratamiento de entidades

def getAtrPK(entidad):
    """ devuelve el nombre del atributo clave de una entidad """
    atrpk = 'ERROR'
    atrs = [a for a in entidad['atributos']]
    for atr in atrs:
        if atr['pk'] == "PK":
            atrpk = atr['nombreatr']
        break;
    return atrpk

