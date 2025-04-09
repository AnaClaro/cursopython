import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pedra, Papel e Tesoura")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
cinza = (128, 128, 128)

# Fonte
fonte = pygame.font.Font(None, 36)

# Opções
opcoes = ["pedra", "papel", "tesoura"]

# Botões
botao_pedra = pygame.Rect(50, 200, 150, 50)
botao_papel = pygame.Rect(325, 200, 150, 50)
botao_tesoura = pygame.Rect(600, 200, 150, 50)

def desenhar_texto(texto, cor, x, y):
    """Desenha texto na tela."""
    texto_renderizado = fonte.render(texto, True, cor)
    tela.blit(texto_renderizado, (x, y))

def desenhar_botao(retangulo, cor_fundo, texto, cor_texto):
    """Desenha um botão na tela."""
    pygame.draw.rect(tela, cor_fundo, retangulo)
    texto_renderizado = fonte.render(texto, True, cor_texto)
    texto_retangulo = texto_renderizado.get_rect(center=retangulo.center)
    tela.blit(texto_renderizado, texto_retangulo)

def jogo():
    """Função principal do jogo."""
    pontuacao_jogador = 0
    pontuacao_computador = 0

    for rodada in range(3):
        tela.fill(branco)
        desenhar_texto(f"Rodada {rodada + 1} de 3", preto, 50, 50)
        desenhar_texto("Escolha:", preto, 50, 100)

        # Desenha os botões
        desenhar_botao(botao_pedra, cinza, "Pedra", azul)
        desenhar_botao(botao_papel, branco, "Papel", azul)
        desenhar_botao(botao_tesoura, vermelho, "Tesoura", azul)

        pygame.display.flip()

        # Captura a escolha do jogador
        escolha_jogador = None
        while escolha_jogador is None:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if botao_pedra.collidepoint(evento.pos):
                        escolha_jogador = "pedra"
                    elif botao_papel.collidepoint(evento.pos):
                        escolha_jogador = "papel"
                    elif botao_tesoura.collidepoint(evento.pos):
                        escolha_jogador = "tesoura"

        # Escolha do computador
        escolha_computador = random.choice(opcoes)

        # Determina o vencedor da rodada
        if escolha_jogador == escolha_computador:
            resultado = "Empate!"
        elif (escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
             (escolha_jogador == "papel" and escolha_computador == "pedra") or \
             (escolha_jogador == "tesoura" and escolha_computador == "papel"):
            resultado = "Você venceu!"
            pontuacao_jogador += 1
        else:
            resultado = "Você perdeu!"
            pontuacao_computador += 1

        # Exibe o resultado da rodada
        tela.fill(branco)
        desenhar_texto(f"Sua escolha: {escolha_jogador}", preto, 50, 50)
        desenhar_texto(f"Escolha do computador: {escolha_computador}", preto, 50, 100)
        desenhar_texto(resultado, preto, 50, 150)
        pygame.display.flip()
        pygame.time.wait(2000)

    # Determina o vencedor do jogo
    tela.fill(branco)
    if pontuacao_jogador > pontuacao_computador:
        desenhar_texto("Você venceu o jogo!", verde, 50, 200)
    elif pontuacao_jogador < pontuacao_computador:
        desenhar_texto("Você perdeu o jogo!", vermelho, 50, 200)
    else:
        desenhar_texto("O jogo terminou em empate!", preto, 50, 200)

    pygame.display.flip()
    pygame.time.wait(3000)

jogo()