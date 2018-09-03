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

def getAtrsFK(entidad):
    """ devuelve lsitado de atributo que son FK """
    atrfk = []
    atrs = [a for a in entidad['atributos']]
    for atr in atrs:
        if atr['fk'] == "FK":
            atrfk.append(atr['nombreatr'])
    
    print(atrfk)
    return atrfk
    
def getAtrs(entidad):
    """ devuelve los atributos de una entidad separados por comas """
    atrs = [a for a in entidad['atributos']]
    return ', '.join([''.join( x['nombreatr'] ) for x in atrs])

def getAtrsForUpdate(entidad):
    """ devuelve los atributos de una entidad para hace un update """
    atrs = [a for a in entidad['atributos']]
    at = [''.join( x['nombreatr'] ) for x in atrs]
    at.remove(getAtrPK(entidad))
    return ', '.join([x for x in [ (element + ' = ? ') for element in at]])


