import time
from playwright.sync_api import sync_playwright
from tests.login_test import (
    esqueci_senha,
    fail_login,
    cadastro,
    login,
)

from tests.event_test import (
    cadastro_evento,
    cancelar_inscricao_evento,
    editar_evento,
    excluir_evento,
    inscrever_evento,
)


def main():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Dados de teste

    email_organizador = "email3@teste.com"
    senha_organizador = "senhaDeTeste@123"

    email_participante = "email@teste.com"
    senha_participante = "senhaDeTeste@123"

    titulo_evento = "Titulo do Evento de Teste"
    titulo_evento_2 = "Titulo Evento de Teste 2"

    # Testes
    fail_login(page)

    cadastro(email_organizador, senha_organizador, page, organizador=True)

    # esqueci_senha(email_organizador, senha_organizador, page)

    login(email_organizador, senha_organizador, page)

    cadastro_evento(titulo_evento, page)

    editar_evento(titulo_evento, page)

    cadastro_evento(titulo_evento_2, page)

    excluir_evento(titulo_evento_2, page)

    cadastro(email_participante, senha_participante, page)

    login(email_participante, senha_participante, page)

    inscrever_evento(titulo_evento, page)

    cancelar_inscricao_evento(titulo_evento, page)

    browser.close()

    return


if __name__ == "__main__":
    main()
