from db.banco import Banco

banco = Banco()

def insertUser(object):
    try:
        c = banco.conexao.cursor()

        c.execute("INSERT INTO users (name_ad, tel, sap_name, location) VALUES (?,?,?,?)", (object.name_ad, object.tel, object.sap_name, object.location,))

        banco.conexao.commit()
        c.close()

        return "INSERT usuário feito com sucesso!"
    except:
        return print("Ocorreu um erro na inserção da usuário")

def selectUser():
    try:
        c = banco.conexao.cursor()

        c.execute("SELECT * FROM users")

        rows = c.fetchall()

        c.close()
        
        return rows
    except:
        return "Ocorreu um erro na busca da usuário"

def selectUserById(id):
    try:
        c = banco.conexao.cursor()

        c.execute("SELECT * FROM users WHERE id = ?", (id,))

        row = c.fetchone()

        c.close()

        if(row == None):
            print("SELECT id não existe na base!")
            return False
        else:
            print("SELECT usuário feita com sucesso!")
            print(row)
            return True
    except:
        print("Ocorreu um erro na pesquisa do id da usuário")
        return False

def updateUser(object):
    try:
        c = banco.conexao.cursor()
        id = object.id

        if(selectUserById(id)):
            c.execute("UPDATE users SET name_ad = ?, tel = ?, sap_name = ?, location = ? WHERE id = ?", (object.name_ad, object.tel, object.sap_name, object.location, object.id,))
            banco.conexao.commit()
            return print("UPDATE usuário atualizada com sucesso!")

        c.close()
    except:
        return print("Ocorreu um erro na atualização da usuário")

def deleteUser(object):
    try:
        c = banco.conexao.cursor()
        id = object.id

        if(selectUserById(id)):
            c.execute("DELETE FROM users WHERE id = ?", (object.id,))
            banco.conexao.commit()
            return print("DELETE usuário excluída com sucesso!")

        c.close()
    except:
        return "Ocorreu um erro na exclusão da usuário"