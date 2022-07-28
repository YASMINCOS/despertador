from ast import While
from this import d
from pygame import mixer
import time
from datetime import datetime
from tkinter import *
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

def tocar_alarme():
   
    mixer.music.load('1.mp3')
    mixer.music.play()
 
 



    
def alarme():
    
  while True:
        
        control=1
        h_alarme="10"
        m_alarme="01"
        s_alarme="00"
        p_alarme="PM".upper()
        
        print(p_alarme)
        
        
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
                            
        sleep(1)
  
        
t1=Thread(target=alarme)

t1.start()     
mixer.init()       
        
        
        
        
        

janela.mainloop()