"""
Created 2024

@author:Abde el moutaki
"""


from tkinter import *
from tkinter import font
import DataBase as bdd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.messagebox import showinfo as info, showerror as error
import datetime
from time import strftime
from numpy import mean
from sqlite3 import Connection

Navigation = ""
monfont = 0
fonttexte = 0
font_titre = 0
recap = 0
Systeme = 0


class interface_user:
    def __init__(self, fen, cne, Nom):
        self.fen = fen
        self.Nom = Nom
        self.Etat_user = [cne]
        self.Etat_user.append(bdd.Parcours_Etudiant)
        date = datetime.datetime.now()
        self.Etat_user.append(str(date))
        self.fenetre = Frame(fen, width=1000, height=600, bg="#FFFFFF")
        global monfont, fonttexte, font_titre, recap, Navigation, Systeme
        Navigation = "Home>"
        monfont = font.Font(family='Helvetica', size=11, weight='bold')
        fonttexte = font.Font(family='Helvetica', size=14, weight='bold')
        font_titre = font.Font(family='Helvetica', size=18, weight='bold', underline=1)
        recap = bdd.recap()
        Systeme = bdd.Erreur_Precision()
        self.fen.protocol("WM_DELETE_WINDOW", self.quitter_fenetre)

        # Create left-side navigation bar
        self.can = Canvas(self.fenetre, width=200, height=600, bg="#305389", bd=0)
        self.can.place(x=0, y=0)
        self.mes_images = []
        self.mes_images.append(PhotoImage(file="Images/accueil1.png", master=self.fenetre))
        self.mes_images.append(PhotoImage(file="Images/accueil2.png", master=self.fenetre))
        self.mes_images.append(PhotoImage(file="Images/recap1.png", master=self.fenetre))
        self.mes_images.append(PhotoImage(file="Images/recap2.png", master=self.fenetre))
        self.mes_images.append(PhotoImage(file="Images/predict1.png", master=self.fenetre))
        self.mes_images.append(PhotoImage(file="Images/predict2.png", master=self.fenetre))
        self.mes_images.append(PhotoImage(file="Images/apropos1.png", master=self.fenetre))
        self.mes_images.append(PhotoImage(file="Images/apropos2.png", master=self.fenetre))
        self.mes_images.append(PhotoImage(file="Images/quitter.png", master=self.fenetre))
        self.mes_images.append(PhotoImage(file="Images/recap3.png", master=self.fenetre))
        self.mes_images.append(PhotoImage(file="Images/predict3.png", master=self.fenetre))
        self.mes_images.append(PhotoImage(file="Images/apropos3.png", master=self.fenetre))
        self.mes_images.append(PhotoImage(file="Images/quitter3.png", master=self.fenetre))

        # Calculate the center position for the icons and add margins
        icon_center_x = 100
        initial_y = 100
        margin_y = 80

        # Adjust the positions of the navigation buttons
        self.accueil = self.can.create_image(icon_center_x, initial_y, anchor=CENTER, image=self.mes_images[1], tag="accueil")
        self.can.tag_bind("accueil", "<Button-1>", self.gestion_accueil)
        self.recapp = self.can.create_image(icon_center_x, initial_y + margin_y, anchor=CENTER, image=self.mes_images[2], tag="recap")
        self.can.tag_bind("recap", "<Button-1>", self.gestion_recap)
        self.predict = self.can.create_image(icon_center_x, initial_y + 2 * margin_y, anchor=CENTER, image=self.mes_images[4], tag="predict")
        self.can.tag_bind("predict", "<Button-1>", self.gestion_predict)
        self.apropos = self.can.create_image(icon_center_x, initial_y + 3 * margin_y, anchor=CENTER, image=self.mes_images[6], tag="apropos")
        self.can.tag_bind("apropos", "<Button-1>", self.gestion_apropos)
        self.quitter = self.can.create_image(icon_center_x, initial_y + 4 * margin_y, anchor=CENTER, image=self.mes_images[8], tag="quitter")
        self.can.tag_bind("quitter", "<Button-1>", self.gestion_quitter)

        self.cadre_accueil = self.menu_home()
        self.cadre_recap = Recap(self.fenetre)
        self.cadre_predict = Predict(self.fenetre)
        self.cadre_apropos = Apropos(self.fenetre)

        self.cadre_accueil.place(x=200, y=0)
        self.fenetre.place(x=0, y=0)

    def menu_home(self):
        cadre_home = Frame(self.fenetre, bg="#FFFFFF", width=800, height=600)
        texte_titre = ("Bienvenue à l'interface d'aide à l'orientation {}".format(self.Nom))
        canvas_home = Canvas(cadre_home, width=800, height=600, bg="#FFFFFF", bd=0)
        canvas_home.place(x=-2, y=-2)
        canvas_home.create_text(400, 50, text=texte_titre, fill="#305389", font=font_titre, justify="left")
        canvas_home.create_text(400, 110, text="Vous pouvez utilisez les options suivantes pour :", fill="black", font=fonttexte, justify="left")

        canvas_home.create_image(50, 170, anchor=NW, image=self.mes_images[9], tag="recap")
        canvas_home.create_text(275, 195, text="Voir le récapitulatif\ndu DEUST", fill="black", activefill="#305389", font=fonttexte, justify="left", tag="recap")
        canvas_home.tag_bind("recap", "<Button-1>", self.gestion_recap)

        canvas_home.create_image(65, 280, anchor=NW, image=self.mes_images[10], tag="predict")
        canvas_home.create_text(280, 300, text="Voir les prédictions", fill="black", activefill="#305389", font=fonttexte, justify="left", tag="predict")
        canvas_home.tag_bind("predict", "<Button-1>", self.gestion_predict)

        canvas_home.create_image(492, 170, anchor=NW, image=self.mes_images[11], tag="apropos")
        canvas_home.create_text(684, 195, text="Plus d'informations\nsur le système", fill="black", activefill="#305389", font=fonttexte, justify="left", tag="apropos")
        canvas_home.tag_bind("apropos", "<Button-1>", self.gestion_apropos)

        canvas_home.create_image(505, 280, anchor=NW, image=self.mes_images[12], tag="quitter")
        canvas_home.create_text(683, 300, text="Retourner à la page\nd'accueil", fill="black", activefill="#305389", font=fonttexte, justify="left", tag="quitter")
        canvas_home.tag_bind("quitter", "<Button-1>", self.gestion_quitter)

        Label_Heure = Label(canvas_home, font=fonttexte, relief='groove', bg='#FFFFFF', fg='#52251C', padx=8, pady=4)
        Label_Heure.place(x=430, y=540)

        def Heure():
            Label_Heure.config(text=strftime('%d-%m-%Y  %H:%M:%S'))
            Label_Heure.after(200, Heure)

        Heure()

        return cadre_home

    def gestion_accueil(self, event):
        global Navigation
        Navigation += "\nHome>"
        self.gestion_focus()
        self.can.itemconfig(self.accueil, image=self.mes_images[1])
        self.cadre_accueil.place(x=200, y=0)

    def gestion_recap(self, event):
        global Navigation
        Navigation += "\nRecap>"
        self.gestion_focus()
        self.can.itemconfig(self.recapp, image=self.mes_images[3])
        self.cadre_recap.affiche()
        self.cadre_recap.place(x=200, y=0)

    def gestion_predict(self, event):
        global Navigation
        Navigation += "\nPredict>"
        self.gestion_focus()
        self.can.itemconfig(self.predict, image=self.mes_images[5])
        self.cadre_predict.predict("PREDICTIONS")
        self.cadre_predict.place(x=200, y=0)

    def gestion_apropos(self, event):
        global Navigation
        Navigation += "\nApropos>"
        self.gestion_focus()
        self.can.itemconfig(self.apropos, image=self.mes_images[7])
        self.cadre_apropos.place(x=200, y=0)

    def gestion_quitter(self, event):
        global Navigation
        Navigation += "\nQuitter"
        date = datetime.datetime.now()
        self.Etat_user.append(str(date))
        self.Etat_user.append(Navigation)
        bdd.Etat_detaille_MAJ("User", self.Etat_user)
        self.Etat_user = 0
        self.fenetre.place_forget()

    def quitter_fenetre(self):
        if self.Etat_user != 0:
            date = datetime.datetime.now()
            self.Etat_user.append(str(date))
            self.Etat_user.append(Navigation)
            bdd.Etat_detaille_MAJ("User", self.Etat_user)
            self.fenetre.place_forget()
        self.fen.destroy()

    def gestion_focus(self):
        self.can.itemconfig(self.accueil, image=self.mes_images[0])
        self.can.itemconfig(self.recapp, image=self.mes_images[2])
        self.can.itemconfig(self.predict, image=self.mes_images[4])
        self.can.itemconfig(self.apropos, image=self.mes_images[6])
        self.cadre_accueil.place_forget()
        self.cadre_recap.place_forget()
        self.cadre_predict.place_forget()
        self.cadre_apropos.place_forget()






# Ensure to replace 'Recap', 'Predict', and 'Apropos' with their actual implementations or mock classes for testing.
# class Recap(Frame):
#     def affiche(self):
#         pass


# class Predict(Frame):
#     def predict(self, text):
#         pass


# class Apropos(Frame):
#     pass

# # Initialize the application
# if __name__ == "__main__":
#     root = Tk()
#     app = interface_user(root, "CNE123", "John Doe")
#     root.mainloop()



        
""" _____________________________________________________Classe Recap____________________________________________________________________________"""


class Recap(Frame):
    def __init__(self, fenetre):
        Frame.__init__(self, fenetre, bg="#FFFFFF", width=1000, height=520)
        self.texte=("Courbe Evolutive des notes du DEUST")
        self.label_recap = Label(self, text=self.texte, bg="#FFFFFF", font=font_titre, fg="#305389")
        self.canvas=0
        self.texte_moyenne="Moyenne du DEUST: "+str(recap["Moyenne_DEUST"])
        self.Moyenne_DEUST=Label(self,text=self.texte_moyenne,bg="#FFFFFF",fg="#305389",font=fonttexte)
        self.Moyenne_DEUST.place(x=540,y=450)
        self.Bouton={}
        self.x=30
        for i in recap:
            if i!="Moyenne_DEUST":
                def gestionnaire(j=i):
                    return self.Recap_DEUST(j)
                self.Bouton[i]=Button(self,bg="#305389",text=i,command=gestionnaire, font=monfont, width=12, cursor="hand2")
                self.Bouton[i].place(x=self.x,y=450)
                self.x+=115
        
        self.label_recap.place(x=250, y=25)
        
        
        
    def affiche(self):
        for i in recap:
            self.Recap_DEUST(i)
            break
        
    def Recap_DEUST(self, Nom):
        global Navigation
        Navigation+=(Nom+">")
        for i in recap:
            if i!="Moyenne_DEUST":
                self.Bouton[i]['bg']="#305389"
        self.Bouton[Nom]['bg']="#027EA4"
        graph = FigureCanvasTkAgg(recap[Nom]["fig"], master=self)
        self.canvas = graph.get_tk_widget()
        self.canvas.place(x=0, y=60)
        texte_moy=(Nom+"\n")
        for i in recap[Nom]["Notes"]:
            texte_moy+="\n"+i+": {}".format(recap[Nom]["Notes"][i])
        texte_moy += "\n\nMoyenne générale: {}".format(recap[Nom]["moy"])
        moyenne = Label(self, text=texte_moy, bg="#FFFFFF", font=fonttexte, justify="center",width=30,height=15)
        moyenne.place(x=480, y=100)
   
    
    
""" _____________________________________________________Classe Predict____________________________________________________________________________"""

class Predict(Frame):
    def __init__(self, fenetre):
        Frame.__init__(self, fenetre, bg="#FFFFFF", width=1000, height=520)
        self.Predictions = bdd.predict()
        
        self.canvas_predict = Canvas(self, bg="#FFFFFF", width=1000, height=520)
        self.canvas_predict.place(x=-2, y=-2)
        self.canvas_predict.create_text(300, 40, text="PREDICTIONS", fill="#305389", font=font_titre, justify="center")
        
        self.Filiere = 0
        self.options = ["PREDICTIONS"]
        for j in self.Predictions:
            if j != "fig":
                self.options.append(j)
        
        self.create_buttons()
        
        self.canvas = None
        self.graph = None
        
        self.canvas_predict.create_text(600, 470, text="Plus d'infos", fill="#305389", activefill="black", tag=("Info", "Fig"), font=fonttexte, state="hidden")
        self.canvas_predict.tag_bind("Info", "<Button-1>", self.Plus_Infos)   
        self.image = PhotoImage(file="Images/aide.png", master=fenetre)
        self.canvas_predict.create_image(600, 450, anchor=NW, image=self.image, tag=("Info", "Fig"), state="hidden") 
        
    def create_buttons(self):
        button_frame = Frame(self, bg="#FFFFFF")
        button_frame.place(relx=0.4, rely=0.05, anchor="n")  # Adjust relx to 0.05 to minimize top margin

        for option in self.options:
            btn = Button(button_frame, text=option, font=fonttexte, bg="#096F91", fg="white", relief="solid", borderwidth=2, command=lambda opt=option: self.predict(opt))
            btn.pack(side="left", padx=0)  # Add horizontal spacing between buttons
            btn.bind("<Enter>", self.on_enter)
            btn.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        event.widget.config(bg="#096F91", fg="white")

    def on_leave(self, event):
        event.widget.config(bg="#305389", fg="white")

    def Plus_Infos(self, event):
        try:
            Connexion = sql.connect("C:\\New Folder (2)\\Application\\Base.db")
            Curseur = Connexion.cursor()
            Curseur.execute("select Description from Filiere where Nom=?", [self.Filiere])
            texte = Curseur.fetchone()[0]
            info("Informations sur la filière", texte)
        except Exception:
            error("Erreur", "Impossible de se connecter à la base de données")
        finally:
            Connexion.close()
    
    def predict(self, option):
        global Navigation
        Navigation += (option + ">")
        self.Filiere = option
        self.canvas_predict.delete("predictions")
        self.canvas_predict.delete("Fig")
        
        if option == "PREDICTIONS":
            self.canvas_predict.itemconfig("Info", state="hidden")
            self.canvas_predict.create_text(930, 160, text="MOYENNES PROBABLES", fill="#305389", font=fonttexte, tag="predictions")
            # self.canvas_predict.create_rectangle(670, 140, 690, 420, tag="predictions")
            y = 200
            for i in self.Predictions:
                if i != "fig":
                    Texte = i + ": {}".format(int(round(mean(self.Predictions[i]))))
                    self.canvas_predict.create_text(630, y, text=Texte, fill="black", font=fonttexte, tag="predictions")
                    y += 50
            
            self.graph = FigureCanvasTkAgg(self.Predictions["fig"]["General"], master=self.canvas_predict)
            self.canvas = self.graph.get_tk_widget()
            self.canvas["width"] = 320
            self.canvas["height"] = 440
            self.canvas_predict.create_window(310, 300, window=self.canvas, tag="predictions")
        else:
            self.canvas_predict.itemconfig("Info", state="normal")
            self.graph = FigureCanvasTkAgg(self.Predictions["fig"][option], master=self.canvas_predict)
            self.canvas = self.graph.get_tk_widget()
            self.canvas_predict.create_window(310, 300, window=self.canvas, tag="Fig")
            Texte_Description = ("Moyenne Prévisionnelle\n\n"
                                 "Semestre 5: {:.2f}\n"
                                 "Semestre 6: {:.2f}\n\n"
                                 "Moyenne générale: {:.2f}(+/-{:.2f})".format(
                                 round(self.Predictions[option][0], 2),
                                 round(self.Predictions[option][1], 2), 
                                 round(mean(self.Predictions[option]), 2),
                                 round(Systeme["error"], 2)))
            self.canvas_predict.create_text(630, 250, text=Texte_Description, justify="center", font=fonttexte, tag=("Fig", "Description"))

# Note: Make sure to replace `font_titre`, `fonttexte`, `bdd`, and `Systeme` with actual references or imports as they are not defined in the provided snippet.

""" _____________________________________________________Classe Apropos____________________________________________________________________________"""


class Apropos(Frame):
    def __init__(self, fenetre):
        Frame.__init__(self, fenetre, bg="#FFFFFF", width=1000, height=520)
        self.Erreur=Systeme["error"]
        self.Precision=round(Systeme["precision"],2)
        self.Label_titre = Label(self, text="A PROPOS DU SYSTEME", font=font_titre, bg="#FFFFFF", fg="#305389")
        self.Label_titre.place(x=250, y=25)
        
        if bdd.modele_utilise == "cnn":
            self.texte = ("Ce système de prédiction utilise un algorithme d'apprentissage\n\n" 
                          "automatique appelé'Réseau de Neurones Convolutif' (CNN), qui extrait \n\n" 
                          "des caractéristiques importantes des données visuelles en utilisant des\n\n" 
                          " couches de neurones spéciales. En combinant ces caractéristiques à travers  \n\n"
                          "le réseau, le CNN est capable de faire des prédictions précises sur de nouvelles données d'entrée.")
        elif bdd.modele_utilise == "mlp":
            self.texte = ("Ce système de prédiction utilise un algorithme d'apprentissage \n\n"
                          " automatique appelé 'Perceptron Multicouche' ('MLP' pour 'Multilayer\n\n"
                          " Perceptron' en anglais).en anglais) L'algorithme MLP est une forme de \n\n"
                          "réseau de neurones artificiels composé de artificiels composé de plusieurs\n\n"
                          " couches de neurones. Chaque neurone est connecté à tous les neurones  à tous\n\n"
                          "les neurones de la couche suivante, formant ainsi un réseau multicouche.")
        elif bdd.modele_utilise=="AD":
            self.texte=("Ce sytème de prédiction utilise un algorithme de l'apprentissage automatique\n\n"
                    "appelé 'Arbre de décision'.\n\n"
                    "Il est une structure semblable à un organigramme représentant un ensemble \n\n"
                    "de choix sous forme d'un arbre.")
        self.label_apropos = Label(self, text=self.texte, bg="#FFFFFF", font=fonttexte, justify="left")
        self.label_apropos.place(x=10, y=100)
        self.texte1 = "Précision du système: {}%\n\nErreur moyenne du système:{}".format(self.Precision,self.Erreur)
        self.label_apropos1 = Label(self, text=self.texte1, bg="#FFFFFF", fg="#305389", font=fonttexte, justify="right")
        self.label_apropos1.place(x=300, y=370 )
        
        self.Canvas_info=Canvas(self,width=200,height=45,bg="#FFFFFF",highlightthickness=-2,cursor='hand2')
        self.Canvas_info.create_text(70,20,text="AIDE", fill="#305389", activefill="black",tag="Info",font=fonttexte)
        self.image = (PhotoImage(file="Images/aide.png", master=fenetre))
        self.Canvas_info.create_image(0, 0, anchor=NW, image=self.image,tag="Info") 
        self.Canvas_info.place(x=665,y=480)
        self.Canvas_info.tag_bind("Info","<Button-1>",self.Plus_Infos)   
        
    def Plus_Infos(self,event):
        fichier = open("fichier/Aide.txt","r")
        texte = fichier.read()
        fichier.close()
        info("Aide",texte)
    
    
""" 
fenetre=Tk()
x = int(fenetre.winfo_screenwidth()/2-500)
y = int(fenetre.winfo_screenheight()/2-300)-30
fenetre.geometry("1000x600+{}+{}".format(x,y))
fenetre.title("AIDE A L'ORIENTATION")
fenetre.resizable(0,0)
a=False
if a:
    res = bdd.interrogation_bdd("1500263809","10/10/1997","AHMED")
    interface_user(fenetre,"1500263809",res)
else:
    res = bdd.interrogation_bdd("1500263804","10/10/1997","MOHAMED")
    interface_user(fenetre,"1500263804",res)
fenetre.mainloop()"""
    