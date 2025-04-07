from tkinter import *
from tkinter import ttk
import math
import cores


# Janela principal
janela = Tk()
janela.title('Calculadora Científica')
janela.geometry('235x287')
janela.config(bg=cores.cor1)


# Criando os frames
frame_tela = Frame(janela, width=300, height=56, bg=cores.cor3)
frame_tela.grid(row=0, column=0)            

frame_cientifica = Frame(janela, width=300, height=86)
frame_cientifica.grid(row=1, column=0)      

frame_corpo = Frame(janela, width=300, height=340)
frame_corpo.grid(row=2, column=0)



global todos_valores
todos_valores = ''
texto = StringVar()


# Função para entrar valores na tela
def entrar_valores(valor):
    global todos_valores

    todos_valores = todos_valores + str(valor)
    texto.set(todos_valores)


# Função para calcular o resultado
def calcular():
    global todos_valores

    modulos = ['math.tan', 'math.sin', 'math.cos', 'math.sqrt', 'math.log', 'math.factorial', 'math.e', 'math.pow', 'math.pi']

    for i in modulos:
        if i == 'math.tan':
            todos_valores = todos_valores.replace('tan', i)
    
    for i in modulos:
        if i == 'math.sin':
            todos_valores = todos_valores.replace('sin', i)
    
    for i in modulos:
        if i == 'math.cos':
            todos_valores = todos_valores.replace('cos', i)
    
    for i in modulos:
        if i == 'math.sqrt':
            todos_valores = todos_valores.replace('sqrt', i)
    
    for i in modulos:
        if i == 'math.log':
            todos_valores = todos_valores.replace('log', i)
    
    for i in modulos:
        if i == 'math.factorial':
            todos_valores = todos_valores.replace('factorial', i)
    
    for i in modulos:
        if i == 'math.e':
            todos_valores = todos_valores.replace('e', i)
    
    for i in modulos:
        if i == 'math.pow':
            todos_valores = todos_valores.replace('pow', i)
    
    for i in modulos:
        if i == 'math.pi':
            todos_valores = todos_valores.replace('pi', i)

    resultado = str(eval(todos_valores))
    texto.set(resultado)

    todos_valores = ''


# Função para apagar os valores
def limpar_tela():
    global todos_valores
    todos_valores = ''
    texto.set("")




# Configurando o frame_tela
label_tela = Label(frame_tela, textvariable=texto, width=16, height=2, padx=7, anchor='e', bd=0, justify=RIGHT, font=('Ivy 18'), bg=cores.cor3, fg=cores.cor2)
label_tela.place(x=0, y=0)


class Frontend:
    def __init__(self, frame_cientifica, frame_corpo):
        self.frame_cientifica = frame_cientifica
        self.frame_corpo = frame_corpo

    def cientifica(self):
        # Configurando o frame_científica
        botao_tan = Button(self.frame_cientifica, command=lambda:entrar_valores('tan'), text='tan', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor1, fg=cores.cor2)
        botao_tan.place(x=0, y=0)
        
        botao_sin = Button(self.frame_cientifica, command=lambda:entrar_valores('sin'), text='sin', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor1, fg=cores.cor2)
        botao_sin.place(x=59, y=0)

        botao_cos = Button(self.frame_cientifica, command=lambda:entrar_valores('cos'), text='cos', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor1, fg=cores.cor2)
        botao_cos.place(x=118, y=0)

        botao_sqrt = Button(self.frame_cientifica, command=lambda:entrar_valores('sqrt'), text='sqrt', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor1, fg=cores.cor2)
        botao_sqrt.place(x=177, y=0)


        botao_log = Button(self.frame_cientifica, command=lambda:entrar_valores('log'), text='log', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor1, fg=cores.cor2)
        botao_log.place(x=0, y=29)
        
        botao_fat = Button(self.frame_cientifica, command=lambda:entrar_valores('factorial'), text='fat', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor1, fg=cores.cor2)
        botao_fat.place(x=59, y=29)

        botao_e = Button(self.frame_cientifica, command=lambda:entrar_valores('e'), text='e', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor1, fg=cores.cor2)
        botao_e.place(x=118, y=29)

        botao_pow = Button(self.frame_cientifica, command=lambda:entrar_valores('pow'), text='pow', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor1, fg=cores.cor2)
        botao_pow.place(x=177, y=29)


        botao_pi = Button(self.frame_cientifica, command=lambda:entrar_valores('pi'), text='pi', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor1, fg=cores.cor2)
        botao_pi.place(x=0, y=58)
        
        botao_virgula = Button(self.frame_cientifica, command=lambda:entrar_valores(','), text=',', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor1, fg=cores.cor2)
        botao_virgula.place(x=59, y=58)

        botao_parentesesI = Button(self.frame_cientifica, command=lambda:entrar_valores('('), text='(', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor1, fg=cores.cor2)
        botao_parentesesI.place(x=118, y=58)

        botao_parentesesII = Button(self.frame_cientifica, command=lambda:entrar_valores(')'), text=')', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor1, fg=cores.cor2)
        botao_parentesesII.place(x=177, y=58)

    def corpo(self):
        # Configurando o frame_corpo
        botao_C = Button(self.frame_corpo, command=limpar_tela, text='C', width=14, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor3, fg=cores.cor2)
        botao_C.place(x=0, y=0)
        
        botao_porcentagem = Button(self.frame_corpo, command=lambda:entrar_valores('%'), text='%', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor3, fg=cores.cor2)
        botao_porcentagem.place(x=118, y=0)

        botao_divisao = Button(self.frame_corpo, command=lambda:entrar_valores('/'), text='/', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor3, fg=cores.cor2)
        botao_divisao.place(x=177, y=0)


        botao_7 = Button(self.frame_corpo, command=lambda:entrar_valores('7'), text='7', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor10, fg=cores.cor2)
        botao_7.place(x=0, y=29)
        
        botao_8 = Button(self.frame_corpo, command=lambda:entrar_valores('8'), text='8', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor10, fg=cores.cor2)
        botao_8.place(x=59, y=29)

        botao_9 = Button(self.frame_corpo, command=lambda:entrar_valores('9'), text='9', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor10, fg=cores.cor2)
        botao_9.place(x=118, y=29)

        botao_multiplica = Button(self.frame_corpo, command=lambda:entrar_valores('*'), text='*', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor3, fg=cores.cor2)
        botao_multiplica.place(x=177, y=29)


        botao_4 = Button(self.frame_corpo, command=lambda:entrar_valores('4'), text='4', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor10, fg=cores.cor2)
        botao_4.place(x=0, y=58)
        
        botao_5 = Button(self.frame_corpo, command=lambda:entrar_valores('5'), text='5', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor10, fg=cores.cor2)
        botao_5.place(x=59, y=58)

        botao_6 = Button(self.frame_corpo, command=lambda:entrar_valores('6'), text='6', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor10, fg=cores.cor2)
        botao_6.place(x=118, y=58)

        botao_menos = Button(self.frame_corpo, command=lambda:entrar_valores('-'), text='-', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor3, fg=cores.cor2)
        botao_menos.place(x=177, y=58)


        botao_1 = Button(self.frame_corpo, command=lambda:entrar_valores('1'), text='1', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor10, fg=cores.cor2)
        botao_1.place(x=0, y=87)
        
        botao_2 = Button(self.frame_corpo, command=lambda:entrar_valores('2'), text='2', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor10, fg=cores.cor2)
        botao_2.place(x=59, y=87)

        botao_3 = Button(self.frame_corpo, command=lambda:entrar_valores('3'), text='3', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor10, fg=cores.cor2)
        botao_3.place(x=118, y=87)

        botao_mais = Button(self.frame_corpo, command=lambda:entrar_valores('+'), text='+', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor3, fg=cores.cor2)
        botao_mais.place(x=177, y=87)


        botao_0 = Button(self.frame_corpo, command=lambda:entrar_valores('0'), text='0', width=14, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor10, fg=cores.cor2)
        botao_0.place(x=0, y=116)
        
        botao_ponto = Button(self.frame_corpo, command=lambda:entrar_valores('.'), text='.', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor10, fg=cores.cor2)
        botao_ponto.place(x=118, y=116)

        botao_igualdade = Button(self.frame_corpo, command=calcular, text='=', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cores.cor3, fg=cores.cor2)
        botao_igualdade.place(x=177, y=116)

frontend = Frontend(frame_cientifica, frame_corpo)
frontend.cientifica()
frontend.corpo()



janela.mainloop()                           