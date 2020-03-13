#Import's & from's
import tkinter as tk
from tkinter import *
from tkinter import ttk
from models.branch import Branch
from models.provider import Provider
from models.template import Template
from models.user import User
import dao.branch as b
import dao.provider as p
import dao.template as t
import dao.user as u

#Window variable
window = tk.Tk()
window.title("Suzano S.A")
widthButtons = 25
fontButtons = ("Arial", "10", "bold")
padxButtons = 10
padyButtons = 1.5

#Branch variable
name_branch = StringVar()

#Provider variable
name_provider = StringVar()
cnpj_provider = StringVar()

#Template variable
name_template = StringVar()
value_template = StringVar()
allocation_template = ['K - Centro de Custo', 'P - Projeto' , 'F - Ordem']
manager_template = ['R06', 'R07', 'R08', 'R09']
service_template = ['Material', 'Serviço']
allocation_value_template = StringVar()
nbs_template = StringVar()
contract_template = ['Sim', 'Não']
average_template = ['Sim', 'Não']
user_list = []
users = u.selectUser()
for user in users:
    user_list.append(user)
provider_list = []
providers = p.selectProvider()
for provider in providers:
    provider_list.append(provider)
branch_list = []
branchs = b.selectBranch()
for branch in branchs:
    branch_list.append(branch)

#User variable
name_user = StringVar()
tel_user = StringVar()
sap_user = StringVar()
location_user = StringVar()

def testeWindow():
    pass

def menuWindowMain():
    remove_all_widgets()

    btnCriar = tk.Button(window, text = "Criar Chamado", command = lambda:testeWindow(), font = fontButtons,
    width = widthButtons)
    btnCriar.pack(padx = padxButtons, pady = padyButtons)

    btnCadastro = tk.Button(window, text = "Cadastro de Informações", command = lambda:menuWindowCreate(), font = fontButtons,
    width = widthButtons)
    btnCadastro.pack(padx = padxButtons, pady = padyButtons)

    btnConsulta = tk.Button(window, text = "Consulta de Informações", command = lambda:testeWindow(), font = fontButtons,
    width = widthButtons)
    btnConsulta.pack(padx = padxButtons, pady = padyButtons)

    btnEdita = tk.Button(window, text = "Edição de Informações", command = lambda:testeWindow(), font = fontButtons,
    width = widthButtons)
    btnEdita.pack(padx = padxButtons, pady = padyButtons)

def menuWindowCreate():
    remove_all_widgets()

    btnCadastraFilial = tk.Button(window, text = "Filial", command = lambda:createWindowBranch(), font = fontButtons,
    width = widthButtons)
    btnCadastraFilial.pack(padx = padxButtons, pady = padyButtons)

    btnCadastraFornecedor = tk.Button(window, text = "Fornecedor", command = lambda:createWindowProvider(), font = fontButtons,
    width = widthButtons)
    btnCadastraFornecedor.pack(padx = padxButtons, pady = padyButtons)

    btnCadastraTemplate = tk.Button(window, text = "Template", command = lambda:createWindowTemplate(), font = fontButtons,
    width = widthButtons)
    btnCadastraTemplate.pack(padx = padxButtons, pady = padyButtons)

    btnCadastraUsuario = tk.Button(window, text = "Usuário", command = lambda:createWindowUser(), font = fontButtons,
    width = widthButtons)
    btnCadastraUsuario.pack(padx = padxButtons, pady = padyButtons)

    btnVoltar = tk.Button(window, text = "Voltar", command = lambda:menuWindowMain(), font = fontButtons,
    width = widthButtons)
    btnVoltar.pack(padx = padxButtons, pady = padyButtons)

def createWindowBranch():
    remove_all_widgets()

    lblTitle = tk.Label(window, text = "Cadastro de Filial").grid(row=0,columnspan=2)

    lblBranch = tk.Label(window, text= "Filial: ").grid(row = 1, column = 0, sticky = E)
    txtBranch = tk.Entry(window, textvariable = name_branch).grid(row=1, column = 1, sticky=(N, S, E, W))

    btnBack = tk.Button(window, text = "Voltar", command = lambda:menuWindowCreate()).grid(row=2, column = 0, sticky=W)
    btnCreate = tk.Button(window, text = "Cadastrar", command = lambda:insertBranch(name_branch)).grid(row=2, column = 1, sticky=E)

def createWindowProvider():
    remove_all_widgets()

    lblTitle = tk.Label(window, text = "Cadastro de Fornecedor").grid(row=0,columnspan=2)

    lblProvider = tk.Label(window, text= "Nome Fornecedor: ").grid(row = 1, column = 0, sticky = E)
    txtName = tk.Entry(window, textvariable = name_provider).grid(row=1, column = 1, sticky=(N, S, E, W))

    lblCnpj = tk.Label(window, text= "CNPJ: ").grid(row = 2, column = 0, sticky = E)
    txtCnpj = tk.Entry(window, textvariable = cnpj_provider).grid(row=2, column = 1, sticky=(N, S, E, W))

    btnBack = tk.Button(window, text = "Voltar", command = lambda:menuWindowCreate()).grid(row=3, column = 0, sticky=W)
    btnCreate = tk.Button(window, text = "Cadastrar", command = lambda:insertProvider(name_provider, cnpj_provider)).grid(row=3, column = 1, sticky=E)

def createWindowTemplate():
    remove_all_widgets()

    lblTitle = tk.Label(window, text = "Cadastro de Template").grid(row=0,columnspan=2)

    lblDesc = tk.Label(window, text= "Descrição Template: ").grid(row=1, column=0, sticky=E)
    txtDesc = tk.Entry(window, textvariable = name_template).grid(row=1, column=1, sticky=(N, S, E, W))

    lblUser = tk.Label(window, text= "Colaborador: ").grid(row=2, column=0, sticky=E)
    lblUser = ttk.Combobox(window, values = user_list).grid(row=2, column=1, sticky=(N, S, E, W))

    lblProvider = tk.Label(window, text= "Fornecedor: ").grid(row=3, column=0, sticky=E)
    txtProvider = ttk.Combobox(window, values = provider_list).grid(row=3, column=1, sticky=(N, S, E, W))

    lblService = tk.Label(window, text= "Tipo de requisição: ").grid(row=4, column=0, sticky=E)
    txtService = ttk.Combobox(window, values = service_template).grid(row=4, column=1, sticky=(N, S, E, W))

    lblAllocation_opt = tk.Label(window, text= "Centro de Custo, Ordem ou PEP: ").grid(row=5, column=0, sticky=E)
    txtAllocation_opt = ttk.Combobox(window, values = allocation_template).grid(row=5, column=1, sticky=(N, S, E, W))

    lblAllocation = tk.Label(window, text= "Custos: ").grid(row=6, column=0, sticky=E)
    txtAllocation = tk.Entry(window, textvariable = allocation_value_template).grid(row=6, column=1, sticky=(N, S, E, W))

    lblManager = tk.Label(window, text= "Área do Aprovador: ").grid(row=7, column=0, sticky=E)
    txtManager = ttk.Combobox(window, values = manager_template).grid(row=7, column=1, sticky=(N, S, E, W))

    lblValue = tk.Label(window, text= "Valor: ").grid(row=8, column = 0, sticky = E)
    txtValue = tk.Entry(window, textvariable = value_template).grid(row=8, column = 1, sticky=(N, S, E, W))

    lblNbs = tk.Label(window, text= "NBS: ").grid(row=9, column = 0, sticky = E)
    txtNbs = tk.Entry(window, textvariable = nbs_template).grid(row=9, column = 1, sticky=(N, S, E, W))

    lblContrato = tk.Label(window, text= "Contrato: ").grid(row=10, column = 0, sticky = E)
    txtContrato = ttk.Combobox(window, values = contract_template).grid(row=10, column = 1, sticky=(N, S, E, W))

    lblRateio = Label(window, text= "Rateio: ").grid(row=11, column = 0, sticky = E)
    txtRateio = ttk.Combobox(window, values = average_template).grid(row=11, column = 1, sticky=(N, S, E, W))

    lblBranch = tk.Label(window, text= "Filial: ").grid(row=12, column = 0, sticky = E)
    txtBranch = ttk.Combobox(window, values = branch_list).grid(row=12, column = 1, sticky=(N, S, E, W))

    btnBack = tk.Button(window, text = "Voltar", command = lambda:menuWindowCreate()).grid(row=13, column = 0, sticky=W)
    btnCreate = tk.Button(window, text = "Cadastrar", command = lambda:insertTemplate(name_template, value_template, allocation_template, manager_template, service_template, allocation_value_template, nbs_template, contract_template, average_template, user_list, provider_list, branch_list)).grid(row=13, column = 1, sticky=E)

def createWindowUser():
    remove_all_widgets()

    lblTitle = tk.Label(window, text = "Cadastro de Colaborador").grid(row=0, columnspan = 2)

    lblName = tk.Label(window, text= "Nome AD: ").grid(row = 1, column = 0, sticky = E)
    txtName = tk.Entry(window, textvariable = name_user).grid(row=1, column = 1,  sticky=(N, S, E, W))

    lblTel = tk.Label(window, text= "Ramal: ").grid(row = 2, column = 0, sticky = E)
    txtTel = tk.Entry(window, textvariable = tel_user).grid(row=2, column = 1,  sticky=(N, S, E, W))

    lblSap = tk.Label(window, text= "Nome SAP: ").grid(row = 3, column = 0, sticky = E)
    txtSap = tk.Entry(window, textvariable = sap_user).grid(row=3, column = 1,  sticky=(N, S, E, W))

    lblLocal = tk.Label(window, text= "Local: ").grid(row = 4, column = 0, sticky = E)
    txtLocal = tk.Entry(window, textvariable = location_user).grid(row=4, column = 1, sticky=(N, S, E, W))

    btnBack = tk.Button(window, text = "Voltar", command = lambda:menuWindowCreate()).grid(row=5, column = 0, sticky=W)
    btnCreate = tk.Button(window, text = "Cadastrar", command = lambda:insertUser(name_user, tel_user, sap_user, location_user)).grid(row=5, column = 1, sticky=E)

def remove_all_widgets():
    global window
    for widget in window.winfo_children():
        widget.destroy()

def selectBranch():
    lista = b.selectBranch()

    for item in lista:
        print(item)

def selectProvider():
    lista = p.selectProvider()

    for item in lista:
        print(item)

def selectTemplate():
    lista = t.selectTemplate()

    for item in lista:
        print(item)

def selectUser():
    lista = u.selectUser()

    for item in lista:
        print(item)

def insertBranch(_name):
    name = (_name.get())
    branch = Branch(0, name_branch)
    d.insertBranch(branch)
    print("Filial {}, cadastrada com sucesso!".format(branch.value_name))

def insertProvider(_name, _cnpj):
    name = (_name.get())
    cnpj = (_cnpj.get())
    provider = Provider(0, name, cnpj)
    p.insertProvider(provider)
    print("Fornecedor {}, cadastrado com sucesso!".format(provider.name))

def insertTemplate(_name, _value, _allocation, _manager, _service, _allocation_value, _nbs, _contract, _average, _user, _provider, _branch):
    name = (_allocation.get())
    value = (_value.get())
    allocation = (_allocation.get())
    manager = (_manager.get())
    service = (_service.get())
    allocation_value = (_allocation_value.get())
    nbs = (_nbs.get())
    contract = (_contract.get())
    average = (_average.get())
    user = (_user.get())
    provider = (_provider.get())
    branch = (_branch.get())
    template = Template(0, name, value, allocation, manager, service, allocation_value, nbs, contract, average, user, provider, branch)
    t.insertTemplate(template)
    print("Template {}, cadastrado com sucesso!".format(template.name))

def insertUser(_name_user, _tel_user, _sap_user, _location_user):
    name_ad = (_name_user.get())
    tel = (_tel_user.get())
    sap_name = (_sap_user.get())
    location = (_location_user.get())
    user = User(0, name_ad, tel, sap_name, location)
    u.insertUser(user) 
    print("Usuário {}, cadastrado com sucesso!".format(user.name_ad))

menuWindowMain()
window.mainloop()