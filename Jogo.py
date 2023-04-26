

import tkinter

from tkinter import

from tkinter import ttk

#cores

cor0="#FFFFFF" # branca / white

cor="#333333" # preta pesado / dark black cor2="#fcc058" #laranja / orange

cor3="#38576b" #valor / value

cor4="#3297a8" # azul / blue

cor5="#fff873" #amarela /

cor6="#fcc058" # laranja / orange

cor7="#e85151" # vermelha / red

cor8= cor4 #+verde

cor9="#fcfbf7"

fundo = "#3b3b3b" #preta / black

#criando janela principal-

janela = TKO

janela.title('Jogo da Velha) janela.geometry(260x370)

janela.configure(background=fundo)

#dividindo a janela em 2 frames

frame_cima Frame(janela, width-240, height=100, background-cor], relief="raised") frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, background=fundo, relief="flat") frame_baixo.grid(row=1, column=0, sticky=NW)

#configurando o frame_cima -

jog_x = Label(frame_cima, text='X, height=1, relief='flat, anchor='center', font=(Ivy 40 bold'), background=cor1,

fg=cor7)

jog_x.place(x=25, y=10)

jog x = Label(frame_cima, text="Jogador 1, height=1, relief='flat, anchor='center', font (Ivy 7 bold), background=cor1,

fg=cor0)

jog_x.place(x=17, y=70)

jog_x_pts= Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), background=cor1,

fg=cor0)

jog_x_pts.place(x=80, y=20)

obj_sep = Label(frame_cima, text=":, height=1, relief= 'flat, anchor='center, font=("Ivy 30 bold), background=cor1,

fg=cor0)

obj_sep.place(x=110, y=20)

jog_o= Label(frame_cima, text='0', height=1, relief="flat", anchor='center', font=('Ivy 40 bold'), background=cor1

fg=cor4)

jog_o= Label(frame_cima, text="Jogador 2', height=1, relief='flat, anchor='center', font=("Ivy 7 bold), background-cor1,

jog_o.place(x=170, y=10)

fg=cor0) jog_o.place(x=165, y=70)

jog_o_pts= Label(frame_cima, text='0', height=1, relief='flat, anchor='center', font=("lvy 30 bold'), background-cor1

fg=cor0)

jog_o_pts.place(x=130, y=20)

#criando logica do jogo

global pontos2

tabela = [[1, 2, 3], [4, 5, 6], [7, 8, 9']]

contador_rodada = 0 pontos1 = 0 b2['state']="disable' b5['state']='disable b8['state']='disable jog fim Label(frame_baixo, text="Fim de jogo', width= 17, relief='flat, anchor='center', font=('Ivy 13 bold'), background cor1, fg= cor2) jog_vancedor.place(x=25, y=90) #linhas horizontais linha = Label(frame_baixo, text=", width=46, relief-flat, padx=2, pady=1, anchor='center', font=("Ivy 5 bold'),

pontos2 = 0 contador = 0

bo['state']='disable

b1['state']='disable

b3['state']='disable b4['state']='disable

b6['state']='disable b7['state']='disable

def play again():

jog x_pts[text] '0'

jog_o_pts['text']='0'

jog fim.destroy b_jogar destroy

iniciar jogo()

b_jogar = Button(frame_baixo, command-play again, text='Jogar de novo, height=1, font-(Ivy 10 bold'), overrelief-RIDGE, relief='raised, background=fundo, fg= coro) b_jogar place(x=80,y=197)

#configurando o frame baixo

#linhas verticais

linha = Label(frame_baixo, text=", height=23, relief='flat, pady=5, anchor='center', font=('Ivy 5 bold'), background-cor0)

linha.place(x=90, y=15)

linha = Label(frame_baixo, text=", height=23, relief='flat, pady-5, anchor='center', font=(Ivy 5 bold').

background-cor0)

linha.place(x=157, y=15)

background-coro) linha.place(x=30, y=63)

linha Label(frame_baixo, text=", width=46, relief-flat', padx=2, pady=1, anchor='center', font=(lvy 5 bold'),

background=cor0) linha.place(x=30, y=127)

#linha0

b0=Button(frame_baixo, command-lambda: controlar('1'), text=", width=3, height=1, font=(Ivy 20 bold'). overrelief=RIDGE, relief='flat, background=fundo)

b0.place(x=30, y=15)

b1 = Button(frame_baixo, command-lambda: controlar(2), text=", width=3, height=1, font=("Ivy 20 bold), overrelief RIDGE, relief='flat, background=fundo) b1.place(x=96, y=15)

b2 = Button(frame_baixo, command-lambda: controlar(3), text=", width=3, height=1, font=(lvy 20 bold"), overrelief RIDGE, relief='flat, background=fundo) b2 place(x=163, y=15)

#linha1

b3 = Button(frame_baixo, command-lambda: controlar(4), text=", width=3, height=1, font=(Ivy 20 bold'). overrelief=RIDGE, relief='flat, background=fundo)

b3.place(x=30, y=75)

b4 = Button(frame_baixo, command-lambda: controlar(5), text=", width=3, height=1, font=(Ivy 20 bold'). overrelief-RIDGE, relief='flat, background-fundo) b4.place(x=96, y=75)

b5 = Button(frame_baixo, command-lambda: controlar('6"), text=", width=3, height=1, font=(Ivy 20 bold"). overrelief=RIDGE, relief='flat, background=fundo) b5.place(x=163, y=75)

#linha2

b6 = Button(frame_baixo, command-lambda: controlar(7), text=", width=3, height=1, font=(Ivy 20 bold'),

overrelief-RIDGE, relief='flat, background=fundo) b6 place(x=30, y=135) b7 = Button(frame_baixo, command-lambda: controlar (8), text=", width=3, height=1, font=(Ivy 20 bold'),

overrelief-RIDGE, relief='flat, background=fundo)

b7.place(x=96, y=135)

b8 = Button(frame_baixo, command-lambda: controlar('9'), text=", width=3, height=1, font=(Ivy 20 bold'). overrelief-RIDGE, relief='flat, background=fundo) b8.place(x=163, y=135)

#botao jogar -

b_jogar = Button(frame_baixo, command= iniciar jogo, text="Jogar', width=10, height=1, font=(Ivy 10 bold), overrelief=RIDGE, relief-'raised, background-fundo, fg= coro) b_jogar.place(x=85, y=197)

janela.mainloop()
