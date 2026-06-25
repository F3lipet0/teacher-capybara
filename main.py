import random

PREDADORES = ("onça", "jacaré", "serpente", "gavião", "piranha")

PERGUNTAS = [
    {"tipo": "matematica", "texto": "Quanto é 7 + 5?", "resposta": "12"},
    {"tipo": "matematica", "texto": "Quanto é 3 x 4?", "resposta": "12"},
    {"tipo": "matematica", "texto": "Quanto é 20 - 8?", "resposta": "12"},
    {"tipo": "matematica", "texto": "Quanto é 15 + 6?", "resposta": "21"},
    {"tipo": "matematica", "texto": "Quanto é 9 x 2?", "resposta": "18"},
    {"tipo": "matematica", "texto": "Quanto é 30 dividido por 5?", "resposta": "6"},
    {"tipo": "matematica", "texto": "Quanto é 11 - 4?", "resposta": "7"},

    {"tipo": "gramatica", "texto": "Qual é o plural de animal?", "resposta": "animais"},
    {"tipo": "gramatica", "texto": "Complete: A capivara ___ pelo rio. (nada/nadam)", "resposta": "nada"},
    {"tipo": "gramatica", "texto": "A palavra 'rio' é substantivo? (sim/não)", "resposta": "sim"},
    {"tipo": "gramatica", "texto": "Qual é o feminino de professor?", "resposta": "professora"},
    {"tipo": "gramatica", "texto": "Qual é o plural de capivara?", "resposta": "capivaras"},
    {"tipo": "gramatica", "texto": "Complete: As crianças ___ felizes. (está/estão)", "resposta": "estão"},
    {"tipo": "gramatica", "texto": "A palavra 'feliz' é uma qualidade? (sim/não)", "resposta": "sim"},

    {"tipo": "animais", "texto": "A capivara é um roedor? (sim/não)", "resposta": "sim"},
    {"tipo": "animais", "texto": "O jacaré vive em ambientes aquáticos? (sim/não)", "resposta": "sim"},
    {"tipo": "animais", "texto": "A onça é um animal herbívoro? (sim/não)", "resposta": "não"},
    {"tipo": "animais", "texto": "A piranha vive na água? (sim/não)", "resposta": "sim"},
    {"tipo": "animais", "texto": "A serpente tem patas? (sim/não)", "resposta": "não"},
    {"tipo": "animais", "texto": "O gavião é uma ave? (sim/não)", "resposta": "sim"},
    {"tipo": "animais", "texto": "A capivara gosta de ambientes com água? (sim/não)", "resposta": "sim"},
]

def limpar(texto):
    return texto.strip().lower()

def mostrar_rio(posicao):
    rio = [["~" for _ in range(7)] for _ in range(3)]
    rio[1][posicao] = "C"

    for linha in rio:
        print(" ".join(linha))

    print()

def contagem(n):
    if n == 0:
        print("Valendo!\n")
    else:
        print(n)
        contagem(n - 1)

def explicar_tipo(tipo):
    match tipo:
        case "matematica":
            return "Desafio de matemática básica!"
        case "gramatica":
            return "Desafio de gramática básica!"
        case "animais":
            return "Curiosidade sobre animais!"
        case _:
            return "Desafio surpresa!"

def perguntar(predador, pergunta, perguntas_usadas):
    perguntas_usadas.add(pergunta["tipo"])

    print(f"A capivara encontrou um(a) {predador}!")
    print(explicar_tipo(pergunta["tipo"]))
    print(pergunta["texto"])

    resposta = limpar(input("Resposta: "))

    while resposta == "":
        resposta = limpar(input("Digite uma resposta válida: "))

    if resposta == pergunta["resposta"]:
        print("Resposta certa! A capivara escapou.\n")
        return True

    print(f"Resposta errada! A resposta correta era: {pergunta['resposta']}.\n")
    return False

def salvar_resultado(nome, pontos, venceu):
    with open("ranking.txt", "a", encoding="utf-8") as arquivo:
        status = "venceu" if venceu else "perdeu"
        arquivo.write(f"{nome} - {pontos} pontos - {status}\n")

def jogar():
    print("=== THE PROFESSOR CAPIVARA ===")
    print("Ajude a capivara a atravessar o rio respondendo aos desafios.\n")

    nome = input("Digite seu nome: ").strip()

    if nome == "":
        nome = "Jogador"

    vidas = 3
    pontos = 0
    posicao = 0
    perguntas_usadas = set()
    perguntas_sorteadas = random.sample(PERGUNTAS, len(PREDADORES))

    contagem(3)

    for i, predador in enumerate(PREDADORES):
        mostrar_rio(posicao)

        if perguntar(predador, perguntas_sorteadas[i], perguntas_usadas):
            pontos += 10
            posicao += 1
        else:
            vidas -= 1

        print(f"Vidas: {vidas} | Pontos: {pontos}\n")

        if vidas == 0:
            break

    venceu = vidas > 0

    if venceu:
        mostrar_rio(6)
        print(f"Parabéns, {nome}! A capivara atravessou o rio!")
    else:
        print(f"Fim de jogo, {nome}. A capivara não conseguiu atravessar.")

    print(f"Tipos de perguntas que apareceram: {perguntas_usadas}")
    salvar_resultado(nome, pontos, venceu)

jogar()