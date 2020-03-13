from db.banco import Banco

banco = Banco()

def insertTemplate(object):
    try:
        c = banco.conexao.cursor()

        c.execute("INSERT INTO templates (name, value, manager_code, service_name, allocation_value, nbs_code, contract_bool, average_bool, user_id, provider_id, allocation_id, branch_id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (object.name, object.value, object.manager_code, object.service_name, object.allocation_value, object.nbs_code, object.contract_bool, object.average_bool, object.user_id, object.provider_id, object.allocation_id, object.branch_id,))

        banco.conexao.commit()
        c.close()

        return "INSERT template feito com sucesso!"
    except:
        return print("Ocorreu um erro na inserção da template")

def selectTemplate():
    try:
        c = banco.conexao.cursor()

        c.execute("SELECT * FROM templates")

        rows = c.fetchall()

        c.close()
        
        return rows
    except:
        return "Ocorreu um erro na busca da template"

def selectTemplateById(id):
    try:
        c = banco.conexao.cursor()

        c.execute("SELECT * FROM templates WHERE id = ?", (id,))

        row = c.fetchone()

        c.close()

        if(row == None):
            print("SELECT id não existe na base!")
            return False
        else:
            print("SELECT template feita com sucesso!")
            print(row)
            return True
    except:
        print("Ocorreu um erro na pesquisa do id da template")
        return False

def updateTemplate(object):
    try:
        c = banco.conexao.cursor()
        id = object.id

        if(selectTemplateById(id)):
            c.execute("UPDATE templates SET name = ?, value = ?, manager_code = ?, service_name = ?, allocation_value = ?, nbs_code = ?, contract_bool = ?, average_bool = ?, user_id = ?, provider_id = ?, allocation_id = ?, branch_id = ? WHERE id = ?", (object.name, object.value, object.manager_code, object.service_name, object.allocation_value, object.nbs_code, object.contract_bool, object.average_bool, object.user_id, object.provider_id, object.allocation_id, object.branch_id, object.id))
            banco.conexao.commit()
            return print("UPDATE template atualizada com sucesso!")

        c.close()
    except:
        return print("Ocorreu um erro na atualização da template")

def deleteTemplate(object):
    try:
        c = banco.conexao.cursor()
        id = object.id

        if(selectTemplateById(id)):
            c.execute("DELETE FROM templates WHERE id = ?", (object.id,))
            banco.conexao.commit()
            return print("DELETE template excluída com sucesso!")

        c.close()
    except:
        return "Ocorreu um erro na exclusão da template"