import thread
import time
import sys
import serial
from Tkinter import *

#ser = serial.Serial('COM3',9600)                #povezivanje sa arduinom
screen=''
password = '1234'                                #trazena sifra
i=3
chng = False
def thread_timer():                              #funkcija koja sluzi za odbrojavanje vremena
    global elapsedTime
    elapsedTime = 0
    while elapsedTime < 15:
        time.sleep(0.1)
        elapsedTime = elapsedTime + 0.1
        if chng:
            break
    if not chng:
        alarm(0)                                  #ukoliko se ne potvrdi sifra za 15 sekundi ukljucuje se alarm
 
def input(a):                                     #funkcija kojom definisemo komande za odredjeno dugme.
	global screen
	if not screen.isdigit():                  #kada pritisnemo na neki broj, na ekranu se ispise taj broj
		screen = ''
	screen+= str(a)
	tekst.config(text = screen)
	
def clr():                                        #funkcija kojom definisemo komandu za dugme C. Kada se pritisne na to dugme, izbrise se poslednja cifra.
    global screen
    screen = screen[:-1]
    tekst.config(text = screen)

def enter():                                      #funkcija kojom definisemo komandu za dugme enter
    global password
    global i
    global screen
    global elapsedTime
    global chng
    elapsedTime = 0
    i=i-1
    if screen == password:                        #nakon potvrde sifre pritiskom na dugme enter, proveravamo da li je ta sifra ista kao zadata sifra.
        screen = 'DOBRODOSLI!'
        buttonsOff()
        tekst.config(text = screen)
        #ser.write('1')                            #ako jeste, arduinu saljemo vrednost 1
        window.configure(background="#136c23")
        chng = True
    else:
        screen = 'preostalo pokusaja: '+str(i)
        tekst.config(text = screen)
        if (i==0):
            alarm(1)                                  #ako tri puta pogresimo sifru, ukljucuje se funkcija alarm
        
def alarm(j):
    global chng
    global screen
    chng = True
    if (j==1):                                    
        screen = 'POGRESAN UNOS\nBOLJE BEZI!'
        buttonsOff()
    if (j==0):
        screen = 'VREME JE ISTEKLO\nBOLJE BEZI!'
        buttonsOff()
    tekst.config(text = screen)
    window.configure(background="red")
    #ser.write('0')
def buttonsOff():                                 #funkcija koja onemoguci rad sa bilo kojim dugmetom
	b1 .config(state='disabled')
	b2 .config(state='disabled')
	b3 .config(state='disabled')              
	b4 .config(state='disabled')
	b5 .config(state='disabled')
	b6 .config(state='disabled')
	b7 .config(state='disabled')
	b8 .config(state='disabled')
	b9 .config(state='disabled')
	b10.config(state='disabled')
	b11.config(state='disabled')
	b12.config(state='disabled', bg='#9da4aa')


    
thread.start_new_thread(thread_timer, ());

window = Tk()
window.title("UNOS SIFRE")
window.resizable(width=False, height=False)
window.configure(background="#4986c2")
    #definisemo karakteristike za prozor gde ce se ispisivati sifra
tekst = Label(window,text = screen,height =2, width=16, bg= "white",font = "Helvetica 18 bold", justify="center")
tekst.grid(row=0, column=0, columnspan=3, pady=(11,2))
    #definisemo karakteristike za svako dugme
b1 = Button(window, text = "1",    font = "Helvetica 15 bold", width = 6, height = 3, command= lambda : input(1))
b2 = Button(window, text = "2",    font = "Helvetica 15 bold", width = 6, height = 3, command= lambda : input(2))						
b3 = Button(window, text = "3",    font = "Helvetica 15 bold", width = 6, height = 3, command= lambda : input(3))						
b4 = Button(window, text = "4",    font = "Helvetica 15 bold", width = 6, height = 3, command= lambda : input(4))						
b5 = Button(window, text = "5",    font = "Helvetica 15 bold", width = 6, height = 3, command= lambda : input(5))						
b6 = Button(window, text = "6",    font = "Helvetica 15 bold", width = 6, height = 3, command= lambda : input(6))						
b7 = Button(window, text = "7",    font = "Helvetica 15 bold", width = 6, height = 3, command= lambda : input(7))						
b8 = Button(window, text = "8",    font = "Helvetica 15 bold", width = 6, height = 3, command= lambda : input(8))						
b9 = Button(window, text = "9",    font = "Helvetica 15 bold", width = 6, height = 3, command= lambda : input(9))						
b10= Button(window, text = "C",    font = "Helvetica 15 bold", width = 6, height = 3, command= lambda : clr(), bg= "#9da4aa")			
b11= Button(window, text = "0",    font = "Helvetica 15 bold", width = 6, height = 3, command= lambda : input(0))						
b12= Button(window, text = "ENTER",font = "Helvetica 15 bold", width = 6, height = 3, command= lambda : enter(), bg= "#136c23")		
b1 .grid(row=1, column=0, padx=(10,0), pady=(0,0)) 
b2 .grid(row=1, column=1, padx=(0,0), pady=(0,0)) 
b3 .grid(row=1, column=2, padx=(0,10), pady=(0,0)) 
b4 .grid(row=2, column=0, padx=(10,0), pady=(0,0)) 
b5 .grid(row=2, column=1, padx=(0,0), pady=(0,0)) 
b6 .grid(row=2, column=2, padx=(0,10), pady=(0,0)) 
b7 .grid(row=3, column=0, padx=(10,0), pady=(0,0)) 
b8 .grid(row=3, column=1, padx=(0,0), pady=(0,0)) 
b9 .grid(row=3, column=2, padx=(0,10), pady=(0,0)) 
b10.grid(row=4, column=0, padx=(10,0), pady=(0,15))
b11.grid(row=4, column=1, padx=(0,0), pady=(0,15))
b12.grid(row=4, column=2, padx=(0,10), pady=(0,15))
b1 .config(state='normal')
b2 .config(state='normal')
b3 .config(state='normal')                                                                          
b4 .config(state='normal')
b5 .config(state='normal')
b6 .config(state='normal')
b7 .config(state='normal')
b8 .config(state='normal')
b9 .config(state='normal')
b10.config(state='normal')
b11.config(state='normal')
b12.config(state='normal')

window.mainloop()
