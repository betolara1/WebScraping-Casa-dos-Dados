# 🔍 WebScraping Casa dos Dados

## 📋 Sobre o Projeto

Script de web scraping desenvolvido em Python para extrair dados do site Casa dos Dados. O projeto automatiza a coleta de informações de empresas através de CNPJ e razão social.

## 🚀 Funcionalidades

- Raspagem automatizada de dados
- Geração de arquivo CSV com os dados coletados
- Suporte para pesquisa por CNPJ e razão social
- Processamento em lote de múltiplos registros

## 🛠️ Pré-requisitos

- Python 3.x
- Bibliotecas Python (listadas em requirements.txt)

## ⚙️ Instalação

1. Clone o repositório:
   git clone https://github.com/betolara1/WebScraping-Casa-dos-Dados.git
   cd WebScraping-Casa-dos-Dados
   
3. Instale as dependências:
```shellscript
pip install -r requirements.txt
```



## 📊 Como Usar

1. Prepare o arquivo de entrada com os dados necessários:

1. Formato: andrea-juliano-duarte-07921640000264
2. O arquivo deve conter a razão social e CNPJ no formato especificado


2. Execute o script:
```shellscript
python main.py
```

3. O resultado será salvo em um arquivo dados.csv


## 📝 Exemplo de Uso

URL de exemplo para raspagem:

```plaintext
https://casadosdados.com.br/solucao/cnpj/andrea-juliano-duarte-07921640000264
```

Para pesquisa avançada, utilize:

```plaintext
https://casadosdados.com.br/solucao/cnpj/pesquisa-avancada
```

## ⚠️ Observações Importantes

1. O tempo de execução pode variar dependendo do volume de dados a serem raspados
2. Para modificar campos específicos, copie o XPATH do elemento desejado
3. Um arquivo dados.csv de exemplo está incluído no repositório para referência
4. Recomenda-se fazer a raspagem com tempo adequado para evitar sobrecarga


## 📁 Estrutura do Projeto

```plaintext
WebScraping-Casa-dos-Dados/
├── main.py            # Script principal
├── dados.csv          # Arquivo de exemplo/resultado
├── requirements.txt   # Dependências do projeto
└── README.md         # Documentação
```

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas alterações (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request


## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👤 Autor

- GitHub: [@betolara1](https://github.com/betolara1)


⭐️ Se este projeto te ajudou, considere dar uma estrela no GitHub!
