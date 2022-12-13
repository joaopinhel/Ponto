from tkinter import *

from conecte import criar_conexao, fechar_conexao

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


def insere_estagiario(con, nome, senha, setor):
    cursor = con.cursor()
    sql = "INSERT INTO estagiario (nome, senha, setor) values (%s, %s, %s)"
    valores = (nome, senha, setor)
    cursor.execute(sql, valores)
    cursor.close()
    con .commit()

def cadastro():
    con = criar_conexao("127.0.0.1", "root", "", "contabilivre")

    insere_estagiario(con, usuario_login, senha_login, setor_trabalha)

    fechar_conexao(con)

def finalizar_cadastro_Click():

    print("Cadastro concluido", end="")


#label
Label(menu_inicial,text="Usuário:", font='Arial' ,background="white",foreground="black",anchor=W).place(x=10,y=25 ,width=100,height=30)
usuario_login = Entry(menu_inicial)

Label(menu_inicial, text="Senha:", font='Arial',  background="white",foreground="black",anchor=W).place(x=10,y=55 ,width=100,height=30)
senha_login = Entry(menu_inicial, show='*')

#Label(menu_inicial, text="Confirme:", font='Arial' , background="white",foreground="black",anchor=W).place(x=10,y=85 ,width=100,height=30)
#senha_confirmacao = Entry(menu_inicial, show='*')

Label(menu_inicial, text="Setor:", font='Arial' , background="white",foreground="black",anchor=W).place(x=10,y=120 ,width=50,height=30)
setor_trabalha = Entry(menu_inicial)

finalizar_cadastro = Button(menu_inicial, text = "Finalizar Cadastro", font='Arial' , width=15, background="black", bg= "white", fg="black", command=finalizar_cadastro_Click)


#place
usuario_login.place(x=115, y=30, width=200, height=20)
senha_login.place(x=115, y=60, width=200, height=20)
#senha_confirmacao.place(x=115, y=85, width=200, height=20)
setor_trabalha.place(x=115, y=120, width=200, height=20)



#pack
finalizar_cadastro.place(x=15, y=190)


menu_inicial.mainloop()
