from playwright.sync_api import Page, expect

def fail_login(page: Page):
    page.goto("http://localhost:4200/login")

    page.locator('input[placeholder="seu@email.com"]').fill("teste@teste.com")

    page.locator('input[placeholder="Digite sua senha"]').fill("teste@teste.com")

    page.locator('xpath=/html/body/app-root/div/app-auth-shell/main/app-login/section/div/div[2]/form/div[3]/app-button[1]/button').click()
    
    page.wait_for_timeout(5000)  # pausa 3 segundos

    page.screenshot(path="tests/img/fail_login.png")

def login_participante(page: Page):
    page.goto("http://localhost:4200/login")

    page.locator('input[placeholder="seu@email.com"]').fill("email@teste.com")

    page.locator('input[placeholder="Digite sua senha"]').fill("senhaDeTeste@123")

    page.locator('xpath=/html/body/app-root/div/app-auth-shell/main/app-login/section/div/div[2]/form/div[3]/app-button[1]/button').click()
    
    page.wait_for_timeout(5000)  # pausa 3 segundos

    page.screenshot(path="tests/img/login_participante.png")


def login_organizador(page: Page):
    page.goto("http://localhost:4200/login")

    page.locator('input[placeholder="seu@email.com"]').fill("email2@teste.com")

    page.locator('input[placeholder="Digite sua senha"]').fill("senhaDeTeste@123")

    page.locator('xpath=/html/body/app-root/div/app-auth-shell/main/app-login/section/div/div[2]/form/div[3]/app-button[1]/button').click()
    
    page.wait_for_timeout(5000)  # pausa 3 segundos

    page.screenshot(path="tests/img/login_organizador.png")

def cadastro_participante(page: Page):
    # Página inicial
    page.goto("http://localhost:4200/login")

    page.locator('xpath=/html/body/app-root/div/app-auth-shell/main/app-login/section/div/div[2]/form/div[3]/app-button[2]/button').click()

    # Página cadastro
    page.locator('input[name="name"]').fill('Nome de teste')

    page.locator('app-cadastro input[name="email"]').fill('email@teste.com')

    page.locator('input[name="telephone_number"]').fill('12345678910')

    page.locator('app-cadastro input[name="password"]').fill('senhaDeTeste@123')

    page.locator('input[name="confirmPassword"]').fill('senhaDeTeste@123')

    page.get_by_role("button", name="Cadastrar").click()

    page.wait_for_timeout(5000)  # pausa 3 segundos

    page.screenshot(path="tests/img/cadastro_participante.png")

def cadastro_organizador(page: Page):
    # Página inicial
    page.goto("http://localhost:4200/login")

    page.locator('xpath=/html/body/app-root/div/app-auth-shell/main/app-login/section/div/div[2]/form/div[3]/app-button[2]/button').click()

    # Página cadastro
    page.locator('input[name="name"]').fill('Nome de teste 2')

    page.locator('app-cadastro input[name="email"]').fill('email2@teste.com')

    page.locator('input[name="telephone_number"]').fill('12345678910')

    page.locator('app-cadastro input[name="password"]').fill('senhaDeTeste@123')

    page.locator('input[name="confirmPassword"]').fill('senhaDeTeste@123')

    page.get_by_label("Organizador").check()

    page.get_by_role("button", name="Cadastrar").click()

    page.wait_for_timeout(5000)  # pausa 3 segundos

    page.screenshot(path="tests/img/cadastro_organizador.png")