import tkinter as tk
from tkinter import messagebox

class WinCalc:
    def __init__(self, master):
        self.master = master
        master.title("WinCalc - A Super Calculadora")
        master.geometry('850x600')
        master.configure(bg='#f0f0f0')
        
        self.setup_ui()
    
    def setup_ui(self):
        # Cabeçalho
        lbl_titulo = tk.Label(
            self.master,
            text="WinCalc",
            font=('Verdana', 35, 'bold italic'),
            fg='white',
            bg='#2f116e',
            width=800
        )
        lbl_titulo.pack(padx=5, pady=5)
        
        # Campos de entrada
        self.create_input_field("Digite um número:", 0)
        self.create_input_field("Digite outro número:", 1)
        
        # Botões de operação
        operations = [
            ('Adição', '+'),
            ('Subtração', '-'),
            ('Multiplicação', '×'),
            ('Divisão', '÷')
        ]
        
        btn_frame = tk.Frame(self.master, bg='#f0f0f0')
        btn_frame.pack(pady=10)
        
        for text, symbol in operations:
            btn = tk.Button(
                btn_frame,
                text=text,
                width=12,
                bg='white',
                command=lambda s=symbol: self.calculate(s)
            )
            btn.pack(side=tk.LEFT, padx=5)
        
        # Resultado
        self.lbl_resultado = tk.Label(
            self.master,
            text='0.00',
            font=('Calibri', 28, 'bold underline'),
            fg='white',
            bg='#2f116e'
        )
        self.lbl_resultado.pack(pady=20)
    
    def create_input_field(self, label_text, index):
        frame = tk.Frame(self.master, bg='#f0f0f0')
        frame.pack(pady=5)
        
        lbl = tk.Label(
            frame,
            text=label_text,
            font=('Calibri', 14),
            bg='#f0f0f0'
        )
        lbl.pack(side=tk.LEFT)
        
        entry = tk.Entry(
            frame,
            width=20,
            font=('Calibri', 14)
        )
        entry.pack(side=tk.LEFT, padx=5)
        
        if index == 0:
            self.entry_numero1 = entry
        else:
            self.entry_numero2 = entry
    
    def calculate(self, operation):
        try:
            x = float(self.entry_numero1.get())
            y = float(self.entry_numero2.get())
            
            if operation == '+':
                result = x + y
            elif operation == '-':
                result = x - y
            elif operation == '×':
                result = x * y
            elif operation == '÷':
                if y == 0:
                    raise ZeroDivisionError("Divisão por zero!")
                result = x / y
            
            self.lbl_resultado.config(text=f'Resultado: {result:.2f}')
        
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos!")
        except ZeroDivisionError:
            messagebox.showerror("Erro", "Não é possível dividir por zero!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WinCalc(root)
    root.mainloop()