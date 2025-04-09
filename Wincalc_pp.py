import tkinter as tk

# Constantes
TITULO = "WinCalc - A Super Calculadora"
COR_FUNDO = '#2f116e'
COR_TEXTO = 'white'
FONTE_TITULO = ('verdana', 35, 'bold', 'italic')
FONTE_NORMAL = ('calibri', 20)
FONTE_RESULTADO = ('calibri', 28, 'bold', "underline")

def realizar_operacao(operacao):
    try:
        x = float(entryNumero1.get())
        y = float(entryNumero2.get())
        
        if operacao == 'adição':
            resultado = x + y
        elif operacao == 'subtração':
            resultado = x - y
        elif operacao == 'multiplicação':
            resultado = x * y
        elif operacao == 'divisão':
            if y != 0:
                resultado = x / y
            else:
                resultado = "Erro: Divisão por zero!"
                raise ValueError("Divisão por zero!")
        
        lblResultado.config(text=f'A sua {operacao} é {resultado}')
    except ValueError as e:
        lblResultado.config(text=f"Erro: {e}")

# Criação da janela
janela = tk.Tk()
janela.title(TITULO)
janela.geometry('850x600')

# Criação dos componentes
lblTitulo = tk.Label(janela, text="WinCalc", font=FONTE_TITULO, fg=COR_TEXTO, bg=COR_FUNDO, width=800, justify='left')
lblTitulo.pack(padx=5, pady=5)

lblNumero1 = tk.Label(janela, text='Digite um número:', font=FONTE_NORMAL)
lblNumero1.pack(padx=5, pady=5)

entryNumero1 = tk.Entry(janela, width=50, font=('calibri', 17))
entryNumero1.pack(padx=5, pady=5)

lblNumero2 = tk.Label(janela, text='Digite outro número:', font=FONTE_NORMAL)
lblNumero2.pack(padx=5, pady=5)

entryNumero2 = tk.Entry(janela, width=50, font=('calibri', 17))
entryNumero2.pack(padx=5, pady=5)

# Botões
btnAdicao = tk.Button(janela, text='Adição', width=10, bg='white', command=lambda: realizar_operacao('adição'))
btnAdicao.pack(padx=5, pady=5)

btnSubtracao = tk.Button(janela, text='Subtração', width=10, bg='white', command=lambda: realizar_operacao('subtração'))
btnSubtracao.pack(padx=5, pady=5)

btnMultiplicacao = tk.Button(janela, text='Multiplicação', width=10, bg='white', command=lambda: realizar_operacao('multiplicação'))
btnMultiplicacao.pack(padx=5, pady=5)

btnDivisao = tk.Button(janela, text='Divisão', width=10, bg='white', command=lambda: realizar_operacao('divisão'))
btnDivisao.pack(padx=5, pady=5)

# Label para resultado
lblResultado = tk.Label(janela, text='0.00', font=FONTE_RESULTADO, fg=COR_TEXTO, bg=COR_FUNDO)
lblResultado.pack(padx=5, pady=5)

janela.mainloop()
