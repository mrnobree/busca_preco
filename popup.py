import tkinter as tk
from tkinter import messagebox

def mostrar_pop_up():
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal do Tkinter
    messagebox.showinfo("Aviso", "O programa irá executar clique em OK para continuar. Por favor, não mexa no computador.")
    root.destroy()

def main():
    mostrar_pop_up()