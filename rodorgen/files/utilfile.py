# utils for file operation

from pathlib import Path
import json

def listado(ruta):
    """ devuelve una lista con los ficheros de tipo .py presentes en la ruta deseada y en directorios hijos """
    p=Path(ruta)
    return list(p.glob('**/*.json'))

def lee(fichero):
    """ lee fichero json y devuelve diccionario """
    with open(fichero, "r",encoding="utf-8") as read_file:
        objeto = json.load(read_file)
    
    read_file.close()
    return objeto


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