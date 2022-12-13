# vamos importar o módulo Tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


# método que permite autenticar o usuário
def autenticar_usuario():
    # vamos obter o valor da caixa de texto usuário
    usuario = txt_usuario.get()
    # vamos obter o valor da caixa de texto senha
    senha = txt_senha.get()
    # vamos testar se o nome de usuário e a senha estão corretos
    if (usuario == "admin" and senha == "1234"):
        messagebox.showinfo("Aviso", "Usuário e senha corretos")
    else:
        messagebox.showinfo("Aviso", "Usuário e senha não conferem")


# método principal
def main():
    global janela_login
    global txt_usuario
    global txt_senha

    # vamos criar a tela de login
    janela_login = Tk()

    # vamos definir o tamanho da janela
    janela_login.geometry("260x120")

    # o titulo da janela
    janela_login.title("Login do Usuário")