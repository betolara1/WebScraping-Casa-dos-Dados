# 🔍 WebScraping — Casa dos Dados

> Script de **web scraping** em Python + Selenium que coleta automaticamente dados cadastrais de empresas a partir de CNPJs, extraindo informações do portal [Casa dos Dados](https://casadosdados.com.br).

---

## 📌 Objetivo & Problema

| | Descrição |
|---|---|
| **Problema** | Consultar manualmente dados de empresas (razão social, e-mail, telefone, endereço) pelo CNPJ no site Casa dos Dados é lento e inviável para grandes volumes. |
| **Solução** | Automatizar a coleta via Selenium, lendo uma lista de CNPJs de um arquivo CSV e exportando os resultados estruturados para outro CSV — pronto para análise ou importação em CRMs. |

---

## 🏗️ Arquitetura

```
┌──────────────────────────────────────────────────────────────────┐
│                        WebScraping Pipeline                      │
│                                                                  │
│  ┌────────────┐    ┌──────────────────┐    ┌──────────────────┐  │
│  │ dados.csv  │───>│     main.py      │───>│  clientes.csv    │  │
│  │  (input)   │    │  Selenium Driver │    │    (output)      │  │
│  └────────────┘    └────────┬─────────┘    └──────────────────┘  │
│                             │                                    │
│                             ▼                                    │
│                  ┌─────────────────────┐                         │
│                  │  casadosdados.com.br │                         │
│                  │   (fonte de dados)  │                         │
│                  └─────────────────────┘                         │
└──────────────────────────────────────────────────────────────────┘
```

**Fluxo:**
1. O script lê cada linha do `dados.csv` (slug: razão social + CNPJ).
2. Abre o Chrome via **Selenium + WebDriver Manager**.
3. Acessa a página do CNPJ no Casa dos Dados.
4. Extrai os campos via **XPath** (nome, e-mail, telefone, endereço).
5. Grava os dados extraídos no arquivo `clientes.csv`.

---

## 🚀 Como Rodar

### Pré-requisitos

- **Python 3.8+**
- **Google Chrome** instalado
- **pip** (gerenciador de pacotes)

### Instalação (Dev)

```bash
# 1. Clone o repositório
git clone https://github.com/betolara1/WebScraping-Casa-dos-Dados.git
cd WebScraping-Casa-dos-Dados

# 2. (Recomendado) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# 3. Instale as dependências
pip install -r requirements.txt
```

### Execução

```bash
python main.py
```

> O script lê o arquivo `dados.csv`, processa cada CNPJ e grava os resultados em `clientes.csv`.

### Docker (Produção)

```bash
# Build da imagem
docker build -t webscraping-casa-dos-dados .

# Execução do container
docker run --rm \
  -v $(pwd)/dados.csv:/app/dados.csv \
  -v $(pwd)/clientes.csv:/app/clientes.csv \
  webscraping-casa-dos-dados
```



```dockerfile
FROM python:3.11-slim

# Instala Chrome e dependências do sistema
RUN apt-get update && apt-get install -y \
    wget gnupg unzip curl \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

</details>

---

## 📊 Exemplos de Input / Output

### Input — `dados.csv`

Cada linha contém o slug no formato `RAZAO-SOCIAL-CNPJ`:

```csv
CARLOS-ANDREI-SOARES-DE-PINHO-15171393000173
GRUPO-DE-ARTES-ESSENCIA-NATIVA-15139244000127
```

### URL gerada pelo script

```
https://casadosdados.com.br/solucao/cnpj/CARLOS-ANDREI-SOARES-DE-PINHO-15171393000173
```

### Output — `clientes.csv`

```csv
Nome Fantasia: EMPRESA EXEMPLO
Razão Social: EMPRESA EXEMPLO LTDA
Email: contato@empresa.com
Telefone: (62) 3333-4444
Rua: Rua das Flores
Número: 123
Complemento: Sala 01
Bairro: Centro
Cidade: Goiânia
```

### Dados extraídos por CNPJ

| Campo | XPath | Exemplo |
|---|---|---|
| Nome Fantasia | `div[3]` | EMPRESA EXEMPLO |
| Razão Social | `div[4]` | EMPRESA EXEMPLO LTDA |
| E-mail | `div[19]` | contato@empresa.com |
| Telefone | `div[20]` | (62) 3333-4444 |
| Logradouro | `div[12]` | Rua das Flores |
| Número | `div[13]` | 123 |
| Complemento | `div[14]` | Sala 01 |
| Bairro | `div[15]` | Centro |
| Cidade | `div[17]` | Goiânia |

---

## 📁 Estrutura do Projeto

```
WebScraping-Casa-dos-Dados/
├── main.py              # Script principal de scraping
├── dados.csv            # Arquivo de entrada (slugs CNPJ)
├── clientes.csv         # Arquivo de saída (gerado após execução)
├── requirements.txt     # Dependências Python
├── Dockerfile           # Containerização
├── .dockerignore        # Arquivos ignorados no build
├── .github/
│   └── workflows/
│       └── ci.yml       # Pipeline CI (lint + testes)
├── tests/
│   └── test_main.py     # Testes unitários (pytest)
└── README.md            # Esta documentação
```

---

## 🧪 Testes

Os testes estão em `tests/test_main.py` e cobrem:

- ✅ Validação do CSV de entrada (existência, formato, slugs)
- ✅ Geração correta de URLs
- ✅ Conversão de lista para string (limpeza de colchetes)
- ✅ Criação e escrita do arquivo de saída
- ✅ Múltiplas entradas gravadas corretamente

**Rodar os testes:**

```bash
pip install pytest
pytest tests/ -v
```

---

## ⚙️ GitHub Actions (CI)

Pipeline configurada em `.github/workflows/ci.yml`:

- **Trigger:** push/PR na branch `main`
- **Lint:** `flake8` no `main.py`
- **Testes:** `pytest tests/ -v`
- **Python:** 3.11 no Ubuntu latest

---

## 🛠️ Tecnologias

| Tecnologia | Versão | Uso |
|---|---|---|
| Python | 3.8+ | Linguagem principal |
| Selenium | 4.14.0 | Automação do navegador |
| WebDriver Manager | 4.0.1 | Gerenciamento automático do ChromeDriver |
| Google Chrome | latest | Navegador para scraping |

---

## ⚠️ Observações Importantes

- **Rate Limiting:** Recomenda-se adicionar `time.sleep()` entre as requisições para evitar bloqueio pelo site.
- **XPaths frágeis:** Os seletores XPath podem quebrar se o site mudar a estrutura HTML. Monitore e atualize conforme necessário.
- **Uso ético:** Respeite os termos de uso do site e faça scraping de forma responsável.
- **Dados pessoais:** Os dados coletados (e-mail, telefone) são sensíveis — utilize-os em conformidade com a LGPD.

---

## 👤 Autor

- GitHub: [@betolara1](https://github.com/betolara1)

---

⭐ Se este projeto te ajudou, considere dar uma estrela no GitHub!
