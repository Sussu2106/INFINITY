from sqlite3 import connect
conexao = connect (database = "sussu's_coffee.db")
 
cursor =  conexao.cursor()

cursor.execute("""
              INSERT INTO clientes (nome, email, cidade, estado, telefone, saldo)
              
              )
               
               
""")

conexao.commit()