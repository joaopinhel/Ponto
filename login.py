import datetime
import getpass
from cProfile import label
from tkinter import *
from tkinter import ttk
from conecte import criar_conexao, fechar_conexao

def login():
    con = criar_conexao("192.168.0.39", "root", "", contabilivre)

    fechar_conexao(con)

largura = 500
altura = 300

#resolução do sistema
menu_inicial = Tk()
menu_inicial.title("HORÁRIO PONTO ESTAGIÁRIO")
menu_inicial.configure(background="white")
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()


#posição janela
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

#definir diametro
menu_inicial.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

def entrar_Click():
    if login == True and senha == True:
        import main
    else:
        print("Sucesso :", end="")

def cadastro_Click():
    import cadastro
    print("Cadastro :", end="")



#label
Label(menu_inicial,text="Usuário:", font='Arial' ,background="white",foreground="black",anchor=W).place(x=10,y=25 ,width=100,height=30)
login = Entry(menu_inicial)

Label(menu_inicial, text="Senha:", font='Arial' , background="white",foreground="black",anchor=W).place(x=10,y=55 ,width=100,height=30)
senha = Entry(menu_inicial, show='*')

#Botão
entrar = Button(menu_inicial, text = "Entrar", font='Arial' , width=8, background="black", bg= "white", fg="black", command=entrar_Click)
cadastro = Button(menu_inicial, text = "Cadastrar", font='Arial' , width=8, background="black", bg= "white", fg="black", command=cadastro_Click)

#place
login.place(x=72, y=30, width=200, height=20)
senha.place(x=72, y=60, width=200, height=20)
#pack
cadastro.place(x=15, y=190)
entrar.place(x=90, y=190)


menu_inicial.mainloop()