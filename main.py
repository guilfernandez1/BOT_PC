#Declaração de imports#
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os
#---------------------#

#Declaração de listas#
lista_templates = []
lista_sequencia_contratos = []
#---------------------#

#Declaração de variáveis#
caminho = 'com.glideapp.servicecatalog.RenderCategory_0158152838378908'
flag = 0
#---------------------#

#Carregamento do arquivo Excel#
excel_file = 'C:/Users/GFERNANDEZ/Desktop/Python/Development/BOT_PC/sources/base.xlsx'
templates = pd.read_excel(excel_file, sheet_name=0)
numero_de_templates = int(templates.Template.count())

for linha in range(numero_de_templates):
    nome_template = templates.loc[linha, 'Template']
    lista_templates.append(nome_template)
#---------------------#

os.system('cls')

for contagem in range(len(lista_templates)):
    print(f'{contagem} - {lista_templates[contagem]}')

quantidade = int(input('Quantos templates ira executar? '))

os.system('cls')

for contador in range(quantidade):
    for contagem in range(len(lista_templates)):
        print(f'{contagem} - {lista_templates[contagem]}')
    escolha = int(input(f'{contador + 1} de {quantidade}: '))
    lista_sequencia_contratos.append(escolha)
    os.system('cls')

for contador in range(len(lista_sequencia_contratos)):
    index = lista_sequencia_contratos[contador]
    localidade = str(templates.loc[index, 'Localidade'])
    telefone = int(templates.loc[index, 'Ramal'])
    nome_SAP = str(templates.loc[index, 'Nome SAP'])
    cod_gestor_aprovador = str(templates.loc[index, 'Código Gestor'])
    tipo_requisicao = str(templates.loc[index, 'Tipo de Serviço'])
    nome_fornecedor = str(templates.loc[index, 'Fornecedor'])
    tipo_alocacao = str(templates.loc[index, 'Alocação'])
    num_cc_pep_ordem = str(templates.loc[index, 'CC/PEP/ORDEM'])
    bool_contrato = str(templates.loc[index, 'Existe Contrato'])
    num_linhasPedido = str(templates.loc[index, 'Linha Pedido'])
    num_CNPJ = str(templates.loc[index, 'CNPJ Fornecedor'])
    num_NBS = str(templates.loc[index, 'NBS'])
    valor_str = str(templates.loc[index, 'Valor'])
    valor = valor_str.replace(".", ",")
    bool_rateio = str(templates.loc[index, 'Existe Rateio'])
    cod_localidade = str(templates.loc[index, 'Filial'])
    num_contrato = int(templates.loc[index, 'Contrato'])
    num_item_contrato = int(templates.loc[index, 'Item Contrato'])
    descricao = str(templates.loc[index, 'Descrição'])
    arquivo_anexo = str(templates.loc[index, 'Arquivo'])

    if(flag == 0):
        #Inicialização WebDriver#
        options = Options()
        options.add_argument('start-maximized') # Inicia o browser com a tela maximizada
        options.add_argument('disable-infobars') # Desativa barra de informações
        options.add_argument("--disable-extensions") # Desativa extensões do navegador

        #Entra no site do CSC#
        driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\GFERNANDEZ\Desktop\Python\Development\BOT_PC\env\chromedriver.exe')
        driver.get("https://suzanoprod.service-now.com/csc")

        #Clica no link "login de rede Suzano"#
        elemento = driver.find_element_by_partial_link_text('login de rede Suzano').click()

        if(driver.current_url == 'https://sts.suzano.com.br/adfs/ls/idpinitiatedsignon.aspx?logintoRP=https://suzanoprod.service-now.com'):
            elemento = driver.find_element_by_id('userNameInput')
            elemento.send_keys('gfernandez@suzano.com.br')
            elemento.send_keys(Keys.ENTER)

            elemento = driver.find_element_by_id('passwordInput')
            elemento.send_keys('Fibria@456')
            elemento.send_keys(Keys.ENTER)

        flag = 1

    driver.get("https://suzanoprod.service-now.com/csc/csc_nucleo_avancado_fiscal.do")

    time.sleep(1)

    #Seleciona iframe dentro do documento HTML#
    iframes = driver.find_element_by_tag_name('iframe')
    driver.switch_to.frame(iframes)

    elemento = driver.find_element_by_partial_link_text('Emissão de Pedidos Descentralizados').click()

    elemento = driver.find_element_by_partial_link_text('Emissão de pedido de compra (PCE, PCD ou PC-CONTRATO)').click()

    time.sleep(1)

    inputLocalidade = driver.find_element_by_id('sys_display.IO:9b4eb656372d22405f58008993990e7b')
    inputLocalidade.send_keys(localidade)
    inputLocalidade.send_keys(Keys.ENTER)

    inputTelefone = driver.find_element_by_id('IO:d99e7696372d22405f58008993990ec0')
    inputTelefone.send_keys(telefone)
    inputTelefone.send_keys(Keys.ENTER) 

    inputFornecedor = driver.find_element_by_id('IO:5c652c360f6d6640646364aa42050e9c')
    inputFornecedor.send_keys(nome_fornecedor)
    inputFornecedor.send_keys(Keys.ENTER)

    inputTipoReq = driver.find_element_by_id('IO:40c4a4360f6d6640646364aa42050e85')
    inputTipoReq.send_keys(tipo_requisicao)
    inputTipoReq.send_keys(Keys.ENTER)

    inputTipoAlocacao = driver.find_element_by_id('IO:5cb0ec2637e962405f58008993990e8b')
    inputTipoAlocacao.send_keys(tipo_alocacao)
    inputTipoAlocacao.send_keys(Keys.ENTER)

    inputCCPEPORDEM = driver.find_element_by_id('IO:20ee7ba2dbe17b00eb87639014961921')
    inputCCPEPORDEM.send_keys(num_cc_pep_ordem)
    inputCCPEPORDEM.send_keys(Keys.ENTER)

    inputAreaAprov = driver.find_element_by_id('IO:c7d60a70db4a3bc0a9a3cf2414961964')
    inputAreaAprov.send_keys(cod_gestor_aprovador)
    inputAreaAprov.send_keys(Keys.ENTER)

    inputBoolContrato = driver.find_element_by_id('IO:63f397496fba3e40f9c1f46abb3ee436')
    inputBoolContrato.send_keys(bool_contrato)
    inputBoolContrato.send_keys(Keys.ENTER)

    if(bool_contrato == 'Sim'):
        inputNumContrato = driver.find_element_by_id('IO:8638d1e96f7fa60099def46abb3ee410')
        inputNumContrato.send_keys(num_contrato)
        inputNumContrato.send_keys(Keys.ENTER)

        inputNumContratoItem = driver.find_element_by_id('IO:b558552d6f7fa60099def46abb3ee460')
        inputNumContratoItem.send_keys(num_item_contrato)
        inputNumContratoItem.send_keys(Keys.ENTER)

    inputLinhasPedido = driver.find_element_by_id('IO:d6e5e8dfdb16cc10a9a3cf2414961984')
    inputLinhasPedido.send_keys(num_linhasPedido)
    inputLinhasPedido.send_keys(Keys.ENTER)

    inputCNPJ = driver.find_element_by_id('IO:3c5520760f6d6640646364aa42050e6e')
    inputCNPJ.send_keys(num_CNPJ)
    inputCNPJ.send_keys(Keys.ENTER)

    inputNumNBS = driver.find_element_by_id('IO:f153c0d0dbc86b00ec121a2f2a96192b')
    inputNumNBS.send_keys(num_NBS)
    inputNumNBS.send_keys(Keys.ENTER)

    inputValor = driver.find_element_by_id('IO:94a02135db439f4039e4a19b8a96191a')
    inputValor.send_keys(valor)
    inputValor.send_keys(Keys.ENTER)

    inputRateio = driver.find_element_by_id('IO:20b0ec2637e962405f58008993990e93')
    inputRateio.send_keys(bool_rateio)
    inputRateio.send_keys(Keys.ENTER)

    inputFilial = driver.find_element_by_id('IO:281915a16fbfa60099def46abb3ee402')
    inputFilial.send_keys(cod_localidade)
    inputFilial.send_keys(Keys.ENTER)

    inputLoginSAP = driver.find_element_by_id('IO:41efca1adbe9f740a9a3cf2414961909')
    inputLoginSAP.send_keys(nome_SAP)
    inputLoginSAP.send_keys(Keys.ENTER)
    
    inputDescricao = driver.find_element_by_id('IO:90b0ec2637e962405f58008993990e90')
    inputDescricao.send_keys(descricao)
    inputDescricao.send_keys(Keys.ENTER)

    elemento = driver.find_element_by_id('ni.IO:e370f45bdb56cc10a9a3cf2414961953_label').click()

    anexo = driver.find_element_by_id('sc_attachment_button')
    anexo.click()

    time.sleep(1)

    procuraArquivo = driver.find_element_by_id('attachFile')
    procuraArquivo.send_keys(f'C://Users/GFERNANDEZ/Desktop/Python/Development/BOT_PC/sources/anexos/{arquivo_anexo}')

    element = driver.find_element_by_xpath('//*[@id="attachment"]/div/div/header/button')
    element.click()

    # confirmaFinalizacao = driver.find_element_by_id('submit_button')
    # confirmaFinalizacao.click()