import sqlite3

class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name_ad TEXT,
            tel TEXT,
            sap_name TEXT,
            location TEXT)""")

        c.execute("""CREATE TABLE IF NOT EXISTS branchs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value_name TEXT)""")

        c.execute("""CREATE TABLE IF NOT EXISTS providers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            cnpj TEXT)""")

        c.execute("""CREATE TABLE IF NOT EXISTS templates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            value TEXT,
            allocation_name TEXT,
            manager_code TEXT,
            service_name TEXT,
            allocation_value TEXT,
            nbs_code TEXT,
            contract_bool TEXT,
            average_bool TEXT,
            user_id INTEGER,
            provider_id INTEGER,
            branch_id INTEGER)""")

        self.conexao.commit()
        c.close()