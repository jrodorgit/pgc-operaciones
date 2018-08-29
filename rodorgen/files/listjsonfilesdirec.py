# lists json files in directory
#from rodorgen.files.listjsonfilesdirec import listado
#importlib.reload(rodorgen.files.listjsonfilesdirec)
from pathlib import Path
def listado(ruta):
    """ devuelve una lista con los ficheros de tipo .py presentes en la ruta deseada y en directorios hijos """
    p=Path(ruta)
    return list(p.glob('**/*.json'))


