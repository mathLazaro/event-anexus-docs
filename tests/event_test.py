from playwright.sync_api import Page, expect


def cadastro_evento(page: Page):

    page.locator("button.border-dashed").click()

    page.locator('input[placeholder="Ex: Workshop de Angular Avançado"]').fill(
        "Titulo do Evento de Teste"
    )

    page.locator(
        'textarea[placeholder="Descreva o evento, conteúdo, público-alvo, etc..."]'
    ).fill("Descricao do Evento de Teste")

    page.locator("select").selectOption("Workshop")

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

    page.screenshot(path="tests/img/cadastro_evento.png")
