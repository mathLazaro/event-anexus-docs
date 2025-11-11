import time
from playwright.sync_api import sync_playwright
from tests.login_test import fail_login, cadastro_organizador, cadastro_participante, login_organizador, login_participante

def main():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    fail_login(page)

    cadastro_organizador(page)

    login_organizador(page)

    cadastro_participante(page)

    login_participante(page)

    browser.close()

    

    return

if __name__ == "__main__":
    main()