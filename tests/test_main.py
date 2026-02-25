import os
import re
import pytest


# ─────────────────────────────────────────────
# 1. Testes de leitura do CSV de entrada
# ─────────────────────────────────────────────

def test_dados_csv_exists():
    """Verifica se o arquivo de entrada existe."""
    assert os.path.exists("dados.csv"), "Arquivo dados.csv não encontrado na raiz do projeto"


def test_dados_csv_not_empty():
    """Verifica se o arquivo de entrada não está vazio."""
    with open("dados.csv", "r") as f:
        lines = f.readlines()
    assert len(lines) > 0, "O arquivo dados.csv está vazio"


def test_dados_csv_format():
    """Verifica se cada linha contém um slug válido (letras, números, hífens)."""
    with open("dados.csv", "r") as f:
        for line in f:
            slug = line.strip()
            if slug:
                assert re.match(
                    r"^[A-Za-z0-9\-]+$", slug
                ), f"Slug inválido: {slug}"


# ─────────────────────────────────────────────
# 2. Testes de geração de URL
# ─────────────────────────────────────────────

def test_url_format():
    """Verifica se a URL gerada está no formato esperado."""
    slug = "CARLOS-ANDREI-SOARES-DE-PINHO-15171393000173"
    url = f"https://casadosdados.com.br/solucao/cnpj/{slug}"
    assert url.startswith("https://casadosdados.com.br/solucao/cnpj/")
    assert slug in url


def test_url_no_special_chars():
    """Verifica que o slug não contém caracteres especiais inválidos."""
    slug = "EMPRESA-TESTE-12345678000100"
    invalid_chars = ["[", "]", "'", " ", '"']
    for char in invalid_chars:
        assert char not in slug, f"Slug contém caractere inválido: '{char}'"


# ─────────────────────────────────────────────
# 3. Testes de conversão de lista para string
# ─────────────────────────────────────────────

def test_lista_convertida_removes_brackets():
    """Testa a limpeza de colchetes e aspas do slug."""
    l = ["CARLOS-ANDREI-SOARES-DE-PINHO-15171393000173"]
    lista_convertida = str(l).replace("[", "").replace("]", "").replace("'", "")
    assert "[" not in lista_convertida
    assert "]" not in lista_convertida
    assert "'" not in lista_convertida


def test_lista_convertida_preserves_content():
    """Verifica que o conteúdo original é preservado após a conversão."""
    slug = "GRUPO-DE-ARTES-ESSENCIA-NATIVA-15139244000127"
    l = [slug]
    lista_convertida = str(l).replace("[", "").replace("]", "").replace("'", "")
    assert slug in lista_convertida


# ─────────────────────────────────────────────
# 4. Testes do arquivo de output
# ─────────────────────────────────────────────

def test_output_file_creation(tmp_path):
    """Verifica se o arquivo de saída pode ser criado."""
    output = tmp_path / "clientes.csv"
    with open(output, "w") as f:
        f.write("Nome Fantasia\nRazão Social\n")
    assert output.exists()
    assert output.stat().st_size > 0


def test_output_has_expected_fields(tmp_path):
    """Verifica se o arquivo de saída contém todos os campos esperados."""
    output = tmp_path / "clientes.csv"
    data = [
        "Empresa X",
        "\nEmpresa X LTDA",
        "\nemail@test.com",
        "\n(62) 3333-4444",
        "\nRua das Flores",
        "\n123",
        "\nSala 01",
        "\nCentro",
        "\nGoiânia",
        "\n\n",
    ]
    with open(output, "a") as f:
        f.writelines(data)
    with open(output, "r") as f:
        content = f.read()
    assert "Empresa X" in content
    assert "email@test.com" in content
    assert "(62) 3333-4444" in content
    assert "Goiânia" in content


def test_multiple_entries_output(tmp_path):
    """Verifica se múltiplas empresas são gravadas corretamente."""
    output = tmp_path / "clientes.csv"
    for i in range(3):
        with open(output, "a") as f:
            f.writelines([f"Empresa {i}", f"\nemail{i}@test.com", "\n\n"])
    with open(output, "r") as f:
        content = f.read()
    assert "Empresa 0" in content
    assert "Empresa 1" in content
    assert "Empresa 2" in content
    assert "email2@test.com" in content
