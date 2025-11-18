import time
from playwright.sync_api import sync_playwright
from tests.login_test import (
    esqueci_senha,
    fail_login,
    cadastro_organizador,
    cadastro_participante,
    login_organizador,
    login_participante,
)

# from tests.event_test import cadastro_evento


def main():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Dados de teste

    email_organizador = "email3@teste.com"
    senha_organizador = "senhaDeTeste@123"

    email_participante = "email@teste.com"
    senha_participante = "senhaDeTeste@123"

    # Testes
    fail_login(page)

    cadastro_organizador(email_organizador, senha_organizador, page)

    # esqueci_senha(email_organizador, senha_organizador, page)

    login_organizador(email_organizador, senha_organizador, page)

    # cadastro_evento(page)

    cadastro_participante(email_participante, senha_participante, page)

    login_participante(email_participante, senha_participante, page)

    browser.close()

    return


if __name__ == "__main__":
    main()
