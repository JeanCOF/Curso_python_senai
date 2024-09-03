import tkinter as tk
from tkinter import messagebox

# Função para mostrar a mensagem
def mostrar_mensagem():
    messagebox.showinfo("Alerta", "Esta é uma caixa de texto de alerta!")

# Configuração da janela principal
root = tk.Tk()
root.title("Exemplo de Caixa de Texto")

# Criação de um botão que chama a função
botao = tk.Button(root, text="Mostrar Alerta", command=mostrar_mensagem)
botao.pack(pady=20)

# Iniciar o loop principal da interface
root.mainloop()