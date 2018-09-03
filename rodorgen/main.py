# generador de codigo java de entidades de tipo operacion

import rodorgen.files.utilfile
import rodorgen.core.gen

TEMPLATES_DML_PATH = r'./rodorgen/resources/templates/ORACLE-DML-TEMPLATE.properties'
TEMPLATES_DDL_PATH = r'./rodorgen/resources/templates/ORACLE-DDL-TEMPLATE.sql'
OUT_MODEL_PATH = r'./rodorgen/resources/outModelo/'

def run():
    """ lanza el proceso de generacion de ficheros fuente """
    
    # obtencion ruta de ficheros a procesar
    ficheros_a_procesar = rodorgen.files.utilfile.listado('.')
    print('Se van a procesar {} ficheros'.format(len(ficheros_a_procesar)))
    
    # lectura de ficheros a procesar
    entidades = [rodorgen.files.utilfile.lee(f) for f in ficheros_a_procesar]
    print('Se han leido {} entidades'.format(len(entidades)))

    # generador de DDl de cada entidad
    [rodorgen.core.gen.generaSQLDDLOracle(e) for e in entidades]
    
    # generador del SQL DML para cada entidad.
    [rodorgen.core.gen.generaSQLDMLOracle(e) for e in entidades]
