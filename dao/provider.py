from db.banco import Banco

banco = Banco()

def insertProvider(object):
    try:
        c = banco.conexao.cursor()

        c.execute("INSERT INTO providers (name, cnpj) VALUES (?,?)", (object.name, object.cnpj,))

        banco.conexao.commit()
        c.close()

        return "INSERT fornecedor feito com sucesso!"
    except:
        return print("Ocorreu um erro na inserção da fornecedor")

def selectProvider():
    try:
        c = banco.conexao.cursor()

        c.execute("SELECT * FROM providers")

        rows = c.fetchall()

        c.close()
        
        return rows
    except:
        return "Ocorreu um erro na busca da fornecedor"

def selectProviderById(id):
    try:
        c = banco.conexao.cursor()

        c.execute("SELECT * FROM providers WHERE id = ?", (id,))

        row = c.fetchone()

        c.close()

        if(row == None):
            print("SELECT id não existe na base!")
            return False
        else:
            print("SELECT fornecedor feita com sucesso!")
            print(row)
            return True
    except:
        print("Ocorreu um erro na pesquisa do id da fornecedor")
        return False

def updateProvider(object):
    try:
        c = banco.conexao.cursor()
        id = object.id

        if(selectProviderById(id)):
            c.execute("UPDATE providers SET name = ?, cnpj = ? WHERE id = ?", (object.name, object.cnpj, object.id,))
            banco.conexao.commit()
            return print("UPDATE fornecedor atualizada com sucesso!")

        c.close()
    except:
        return print("Ocorreu um erro na atualização da fornecedor")

def deleteProvider(object):
    try:
        c = banco.conexao.cursor()
        id = object.id

        if(selectProviderById(id)):
            c.execute("DELETE FROM providers WHERE id = ?", (object.id,))
            banco.conexao.commit()
            return print("DELETE fornecedor excluída com sucesso!")

        c.close()
    except:
        return "Ocorreu um erro na exclusão da fornecedor"