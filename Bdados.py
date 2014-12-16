# -*- coding: utf-8 -*-
import sqlite3

con = sqlite3.connect('manprev.db') # Conecta ao banco de dados, se não existir, cria o mesmo.
cur = con.cursor()

class CriaTabelas:

    def cria(self):
    	
    	''' Método para criar as tabelas do banco de dados'''

    	cur.execute("""CREATE TABLE IF NOT EXISTS carros (
    		placa TEXT PRIMARY KEY,
    		cliente TEXT,
    		endereco TEXT,
    		cidade TEXT,
    		cep TEXT,
    		cpf TEXT,
    		telefone TEXT,
    		email TEXT)""")