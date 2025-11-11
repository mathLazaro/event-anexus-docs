# Event-Anexus Docs & Tests

Pequeno repositório com testes e recursos de documentação para o projeto Event-Anexus.

Pré-requisitos

- Python 3.8+ instalado

Instalação e setup (Windows e Linux/macOS)

Windows (CMD)

```cmd
python -m venv .venv
\.venv\Scripts\activate.bat
pip install -r requirements.txt
```

Linux / macOS (bash / zsh)

```bash
python3 -m venv .venv
# Ativar o venv
source .venv/bin/activate
pip install -r requirements.txt
```

Instalação de navegadores para Playwright

```bash
playwright install
```

- Dependências do sistema:

```bash
playwright install-deps
```

Executando os testes

- Executar o arquivo principal de testes diretamente:

```bash
python main_tests.py
```

Resultados

Imagens ou artefatos gerados pelos testes podem ser encontrados em `tests/img`.
