from playwright.sync_api import Page, expect


def fail_login(page: Page, screenshot_prefix: str = ""):
    page.goto("http://localhost:4200/login")

    page.locator('input[placeholder="seu@email.com"]').fill("teste@teste.com")

    page.locator('input[placeholder="Digite sua senha"]').fill("teste@teste.com")

    page.locator(
        "xpath=/html/body/app-root/div/app-auth-shell/main/app-login/section/div/div[2]/form/div[3]/app-button[1]/button"
    ).click()

    page.wait_for_timeout(3000)  # pausa 3 segundos

    page.screenshot(path=f"tests/img/{screenshot_prefix} fail_login.png")

    # Lida com o possível pop-up de erro
    try:
        page.locator('button.bg-red-600:has-text("OK")').click(timeout=1000)
    except:
        pass


def login(email: str, senha: str, page: Page, screenshot_prefix: str = ""):
    page.goto("http://localhost:4200/login")

    page.locator('input[placeholder="seu@email.com"]').fill(email)

    page.locator('input[placeholder="Digite sua senha"]').fill(senha)

    page.locator(
        "xpath=/html/body/app-root/div/app-auth-shell/main/app-login/section/div/div[2]/form/div[3]/app-button[1]/button"
    ).click()

    page.wait_for_timeout(3000)  # pausa 3 segundos

    page.screenshot(path=f"tests/img/{screenshot_prefix} login.png")

    # Lida com o possível pop-up de erro
    try:
        page.locator('button.bg-red-600:has-text("OK")').click(timeout=1000)
    except:
        pass


def cadastro(
    email: str,
    senha: str,
    page: Page,
    organizador: bool = False,
    screenshot_prefix: str = "",
):
    # Página inicial
    page.goto("http://localhost:4200/login")

    page.locator(
        "xpath=/html/body/app-root/div/app-auth-shell/main/app-login/section/div/div[2]/form/div[3]/app-button[2]/button"
    ).click()

    # Página cadastro
    page.locator('input[placeholder="Digite seu nome"]').fill("Nome de teste 2")

    page.locator('input[placeholder="seu@email.com"]').fill(email)

    page.locator('input[placeholder="(00) 00000-0000"]').fill("12345678910")

    page.locator('input[placeholder="Mínimo 8 caracteres"]').fill(senha)
    page.locator('input[placeholder="Digite a senha novamente"]').fill(senha)

    if organizador:
        page.get_by_label("Organizador").check()

    page.get_by_role("button", name="Cadastrar").click()

    page.wait_for_timeout(3000)  # pausa 3 segundos

    if organizador:
        path = f"tests/img/{screenshot_prefix} cadastro_organizador.png"
    else:
        path = f"tests/img/{screenshot_prefix} cadastro_participante.png"

    page.screenshot(path=path)

    # Lida com o possível pop-up de erro
    try:
        page.locator('button.bg-red-600:has-text("OK")').click(timeout=1000)
    except:
        pass


def edit_user(
    page: Page,
    name: str = None,
    tel: str = None,
    Departamento: str = None,
    excluir: bool = False,
    screenshot_prefix: str = "",
):
    page.locator('button:has-text("Ver perfil")').click()

    if excluir:
        page.locator('button:has-text("Excluir Conta")').click()

        page.locator('button:has-text("Confirmar")').click()

        page.wait_for_timeout(3000)  # pausa 3 segundos

        page.screenshot(path=f"tests/img/{screenshot_prefix} excluir_user.png")

        page.locator('button:has-text("OK")').click()

        page.screenshot(path=f"tests/img/{screenshot_prefix}2 excluir_user.png")

        return

    if name:
        page.locator('input[placeholder="Digite seu nome completo"]').fill(name)

    if tel:
        page.locator('input[placeholder="(00) 00000-0000"]').fill(tel)

    if Departamento:
        page.locator('input[placeholder="Ex: TI, RH, Vendas"]').fill(Departamento)

    page.locator('button.bg-secondary:has-text("Salvar Alterações")').click()

    page.wait_for_timeout(3000)  # pausa 3 segundos

    page.screenshot(path=f"tests/img/{screenshot_prefix} edit_user.png")

    page.locator('button:has-text("OK")').click()

    page.screenshot(path=f"tests/img/{screenshot_prefix}2 edit_user.png")

    page.locator('a:has-text("Dashboard")').click()
