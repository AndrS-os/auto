Import services.database as db;
import clientecontroller ;

def INCLUIR(){
count = cursor.execute("""
  INSERT INTO cliente (clinome, clicidade, cliprofissao,)
  VALUES (?,?,?) """,
  cliente.nome,cliente.idade, cliente.profissao).rowcount
  db.cnxn.commit()

  }