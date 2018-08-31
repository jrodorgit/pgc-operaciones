# generador de codigo fuente
import rodorgen.files.utilfile
import rodorgen.core.ent

def generaSQLOracle(entidad):
    """ por cada entidad (solo debe de haber 1) leida en el fichero del modelo genera los archivos SQL para trabajar con Oracle """
    
    entity = entidad['Entidades'][0]
    
    #print(entidad)
    print('Nombre de la entidad a generar:'+entity['nombre'])
    
    #apertura de fichero donde escribir DML de la entidad
    fSQLDML = open(r'./rodorgen/resources/outModelo/Oracle_DML_'+entity['nombre']+'.sql', 'w')
    
    #generamos SELECT_BY_PK
    sql_select_pk = rodorgen.files.utilfile.leeLineaAjustaPatron(r'./rodorgen/resources/templates/ORACLE-DML-TEMPLATE.properties','SELECT_BY_PK')
    sql_select_pk = sql_select_pk.replace(r'{nombre}', entity['nombre'])
    #nombrePK = rodorgen.core.ent.getAtrPK(entity)
    sql_select_pk = sql_select_pk.replace(r'{ATR_PK}', rodorgen.core.ent.getAtrPK(entity))
    #print(sql_select_pk)
    fSQLDML.write(sql_select_pk)
    fSQLDML.close()
    