import random
import datetime
import webbrowser
import time
import vlc
from tkinter import *
scoreboard=0
a=datetime.datetime(1,1,1,1,1).today()
licznik=0
print("oblicz")
while licznik < 5:  #dodawanie
    C = random.randint(0,15)
    B = random.randint(0,15)
    G = (input(str(C)+"-"+str(B)+"=" ))
    F = C-B
    if int(G)==F:
        scoreboard += 0
    elif F is not int(G): 
        scoreboard += 1
    licznik +=1
licznik=0
print("rozpoznaj obrazek")
while licznik < 2:
    obraz = random.randint(1,6) # obrazki
    if obraz == 1:
        webbrowser.open('obraz1.html')
        nazwaobraz=input("co widzisz na obrazku ")
        if nazwaobraz == "wilwe" or nazwaobraz =="owca":
            scoreboard += 0
        else:
            scoreboard += 2
    elif obraz==2:
        webbrowser.open('obraz2.html')
        nazwaobraz=input("co widzisz na obrazku ")
        if nazwaobraz == "sigma" or nazwaobraz == "rizler":
            scoreboard += 0
        else:
            scoreboard += 2
    elif obraz==3:
        webbrowser.open('obraz3.html')
        nazwaobraz=input("co widzisz na obrazku ")
        if nazwaobraz == "skibidi" or nazwaobraz == "skibiditoilet" or nazwaobraz == "skibiditoaleta" :
            scoreboard += 0
        else:
            scoreboard += 2
    elif obraz==4:
        webbrowser.open('obraz4.html')
        nazwaobraz=input("co widzisz na obrazku ")
        if nazwaobraz == "JD" or nazwaobraz == "jD" or nazwaobraz =="jd" or nazwaobraz =="Jd" or nazwaobraz == "ork" or nazwaobraz =="diss" or nazwaobraz =="disstream" or nazwaobraz == "Disstream":
            scoreboard += 0
        else:
            scoreboard += 2
    elif obraz==5:
        webbrowser.open('obraz5.html')
        nazwaobraz=input("co widzisz na obrazku ")
        if nazwaobraz == "krecik" or nazwaobraz == "kret" or nazwaobraz == "Bartek" or nazwaobraz == "menel":
            scoreboard += 0
        else:
            scoreboard += 2
    elif obraz==6:
        webbrowser.open('obraz6.html')
        nazwaobraz=input("co widzisz na obrazku ")
        if nazwaobraz == "papaj"  or nazwaobraz == "papierz" or nazwaobraz == "zolty czlowiek" or nazwaobraz == "papiesz":
            scoreboard += 0
        else:
            scoreboard += 2
    licznik +=1
licznik = 0
print("papier kamień nożyce")
while licznik < 3:
    gra =["papier","kamień","nożyce"] #papier kamien nozyce
    pickai=random.choice(gra)
    pickgra=input("wybierz miedzy papier,kamień,nożyce ")
    print("ai wybralo " + pickai)
    if pickgra == "kamień" and pickai == "kamień": #kamień
        print("moze nie przejebales ale czas tracisz")
        time.sleep(2)
    elif pickgra == "kamień" and pickai == "papier":
        print("ha ha ale z cb bambik przejebales")
        scoreboard += 1
    elif pickgra == "kamień" and pickai == "nożyce":
        print("wygrałeś")
    elif pickgra == "papier" and pickai == "kamień": #papier
        print("wygrałeś")
    elif pickgra == "papier" and pickai == "papier":
        print("moze nie przejebales ale czas tracisz")
        time.sleep(2)
    elif pickgra == "papier" and pickai == "nożyce":
        print("ha ha ale z cb bambik przejebales")
        scoreboard += 1
    elif pickgra == "nożyce" and pickai == "papier": #nożyce
        print("wygrałeś")
    elif pickgra == "nożyce" and pickai == "kamień":
        print("ha ha ale z cb bambik przejebales")
        scoreboard += 1            
    elif pickgra == "nożyce" and pickai == "nożyce":
        print("moze nie przejebales ale czas tracisz")
        time.sleep(2)
    else:
        print("no dla takiego debila to dam +3 do sc")
        scoreboard += 3
    licznik +=1
licznik = 0

while licznik < 2:
    song = random.randint(1,6)
    if song == 1:
        song1=vlc.MediaPlayer("song1.mp3")
        song1.play()
        piosenka=input("co to za piosenka ") 
        song1.pause()
        song1.stop()
        if piosenka == "Bajo Jajo" or piosenka =="Żaluzja Solonez x LIMBØ - Bajo Jajo" or piosenka == "bajo jajo" or piosenka =="bajojajo":
            print("dobrze")
        else:
            print("zle")
            scoreboard += 1
    elif song == 2:
        song1=vlc.MediaPlayer("song2.mp3")
        song1.play()
        piosenka=input("co to za piosenka ") 
        song1.pause()
        song1.stop()
        if piosenka == "Genziara" or piosenka == "genziara" or piosenka =="GENZIE - GENZIARA" or piosenka =="GENZIARA":
            print("dobrze wie ze masz ujemne IQ")
            scoreboard += 3
        else:
            print("ooo widze ze masz muzg")
    elif song == 3:
        song1=vlc.MediaPlayer("song3.mp3")
        song1.play()
        piosenka=input("co to za piosenka ") 
        song1.pause()
        song1.stop()
        if piosenka == "Lato w Auschwitz" or piosenka == "Kuki Lato w Auschwitz" or piosenka == "lato w auschwitz" :
            print("dobrze")
        else:
            print("zle")
            scoreboard += 1
    elif song == 4:
        song1=vlc.MediaPlayer("song4.mp3")
        song1.play()
        piosenka=input("co to za piosenka ") 
        song1.pause()
        song1.stop()
        if piosenka == "Malcolm x Pattros - All Champ - League of Legends Song" or piosenka == "All Champ League of Legends Song" or piosenka == "all champ league of legends song" or piosenka == "all champ league of legends" or piosenka == "All Champ League of Legends" or piosenka == "all champ lol" or piosenka == "all champ lol song":
            print("dobrze wiedziec ze nie masz zycia")
        else:
            print("zle ,ale przynajmniej masz zycie")
            scoreboard += 1
    elif song == 5:
        song1=vlc.MediaPlayer("song5.mp3")
        song1.play()
        piosenka=input("co to za piosenka ") 
        song1.pause()
        song1.stop()
        if piosenka == "BUDDA- Samochodowe Stereotypy (prod. CrackHouse)" or piosenka =="BUDDA- Samochodowe Stereotypy" or piosenka =="Samochodowe Stereotypy" or piosenka =="samochodowe stereotypy":
            print("dobrze")
        else:
            print("zle")
    elif song == 6:
        song1=vlc.MediaPlayer("song6.mp3")
        song1.play()
        piosenka=input("co to za piosenka ") 
        song1.pause()
        song1.stop()
        if piosenka == "Kuki- Córka mi zm@rła" or piosenka =="Córka mi zm@rła" or piosenka =="córka mi zm@rła" or piosenka =="Córka mi zmarła" or piosenka =="córka mi zmarła":
            print("dobrze")
        else:
            print("zle")
            scoreboard += 1
    song1 = 0
    licznik +=1
licznik =0
tk = Tk()
tk.title("Apple")
w = Label(tk, text='Darmowy iphone 6 scx 500 y + 200IQ!')
w.pack()
def przycisktak():
    tk.destroy()
    global scoreboard
    global sigma
    sigma = scoreboard + 3
def przycisknie():
    tk.destroy()
    global scoreboard
    global sigma
    sigma = scoreboard
button = Button(tk, text='odbieram', width=25, command=przycisktak)
button.pack()
button2 = Button(tk, text='zamykam', width=25, command=przycisknie)
button2.pack()
tk.mainloop()


b=datetime.datetime(1,1,1,1,1).today()
c=b-a
c=c.total_seconds()
sigma = sigma *9
wynik = 337 - (c*4)-sigma
print(str(round(wynik,2)) +"IQ")
