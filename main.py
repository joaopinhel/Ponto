#from datetime import date
import datetime
from cProfile import label
from tkinter import *
from tkinter import ttk

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

current_time = datetime.datetime.now()

agora = datetime.datetime.now()
hora = agora.strftime("%H:%M")
#today = date.today()
#print("Today date is: ", today)

data= datetime.date.today()
dataf = data.strftime("%d/%m/%Y")
def chegada_Click():
    print("Chegada :", end="")
    print(dataf,hora)

def almoco_Click():
    print("Almoço :", end="")
    print(dataf,hora)

def volta_Click():
    print("Volta :", end="")
    print(dataf,hora)

def fim_expediente_Click():
    print("Fim de Expediente :", end="")
    print(dataf,hora)

#botão
chegada = Button(menu_inicial, text = "Chegada", font='Arial', height = 3, width=20, bg= "white", fg="black", command=chegada_Click)
almoco = Button(menu_inicial, text = "Almoço", font='Arial' , height = 3, width=20, bg= "white", fg="black", command=almoco_Click)
volta = Button(menu_inicial, text = "Volta", font='Arial' , height = 3, width=20, bg= "white", fg="black", command=volta_Click)
fim_expediente = Button(menu_inicial, text = "Fim de Expediente", font='Arial', height = 3, width=20, bg= "white", fg="black", command=fim_expediente_Click)


#pack

chegada.pack()
almoco.pack()
volta.pack()
fim_expediente.pack()


menu_inicial.mainloop()