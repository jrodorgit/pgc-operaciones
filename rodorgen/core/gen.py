# generador de codigo fuente
import rodorgen.files.utilfile
import rodorgen.core.ent
import rodorgen.main

def generaSQLDMLOracle(entidad):
    """ por cada entidad (solo debe de haber 1) leida en el fichero del modelo genera los archivos SQL DML para trabajar con Oracle """
    
    entity = entidad['Entidades'][0]
    
    #print(entidad)
    print('Nombre de la entidad a generar DML:'+entity['nombre'])
    
    #apertura de fichero donde escribir DML de la entidad
    fSQLDML = open(rodorgen.main.OUT_MODEL_PATH+'Oracle_DML_'+entity['nombre']+'.sql', 'w')
    
    #generamos SELECT_BY_PK
    #sql_select_pk = rodorgen.files.utilfile.leeLineaAjustaPatron(r'./rodorgen/resources/templates/ORACLE-DML-TEMPLATE.properties','SELECT_BY_PK')
    sql_select_pk = rodorgen.files.utilfile.leeLineaAjustaPatron(rodorgen.main.TEMPLATES_DML_PATH,'SELECT_BY_PK')
    sql_select_pk = sql_select_pk.replace(r'{ENTIDAD}', entity['nombre'])
    sql_select_pk = sql_select_pk.replace(r'{ATR_PK}', rodorgen.core.ent.getAtrPK(entity))
    sql_select_pk = sql_select_pk.replace(r'{ATRS}', rodorgen.core.ent.getAtrs(entity))
    fSQLDML.write(sql_select_pk)
    
    #generamos UPDATE_BY_PK
    sql_update_by_pk = rodorgen.files.utilfile.leeLineaAjustaPatron(rodorgen.main.TEMPLATES_DML_PATH,'UPDATE_BY_PK')
    sql_update_by_pk = sql_update_by_pk.replace(r'{ENTIDAD}', entity['nombre'])
    sql_update_by_pk = sql_update_by_pk.replace(r'{ATR_PK}', rodorgen.core.ent.getAtrPK(entity))
    sql_update_by_pk = sql_update_by_pk.replace(r'{ATRS}', rodorgen.core.ent.getAtrsForUpdate(entity))
    fSQLDML.write(sql_update_by_pk)
    
    # generamos DELETE_BY_PK
    sql_delete_by_pk = rodorgen.files.utilfile.leeLineaAjustaPatron(rodorgen.main.TEMPLATES_DML_PATH,'DELETE_BY_PK')
    sql_delete_by_pk = sql_delete_by_pk.replace(r'{ENTIDAD}', entity['nombre'])
    sql_delete_by_pk = sql_delete_by_pk.replace(r'{ATR_PK}', rodorgen.core.ent.getAtrPK(entity))
    fSQLDML.write(sql_delete_by_pk)
    
    # generamos INSERT
    sql_insert = rodorgen.files.utilfile.leeLineaAjustaPatron(rodorgen.main.TEMPLATES_DML_PATH,'INSERT')
    sql_insert = sql_insert.replace(r'{ENTIDAD}', entity['nombre'])
    sql_insert = sql_insert.replace(r'{ATRS}', rodorgen.core.ent.getAtrs(entity))
    sql_insert = sql_insert.replace(r'{ATRS_VAL}', ', '.join(['?' for x in range(0,len(entity['atributos']) )]))
    fSQLDML.write(sql_insert)
     
    # generamos SELECT BY FK
    for fk in rodorgen.core.ent.getAtrsFK(entity):
        sql_select_by_fk = rodorgen.files.utilfile.leeLineaAjustaPatron(rodorgen.main.TEMPLATES_DML_PATH,'SELECT_BY_FK')
        sql_select_by_fk = sql_select_by_fk.replace(r'{ENTIDAD}', entity['nombre'])
        sql_select_by_fk = sql_select_by_fk.replace(r'{ATRS}', rodorgen.core.ent.getAtrs(entity)) 
        sql_select_by_fk = sql_select_by_fk.replace(r'{ATR_FK}', fk)  
        sql_select_by_fk = sql_select_by_fk.replace(r'{ATR}', fk.upper() )
        fSQLDML.write(sql_select_by_fk)
    
    fSQLDML.close()
    
def generaSQLDDLOracle(entidad):
    """ por cada entidad (solo debe de haber 1) leida en el fichero del modelo genera los archivos SQL DdL para trabajar con Oracle """
    
    entity = entidad['Entidades'][0]
    
    #print(entidad)
    print('Nombre de la entidad a generar DDL:'+entity['nombre'])
    
    # obtenemos plantilla
    sql_create = rodorgen.files.utilfile.leeFicheroAString(rodorgen.main.TEMPLATES_DDL_PATH)
    
    #apertura de fichero donde escribir DML de la entidad
    fSQLDDL = open(rodorgen.main.OUT_MODEL_PATH+'Oracle_DDL_'+entity['nombre']+'.sql', 'w')
    
    #generamos CREATE TABLE
    sql_create = sql_create.replace(r'{ENTIDAD}', entity['nombre'])
    sql_create = sql_create.replace(r'{DOC_ENTIDAD}', entity['descripcion'])
    # LSITA DE ATRIBUTOS DE LA ENTIDAD
    atrsent = [a for a in entity['atributos']]
    atrdef = [rodorgen.core.ent.getAtrDef(a) for a in atrsent]
    sql_create = sql_create.replace(r'{ATRS}', ',\r\n\t'.join([p for p in atrdef])) 
    fSQLDDL.write(sql_create)
    sql_coment = rodorgen.files.utilfile.leePropiedad(rodorgen.main.TEMPLATES_DML_PATH,'COMMENT_ATR')
    sql_coment = sql_coment.replace(r'{ENTIDAD}', entity['nombre'])
    for atr in entity['atributos']:
        sql_coment_aux = sql_coment
        fSQLDDL.write(sql_coment_aux.replace(r'{ATR}', atr['nombreatr'] ).replace(r'{ATR_DESC}', atr['descatr'] ) )
    
    #DEFINICION DE PK
    sql_pkdef = rodorgen.files.utilfile.leePropiedad(rodorgen.main.TEMPLATES_DML_PATH,'PK_DEFINITION')
    sql_pkdef = sql_pkdef.replace(r'{ENTIDAD}', entity['nombre'])
    sql_pkdef = sql_pkdef.replace(r'{ATR_PK}', rodorgen.core.ent.getAtrPK(entity))
    fSQLDDL.write(sql_pkdef)
    
    fSQLDDL.close()
