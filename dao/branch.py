from db.banco import Banco

banco = Banco()

def insertBranch(object):
    try:
        c = banco.conexao.cursor()

        c.execute("INSERT INTO branchs (value_name) VALUES (?)", (object.value_name,))

        banco.conexao.commit()
        c.close()

        return "INSERT filial feito com sucesso!"
    except:
        return "Ocorreu um erro na inserção da filial"

def selectBranch():
    try:
        c = banco.conexao.cursor()

        c.execute("SELECT * FROM branchs")

        rows = c.fetchall()

        c.close()
        
        return rows
    except:
        return "Ocorreu um erro na busca da filial"

def selectBranchById(id):
    try:
        c = banco.conexao.cursor()

        c.execute("SELECT * FROM branchs WHERE id = ?", (id,))

        row = c.fetchone()

        c.close()

        if(row == None):
            print("SELECT id não existe na base!")
            return False
        else:
            print("SELECT filial feita com sucesso!")
            print(row)
            return True
    except:
        print("Ocorreu um erro na pesquisa do id da filial")
        return False

def updateBranch(object):
    try:
        c = banco.conexao.cursor()
        id = object.id

        if(selectBranchById(id)):
            c.execute("UPDATE branchs SET value_name = ? WHERE id = ?", (object.value_name,object.id,))
            banco.conexao.commit()
            return print("UPDATE filial atualizada com sucesso!")

        c.close()
    except:
        return "Ocorreu um erro na atualização da filial"

def deleteBranch(object):
    try:
        c = banco.conexao.cursor()
        id = object.id

        if(selectBranchById(id)):
            c.execute("DELETE FROM branchs WHERE id = ?", (object.id,))
            banco.conexao.commit()
            return print("DELETE filial excluída com sucesso!")

        c.close()
    except:
        return "Ocorreu um erro na exclusão da filial"