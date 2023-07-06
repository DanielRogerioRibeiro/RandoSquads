# Este é um programa que gera grupo de pessoas de forma aleatória

# Importando as bibliotecas
from tkinter import *
from tkinter import ttk, filedialog
from tkscrolledframe import ScrolledFrame
import csv
import random

# Definido Cores

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # Grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"  # Letra
co6 = "#003452"  # Azul
co7 = "#ef5350"  # Vermelha

#Criando Janela

janela = Tk()
janela.title("")
janela.geometry('390x500')
janela.configure(background=co6)
janela.resizable(width=FALSE, height=FALSE)

#Criando o Estilo e tema da Janela
style = ttk.Style(janela)
style.theme_use("clam")

#Criando o Frame Principal

frame_principal = Frame(janela, width=390, height=500, bg=co6, relief="flat")
frame_principal.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)


# Função para criar grupos
def gerar():
    global grupos_gerados
    print(Lista_de_nomes)
                       
    def chunks(l, n):
        """Produza grupos sucessivos de tamanho n de l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    random.shuffle(Lista_de_nomes)
    numero = int(e_total.get())
    grupos_gerados = list(chunks(Lista_de_nomes, numero))
    gerar_tabelas()

#Função para gerar tabelas
def gerar_tabelas():
    global grupos_gerados
    
    r = 0
    c = 0
    r_linha = 0
    n = 1
        
    for grupo in grupos_gerados:
        if c == 1:
            r = 0
            
        if c == 2:
            c = 0
            r = 0
            r_linha += 1

        frame = Frame(framecanva, width=190, height=190, relief="solid", bg=co1)
        frame.grid(row=r_linha, column=c, pady=10, padx=10, sticky=NSEW)

        l_grupo = Label(frame, text="Grupo - {}".format(n), width=20, justify=LEFT, anchor=NW, font=('verdana 10'), bg=co6, fg=co1)
        l_grupo.grid(row=r, column=0)

        for i in grupo:
            r += 1
            l_participante = Label(frame, text=i, justify=LEFT, anchor=NW, font=('verdana 8'), bg=co1, fg=co4)
            l_participante.grid(row=r, column=0, sticky=NSEW)
            r += 1
        
        c += 1
        n += 1