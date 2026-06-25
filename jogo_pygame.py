import os
import random
import unicodedata
import pygame

pygame.init()

LARGURA = 900
ALTURA = 600
FPS = 60

TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("The Professor Capivara")
RELOGIO = pygame.time.Clock()

AZUL_CEU = (135, 210, 245)
AZUL_RIO = (65, 160, 230)
AZUL_ESCURO = (30, 90, 150)
VERDE = (95, 185, 95)
VERDE_ESCURO = (45, 125, 60)
BRANCO = (245, 245, 245)
PRETO = (25, 25, 25)
BEGE = (255, 247, 225)
AMARELO = (245, 210, 80)
VERMELHO = (210, 65, 65)
MARROM = (155, 95, 45)

FONTE_TITULO = pygame.font.SysFont("arial", 40, bold=True)
FONTE_MEDIA = pygame.font.SysFont("arial", 26, bold=True)
FONTE_NORMAL = pygame.font.SysFont("arial", 22)
FONTE_PEQUENA = pygame.font.SysFont("arial", 18)
FONTE_SIMBOLO = pygame.font.SysFont("arial", 50, bold=True)

PREDADORES = [
    {"nome": "onça", "simbolo": "O", "arquivo": "onca.png", "cor": (240, 170, 80)},
    {"nome": "jacaré", "simbolo": "J", "arquivo": "jacare.png", "cor": (90, 170, 80)},
    {"nome": "serpente", "simbolo": "S", "arquivo": "serpente.png", "cor": (80, 180, 110)},
    {"nome": "gavião", "simbolo": "G", "arquivo": "gaviao.png", "cor": (180, 180, 180)},
    {"nome": "piranha", "simbolo": "P", "arquivo": "piranha.png", "cor": (220, 80, 80)},
]

PERGUNTAS = [
    {"tipo": "matematica", "texto": "Quanto é 7 + 5?", "resposta": "12"},
    {"tipo": "matematica", "texto": "Quanto é 3 x 4?", "resposta": "12"},
    {"tipo": "matematica", "texto": "Quanto é 20 - 8?", "resposta": "12"},
    {"tipo": "matematica", "texto": "Quanto é 15 + 6?", "resposta": "21"},
    {"tipo": "matematica", "texto": "Quanto é 9 x 2?", "resposta": "18"},
    {"tipo": "matematica", "texto": "Quanto é 30 dividido por 5?", "resposta": "6"},
    {"tipo": "matematica", "texto": "Quanto é 11 - 4?", "resposta": "7"},
    {"tipo": "matematica", "texto": "Quanto é 8 + 9?", "resposta": "17"},
    {"tipo": "matematica", "texto": "Quanto é 6 x 6?", "resposta": "36"},
    {"tipo": "matematica", "texto": "Quanto é 100 - 45?", "resposta": "55"},

    {"tipo": "gramatica", "texto": "Qual é o plural de animal?", "resposta": "animais"},
    {"tipo": "gramatica", "texto": "Complete: A capivara ___ pelo rio. (nada/nadam)", "resposta": "nada"},
    {"tipo": "gramatica", "texto": "A palavra 'rio' é substantivo? (sim/não)", "resposta": "sim"},
    {"tipo": "gramatica", "texto": "Qual é o feminino de professor?", "resposta": "professora"},
    {"tipo": "gramatica", "texto": "Qual é o plural de capivara?", "resposta": "capivaras"},
    {"tipo": "gramatica", "texto": "Complete: As crianças ___ felizes. (está/estão)", "resposta": "estão"},
    {"tipo": "gramatica", "texto": "A palavra 'feliz' é uma qualidade? (sim/não)", "resposta": "sim"},
    {"tipo": "gramatica", "texto": "A palavra 'onça' começa com qual letra?", "resposta": "o"},
    {"tipo": "gramatica", "texto": "Qual é o contrário de grande?", "resposta": "pequeno"},
    {"tipo": "gramatica", "texto": "Complete: O jacaré ___ forte. (é/são)", "resposta": "é"},

    {"tipo": "animais", "texto": "A capivara é um roedor? (sim/não)", "resposta": "sim"},
    {"tipo": "animais", "texto": "O jacaré vive em ambientes aquáticos? (sim/não)", "resposta": "sim"},
    {"tipo": "animais", "texto": "A onça é um animal herbívoro? (sim/não)", "resposta": "não"},
    {"tipo": "animais", "texto": "A piranha vive na água? (sim/não)", "resposta": "sim"},
    {"tipo": "animais", "texto": "A serpente tem patas? (sim/não)", "resposta": "não"},
    {"tipo": "animais", "texto": "O gavião é uma ave? (sim/não)", "resposta": "sim"},
    {"tipo": "animais", "texto": "A capivara gosta de ambientes com água? (sim/não)", "resposta": "sim"},
    {"tipo": "animais", "texto": "A onça é um predador? (sim/não)", "resposta": "sim"},
    {"tipo": "animais", "texto": "Peixes respiram debaixo da água? (sim/não)", "resposta": "sim"},
    {"tipo": "animais", "texto": "A capivara é uma ave? (sim/não)", "resposta": "não"},
]


def normalizar(texto):
    texto = texto.strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")
    return texto


def texto(texto, fonte, cor, x, y):
    imagem = fonte.render(texto, True, cor)
    TELA.blit(imagem, (x, y))


def texto_centro(texto, fonte, cor, x, y):
    imagem = fonte.render(texto, True, cor)
    ret = imagem.get_rect(center=(x, y))
    TELA.blit(imagem, ret)


def quebrar_texto(frase, fonte, largura_maxima):
    palavras = frase.split()
    linhas = []
    linha = ""

    for palavra in palavras:
        teste = linha + palavra + " "
        if fonte.size(teste)[0] <= largura_maxima:
            linha = teste
        else:
            linhas.append(linha.strip())
            linha = palavra + " "

    if linha:
        linhas.append(linha.strip())

    return linhas


def texto_multilinha(frase, fonte, cor, x, y, largura_maxima, altura_linha):
    linhas = quebrar_texto(frase, fonte, largura_maxima)

    for linha in linhas:
        texto(linha, fonte, cor, x, y)
        y += altura_linha

    return y


def carregar_imagem(nome_arquivo, tamanho):
    caminho = os.path.join("assets", nome_arquivo)

    try:
        if os.path.exists(caminho):
            imagem = pygame.image.load(caminho).convert_alpha()
            return pygame.transform.smoothscale(imagem, tamanho)
    except:
        return None

    return None


CAPIVARA_IMG = carregar_imagem("capivara.png", (120, 120))

IMAGENS_PREDADORES = {}
for predador in PREDADORES:
    IMAGENS_PREDADORES[predador["nome"]] = carregar_imagem(predador["arquivo"], (95, 95))


def salvar_resultado(nome, pontos, venceu):
    with open("ranking.txt", "a", encoding="utf-8") as arquivo:
        status = "venceu" if venceu else "perdeu"
        arquivo.write(f"{nome} - {pontos} pontos - {status}\n")


def sortear_baralho():
    return random.sample(PERGUNTAS, len(PERGUNTAS))


def criar_partida():
    baralho = sortear_baralho()
    pergunta = baralho.pop()

    return {
        "vidas": 3,
        "pontos": 0,
        "posicao": 0,
        "resposta": "",
        "mensagem": "Digite sua resposta e pressione ENTER.",
        "baralho": baralho,
        "pergunta": pergunta,
        "tipos_usados": {pergunta["tipo"]},
    }


def nova_pergunta(partida):
    if len(partida["baralho"]) == 0:
        partida["baralho"] = sortear_baralho()

    pergunta = partida["baralho"].pop()
    partida["pergunta"] = pergunta
    partida["tipos_usados"].add(pergunta["tipo"])


def desenhar_fundo():
    TELA.fill(AZUL_CEU)

    pygame.draw.circle(TELA, AMARELO, (800, 75), 35)

    pygame.draw.circle(TELA, BRANCO, (110, 80), 22)
    pygame.draw.circle(TELA, BRANCO, (140, 70), 28)
    pygame.draw.circle(TELA, BRANCO, (175, 80), 22)

    pygame.draw.circle(TELA, BRANCO, (430, 65), 22)
    pygame.draw.circle(TELA, BRANCO, (460, 55), 28)
    pygame.draw.circle(TELA, BRANCO, (495, 65), 22)

    pygame.draw.rect(TELA, VERDE, (0, 130, LARGURA, 70))
    pygame.draw.rect(TELA, VERDE_ESCURO, (0, 190, LARGURA, 12))

    pygame.draw.rect(TELA, AZUL_RIO, (0, 202, LARGURA, 205))
    pygame.draw.rect(TELA, AZUL_ESCURO, (0, 395, LARGURA, 12))

    pygame.draw.rect(TELA, VERDE, (0, 407, LARGURA, 193))

    for x in range(0, LARGURA, 80):
        pygame.draw.arc(TELA, BRANCO, (x, 260, 55, 25), 0, 3.14, 2)
        pygame.draw.arc(TELA, BRANCO, (x + 30, 325, 55, 25), 0, 3.14, 2)


def desenhar_painel(partida):
    pygame.draw.rect(TELA, BEGE, (25, 20, 390, 90), border_radius=16)
    pygame.draw.rect(TELA, PRETO, (25, 20, 390, 90), 3, border_radius=16)

    texto("THE PROFESSOR CAPIVARA", FONTE_MEDIA, PRETO, 42, 35)
    texto(f"Vidas: {partida['vidas']}", FONTE_NORMAL, VERMELHO, 42, 72)
    texto(f"Pontos: {partida['pontos']}", FONTE_NORMAL, PRETO, 165, 72)


def desenhar_capivara(x, y):
    if CAPIVARA_IMG:
        ret = CAPIVARA_IMG.get_rect(center=(x, y))
        TELA.blit(CAPIVARA_IMG, ret)
    else:
        pygame.draw.circle(TELA, MARROM, (x, y), 48)
        pygame.draw.circle(TELA, PRETO, (x, y), 48, 3)
        texto_centro("C", FONTE_SIMBOLO, BRANCO, x, y - 4)
        texto_centro("capivara", FONTE_PEQUENA, PRETO, x, y + 60)


def desenhar_predador(predador, x, y):
    imagem = IMAGENS_PREDADORES[predador["nome"]]

    if imagem:
        ret = imagem.get_rect(center=(x, y))
        TELA.blit(imagem, ret)
    else:
        pygame.draw.circle(TELA, predador["cor"], (x, y), 48)
        pygame.draw.circle(TELA, PRETO, (x, y), 48, 3)
        texto_centro(predador["simbolo"], FONTE_SIMBOLO, PRETO, x, y - 4)

    texto_centro(predador["nome"], FONTE_PEQUENA, PRETO, x, y + 60)


def desenhar_travessia(partida):
    posicoes = [100, 240, 380, 520, 660, 800]

    for i, x in enumerate(posicoes):
        pygame.draw.circle(TELA, AMARELO, (x, 390), 9)

        if i < len(posicoes) - 1:
            pygame.draw.line(TELA, AMARELO, (x + 12, 390), (posicoes[i + 1] - 12, 390), 3)

    desenhar_capivara(posicoes[partida["posicao"]], 300)

    if partida["posicao"] < len(PREDADORES):
        predador = PREDADORES[partida["posicao"]]
        desenhar_predador(predador, posicoes[partida["posicao"] + 1], 300)


def desenhar_pergunta(partida):
    pygame.draw.rect(TELA, BEGE, (35, 425, 830, 145), border_radius=18)
    pygame.draw.rect(TELA, PRETO, (35, 425, 830, 145), 3, border_radius=18)

    predador = PREDADORES[partida["posicao"]]
    pergunta = partida["pergunta"]

    pygame.draw.rect(TELA, AMARELO, (55, 440, 180, 28), border_radius=8)
    pygame.draw.rect(TELA, AZUL_CEU, (245, 440, 190, 28), border_radius=8)

    texto(f"Predador: {predador['nome']}", FONTE_PEQUENA, PRETO, 65, 444)
    texto(f"Tipo: {pergunta['tipo']}", FONTE_PEQUENA, PRETO, 255, 444)

    texto_multilinha(pergunta["texto"], FONTE_NORMAL, PRETO, 55, 478, 780, 26)

    pygame.draw.rect(TELA, BRANCO, (55, 520, 590, 35), border_radius=8)
    pygame.draw.rect(TELA, PRETO, (55, 520, 590, 35), 2, border_radius=8)

    texto(partida["resposta"], FONTE_NORMAL, PRETO, 65, 526)

    pygame.draw.rect(TELA, VERDE, (670, 520, 170, 35), border_radius=8)
    pygame.draw.rect(TELA, PRETO, (670, 520, 170, 35), 2, border_radius=8)
    texto_centro("ENTER", FONTE_NORMAL, PRETO, 755, 537)

    texto_multilinha(partida["mensagem"], FONTE_PEQUENA, AZUL_ESCURO, 55, 560, 780, 20)


def desenhar_tela_nome(nome_digitado):
    desenhar_fundo()

    pygame.draw.rect(TELA, BEGE, (150, 35, 600, 105), border_radius=20)
    pygame.draw.rect(TELA, PRETO, (150, 35, 600, 105), 4, border_radius=20)

    texto_centro("THE PROFESSOR CAPIVARA", FONTE_TITULO, PRETO, LARGURA // 2, 72)
    texto_centro("A travessia educativa pelo rio dos predadores", FONTE_NORMAL, AZUL_ESCURO, LARGURA // 2, 112)

    desenhar_capivara(300, 300)
    desenhar_predador(PREDADORES[1], 600, 300)

    pygame.draw.rect(TELA, BEGE, (210, 445, 480, 95), border_radius=18)
    pygame.draw.rect(TELA, PRETO, (210, 445, 480, 95), 3, border_radius=18)

    texto_centro("Digite seu nome e pressione ENTER", FONTE_MEDIA, PRETO, LARGURA // 2, 470)

    pygame.draw.rect(TELA, BRANCO, (250, 492, 400, 36), border_radius=8)
    pygame.draw.rect(TELA, PRETO, (250, 492, 400, 36), 2, border_radius=8)

    texto(nome_digitado, FONTE_NORMAL, PRETO, 262, 498)
    texto_centro("Responda aos desafios para ajudar a capivara a atravessar.", FONTE_PEQUENA, PRETO, LARGURA // 2, 570)


def desenhar_tela_jogo(partida):
    desenhar_fundo()
    desenhar_painel(partida)
    desenhar_travessia(partida)
    desenhar_pergunta(partida)


def desenhar_resultado(partida, nome, venceu):
    desenhar_fundo()
    desenhar_painel(partida)

    pygame.draw.rect(TELA, BEGE, (155, 150, 590, 300), border_radius=22)
    pygame.draw.rect(TELA, PRETO, (155, 150, 590, 300), 4, border_radius=22)

    if venceu:
        texto_centro("VITÓRIA!", FONTE_TITULO, VERDE_ESCURO, LARGURA // 2, 200)
        desenhar_capivara(LARGURA // 2, 285)
        frase = f"Parabéns, {nome}! A capivara atravessou o rio."
    else:
        texto_centro("FIM DE JOGO!", FONTE_TITULO, VERMELHO, LARGURA // 2, 200)
        desenhar_predador(PREDADORES[-1], LARGURA // 2, 285)
        frase = f"{nome}, a capivara perdeu todas as vidas."

    texto_centro(frase, FONTE_NORMAL, PRETO, LARGURA // 2, 360)
    texto_centro(f"Pontuação final: {partida['pontos']}", FONTE_MEDIA, PRETO, LARGURA // 2, 395)

    tipos = ", ".join(sorted(partida["tipos_usados"]))
    texto_centro(f"Tipos usados: {tipos}", FONTE_PEQUENA, PRETO, LARGURA // 2, 425)

    texto_centro("Pressione R para jogar novamente ou ESC para sair.", FONTE_PEQUENA, AZUL_ESCURO, LARGURA // 2, 485)


def processar_resposta(partida):
    resposta_jogador = normalizar(partida["resposta"])
    resposta_certa = normalizar(partida["pergunta"]["resposta"])
    resposta_correta_texto = partida["pergunta"]["resposta"]

    if resposta_jogador == "":
        partida["mensagem"] = "Digite uma resposta antes de apertar ENTER."
        return "continua"

    if resposta_jogador == resposta_certa:
        partida["pontos"] += 10
        partida["posicao"] += 1
        partida["resposta"] = ""

        if partida["posicao"] == len(PREDADORES):
            return "venceu"

        nova_pergunta(partida)
        partida["mensagem"] = "Resposta certa! A capivara avançou."
        return "continua"

    partida["vidas"] -= 1
    partida["resposta"] = ""

    if partida["vidas"] == 0:
        return "perdeu"

    nova_pergunta(partida)
    partida["mensagem"] = f"Resposta errada! A resposta correta era: {resposta_correta_texto}."
    return "continua"


def main():
    estado = "nome"
    nome_digitado = ""
    nome = ""
    partida = criar_partida()
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

                elif estado == "nome":
                    if evento.key == pygame.K_BACKSPACE:
                        nome_digitado = nome_digitado[:-1]
                    elif evento.key == pygame.K_RETURN:
                        nome = nome_digitado.strip()

                        if nome == "":
                            nome = "Jogador"

                        partida = criar_partida()
                        estado = "jogando"
                    elif evento.unicode.isprintable() and len(nome_digitado) < 18:
                        nome_digitado += evento.unicode

                elif estado == "jogando":
                    if evento.key == pygame.K_BACKSPACE:
                        partida["resposta"] = partida["resposta"][:-1]
                    elif evento.key == pygame.K_RETURN:
                        resultado = processar_resposta(partida)

                        if resultado == "venceu":
                            salvar_resultado(nome, partida["pontos"], True)
                            estado = "venceu"
                        elif resultado == "perdeu":
                            salvar_resultado(nome, partida["pontos"], False)
                            estado = "perdeu"
                    elif evento.unicode.isprintable() and len(partida["resposta"]) < 35:
                        partida["resposta"] += evento.unicode

                elif estado in ("venceu", "perdeu"):
                    if evento.key == pygame.K_r:
                        partida = criar_partida()
                        estado = "jogando"

        if estado == "nome":
            desenhar_tela_nome(nome_digitado)
        elif estado == "jogando":
            desenhar_tela_jogo(partida)
        elif estado == "venceu":
            desenhar_resultado(partida, nome, True)
        elif estado == "perdeu":
            desenhar_resultado(partida, nome, False)

        pygame.display.flip()
        RELOGIO.tick(FPS)

    pygame.quit()


main()