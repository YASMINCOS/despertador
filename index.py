from tkinter.ttk import *
from tkinter import *
from tkinter import Entry, IntVar, Tk
from PIL import ImageTk, Image
from matplotlib  import image
from matplotlib.pyplot import text
from pygame import mixer
import time
from datetime import datetime
from threading import Thread
from time import sleep


cor_0preta="#f0f3f5"
cor_1branca="#feffff"
cor_2ouro="#d6872d"
cor_3vermelha="#fc766d"
cor_4letra="#403d3d"
cor_5azul="#4a88e8"



janela=Tk()
janela.title("")
janela.geometry("350x150")
janela.configure(background=cor_1branca)
janela.resizable(width=False,height=False)

#dividindo a janela
frame_logo=Frame(janela,width=400,height=10,bg=cor_1branca)
frame_logo.grid(row=0,column=0,pady=1,padx=0)


frame_corpo=Frame(janela,width=400,height=290,bg=cor_1branca)
frame_corpo.grid(row=1,column=0,pady=1,padx=0)


#configurando logo

l_linha=Label(frame_logo,width=400,height=1,anchor=NW,font=('Ivy 1'),bg=cor_2ouro)
l_linha.place(x=0,y=0)

#configurando corpo

imagem=Image.open('alarme.png')
imagem=imagem.resize((100,100))
imagem=ImageTk.PhotoImage(imagem)


l_imagem=Label(frame_corpo,height=100,image=imagem,compound=LEFT,padx=10,anchor=NW,font=('Ivy 16 bold'),bg=cor_1branca,fg=cor_0preta)
l_imagem.place(x=10,y=10)

l_nome=Label(frame_corpo,height=1,text='Alarme',anchor=NE,font=('Ivy 10 '),bg=cor_1branca,fg=cor_4letra)
l_nome.place(x=105,y=10)



#criando combo boxs
l_hora=Label(frame_corpo,height=1,text='Horas',anchor=NW,font=('Arial 7'),bg=cor_1branca,fg=cor_4letra)
l_hora.place(x=127,y=40)
c_hora=Combobox(frame_corpo,width=2,font=('Ivy 15 ' ))
c_hora['value']=("00","01","02","03","04","05","06","07","08","09","10","11","12")
c_hora.current(0)
c_hora.place(x=130,y=58)

l_minutos=Label(frame_corpo,height=1,text='Minutos',anchor=NW,font=('Arial 7'),bg=cor_1branca,fg=cor_4letra)
l_minutos.place(x=177,y=40)
c_minutos=Combobox(frame_corpo,width=2,font=('Ivy 15 '))
c_minutos['value']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41",
                    "42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_minutos.current(0)
c_minutos.place(x=180,y=58)

l_segundos=Label(frame_corpo,height=1,text='Segundos',anchor=NW,font=('arial 7 '),bg=cor_1branca,fg=cor_4letra)
l_segundos.place(x=227,y=40)
c_segunods=Combobox(frame_corpo,width=2,font=('Ivy 15'))
c_segunods['value']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41",
                    "42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_segunods.current(0)
c_segunods.place(x=230,y=58)

l_periodo=Label(frame_corpo,height=1,text='Período',anchor=NW,font=('arial 7 '),bg=cor_1branca,fg=cor_4letra)
l_periodo.place(x=277,y=40)
c_periodo=Combobox(frame_corpo,width=3,font=('Ivy 15'))
c_periodo['value']=("AM","PM")
c_periodo.current(0)
c_periodo.place(x=280,y=58)



def ativar_alarme():
    if selecionado.get() ==1:
       print('Ativar:',selecionado.get()) 
    else:
                
      t1=Thread(target=alarme)
      t1.start()
   
   
def desativar_alarme():
    print('Alarme desativado:',selecionado.get()) 
    mixer.music.stop()
   
    
      



selecionado= IntVar()

radio=Radiobutton(frame_corpo,command=ativar_alarme,text='Ativer',variable=selecionado,font=("Arial 8"),bg=cor_1branca,fg=cor_4letra)
radio.place(x=125,y=95)

def tocar_alarme():
       
    mixer.music.load('2.mp3')
    mixer.music.play()
    selecionado.set(0)
    
    radio=Radiobutton(frame_corpo,command=desativar_alarme,text='Destaivar',variable=selecionado,font=("Arial 8"),bg=cor_1branca,fg=cor_4letra)
    radio.place(x=187,y=95)
    
def alarme():
  while True:
    control = selecionado.get()
    h_alarme=c_hora.get()
    m_alarme=c_minutos.get()
    s_alarme=c_segunods.get()
    p_alarme=c_periodo.get().upper()
        
        #obtendo hora atual
        
    hora_atual= datetime.now() 
           
    hora = hora_atual.strftime("%I")   
    minutos = hora_atual.strftime("%M")   
    segundos = hora_atual.strftime("%S") 
    periodo = hora_atual.strftime("%p")
        
    if control ==1:
        if p_alarme==periodo:
            if h_alarme==hora:
                if m_alarme==minutos:
                    if s_alarme== segundos:
                        print("Hora de fazer uma pausa")
                        tocar_alarme()
                        ativar_alarme()
                            
        sleep(1)
        
t1=Thread(target=alarme)
 #iniciar o thread
t1.start()     
mixer.init()       
         

janela.mainloop()