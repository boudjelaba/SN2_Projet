# SN2_Projet

---

### Code Arduino

```cpp
void setup() {
  Serial.begin(9600);
  Serial.println("Initialisation");
  
  analogReference(DEFAULT);
  pinMode(7, OUTPUT);
}
 
void loop() {
  float tensionVide;
  float tensionCharge;
 
  digitalWrite(7, LOW);
  delay(500);
  tensionVide = analogRead(A0)*5.0/1023;
 
  digitalWrite(7, HIGH);
  delay(500);
  tensionCharge = analogRead(A0)*5.0/1023;
 
  Serial.print("Tension à vide = ");
  Serial.print(tensionVide);
  Serial.println("V");
  Serial.print("Tension en charge = ");
  Serial.print(tensionCharge);
  Serial.println("V");
  if (tensionCharge > 1.2) {
    Serial.println("Batterie bonne");
  } else if (tensionCharge > 1.0) {
    Serial.println("Batterie faible");
  } else {
    Serial.println("Batterie à remplacer");
  }
}
```

## Four

https://fr.mathworks.com/help/physmod/simscape/ug/linearize-an-electronic-circuit.html


## ECG

https://maker.pro/raspberry-pi/tutorial/how-to-use-a-gps-receiver-with-raspberry-pi-4

https://tutorials-raspberrypi.com/build-raspberry-pi-gps-location-navigation-device/

https://www.instructables.com/Interfacing-GPS-Module-With-Raspberry-Pi/

---

## Email

https://maker.pro/raspberry-pi/projects/how-to-use-the-raspberry-pi4-camera-and-pir-sensor-to-send-emails

---

## GPS

https://www.electronicwings.com/raspberry-pi/gps-module-interfacing-with-raspberry-pi

---


## Interfaces graphiques :

### Exemple 1 :

```python
from tkinter import *
from tkinter import ttk

# déclarer l'objet Tk() qui deviendra la fenêtre principale
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
# on crée un objet Label() rattaché à fenetre pour afficher du texte non éditable
# on définit un texte "Hello World"
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# on crée ensuite un objet Button()
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
```

### Exemple 2 :

```python
from tkinter import *

def repondre():
    affichage['text'] = reponse.get()	# lecture du contenu du widget "reponse"

Fenetre = Tk()
Fenetre.title('Mon nom')

nom = Label(Fenetre, text = 'Votre nom :')
reponse = Entry(Fenetre)
valeur = Button(Fenetre, text =' Valider', command=repondre)
affichage = Label(Fenetre, width=30)
votre_nom=Label(Fenetre, text='Votre nom est :')
nom.pack()
reponse.pack()
valeur.pack()
votre_nom.pack()
affichage.pack()

Fenetre.mainloop()
```


### Exemple 3 :

```python
from tkinter import *

racine= Tk()

zone_dessin = Canvas(racine, width=500, height=500) #Les dimensions du canevas
zone_dessin.pack() #Affiche le canevas
zone_dessin.create_line(0,0,500,500) #Dessine une ligne en diagonale
zone_dessin.create_rectangle(100,100,200,200) #Dessine un rectangle

bouton_sortir = Button(racine,text="Sortir",command=racine.destroy)
bouton_sortir.pack()

racine.mainloop()
```


### Exemple 4 :

```python
from tkinter import *

Fenetre=Tk()  #La fonction Tk() du module Tkinter permet de créer une fenêtre qui se nomme Fenetre
Fenetre.title("Mon programme avec Tkinter") # Donne un titre à la fenêtre (par défaut c'est Tk)

# Dans Fenetre nous allons créer un objet type Canvas qui se nomme zone_dessin
# On donne des valeurs aux propriétés "width", "height", "bg", "bd", "relief"
zone_dessin = Canvas(Fenetre,width=500,height=500,bg='yellow',bd=8,relief="ridge")
zone_dessin.pack() #Affiche le Canvas

# On va utiliser quelques méthodes du widget "zone_dessin"
zone_dessin.create_line(0,0,500,500,fill='red',width=4) # Dessine une ligne
zone_dessin.create_line(0,500,500,0,fill='red',width=4) # Dessine une ligne
zone_dessin.create_rectangle(150,150,350,350) # Dessine un rectangle
zone_dessin.create_oval(150,150,350,350,fill='white',width=4) # Dessine un cercle

# boutons_sortir est un widget de type "Button"
# dont nous définissons les propriétés "text" et "command"
bouton_sortir= Button(Fenetre,text="Sortir",command=Fenetre.destroy)
# la commande "destroy" appliquée à la fenêtre détruit l'objet "Fenetre" et clôture le programme
bouton_sortir.pack()

Fenetre.mainloop() # Lancement de la boucle du programme, en attente d'événements (clavier, souris,...)
```


### Exemple 5 :

```python
import tkinter as tk
from tkinter import ttk

def callbackFunc(event):
     print("Nouvel élément sélectionné")
     
app = tk.Tk() 
app.geometry('200x100')

def changeMonth():
    comboExample["values"] = ["Janvier",
                              "Février",
                              "Mars",
                              "Avril"
                                ]

labelTop = tk.Label(app,
                    text = "Choix du mois")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app, 
                            values=[
                                    "Janvier", 
                                    "Février",
                                    "Mars",
                                    "Avril"],
                            postcommand=changeMonth)


comboExample.grid(column=0, row=1)

app.mainloop()
```

### Exemple 6 :

```python
import tkinter as tk
from tkinter import ttk

def callbackFunc():
    resultString.set("{} - {}".format(landString.get(),
                                      cityString.get()))
     
app = tk.Tk() 
app.geometry('200x100')

labelLand = tk.Label(app,
                    text = "Pays")
labelLand.grid(column=0, row=0, sticky=tk.W)
labelCity = tk.Label(app,
                    text = "Ville")
labelCity.grid(column=0, row=1, sticky=tk.W)

landString = tk.StringVar()
cityString = tk.StringVar()
entryLand = tk.Entry(app, width=20, textvariable=landString)
entryCity = tk.Entry(app, width=20, textvariable=cityString)

entryLand.grid(column=1, row=0, padx=10)
entryCity.grid(column=1, row=1, padx=10)


resultButton = tk.Button(app, text = 'Afficher',
                         command=callbackFunc)

resultButton.grid(column=0, row=2, pady=10, sticky=tk.W)

resultString=tk.StringVar()
resultLabel = tk.Label(app, textvariable=resultString)
resultLabel.grid(column=1, row=2, padx=10, sticky=tk.W)

app.mainloop()
```


### Exemple 7 :

```python
import tkinter as tk
    
    
app = tk.Tk()
app.geometry('400x200')

buttonW = tk.Button(app, text="gauche", width=30)
buttonW.pack(side='left')

buttonE1 = tk.Button(app, text="droite", width=15)
buttonE1.pack(side='right')

app.mainloop()
```


### Exemple 8 :

```python
import tkinter as tk

app = tk.Tk() 

labelWidth = tk.Label(app,
                    text = "Width Ratio")
labelWidth.grid(column=0, row=0, ipadx=5, pady=5, sticky=tk.W+tk.N)

labelHeight = tk.Label(app,
                    text = "Height Ratio")
labelHeight.grid(column=0, row=1, ipadx=5, pady=5, sticky=tk.W+tk.S)


entryWidth = tk.Entry(app, width=20)
entryHeight = tk.Entry(app, width=20)

entryWidth.grid(column=1, row=0, padx=10, pady=5, sticky=tk.N)
entryHeight.grid(column=1, row=1, padx=10, pady=5, sticky=tk.S)


resultButton = tk.Button(app, text = 'Afficher')
resultButton.grid(column=0, row=2, pady=10, sticky=tk.W)

logo = tk.PhotoImage(file='contraste1-Lenna_gray.png')
labelLogo = tk.Label(app, image=logo)

labelLogo.grid(row=0, column=2, columnspan=2, rowspan=2,
               sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

app.mainloop()
```


### Exemple 9 :

```python
import tkinter as tk

app = tk.Tk()
app.geometry('300x300') 

labelA = tk.Label(app, text = "Label (0, 0)", fg="blue", bg="#FF0")
labelB = tk.Label(app, text = "Label (20, 20)", fg="green", bg="#300")
labelC = tk.Label(app, text = "Label (40, 50)", fg="black", bg="#f03")
labelD = tk.Label(app, text = "Label (0.5, 0.5)", fg="orange", bg="#0ff")

labelA.place(x=0, y=0)
labelB.place(x=20, y=20)
labelC.place(x=40, y=50)
labelD.place(relx=0.5, rely=0.5)

app.mainloop()
```


### Exemple 10 :

```python
import tkinter as tk
from tkinter import messagebox

root= tk.Tk()
root.geometry('300x200')

def ExitApp():
    MsgBox = tk.messagebox.askquestion ('Quitter','Etes-vous sûr ?',icon = 'error')
    if MsgBox == 'yes':
        root.destroy()
    else:
        tk.messagebox.showinfo('Bienvenue de nouveau','Bienvenue de nouveau dans application')
        
buttonEg = tk.Button (root, text='Quitter lapplication',command=ExitApp)
buttonEg.pack()
  
root.mainloop()
```


### Exemple 11 :

```python
from tkinter import *

for i in range(5):
    for j in range(4):
        l = Label(text='%d.%d' % (i, j), relief=RIDGE)
        l.grid(row=i, column=j, sticky=NSEW)

mainloop()
```


### Exemple 12 :

```python
from tkinter import *
import tkinter.font as font
gui = Tk()
gui.geometry("300x200")
# définir le font
f = font.Font(family='Times New Roman', size=35, weight="bold")
# créer un bouton
btn = Button(gui, text='Cliquez ici!', bg='red', fg='white')
# appliquer la police à l'étiquette du bouton
btn['font'] = f
# ajouter le bouton à la fenêtre
btn.pack()
gui.mainloop()
```


### Exemple 13 :

```python
from tkinter import *

root = Tk()

root.title("Bienvenue")
root.geometry('350x200')

menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

lbl = Label(root, text = "Etes-vous adulte?")
lbl.grid()

txt = Entry(root, width=10)
txt.grid(column =1, row =0)
 
def clicked():
    res = "Vous avez répondu : " + txt.get()
    lbl.configure(text = res)

btn = Button(root, text = "Clic" ,
             fg = "red", command=clicked)

btn.grid(column=2, row=0)

root.mainloop()
```


### Exemple 14 :

```python
from tkinter import *

fenetre = Tk()
titre = Label(fenetre, text = "Electronique",fg = 'red')

titre.pack()

fenetre.title("Calculatrice BTS")
fenetre.minsize(300,200)

cadre = Frame(fenetre)
cadre.pack()

expression = StringVar()
expression.set("16*6")   # texte par défaut affiché dans l'entrée
entree = Entry(cadre, textvariable = expression, width = 30)
entree.pack()

sortie = Label(cadre, textvariable = expression)
sortie.pack()

resultat = StringVar()
sortie = Label(cadre, textvariable = resultat)
sortie.pack()

#def calculer():
#    resultat.set(eval(expression.get()))

def calculer():
    try:
        resultat.set(eval(expression.get()))
    except:
        pass

# Bouton pour exécuter les calculs
bouton = Button(cadre, text = "Calculer", command = calculer)
bouton.pack()

fenetre.mainloop()
```

