package {PACKAGE};

//Fichero generado automaticamente por PGC.

import java.util.ResourceBundle;


public class PreparedStatementFactory{
	
	private  static  ResourceBundle sqls = ResourceBundle.getBundle ("{PACKAGE}");
	private  volatile static PreparedStatementFactory instance;
	private PreparedStatementFactory(){}
	public  static PreparedStatementFactory getInstance(){
		if(instance == null){
			synchronized (PreparedStatementFactory.class){
				if(instance == null){
					instance = new PreparedStatementFactory();
				}
			}
		}
		return instance;
	}
	public  String  getSQL(String idSQL) {return sqls.getString(idSQL);}

}