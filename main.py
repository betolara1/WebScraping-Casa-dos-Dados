from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

lista = [] #LISTA ONDE SERA SALVO OS DADOS DO ARQUIVO IMPORTADO

with open("dados.csv", "r") as arquivo: # ABRE O ARQUIVO DADOS.CSV
    for arq in arquivo:
        lista.append(arq.splitlines())

for l in lista:
    lista_convertida = str(l).replace('[', '').replace(']', '').replace("'", '') #RETIRA OS PONTOS NECESSARIO DO LINK
    servico = Service(ChromeDriverManager().install())

    navegador = webdriver.Chrome(service=servico)
    navegador.get('https://casadosdados.com.br/solucao/cnpj/' + lista_convertida)

    nome_empresa = navegador.find_element(By.XPATH, '//*[@id="__nuxt"]/div/section[4]/div[2]/div[1]/div/div[4]').text
    nome_fantasia = navegador.find_element(By.XPATH, '//*[@id="__nuxt"]/div/section[4]/div[2]/div[1]/div/div[3]').text
    email = navegador.find_element(By.XPATH, '//*[@id="__nuxt"]/div/section[4]/div[2]/div[1]/div/div[19]').text
    telefone = navegador.find_element(By.XPATH, '//*[@id="__nuxt"]/div/section[4]/div[2]/div[1]/div/div[20]').text
    rua = navegador.find_element(By.XPATH, '//*[@id="__nuxt"]/div/section[4]/div[2]/div[1]/div/div[12]').text
    numero = navegador.find_element(By.XPATH, '//*[@id="__nuxt"]/div/section[4]/div[2]/div[1]/div/div[13]').text
    complemento = navegador.find_element(By.XPATH, '//*[@id="__nuxt"]/div/section[4]/div[2]/div[1]/div/div[14]').text
    bairro = navegador.find_element(By.XPATH, '//*[@id="__nuxt"]/div/section[4]/div[2]/div[1]/div/div[15]').text
    cidade = navegador.find_element(By.XPATH, '//*[@id="__nuxt"]/div/section[4]/div[2]/div[1]/div/div[17]').text

    # CRIA UMA LISTA ONDE SALVA AS INFORMAÇÕES PARA GERAR O ARQUIVO CLIENTES.CSV
    arq = [nome_fantasia,'\n' + nome_empresa, '\n' + email, '\n' + telefone, '\n' + rua, '\n' + numero, '\n' + complemento, '\n' + bairro, '\n' + cidade, '\n\n']

    # ABRE/CRIA O ARQUIVO CLIENTES.CSV E ESCREVE OS DADOS RASPADOS
    arquivo = open('clientes.csv', 'a')
    arquivo.writelines(arq)
    arquivo.close()
