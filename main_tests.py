import time
from playwright.sync_api import sync_playwright
from tests.login_test import (
    edit_user,
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

    email_organizador = "email_org_6@teste.com"
    senha_organizador = "senhaDeTeste@123"

    email_participante = "email_part_6@teste.com"
    senha_participante = "senhaDeTeste@123"

    titulo_evento = "Titulo do Evento de Teste 1"
    titulo_evento_2 = "Titulo do Evento de Teste 2"

    # Testes
    fail_login(page, screenshot_prefix="1.")

    # RFS01 - Cadastro de Usuário
    cadastro(
        email_organizador,
        senha_organizador,
        page,
        organizador=True,
        screenshot_prefix="2.",
    )

    # RFS12 - Login Usuário
    login(email_organizador, senha_organizador, page, screenshot_prefix="3.")

    # RFS02 - Editar Usuário
    edit_user(
        page,
        name="Organizador de Teste Editado",
        tel="11999998888",
        Departamento="Eventos",
        screenshot_prefix="4.",
    )

    # RFS04 - Cadastro de Evento
    cadastro_evento(titulo_evento, page, screenshot_prefix="5.")

    # RFS05 - Edição de Evento
    editar_evento(titulo_evento, page, screenshot_prefix="6.")

    # RFS06 - Exclusão de Evento
    cadastro_evento(titulo_evento_2, page, screenshot_prefix="7.")

    excluir_evento(titulo_evento_2, page, screenshot_prefix="8.")

    # RFS01 - Cadastro de Usuário Participante
    cadastro(email_participante, senha_participante, page, screenshot_prefix="9.")

    # RFS12 - Login Usuário
    login(email_participante, senha_participante, page, screenshot_prefix="10.")

    # RFS08 e RFS09 - Visualizar e Inscrever em Evento
    inscrever_evento(titulo_evento, page, screenshot_prefix="11.")

    # RFS10 - Cancelar Inscrição em Evento
    cancelar_inscricao_evento(titulo_evento, page, screenshot_prefix="12.")

    # RFS03 - Excluir Usuário
    edit_user(excluir=True, page=page, screenshot_prefix="13.")

    browser.close()

    return


if __name__ == "__main__":
    main()
