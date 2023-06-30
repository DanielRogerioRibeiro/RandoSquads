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