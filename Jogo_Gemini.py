import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo de Adivinhação de Palavras")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Fonte
fonte = pygame.font.Font(None, 36)

# Lista de palavras e dicas
palavras = {
    "python": "Uma linguagem de programação",
    "gato": "Um animal de estimação",
    "sol": "Uma estrela no centro do nosso sistema solar",
    "livro": "Uma coleção de páginas com palavras",
    "computador": "Uma máquina que processa dados",
}

def escolher_palavra():
    """Escolhe uma palavra aleatória do dicionário."""
    palavra, dica = random.choice(list(palavras.items()))
    return palavra, dica

def desenhar_texto(texto, cor, x, y):
    """Desenha texto na tela."""
    texto_renderizado = fonte.render(texto, True, cor)
    tela.blit(texto_renderizado, (x, y))

def jogo(rodada, total_rodadas):
    """Função principal do jogo com barra de progresso."""
    palavra, dica = escolher_palavra()
    tentativas = 3
    adivinhou = False
    entrada = ""

    while tentativas > 0 and not adivinhou:
        tela.fill(branco)

        # Barra de progresso
        progresso = (rodada / total_rodadas) * 100
        pygame.draw.rect(tela, preto, (50, 550, 700, 20), 2)
        pygame.draw.rect(tela, verde, (52, 552, (progresso / 100) * 696, 16))
        desenhar_texto(f"Progresso: {progresso:.2f}%", preto, 50, 520)

        # Dica com número de letras
        desenhar_texto(f"Dica: {dica} ({len(palavra)} letras)", preto, 50, 50)
        desenhar_texto(f"Tentativas restantes: {tentativas}", preto, 50, 100)
        desenhar_texto("Digite sua adivinhação:", preto, 50, 200)
        desenhar_texto(entrada, preto, 50, 250)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return 0
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if entrada.lower() == palavra:
                        adivinhou = True
                        desenhar_texto("Parabéns! Você adivinhou a palavra!", verde, 50, 300)
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        return 1
                    else:
                        tentativas -= 1
                        desenhar_texto("Adivinhação incorreta.", vermelho, 50, 300)
                        pygame.display.flip()
                        pygame.time.wait(2000)
                    break
                elif evento.key == pygame.K_BACKSPACE:
                    entrada = entrada[:-1]
                else:
                    entrada += evento.unicode

    tela.fill(branco)
    desenhar_texto(f"Você perdeu! A palavra era: {palavra}", vermelho, 50, 350)
    pygame.display.flip()
    pygame.time.wait(2000)
    return -0.33

def jogar_novamente():
    """Pergunta se o jogador quer jogar novamente."""
    desenhar_texto("Jogar novamente? (S/N)", preto, 50, 400)
    pygame.display.flip()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_s:
                    return True
                elif evento.key == pygame.K_n:
                    pygame.quit()
                    return False

def main():
    """Função principal para controlar o fluxo do jogo."""
    pontuacao = 0
    rodada_atual = 1
    total_rodadas = 3

    while True:
        pontuacao += jogo(rodada_atual, total_rodadas)
        if not jogar_novamente():
            break
        tela.fill(branco)
        desenhar_texto(f"Pontuação: {pontuacao:.2f}", preto, 50, 450)
        pygame.display.flip()
        pygame.time.wait(2000)
        rodada_atual += 1

main()