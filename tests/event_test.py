from playwright.sync_api import Page, expect


def cadastro_evento(titulo: str, page: Page):

    if page.url.startswith("http://localhost:4200/dashboard-admin/eventos"):
        page.locator('button:has-text("Criar Novo Evento")').click()
    else:
        page.locator('button:has-text("Criar Evento")').click()

    page.locator('input[placeholder="Ex: Workshop de Angular Avançado"]').fill(titulo)

    page.locator(
        'textarea[placeholder="Descreva o evento, conteúdo, público-alvo, etc..."]'
    ).fill("Descricao do Evento de Teste")

    page.locator("select").select_option("Workshop")

    page.locator('input[placeholder="DD/MM/AAAA"]').fill("24122025")

    page.locator('input[placeholder="HH:MM"]').fill("1800")

    page.locator('input[placeholder="Ex: Auditório Central, Online, etc."]').fill(
        "Na rua"
    )

    page.locator('input[placeholder="Digite a capacidade"]').fill("12")

    page.locator(
        'input[placeholder="Nome do responsável (aparecerá no certificado)"]'
    ).fill("Cleitinho")

    page.locator('button:has-text("Criar Evento")').click()

    page.locator('button:has-text("OK")').click()

    page.wait_for_timeout(3000)  # pausa 3 segundos

    page.screenshot(path="tests/img/cadastro_evento.png")


def editar_evento(titulo: str, page: Page):

    page.locator(
        f'div.bg-white:has(h3:has-text("{titulo}")) button:has-text("Editar")'
    ).first.click()

    page.locator('input[placeholder="Nome do palestrante"]').fill("Cleitinho da Silva")

    page.locator('button:has-text("Salvar Alterações")').click()

    page.locator('button:has-text("OK")').click()

    page.wait_for_timeout(3000)  # pausa 3 segundos

    page.screenshot(path="tests/img/editar_evento.png")


def excluir_evento(titulo: str, page: Page):

    page.locator(
        f'div.bg-white:has(h3:has-text("{titulo}")) button.bg-red-500'
    ).first.click()

    page.locator('button:has-text("Confirmar")').click()

    page.locator('button:has-text("OK")').click()

    page.wait_for_timeout(3000)  # pausa 3 segundos

    page.screenshot(path="tests/img/excluir_evento.png")


def inscrever_evento(titulo: str, page: Page):

    page.locator('button:has-text("Ver todos")')

    # Pesquisar evento
    # page.locator('input[placeholder="Buscar eventos por título, descrição..."]').fill("Eventos")

    page.locator(
        f'article:has(h3:has-text("{titulo}")) button:has-text("Inscrever-se")'
    ).first.click()

    # Lida com o possível pop-up de erro
    try:
        page.locator('button.bg-red-600:has-text("OK")').click(timeout=1000)
    except:
        page.screenshot(path="tests/img/inscrever_evento.png")
        return

    page.locator('button:has-text("Inscrever-se no Evento")').click()

    page.locator('button.bg-blue-600:has-text("Confirmar")').click()

    page.locator('button:has-text("OK")').click()

    page.wait_for_timeout(3000)  # pausa 3 segundos

    page.screenshot(path="tests/img/inscrever_evento.png")


def cancelar_inscricao_evento(titulo: str, page: Page):

    if not page.url.startswith("http://localhost:4200/dashboard-admin/eventos"):
        page.locator('a:has-text("Minhas Inscrições")').click()

    page.locator(
        f'div.bg-white:has(h3:has-text("{titulo}")) button:has-text("Cancelar Inscrição")'
    ).first.click()

    page.locator('button:has-text("Confirmar")').click()

    page.locator('button:has-text("OK")').click()

    page.wait_for_timeout(3000)  # pausa 3 segundos

    page.screenshot(path="tests/img/cancelar_inscricao_evento.png")


def ver_detalhes_evento(titulo: str, page: Page):

    if not page.url.startswith(
        "http://localhost:4200/dashboard-participant/minhas-inscricoes"
    ):
        page.locator('a:has-text("Minhas Inscrições")').click()

    page.locator(
        f'article:has(h3:has-text("{titulo}")) button:has-text("Ver Detalhes")'
    ).first.click()

    page.wait_for_timeout(3000)  # pausa 3 segundos

    page.screenshot(path="tests/img/ver_detalhes_evento.png")
