# generador de codigo java de entidades de tipo operacion

import rodorgen.files.utilfile
import rodorgen.core.gen

def run():
    """ lanza el proceso de generacion de ficheros fuente """
    
    # obtencion ruta de ficheros a procesar
    ficheros_a_procesar = rodorgen.files.utilfile.listado('.')
    print('Se van a procesar {} ficheros'.format(len(ficheros_a_procesar)))
    
    # lectura de ficheros a procesar
    entidades = [rodorgen.files.utilfile.lee(f) for f in ficheros_a_procesar]
    print('Se han leido {} entidades'.format(len(entidades)))

    # generador del SQL para cada entidad.
    [rodorgen.core.gen.generaSQLOracle(e) for e in entidades]

