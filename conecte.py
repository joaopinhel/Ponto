import mysql.connector


def criar_conexao(host, usuario, senha, banco):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)


def fechar_conexao(con):
    return con.closed()

#import MySQLdb
#
#connection = MySQLdb.connect(
#    host="127.0.0.1",
#    user="root",
#    passwd="",
#    db="contabilivre"
#)
#
#cursor = connection.cursor()
#cursor.execute("select database();")
#db = cursor.fetchone()
#
#if db:
#    print("Você está conectado ao banco de dados: ", db)
#else:
#    print('Não conectado.')