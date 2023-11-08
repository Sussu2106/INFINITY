import sqlite3 as sql

def conectar(banco_dados: str) -> any:
    conexao = sql.connect(banco_dados)
    cursor = conexao.cursor
    return conexao, cursor

def inserir(banco_dados: str, nome_tabela:str, colunas_tabela: tuple, valores_tabela: tuple) -> None:
    """Método para inserir dados/registros na tabela"""
    conexao = conectar(banco_dados)[0]
    cursor = conectar(banco_dados)[1]
    
    
    cursor.execute(f"INSERT INTO {nome_tabela} {colunas_tabela} VALUES {valores_tabela}")
    conectar(banco_dados)[0].commit()