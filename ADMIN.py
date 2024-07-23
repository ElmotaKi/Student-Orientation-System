from tkinter import *
from tkinter import font
import DataBase as bdd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.messagebox import askokcancel as ok, showinfo as info, showerror as error
from tkinter.filedialog import askopenfilename as Ouvrir_Fichier, asksaveasfilename as Enregistrer
import datetime
from time import strftime
from pandas import DataFrame
from shutil import copyfile
from os import path

Navigation = ""
Nom = 0
Password = 0
Login = 0
Algo_utilise = "cnn"
Action = "Algo"
monfont = 0
fonttexte = 0
font_titre = 0
Supprimer_Login_admin = 0
Supprimer_Password_admin = 0
Ajouter_User_chemin = 0
Supprimer_User_chemin = 0
Nom_New_admin = 0
Login_New_admin = 0
Password_New_admin = 0
Confirmer_New_admin = 0
Nom_admin = 0
Login_admin = 0
Password_admin = 0
Nom_Nouvelle_Filiere = 0
Description_Nouvelle_Filiere = 0
Parcours_Nouvelle_Filiere = 0
Parcours_Nouvel_Etudiant = 0

Info_train = 0
Importance_Filiere_Figure = 0
figure = 0
train_filiere = 0
Filieres = 0
etat_general_info = 0
etat_historique_info_admin = 0
etat_historique_info_user = 0

mes_images = []

class interface_admin:
    def __init__(self, fen, info):
        self.margin_top = 20
        self.margin_right = 20  # Add margin for the right side of the sidebar
        self.fen = fen
        self.Etat_user = [info[0], info[1]]
        date = datetime.datetime.now()
        self.Etat_user.append(str(date))
        self.fenetre = Frame(fen, width=1200 + self.margin_right, height=600, bg="#FFFFFF")
        global monfont, fonttexte, font_titre, Navigation
        monfont = font.Font(family='Helvetica', size=11, weight='bold')
        fonttexte = font.Font(family='Helvetica', size=14, weight='bold')
        font_titre = font.Font(family='Helvetica', size=18, weight='bold', underline=1)
        self.fen.protocol("WM_DELETE_WINDOW", self.quitter_fenetre)
        
        # Create a canvas for the menu on the left with increased width
        self.can = Canvas(self.fenetre, width=140, height=600, bg="#305389", bd=2)
        self.can.place(x=0, y=-2)

        # Adjust image loading to the new context
        mes_images.append(PhotoImage(file="Images/accueil1.png", master=self.fenetre))
        mes_images.append(PhotoImage(file="Images/accueil2.png", master=self.fenetre))
        mes_images.append(PhotoImage(file="Images/algo1.png", master=self.fenetre))
        mes_images.append(PhotoImage(file="Images/algo2.png", master=self.fenetre))
        mes_images.append(PhotoImage(file="Images/train1.png", master=self.fenetre))
        mes_images.append(PhotoImage(file="Images/train2.png", master=self.fenetre))
        mes_images.append(PhotoImage(file="Images/filiere1.png", master=self.fenetre))
        mes_images.append(PhotoImage(file="Images/filiere2.png", master=self.fenetre))
        mes_images.append(PhotoImage(file="Images/etat1.png", master=self.fenetre))
        mes_images.append(PhotoImage(file="Images/etat2.png", master=self.fenetre))
        mes_images.append(PhotoImage(file="Images/admin1.png", master=self.fenetre))
        mes_images.append(PhotoImage(file="Images/admin2.png", master=self.fenetre))
        mes_images.append(PhotoImage(file="Images/quitter.png", master=self.fenetre))
        mes_images.append(PhotoImage(file="Images/algo3.png", master=self.fenetre))
        mes_images.append(PhotoImage(file="Images/filiere3.png", master=self.fenetre))
        mes_images.append(PhotoImage(file="Images/train3.png", master=self.fenetre))
        mes_images.append(PhotoImage(file="Images/etat3.png", master=self.fenetre))
        mes_images.append(PhotoImage(file="Images/admin3.png", master=self.fenetre))
        mes_images.append(PhotoImage(file="Images/quitter3.png", master=self.fenetre))

        # Create menu items on the left, centered
        self.accueil = self.create_menu_item(self.can, 40, mes_images[1], "accueil", self.gestion_accueil)
        self.algo = self.create_menu_item(self.can, 120, mes_images[2], "algo", self.gestion_algo)
        self.train = self.create_menu_item(self.can, 200, mes_images[4], "train", self.gestion_train)
        self.etat = self.create_menu_item(self.can, 280, mes_images[8], "etat", self.gestion_etat)
        self.admin = self.create_menu_item(self.can, 360, mes_images[10], "admin", self.gestion_admin)
        self.quitter = self.create_menu_item(self.can, 440, mes_images[12], "quitter", self.gestion_quitter)

        global Info_train, Importance_Filiere_Figure, figure, etat_general_info, etat_historique_info_user
        Info_train = bdd.Information_Train()
        figure = bdd.Info_Train()
        etat_general_info = bdd.Etat_General()
        etat_historique_info_user = bdd.Etat_historique("", "", "User")

        global Supprimer_Login_admin, Supprimer_Password_admin, Nom_New_admin, Login_New_admin, Ajouter_User_chemin, Parcours_Nouvel_Etudiant, Supprimer_User_chemin
        global Password_New_admin, Confirmer_New_admin, Nom_admin, Login_admin, Password_admin, Parcours_Nouvelle_Filiere, Nom_Nouvelle_Filiere
        Supprimer_Login_admin = StringVar()
        Supprimer_Password_admin = StringVar()
        Nom_New_admin = StringVar()
        Login_New_admin = StringVar()
        Password_New_admin = StringVar()
        Ajouter_User_chemin = StringVar()
        Supprimer_User_chemin = StringVar()
        Confirmer_New_admin = StringVar()
        Nom_admin = StringVar()
        Login_admin = StringVar()
        Password_admin = StringVar()
        Nom_Nouvelle_Filiere = StringVar()
        Parcours_Nouvelle_Filiere = StringVar()
        Parcours_Nouvel_Etudiant = StringVar()

        global Nom, Password, Login
        Nom = info[2]
        Password = info[1]
        Login = info[0]

        global etat_historique_info_admin
        etat_historique_info_admin = bdd.Etat_historique(Login, Password, "Admin")

        self.cadre_algo = Algo(self.fenetre)
        self.cadre_filiere = Filiere(self.fenetre)
        self.cadre_train = Train(self.fenetre)
        self.cadre_etat = Etat(self.fenetre)
        self.cadre_admin = Admin(self.fenetre)
        Navigation = ""
        self.cadre_home = self.menu_home()
        self.cadre_home.place(x=140, y=0)  # Adjust the x position to accommodate the wider sidebar

        self.fenetre.place(x=0, y=0)

    def create_menu_item(self, canvas, y, image, tag, command):
        item = canvas.create_image(70, y, anchor=CENTER, image=image, tag=tag)
        canvas.tag_bind(tag, "<Button-1>", command)
        return item

    def menu_home(self):
        global Navigation
        if Navigation == "":
            Navigation += "Home>"
        else:
            Navigation += "\nHome>"
        cadre_home = Frame(self.fenetre, bg="#FFFFFF", width=900, height=600)
        texte_titre = ("BIENVENUE M/Mme {}".format(Nom))
        canvas_home = Canvas(cadre_home, width=900, height=600, bg="#FFFFFF", bd=0)
        canvas_home.place(x=-2, y=-2)
        canvas_home.create_text(450, 50, text=texte_titre, fill="#305389", font=font_titre, justify="left")
        canvas_home.create_text(420, 100, text="Vous pouvez utilisez les options suivantes pour :", fill="black", font=fonttexte, justify="left")
        canvas_home.create_image(115, 150, anchor=NW, image=mes_images[13], tag="algo")
        canvas_home.create_text(320, 175, text="Choix de l'algorithme", fill="black", activefill="#305389", font=fonttexte, justify="left", tag="algo")
        canvas_home.tag_bind("algo", "<Button-1>", self.gestion_algo)

        # canvas_home.create_image(135, 250, anchor=NW, image=mes_images[14], tag="filiere")
        # canvas_home.create_text(325, 280, text="Ajouter ou supprimer \nune filière", fill="black", activefill="#305389", font=fonttexte, justify="left", tag="filiere")
        # canvas_home.tag_bind("filiere", "<Button-1>", self.gestion_filiere)

        canvas_home.create_image(135, 250, anchor=NW, image=mes_images[15], tag="train")
        canvas_home.create_text(325, 280, text="train", fill="black", activefill="#305389", font=fonttexte, justify="left", tag="train")
        canvas_home.tag_bind("train", "<Button-1>", self.gestion_train)

        canvas_home.create_image(592, 150, anchor=NW, image=mes_images[16], tag="etat")
        canvas_home.create_text(734, 175, text="Etat du système", fill="black", activefill="#305389", font=fonttexte, justify="left", tag="etat")
        canvas_home.tag_bind("etat", "<Button-1>", self.gestion_etat)

        canvas_home.create_image(585, 250, anchor=NW, image=mes_images[17], tag="admin")
        canvas_home.create_text(733, 280, text="Paramètres", fill="black", activefill="#305389", font=fonttexte, justify="left", tag="admin")
        canvas_home.tag_bind("admin", "<Button-1>", self.gestion_admin)

        canvas_home.create_image(580, 350, anchor=NW, image=mes_images[18], tag="quitter")
        canvas_home.create_text(730, 375, text="Retourner à la page\nd'accueil", fill="black", activefill="#305389", font=fonttexte, justify="left", tag="quitter")
        canvas_home.tag_bind("quitter", "<Button-1>", self.gestion_quitter)

        Label_Heure = Label(canvas_home, font=fonttexte, relief='groove', bg='#FFFFFF', fg='#52251C', padx=8, pady=4)
        Label_Heure.place(x=600, y=440)
        
        def Heure():
            Label_Heure.config(text=strftime('%d-%m-%Y  %H:%M:%S'))
            Label_Heure.after(200, Heure) 
        
        Heure()

        return cadre_home

    def gestion_accueil(self, event):
        self.gestion_focus()
        self.can.itemconfig(self.accueil, image=mes_images[1])
        self.cadre_home = self.menu_home()
        self.cadre_home.place(x=140, y=0)  # Adjust the x position

    def gestion_algo(self, event):
        self.gestion_focus()
        self.can.itemconfig(self.algo, image=mes_images[3])
        self.cadre_algo = Algo(self.fenetre)
        self.cadre_algo.place(x=140, y=0)  # Adjust the x position

    def gestion_train(self, event):
        self.gestion_focus()
        self.can.itemconfig(self.train, image=mes_images[5])
        self.cadre_train = Train(self.fenetre)
        self.cadre_train.place(x=140, y=0)  # Adjust the x position

    # def gestion_filiere(self, event):
    #     self.gestion_focus()
    #     self.can.itemconfig(self.filiere, image=mes_images[7])
    #     self.cadre_filiere = Filiere(self.fenetre)
    #     self.cadre_filiere.place(x=200, y=0)

    def gestion_etat(self, event):
        self.gestion_focus()
        self.can.itemconfig(self.etat, image=mes_images[9])
        self.cadre_etat = Etat(self.fenetre)
        self.cadre_etat.place(x=140, y=0)  # Adjust the x position

    def gestion_admin(self, event):
        self.gestion_focus()
        self.can.itemconfig(self.admin, image=mes_images[11])
        self.cadre_admin = Admin(self.fenetre)
        self.cadre_admin.place(x=140, y=0)  # Adjust the x position

    def gestion_quitter(self, event):
        global Navigation
        Navigation += "\nQuitter"
        date = datetime.datetime.now()
        self.Etat_user.append(str(date))
        self.Etat_user.append(Navigation)
        bdd.Etat_detaille_MAJ("Admin", self.Etat_user)
        self.Etat_user = 0
        self.fenetre.place_forget()

    def quitter_fenetre(self):
        if self.Etat_user != 0:
            date = datetime.datetime.now()
            self.Etat_user.append(str(date))
            self.Etat_user.append(Navigation)
            bdd.Etat_detaille_MAJ("Admin", self.Etat_user)
        self.fen.destroy()

    def gestion_focus(self):
        self.can.itemconfig(self.accueil, image=mes_images[0])
        self.can.itemconfig(self.algo, image=mes_images[2])
        self.can.itemconfig(self.train, image=mes_images[4])
        # self.can.itemconfig(self.filiere, image=mes_images[6])
        self.can.itemconfig(self.etat, image=mes_images[8])
        self.can.itemconfig(self.admin, image=mes_images[10])
        self.cadre_home.place_forget()
        self.cadre_algo.place_forget()
        self.cadre_train.place_forget()
        self.cadre_filiere.place_forget()
        self.cadre_etat.place_forget()
        self.cadre_admin.place_forget()

# Assuming you have the definitions for Algo, Filiere, Train, Etat, and Admin classes
# The rest of your program continues here...


        
"""____________________________________________________Classe Algo____________________________________________________________________________"""



class Algo(Frame):
    def __init__(self, fenetre):
        super().__init__(fenetre, bg="#FFFFFF", width=1200, height=490)
        self.fenetre = fenetre
        self.navigation = ""
        self.navigation += "\nAlgo>"
        self.algo_utilise = None
        self.create_widgets()

    def create_widgets(self):
        self.canvas_algo = Canvas(self, bg="#FFFFFF", width=1000, height=490)
        self.canvas_algo.place(x=-2, y=-2)
        
        self.canvas_algo.create_text(400, 50, text="MODIFIER L'ALGORITHME UTILISE", fill="#305389", font=font_titre, justify="center")
        self.canvas_algo.create_text(200, 130, text="ALGORITHMES :", fill="black", font=font_titre, justify="center")
        self.canvas_algo.create_line(360, 130, 360, 500, width=1)
        
        self.algorithmes = ["Réseau de Neurones Convolutif", "Perceptron Multicouche"]
        
        y = 200
        for algo in self.algorithmes:
            self.create_algo_option(algo, y)
            y += 50
        
        self.canvas_algo.create_text(600, 230, text="", fill="black", font=fonttexte, justify="center", tag="texte_description")
        self.boutton_utiliser = Button(self, text="UTILISER", font=monfont, bg="#305389", width=17, fg="white", command=self.utiliser_algo, cursor="hand2")
        self.canvas_algo.create_window(600, 430, window=self.boutton_utiliser)
        
        self.algo(self.algorithmes[0])
      
    def create_algo_option(self, algo, y):
        self.canvas_algo.create_text(200, y, text=algo, fill="#305389", activefill="#305389", font=fonttexte, justify="center", tag=("algo", algo))
        self.canvas_algo.tag_bind(algo, "<Button-1>", lambda evt, algo=algo: self.algo_event(algo))
        
    def algo_event(self, algo):
        self.algo(algo)
    
    def algo(self, algo):
        descriptions = {
            "Réseau de Neurones Convolutif": (
                "Le 'Réseau de Neurones Convolutif' signifie \n\n" 
                "Forêts Aléatoires. Il est constitué d'un ensembe\n\n"
                " d'arbresd'arbres de décisions qui permettent de\n\n"
                " faire chacun une prédiction. Le résultat fourni\n\n"
                "est alors la moyenne de toutes ces prédictions."
            ),
            "Perceptron Multicouche": (
                "La 'Perceptron Multicouche' est utilisée\n\n"
                "pour estimer les valeurs réelles basées\n\n"
                "sur des variables continues. Elle consiste\n\n"
                "à ajuster une ligne droite à travers un\n\n"
                "ensemble de points."
            ),
            # "Arbre de décision": (
            #     "L'Arbre de decision est une structure\n\n"
            #     "semblable à un organigramme représentant\n\n"
            #     "un ensemble de choix sous forme d'un arbre."
            # )
        }

        self.canvas_algo.itemconfig("algo", fill="black")
        self.canvas_algo.itemconfig(algo, fill="#305389")
        self.navigation += f"Algo_{algo.lower().replace(' ', '_')}>"
        self.algo_utilise = algo.lower().replace(' ', '_')
        self.canvas_algo.itemconfig("texte_description", text=descriptions[algo])
        self.canvas_algo.itemconfig("erreur", state="hidden")
    
    def utiliser_algo(self):
        self.navigation += "Utiliser>"
        if self.algo_utilise == bdd.modele_utilise:
            self.canvas_algo.create_text(600, 470, text="L'algorithme est déja en cours d'utilisation", fill="red", font=fonttexte, tag="erreur")
        else:
            self.place_forget()
            identification("Algo", self.fenetre, self)

# Note: Make sure to define or import 'font_titre', 'fonttexte', 'monfont', 'bdd', and 'identification' as they are used in the code.

# Note: Make sure to define or import 'font_titre', 'fonttexte', 'monfont', 'bdd', and 'identification' as they are used in the code.



""" _____________________________________________________Classe Filiere____________________________________________________________________________"""

        
class Filiere(Frame):
    def __init__(self,fenetre):
        Frame.__init__(self, fenetre, bg="#FFFFFF",width=1000,height=490)
        global Navigation
        Navigation+="\nFilière>"
        # self.mes_images=[]
        # self.Changer="MIP"
        # Parcours_Nouvelle_Filiere.set("MIP")
        # self.canvas_filiere = Canvas(self, bg="#FFFFFF", width=1000, height=490)
        # self.canvas_filiere.place(x=-2, y=-2)
        # self.fenetre=fenetre
        # self.Can=Canvas(width=630, height=355,master=self.canvas_filiere)
        # self.canvas_filiere.create_window(730,270,window=self.Can,tag="Info_Filiere")
        # self.canvas_filiere.create_text(500, 50, text="PARAMETRES DES FILIERES", fill="#305389", font=font_titre, justify="center")
        # self.canvas_filiere.create_text(250, 130, text="FILIERES :", fill="black", font=font_titre, justify="center")
        # self.canvas_filiere.create_line(410,130,410,500, width=1)
        # self.mes_images.append(PhotoImage(file="Images/admin.png", master=self))
        # self.mes_images.append(PhotoImage(file="Images/user.png", master=self))
        # self.canvas_filiere.create_text(50,60,text="MIP",font=monfont,tag=("Filiere","MIP"))
        # self.canvas_filiere.create_text(130,60,text="BCG",font=monfont,tag=("Filiere","BCG"))
        # self.canvas_filiere.create_image(68,50,image=self.mes_images[1], anchor=NW,tag=("Image","Filiere"))
        # self.canvas_filiere.tag_bind("Filiere","<Button-1>",self.Changer_Image_Filiere)   
        self.descritption=0
        
        # self.y=180
        # for i in Importance_Filiere_Figure["MIP"]:
        #     self.canvas_filiere.create_text(250, self.y, text=i, fill="#305389", activefill="#305389", font=fonttexte, justify="center", tag=("filiere",i,"mip"))
        #     def gestionnaire(evt, i=i):
        #         return self.filiere_event(evt, i)
        #     self.canvas_filiere.tag_bind(i, "<Button-1>",gestionnaire)
        #     self.y+=50
        
        # self.y=180
        # for i in Importance_Filiere_Figure["BCG"]:
        #     self.canvas_filiere.create_text(250, self.y, text=i, fill="#305389", activefill="#305389", font=fonttexte, justify="center", tag=("filiere",i,"bcg"), state="hidden")
        #     def gestionnaire(evt, i=i):
        #         return self.filiere_event(evt, i)
        #     self.canvas_filiere.tag_bind(i, "<Button-1>",gestionnaire)
        #     self.y+=50
        # self.boutton_supprimer=Button(self,text="Supprimer la filière",font=monfont,bg="#305389",width=25,fg="white",command=self.Supprimer, cursor="hand2")
        # self.canvas_filiere.create_window(710, 475, window=self.boutton_supprimer, tag="boutons")
        # self.boutton_ajouter=Button(self,text="Ajouter une nouvelle filière",font=monfont,bg="#305389",width=25,fg="white",command=self.Ajouter, cursor="hand2")
        # self.canvas_filiere.create_window(250, 475, window=self.boutton_ajouter, tag="boutons")
        
        # for i in Importance_Filiere_Figure["MIP"]:
        #     self.filiere(i)
        #     break
    
    # def Changer_Image_Filiere(self,event):
    #     if self.Changer=="MIP":
    #         self.Changer="BCG"
    #         self.canvas_filiere.itemconfig("mip", state="hidden")
    #         self.canvas_filiere.itemconfig("bcg", state="normal")
    #         self.canvas_filiere.itemconfig("Image", image=self.mes_images[0])
    #         for i in Importance_Filiere_Figure["BCG"]:
    #             self.filiere(i)
    #             break
    #     elif self.Changer=="BCG":
    #         self.Changer="MIP"
    #         self.canvas_filiere.itemconfig("bcg", state="hidden")
    #         self.canvas_filiere.itemconfig("mip", state="normal")
    #         self.canvas_filiere.itemconfig("Image", image=self.mes_images[1])
    #         for i in Importance_Filiere_Figure["MIP"]:
    #             self.filiere(i)
    #             break
    
            
    # def filiere_event(self,event,Nom_Filiere):
    #     self.filiere(Nom_Filiere)
    # def filiere(self,Nom_Filiere):          
    #     global Navigation,Filieres
    #     Navigation+=(Nom_Filiere.lower()+">")
    #     Filieres=Nom_Filiere
    #     self.canvas_filiere.itemconfig("filiere", fill="black")
    #     self.canvas_filiere.itemconfig(Nom_Filiere, fill="#305389")
    #     self.canvas_filiere.itemconfig("boutons", state="normal")
    #     self.graph = FigureCanvasTkAgg(Importance_Filiere_Figure[self.Changer][Nom_Filiere], master=self.canvas_filiere)
    #     canvas= self.graph.get_tk_widget()
    #     canvas["height"]=355
    #     canvas["width"]=630
    #     self.canvas_filiere.itemconfig("Info_Filiere", window=canvas) 
    
    # def Supprimer(self):
    #     self.place_forget()
    #     identification("Supprimer_Filiere",self.fenetre,self)
    # def Ajouter(self):
    #     self.canvas_filiere.itemconfig("boutons", state="hidden")
    #     self.canvas_filiere.itemconfig("filiere", fill="black")
    #     Nom_Nouvelle_Filiere.set("")
    #     canvas_ajouter = Canvas(self.canvas_filiere, bg="#FFFFFF", width=500, height=380, bd=-2, highlightthickness=0)
    #     self.canvas_filiere.itemconfig("Info_Filiere", window=canvas_ajouter)
        
        # def focus_Nom(event):
        #     self.description.focus()
        
        # canvas_ajouter.create_text(100, 50, text="Nom de la Filière", fill="#52251C", font=monfont, justify="center")
        # Cadre_Nom=Frame(canvas_ajouter,bg="#FFFFFF")
        # Entry_Nom=Entry(Cadre_Nom,textvariable=Nom_Nouvelle_Filiere,bg="#4C1B1B",font=monfont,width=40, fg="white", insertbackground="white")
        # Entry_Nom.pack(ipady=3)
        # Entry_Nom.bind("<Return>",focus_Nom)
        # canvas_ajouter.create_window(205, 80, window=Cadre_Nom)
        
        # canvas_ajouter.create_text(128, 120, text="Description de la Filière", fill="#52251C", font=monfont, justify="center")
        # self.description=Text(canvas_ajouter,bg="#4C1B1B",bd=1,width=40, height=5, font=monfont, fg="white", insertbackground="white")
        # canvas_ajouter.create_window(205, 180, window=self.description)
                                   
        # Cadre_Parcours=Frame(canvas_ajouter,bg="#FFFFFF", width=300, height=80)
        # canvas_ajouter.create_text(120, 250, text="Parcours de la Filière", fill="#52251C", font=monfont, justify="center")
        # Parcours_mip = Radiobutton(Cadre_Parcours, bg="#FFFFFF", variable=Parcours_Nouvelle_Filiere, text="Mathématiques-Informatique-Physique", value="MIP", font=monfont,activeforeground="#305389", activebackground="#FFFFFF", cursor="hand2")
        # Parcours_bcg = Radiobutton(Cadre_Parcours, bg="#FFFFFF", variable=Parcours_Nouvelle_Filiere, text="Biologie-Chimie-Géologie", value="BCG", font=monfont,activeforeground="#305389", activebackground="#FFFFFF", cursor="hand2")
        # Parcours_mip.place(x=2,y=2)
        # Parcours_bcg.place(x=2,y=40)
        # canvas_ajouter.create_window(190, 300, window=Cadre_Parcours)
        
        
        # Boutton_ajouter =Button(canvas_ajouter, text="Ajouter", bg="#305389", fg="white",width=35,font=monfont,command=self.Ajouter_Nouvelle_Filiere, cursor="hand2")
        # canvas_ajouter.create_window(205, 360, window=Boutton_ajouter)
        
    # def Ajouter_Nouvelle_Filiere(self):
    #     global Description_Nouvelle_Filiere
    #     Description_Nouvelle_Filiere=self.description.get('1.0','end')
    #     if(Nom_Nouvelle_Filiere.get()==""):
    #         error("Erreur","Veuillez saisir le nom de la filière")
    #     else:
    #         self.place_forget()
    #         identification("Ajouter_Filiere",self.fenetre,self)

""" _____________________________________________________Classe Train____________________________________________________________________________"""

        
class Train(Frame):
    def __init__(self,fenetre):
        Frame.__init__(self, fenetre, bg="#FFFFFF",width=1000,height=520)
        self.fenetre = fenetre
        global Navigation
        Navigation+="\nTrain>"
        self.Changer="MIP"
        self.mes_images=[]
        self.canvas_train=Canvas(self,width=1000,height=520,bg="#FFFFFF")
        self.canvas_train.place(x=-2, y=-2)
        self.canvas_train.create_text(490, 50, text="INFORMATION D'ENTRAINEMENT", fill="#305389", font=font_titre, justify="center")
        self.Bouton_train=Button(self,text="ENTRAINER LE MODELE",bg="#305389",fg="white",width="25",font=monfont,command=self.Entrainement, cursor="hand2")
        self.canvas_train.create_window(200,450,window=self.Bouton_train)
        self.mes_images.append(PhotoImage(file="Images/admin.png", master=self))
        self.mes_images.append(PhotoImage(file="Images/user.png", master=self))
        self.canvas_train.create_text(50,60,text="MIP",font=monfont,tag=("Parcours","MIP"))
        self.canvas_train.create_text(130,60,text="BCG",font=monfont,tag=("Parcours","BCG"))
        self.canvas_train.create_image(68,50,image=self.mes_images[1], anchor=NW,tag=("Image","Parcours"))
        self.canvas_train.tag_bind("Parcours","<Button-1>",self.Changer_Image_Train) 
       
        self.x=200
        self.Bouton_MIP={}
        for j in Info_train["MIP"]:
            def gestionnaire(x=j):
                return self.Info_Train(x)
            self.Bouton_MIP[j]=Button(self,text=j,bg="#305389",width="25",font=monfont,command=gestionnaire, cursor="hand2")
            self.canvas_train.create_window(self.x,100,window=self.Bouton_MIP[j],tag=("mip"))
            self.x+=200
            
        self.x=125
        self.Bouton_BCG={}
        for j in Info_train["BCG"]:
            def gestionnaire(x=j):
                return self.Info_Train(x)
            self.Bouton_BCG[j]=Button(self,text=j,bg="#305389",width="25",font=monfont,command=gestionnaire, cursor="hand2")
            self.canvas_train.create_window(self.x,100,window=self.Bouton_BCG[j],tag=("bcg"))
            self.x+=200
        
        self.canvas_train.itemconfig("bcg", state="hidden")
        self.canvas_train.create_text(210, 270, text="", fill="black", font=fonttexte, justify="center",tag="Texte_Info")
        for i in Info_train["MIP"]:
            self.Info_Train(i)
            break
     
    def Changer_Image_Train(self,event):
        if self.Changer=="MIP":
            self.Changer="BCG"
            self.canvas_train.itemconfig("mip", state="hidden")
            self.canvas_train.itemconfig("bcg", state="normal")
            self.canvas_train.itemconfig("Image", image=self.mes_images[0])
            for i in Info_train["BCG"]:
                self.Info_Train(i)
                break
        elif self.Changer=="BCG":
            self.Changer="MIP"
            self.canvas_train.itemconfig("bcg", state="hidden")
            self.canvas_train.itemconfig("mip", state="normal")
            self.canvas_train.itemconfig("Image", image=self.mes_images[1])
            for i in Info_train["MIP"]:
                self.Info_Train(i)
                break
    def Info_Train(self,Nom_train):
        global Navigation, train_filiere
        Navigation+=(Nom_train.lower()+">")
        train_filiere=Nom_train
        if self.Changer=="MIP":
            for i in self.Bouton_MIP:
                self.Bouton_MIP[i]["bg"]="#305389"
            self.Bouton_MIP[Nom_train]["bg"]="#F0F0FB"
        else:
            for i in self.Bouton_BCG:
                self.Bouton_BCG[i]["bg"]="#305389"
            self.Bouton_BCG[Nom_train]["bg"]="#F0F0FB"
        texte=("Nombre de données d'entrainement: {}\n\n"
                "Nombre de données de test: {}\n\n"
                "Erreur Maximale: {}\n\n"
                "Erreur Minimale: {}\n\n"
                "Erreur Moyenne: {}\n\n"
                "Précision: {}%".format(Info_train[self.Changer][Nom_train]["Train"],Info_train[self.Changer][Nom_train]["Test"], 
                           Info_train[self.Changer][Nom_train]["Max"], Info_train[self.Changer][Nom_train]["Min"], 
                           Info_train[self.Changer][Nom_train]["Moy"], Info_train[self.Changer][Nom_train]["Prec"]))
        self.canvas_train.itemconfig("Texte_Info", text="")
        self.canvas_train.itemconfig("Texte_Info", text=texte)
        graph = FigureCanvasTkAgg(figure[self.Changer][Nom_train], master=self.canvas_train)
        canvas = graph.get_tk_widget()
        canvas.place(x=400, y=100)
    
        
    def Entrainement(self):
        global Navigation
        Navigation+="Entrainer>"
        texte=("Pour entrainer un modèle il faut importer\n"
               "un fichier contenant les notes des etudiants:\n\n"
               "  - au format .xlsx(fixhier excel)\n\n"
               "  - Les 24 premieres colonnes sont les notes du DEUST\n"
               "    avec pour en-têtes les codes des 24 modules\n    du DEUST(ex:M135)\n\n"
               "  - Les deux dernières colonnes sont les moyennes générales\n"
               "   des semestres 5 et 6 avec pour en-tête 'Moyenne_S5' et 'Moyenne_S6'.\n\n\n"
               "Voulez-vous continuer?")
        if ok(train_filiere,texte):
           self.place_forget()
           identification("Train",self.fenetre,self)

""" _____________________________________________________Classe Etat____________________________________________________________________________"""

        


class Etat(Frame):
    def __init__(self,fenetre):
        Frame.__init__(self, fenetre, bg="#FFFFFF",width=1000,height=490)
        global Navigation
        Navigation+="\nEtat>"
        self.etat_historique_admin_position=1
        self.etat_historique_user_position=1
        self.etat_action=""
        self.Changer_Image=0
        self.canvas_etat = Canvas(self, bg="#FFFFFF", width=1000, height=490)
        self.canvas_etat.create_text(400, 50, text="ETAT DU SYSTEME", fill="#305389", font=font_titre, justify="center")
        self.canvas_etat.create_text(230, 130, text="OPTIONS :", fill="black", font=font_titre, justify="center")
        self.canvas_etat.create_line(390,130,390,500, width=1)
        
        self.Canvas_description = Canvas(self.canvas_etat)
        self.canvas_etat.create_window(650,280, window=self.Canvas_description, tag="canva_description", state="hidden")
        self.scrollbar = Scrollbar(self.Canvas_description)
        self.textfield = Text(self.Canvas_description,yscrollcommand=self.scrollbar.set,bg="#FFFFFF",bd=0,width=50, height=20, font=monfont, cursor="arrow")
        self.scrollbar.config(command=self.textfield.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.textfield.pack(side='left', expand=0, fill='both')
        
        self.canvas_etat.itemconfig("nav", state="hidden")
        self.canvas_etat.itemconfig("texte_pos", state="hidden")
        self.canvas_etat.create_text(630, 260, text="", fill="black", font=fonttexte, justify="center", tag="texte_description", width=470)
        self.canvas_etat.create_text(250, 180, text="Générale", fill="#305389", activefill="#305389", font=fonttexte, justify="center", tag=("etat","générale"))
        self.canvas_etat.tag_bind("générale", "<Button-1>", self.etat_general)
        self.canvas_etat.create_text(250, 230, text="Historique Personnel", fill="black", activefill="#305389", font=fonttexte, justify="center", tag=("etat","historique"))
        self.canvas_etat.tag_bind("historique", "<Button-1>", self.etat_historique_event)
        self.canvas_etat.create_text(250, 280, text="Activités des Utilisateurs", fill="black", activefill="#305389", font=fonttexte, justify="center", tag=("etat","activités"))
        self.canvas_etat.tag_bind("activités", "<Button-1>", self.etat_activite_event)
        
        self.mes_images = []
        self.mes_images.append(PhotoImage(file="Images/suivant1.png", master=self))
        self.mes_images.append(PhotoImage(file="Images/suivant2.png", master=self))
        self.mes_images.append(PhotoImage(file="Images/precedent1.png", master=self))
        self.mes_images.append(PhotoImage(file="Images/precedent2.png", master=self))
        self.mes_images.append(PhotoImage(file="Images/admin.png", master=self))
        self.mes_images.append(PhotoImage(file="Images/user.png", master=self))
        self.suivant = self.canvas_etat.create_image(960, 230, anchor=NW, image=self.mes_images[0], activeimage=self.mes_images[1], tag=("suivant","nav"),state="hidden")
        self.canvas_etat.tag_bind("suivant", "<Button-1>", self.etat_suivant)
        self.precedent = self.canvas_etat.create_image(420, 230, anchor=NW, image=self.mes_images[2], activeimage=self.mes_images[3], tag=("precedent","nav"),state="hidden")
        self.canvas_etat.tag_bind("precedent", "<Button-1>", self.etat_precedent)
        
        self.texte_pos=("{}/{}".format(self.etat_historique_admin_position,etat_historique_info_admin[0]))
        self.canvas_etat.create_text(950, 470, text=self.texte_pos, font=monfont, tag="texte_pos", state="hidden")
        self.Boutton_Historique=Button(self.canvas_etat,text="SUPPRIMER",bg="#305389",fg="white",font=monfont,width=20,command=self.Supprimer_Historique_Admin, cursor="hand2")
        self.canvas_etat.create_window(240,470,window=self.Boutton_Historique,tag="Supprimer_Historique")
        self.canvas_etat.create_text(135,420,text="Tout l'historique",font=monfont,tag=("Supprimer_Historique","Total"))
        self.canvas_etat.create_text(310,420,text="Historique courant",font=monfont,tag=("Supprimer_Historique","Courant"))
        self.canvas_etat.create_image(200,410,image=self.mes_images[4], anchor=NW,tag=("Tout_historique","Supprimer_Historique"))
        self.canvas_etat.tag_bind("Tout_historique","<Button-1>",self.Changer_Image_historique)   
        
        self.Boutton_Telecharger=Button(self.canvas_etat,text="Telecharger",bg="#305389",fg="white",font=monfont,width=20,command=self.Telecharger_user_activite, cursor="hand2")
        self.canvas_etat.create_window(240,470,window=self.Boutton_Telecharger,tag=("Supprimer_Historique","Telecharger"))
         
        self.canvas_etat.itemconfig("Supprimer_Historique", state="hidden")
        self.etat_general_()
        self.canvas_etat.place(x=-2, y=-2)
    
    def Telecharger_user_activite(self):
        Chemin=Enregistrer(filetypes =[("Fichier excel","*.xlsx")])
        if Chemin!="":
            fic=[]
            for i in range (1,len(etat_historique_info_user)):
                fic.append(etat_historique_info_user[i])
            fic=DataFrame(fic,columns=("CNE","Parcours","Connexion","Deconnexion","Navigation"))
            fic.to_excel(Chemin+".xlsx",index=False,sheet_name='Activité des utilisateurs')
            info("Succès","Fichier téléchargé avec succès")
        
    def Changer_Image_historique(self,event):
        if self.Changer_Image==0:
            self.canvas_etat.itemconfig("Tout_historique", image=self.mes_images[5])
            self.Changer_Image=1
        else:
            self.canvas_etat.itemconfig("Tout_historique", image=self.mes_images[4])
            self.Changer_Image=0
     
    def Supprimer_Historique_Admin(self):
        global etat_historique_info_admin
        if(self.Changer_Image==1):
            bdd.Supprimer_Historique_Admin("*",Login,Password)
            etat_historique_info_admin=bdd.Etat_historique(Login,Password,"Admin")
            
        else:
            bdd.Supprimer_Historique_Admin(etat_historique_info_admin[self.etat_historique_admin_position][0],Login,Password)
            etat_historique_info_admin=bdd.Etat_historique(Login,Password,"Admin")
        
        if self.etat_historique_admin_position>1:
            self.etat_historique_admin_position-=1
        self.etat_historique()
        
    def etat_suivant(self,event):
        if self.etat_action=="historique":
            if self.etat_historique_admin_position<etat_historique_info_admin[0]:
                self.etat_historique_admin_position+=1
                self.etat_historique()
        else:
            if self.etat_historique_user_position<etat_historique_info_user[0]:
                self.etat_historique_user_position+=1
                self.etat_activite()
        
    def etat_precedent(self,event):
        if self.etat_action=="historique":
            if self.etat_historique_admin_position>1:
                self.etat_historique_admin_position-=1
                self.etat_historique()
        else:
            if self.etat_historique_user_position>1:
                self.etat_historique_user_position-=1
                self.etat_activite()
    
    
    def etat_general(self,event):
        self.canvas_etat.itemconfig("texte_description", state="normal")
        self.etat_general_()
    def etat_general_(self):
        global Navigation
        Navigation+="Général>"
        self.canvas_etat.itemconfig("canva_description", state="hidden")
        self.canvas_etat.itemconfig("etat", fill="black")
        self.canvas_etat.itemconfig("générale", fill="#305389")
        self.canvas_etat.itemconfig("texte_pos", state="hidden")
        self.canvas_etat.itemconfig("nav", state="hidden")
        self.canvas_etat.itemconfig("Supprimer_Historique", state="hidden")
        if etat_general_info[6] == "cnn":
            algo = "cnn"
        elif etat_general_info[6] == "mlp":
            algo = "mlp"
        elif etat_general_info[6] == "AD":
            algo = "Arbre de décision"
        texte=("Nombre d'utilisateurs: {}\n\n"
               "Nombre d'administrateurs: {}\n\n"
               "Nombre de connexion à l'interface utilisateur: \n"
               "    - Réussies: {}\n"
               "    - Echouées: {}\n\n"
               "Nombre de connexion à l'interface administrateur: \n"
               "    - Réussies: {}\n"
               "    - Echouées: {}\n\n"
               "Algorithme utilisé: {}".format(etat_general_info[0],etat_general_info[1],
                                etat_general_info[4],etat_general_info[2],
                                etat_general_info[5],etat_general_info[3],algo))
        self.canvas_etat.itemconfig("texte_description", text=texte, justify="center", font=fonttexte)
   
    def etat_historique_event(self,event):
        global Navigation
        Navigation+="Historique>"
        self.etat_historique()
    def etat_historique(self):
        self.etat_action="historique"
        self.canvas_etat.itemconfig("etat", fill="black")
        self.canvas_etat.itemconfig("historique", fill="#305389")
        if etat_historique_info_admin[0]!=0:
            self.canvas_etat.itemconfig("nav", state="normal")
            if self.etat_historique_admin_position==1:
                self.canvas_etat.itemconfig("precedent", state="hidden")
            if self.etat_historique_admin_position==(etat_historique_info_admin[0]):
                self.canvas_etat.itemconfig("suivant", state="hidden")
            
            texte=("Connexion: {}\n"
                   "Déconnexion: {}\n"
                   "Activité: \n{}".format(etat_historique_info_admin[self.etat_historique_admin_position][0],
                              etat_historique_info_admin[self.etat_historique_admin_position][1],
                              etat_historique_info_admin[self.etat_historique_admin_position][2]))
            texte_pos=("{}/{}".format(self.etat_historique_admin_position,etat_historique_info_admin[0]))
            self.canvas_etat.itemconfig("texte_pos", state="normal",text=texte_pos)
            self.canvas_etat.itemconfig("canva_description", state="normal")
            self.canvas_etat.itemconfig("texte_description", state="hidden")
            self.textfield["state"]='normal'
            self.textfield.delete('1.0', END)
            self.textfield.insert(0.0, texte)
            self.textfield["state"]='disabled'
            self.canvas_etat.itemconfig("Supprimer_Historique", state="normal")
            self.canvas_etat.itemconfig("Telecharger", state="hidden")
        else:
            self.canvas_etat.itemconfig("nav", state="hidden")
            self.canvas_etat.itemconfig("canva_description", state="hidden")
            texte=("Aucun Historique")
            self.canvas_etat.itemconfig("texte_pos", state="hidden")
            self.canvas_etat.itemconfig("Supprimer_Historique", state="hidden")
            self.canvas_etat.itemconfig("texte_description", text=texte, justify="left", font=fonttexte,state="normal")
        
    def etat_activite_event(self,event):
        global Navigation
        Navigation+="Activité>"
        self.etat_activite()
    def etat_activite(self):
        self.etat_action="activite"
        self.canvas_etat.itemconfig("etat", fill="black")
        self.canvas_etat.itemconfig("activités", fill="#305389")
        self.canvas_etat.itemconfig("nav", state="normal")
        self.canvas_etat.itemconfig("texte_pos", state="hidden")
        
        if etat_historique_info_user[0]!=0:
            self.canvas_etat.itemconfig("nav", state="normal")
            if self.etat_historique_user_position==1:
                self.canvas_etat.itemconfig("precedent", state="hidden")
            if self.etat_historique_user_position==(etat_historique_info_user[0]):
                self.canvas_etat.itemconfig("suivant", state="hidden")
            texte=("CNE: {}\n"
                   "Parcours: {}\n"
                   "Connexion: {}\n"
                   "Déconnexion: {}\n"
                   "Activité: \n{}".format(etat_historique_info_user[self.etat_historique_user_position][0],
                              etat_historique_info_user[self.etat_historique_user_position][1],
                              etat_historique_info_user[self.etat_historique_user_position][2],
                              etat_historique_info_user[self.etat_historique_user_position][3],
                              etat_historique_info_user[self.etat_historique_user_position][4]))
            texte_pos=("{}/{}".format(self.etat_historique_user_position,etat_historique_info_user[0]))
            self.canvas_etat.itemconfig("texte_pos", state="normal",text=texte_pos)
            self.canvas_etat.itemconfig("canva_description", state="normal")
            self.canvas_etat.itemconfig("texte_description", state="hidden")
            self.textfield["state"]='normal'
            self.textfield.delete('1.0', END)
            self.textfield.insert(0.0, texte)
            self.textfield["state"]='disabled'
            self.canvas_etat.itemconfig("Supprimer_Historique", state="hidden")
            self.canvas_etat.itemconfig("Telecharger", state="normal")
        else:
            self.canvas_etat.itemconfig("nav", state="hidden")
            texte=("Aucun Historique")
            self.canvas_etat.itemconfig("texte_pos", state="hidden")
            self.canvas_etat.itemconfig("canva_description", state="hidden")
            self.canvas_etat.itemconfig("Supprimer_Historique", state="hidden")
            self.canvas_etat.itemconfig("texte_description", text=texte, justify="left", font=fonttexte, state="normal")
            
# Note: Make sure to replace `font_titre`, `fonttexte`, `bdd`, and `Systeme` with actual references or imports as they are not defined in the provided snippet.



""" _____________________________________________________Classe Admin____________________________________________________________________________"""

        
class Admin(Frame):
    def __init__(self,fenetre):
        Frame.__init__(self, fenetre, bg="#FFFFFF",width=1000,height=490)
        self.fenetre = fenetre
        global Navigation
        Navigation+="\nAdmin>"
        self.canvas_admin = Canvas(self, bg="#FFFFFF", width=1000, height=490)
        self.canvas_admin.place(x=-2, y=-2)
        self.canvas_admin.create_text(500, 50, text="PARAMETRES ADMINISTRATEURS", fill="#305389", font=font_titre, justify="center")
        self.canvas_admin.create_text(200, 130, text="OPTIONS :", fill="black", font=font_titre, justify="center")
        self.canvas_admin.create_line(340,130,340,500, width=1)
        self.admin_compte()
        
        self.canvas_admin.create_text(200, 180, text="Mon Compte", fill="#305389", activefill="#305389", font=fonttexte, justify="center", tag=("admin","Compte"))
        self.canvas_admin.tag_bind("Compte", "<Button-1>", self.admin_Compte)
        self.canvas_admin.create_text(200, 230, text="Ajouter un admin", fill="black", activefill="#305389", font=fonttexte, justify="center", tag=("admin","Ajouter"))
        self.canvas_admin.tag_bind("Ajouter", "<Button-1>", self.admin_ajouter)
        self.canvas_admin.create_text(200, 280, text="Supprimer un admin", fill="black", activefill="#305389", font=fonttexte, justify="center", tag=("admin","Supprimer"))
        self.canvas_admin.tag_bind("Supprimer", "<Button-1>", self.admin_supprimer)
        self.canvas_admin.create_text(200, 330, text="Ajouter des étudiants", fill="black", activefill="#305389", font=fonttexte, justify="center", tag=("admin","Ajouter_User"))
        self.canvas_admin.tag_bind("Ajouter_User", "<Button-1>", self.Ajouter_User)
        self.canvas_admin.create_text(200, 380, text="Supprimer des étudiants", fill="black", activefill="#305389", font=fonttexte, justify="center", tag=("admin","Supprimer_User"))
        self.canvas_admin.tag_bind("Supprimer_User", "<Button-1>", self.Supprimer_User)
        Nom_admin.set(Nom)
        Login_admin.set(Login)
        Password_admin.set(Password)
        Supprimer_Login_admin.set("")
        Supprimer_Password_admin.set("")
        Nom_New_admin.set("")
        Login_New_admin.set("")
        Password_New_admin.set("")
        Confirmer_New_admin.set("")
        Ajouter_User_chemin.set("")
        Supprimer_User_chemin.set("")
        
    def admin_Compte(self,event):
        self.admin_compte()
    def admin_compte(self):
        global Navigation
        Navigation+="Compte>"
        self.canvas_admin.itemconfig("canvas_ajouter", state="hidden")
        self.canvas_admin.itemconfig("canvas_supprimer", state="hidden")
        self.canvas_admin.itemconfig("canvas_Ajouter_User", state="hidden")
        self.canvas_admin.itemconfig("canvas_Supprimer_User", state="hidden")
        self.canvas_admin.itemconfig("admin", fill="black")
        self.canvas_admin.itemconfig("Compte", fill="#305389")
        
        canvas_compte = Canvas(self.canvas_admin, bg="#FFFFFF", width=550, height=350, bd=-2, highlightthickness=0)
        self.canvas_admin.create_window(650,300, window=canvas_compte, tag="canvas_compte")

        Cadre_Nom=Frame(canvas_compte,bg="#FFFFFF")
        Entry_Nom=Entry(Cadre_Nom,textvariable=Nom_admin,bg="#4C1B1B",font=monfont,width=35, fg="white", insertbackground="white")
        Entry_Nom.bind("<Return>",self.focus_Nom_admin)                        
        Entry_Nom.pack(ipady=4,side='left',padx=10)
        canvas_compte.create_text(60, 40, text="Nom", fill="#52251C", font=monfont, justify="center")
        Boutton_Nom=Button(Cadre_Nom,text="Modifier",bg="#305389",fg="white",width="12",font=monfont,command=lambda:self.admin_modifier_compte("nom"), cursor="hand2")
        Boutton_Nom.pack()               
        canvas_compte.create_window(250,70, window=Cadre_Nom)
   
        Cadre_Login=Frame(canvas_compte,bg="#FFFFFF")
        Entry_Login=Entry(Cadre_Login,textvariable=Login_admin,bg="#4C1B1B",font=monfont,width=35, fg="white", insertbackground="white")
        Entry_Login.pack(ipady=4,padx=10,side='left')
        Entry_Login.bind("<Return>",self.focus_Login_admin)  
        canvas_compte.create_text(70, 140, text="Login", fill="#52251C", font=monfont, justify="center")
        Boutton_Login=Button(Cadre_Login,text="Modifier",bg="#305389",fg="white",width="12",font=monfont,command=lambda:self.admin_modifier_compte("login"), cursor="hand2")
        Boutton_Login.pack() 
        canvas_compte.create_window(250, 170, window=Cadre_Login)
        
        Cadre_Password=Frame(canvas_compte,bg="#FFFFFF")
        Entry_Password=Entry(Cadre_Password,textvariable=Password_admin,show="*",bg="#4C1B1B",font=monfont,width=35, fg="white", insertbackground="white")
        Entry_Password.pack(ipady=4,padx=10,side='left')
        Entry_Password.bind("<Return>",self.focus_Password_admin) 
        canvas_compte.create_text(100, 240, text="Mot de Passe", fill="#52251C", font=monfont, justify="center")
        Boutton_Login=Button(Cadre_Password,text="Modifier",bg="#305389",fg="white",width="12",font=monfont,command=lambda:self.admin_modifier_compte("password"), cursor="hand2")
        Boutton_Login.pack()
        canvas_compte.create_window(250, 270, window=Cadre_Password)
    
    def focus_Nom_admin(self,event):
        self.admin_modifier_compte("nom")
        
    def focus_Login_admin(self,event):
        self.admin_modifier_compte("login")
        
    def focus_Password_admin(self,event):
        self.admin_modifier_compte("password")
        
    def admin_modifier_compte(self,Action):
        global Navigation
        Navigation+="Modifier>"
        if(Action=="nom" and Nom_admin.get()==Nom):
            error("Erreur","Entrer un nom différent")
        elif(Action=="login" and Login_admin.get()==Login):
            error("Erreur","Entrer un login différent")
        elif(Action=="password" and Password_admin.get()==Password):
            error("Erreur","Entrer un mot de passe différent")
        else:
            self.place_forget()
            identification("admin_"+Action,self.fenetre,self)
            
    def admin_ajouter(self,event):
        global Navigation
        Navigation+="Ajouter>"
        self.canvas_admin.itemconfig("canvas_compte", state="hidden")
        self.canvas_admin.itemconfig("canvas_supprimer", state="hidden")
        self.canvas_admin.itemconfig("canvas_Ajouter_User", state="hidden")
        self.canvas_admin.itemconfig("canvas_Supprimer_User", state="hidden")
        self.canvas_admin.itemconfig("admin", fill="black")
        self.canvas_admin.itemconfig("Ajouter", fill="#305389")
        canvas_ajouter = Canvas(self.canvas_admin, bg="#FFFFFF", width=550, height=360, bd=-2, highlightthickness=0)
        self.canvas_admin.create_window(650,300, window=canvas_ajouter, tag="canvas_ajouter")
        def focus_ajouter_nom_admin(event):
            Entry_Login.focus()
        def focus_ajouter_login_admin(event):
            Entry_Password.focus()
        def focus_ajouter_password_admin(event):
            Entry_Password_confirmation.focus()
        def focus_ajouter_confirmer_admin(event):
            self.Ajouter_Admin()
        
        Cadre_Nom=Frame(canvas_ajouter,bg="#FFFFFF")
        Entry_Nom=Entry(Cadre_Nom,textvariable=Nom_New_admin,bg="#4C1B1B",font=monfont,width=40, fg="white", insertbackground="white")
        Entry_Nom.pack(ipady=3)
        Entry_Nom.bind("<Return>",focus_ajouter_nom_admin)
        canvas_ajouter.create_text(75, 10, text="Nom", fill="#52251C", font=monfont, justify="center")              
        canvas_ajouter.create_window(220,40, window=Cadre_Nom)
        
        Cadre_Login=Frame(canvas_ajouter,bg="#FFFFFF")
        Entry_Login=Entry(Cadre_Login,textvariable=Login_New_admin,bg="#4C1B1B",font=monfont,width=40, fg="white", insertbackground="white")
        Entry_Login.pack(ipady=3)
        Entry_Login.bind("<Return>",focus_ajouter_login_admin)
        canvas_ajouter.create_text(80, 90, text="Login", fill="#52251C", font=monfont, justify="center")
        canvas_ajouter.create_window(220, 120, window=Cadre_Login)
        
        Cadre_Password=Frame(canvas_ajouter,bg="#FFFFFF")
        Entry_Password=Entry(Cadre_Password,textvariable=Password_New_admin,show="*",bg="#4C1B1B",font=monfont,width=40, fg="white", insertbackground="white")
        Entry_Password.pack(ipady=3)
        Entry_Password.bind("<Return>",focus_ajouter_password_admin)
        canvas_ajouter.create_text(110, 170, text="Mot de Passe", fill="#52251C", font=monfont, justify="center")
        canvas_ajouter.create_window(220, 200, window=Cadre_Password)
        
        Cadre_Password_confirmation=Frame(canvas_ajouter,bg="#FFFFFF")
        Entry_Password_confirmation=Entry(Cadre_Password_confirmation,textvariable=Confirmer_New_admin,show="*",bg="#4C1B1B",font=monfont,width=40, fg="white", insertbackground="white")
        Entry_Password_confirmation.pack(ipady=3)
        Entry_Password_confirmation.bind("<Return>",focus_ajouter_confirmer_admin)
        canvas_ajouter.create_text(95, 240, text="Confirmer", fill="#52251C", font=monfont, justify="center")
        canvas_ajouter.create_window(220, 270, window=Cadre_Password_confirmation)
        
        Boutton_ajouter=Button(canvas_ajouter,text="Ajouter",bg="#305389",fg="white",width=35,font=monfont,command=self.Ajouter_Admin, cursor="hand2")
        canvas_ajouter.create_window(220, 340, window=Boutton_ajouter)
    def Ajouter_Admin(self):
        if(Nom_New_admin.get()=="" or Login_New_admin.get()=="" or Password_New_admin.get()=="" or Confirmer_New_admin.get()==""):
            error("Erreur","Veuillez remplir tous les champs")
        elif(Password_New_admin.get()!=Confirmer_New_admin.get()):
            error("Erreur","Les mots de passes ne correspondent pas")
        else:
            self.place_forget()
            identification("Ajouter_admin",self.fenetre,self)
            
    def admin_supprimer(self,event):
        global Navigation
        Navigation+="Supprimer>"
        self.canvas_admin.itemconfig("canvas_compte", state="hidden")
        self.canvas_admin.itemconfig("canvas_ajouter", state="hidden")
        self.canvas_admin.itemconfig("canvas_Ajouter_User", state="hidden")
        self.canvas_admin.itemconfig("canvas_Supprimer_User", state="hidden")
        self.canvas_admin.itemconfig("admin", fill="black")
        self.canvas_admin.itemconfig("Supprimer", fill="#305389")
        canvas_supprimer = Canvas(self.canvas_admin, bg="#FFFFFF", width=550, height=360, bd=-2, highlightthickness=0)
        self.canvas_admin.create_window(650,300, window=canvas_supprimer, tag="canvas_supprimer")
        
        def Login_admin(event):
            Entry_Password.focus()
        def Password_admin(event):
            self.Supprimer_Admin()
        
        
        Cadre_Login=Frame(canvas_supprimer,bg="#FFFFFF")
        Entry_Login=Entry(Cadre_Login,textvariable=Supprimer_Login_admin,bg="#4C1B1B",font=monfont,width=40, fg="white", insertbackground="white")
        Entry_Login.pack(ipady=3)
        Entry_Login.bind("<Return>",Login_admin)
        canvas_supprimer.create_text(80, 60, text="Login", fill="#52251C", font=monfont, justify="center")
        canvas_supprimer.create_window(220, 90, window=Cadre_Login)
        
        Cadre_Password=Frame(canvas_supprimer,bg="#FFFFFF")
        Entry_Password=Entry(Cadre_Password,textvariable=Supprimer_Password_admin,show="*",bg="#4C1B1B",font=monfont,width=40, fg="white", insertbackground="white")
        Entry_Password.pack(ipady=3)
        Entry_Password.bind("<Return>",Password_admin)
        canvas_supprimer.create_text(110, 140, text="Mot de Passe", fill="#52251C", font=monfont, justify="center")
        canvas_supprimer.create_window(220, 170, window=Cadre_Password)
        
        Boutton_supprimer=Button(canvas_supprimer,text="Supprimer",bg="#305389",fg="white",width=35,font=monfont,command=self.Supprimer_Admin, cursor="hand2")
        canvas_supprimer.create_window(220, 250, window=Boutton_supprimer)
        
    def Supprimer_Admin(self):
        if(Supprimer_Login_admin.get()=="" or Supprimer_Password_admin.get()==""):
            error("Erreur","Veuillez remplir tous les champs")
        else:
            self.place_forget()
            identification("Supprimer",self.fenetre,self)
    def Ajouter_User(self,event):
        global Navigation
        Navigation+="Ajouter_User>"
        self.canvas_admin.itemconfig("canvas_compte", state="hidden")
        self.canvas_admin.itemconfig("canvas_supprimer", state="hidden")
        self.canvas_admin.itemconfig("canvas_ajouter", state="hidden")
        self.canvas_admin.itemconfig("canvas_Supprimer_User", state="hidden")
        self.canvas_admin.itemconfig("admin", fill="black")
        self.canvas_admin.itemconfig("Ajouter_User", fill="#305389")
        canvas_Ajouter_User = Canvas(self.canvas_admin, bg="#FFFFFF", width=570, height=360, bd=-2, highlightthickness=0)
        self.canvas_admin.create_window(630,300, window=canvas_Ajouter_User, tag="canvas_Ajouter_User")
        texte=("Pour ajouter de nouveaux étudiants à la base de données il faut importer un\n"
                       "fichier contenant les informations des etudiants du même parcours:\n\n"
                       "- au format .xlsx(fixhier excel)\n"
                       "- La première colonne contient les CNE avec pour entête 'CNE'\n"
                       "- La deuxième colonne contient les Noms avec pour entête 'Nom'\n"
                       "- La troisième colonne contient les dates de naissance avec pour entête 'DN'\n"
                       "  au format JJ/MM/AAAA\n"
                       "- La quatrième colonne contient les prénoms des pères avec pour entête 'Pere'\n"
                       "- Les 24 dernières colonnes sont les notes du DEUST avec pour en-têtes\n"
                       "  les codes des 24 modules du DEUST(ex:M135)")
        canvas_Ajouter_User.create_text(285, 100, text=texte, fill="#52251C", font=monfont, justify="left")
        canvas_Ajouter_User.create_text(250, 215, text=">>Télécharger un exemple", activefill="#52251C", fill="#305389", font=monfont, justify="left",tag="telecharger")
        canvas_Ajouter_User.tag_bind("telecharger", "<Button-1>", self.Telecharger_Exemple)
        Cadre_fichier=Frame(canvas_Ajouter_User,bg="#FFFFFF")
        Entry_fichier=Entry(Cadre_fichier,textvariable=Ajouter_User_chemin,bg="#4C1B1B",font=monfont,width=35, fg="white", insertbackground="white")
        Entry_fichier.pack(ipady=4,padx=10,side='left')
        Boutton_fichier=Button(Cadre_fichier,text="Choisir le Fichier",bg="#305389",fg="white",font=monfont,command=lambda:self.Ajouter_Etudiant("Chemin"), cursor="hand2")
        Boutton_fichier.pack()
        canvas_Ajouter_User.create_window(270, 250, window=Cadre_fichier)
        
        Cadre_Parcours=Frame(canvas_Ajouter_User,bg="#FFFFFF", width=300, height=80)
        canvas_Ajouter_User.create_text(140, 290, text="Parcours des étudiants:", fill="#52251C", font=monfont, justify="center")
        Parcours_mip = Radiobutton(Cadre_Parcours, bg="#FFFFFF", variable=Parcours_Nouvel_Etudiant, text="MIP", value="MIP", font=monfont,activeforeground="#305389", activebackground="#FFFFFF", cursor="hand2")
        Parcours_bcg = Radiobutton(Cadre_Parcours, bg="#FFFFFF", variable=Parcours_Nouvel_Etudiant, text="BCG", value="BCG", font=monfont,activeforeground="#305389", activebackground="#FFFFFF", cursor="hand2")
        Parcours_mip.place(x=2,y=2)
        Parcours_bcg.place(x=80,y=2)
        Parcours_Nouvel_Etudiant.set("MIP")
        canvas_Ajouter_User.create_window(380, 315, window=Cadre_Parcours)
        
        Boutton_ajouter=Button(canvas_Ajouter_User,text="AJOUTER",bg="#305389",fg="white",width=47,font=monfont,command=lambda:self.Ajouter_Etudiant("Ajouter"), cursor="hand2")
        canvas_Ajouter_User.create_window(275, 330, window=Boutton_ajouter)
        
        
    def Ajouter_Etudiant(self,option):
        if option=="Chemin":
            Ajouter_User_chemin.set(Ouvrir_Fichier(filetypes =[("Fichier excel","*.xlsx")]))
        elif option=="Ajouter":
            if(Ajouter_User_chemin.get()==""):
                error("Erreur","Veuillez choisir un fichier")
            else:
                if path.isfile(Ajouter_User_chemin.get()):
                    self.place_forget()
                    identification("Ajouter_Etudiant",self.fenetre,self)
                else:
                    error("Erreur","Chemin incorrect")
                    
    def Telecharger_Exemple(self,event):
        Chemin=Enregistrer(filetypes =[("Fichier excel","*.xlsx")])
        if Chemin!="":
            copyfile("C:\\New Folder (2)\\Application\fichier\\Exemple_Etudiant.xlsx",Chemin+".xlsx")
            info("Succès","Fichier téléchargé avec succès")
        
        
    def Supprimer_User(self,event):
        global Navigation
        Navigation+="Supprimer_User>"
        self.canvas_admin.itemconfig("canvas_compte", state="hidden")
        self.canvas_admin.itemconfig("canvas_supprimer", state="hidden")
        self.canvas_admin.itemconfig("canvas_ajouter", state="hidden")
        self.canvas_admin.itemconfig("canvas_Ajouter_User", state="hidden")
        self.canvas_admin.itemconfig("admin", fill="black")
        self.canvas_admin.itemconfig("Supprimer_User", fill="#305389")
        canvas_Supprimer_User = Canvas(self.canvas_admin, bg="#FFFFFF", width=570, height=360, bd=-2, highlightthickness=0)
        self.canvas_admin.create_window(650,300, window=canvas_Supprimer_User, tag="canvas_Supprimer_User")
        texte=("Pour supprimer des étudiants de la base de données,\n\n"
               "il faut importer un fichier au format .xlsx(fixhier excel)\n\n"
               "avec une colonne contenant les CNE des étudiants à\n\n"
               "supprimer ayant pour en tête 'CNE'")
        canvas_Supprimer_User.create_text(250, 100, text=texte, fill="#52251C", font=monfont, justify="left")
        Cadre_fichier=Frame(canvas_Supprimer_User,bg="#FFFFFF")
        Entry_fichier=Entry(Cadre_fichier,textvariable=Supprimer_User_chemin,bg="#4C1B1B",font=monfont,width=35, fg="white", insertbackground="white")
        Entry_fichier.pack(ipady=4,padx=10,side='left')
        Boutton_fichier=Button(Cadre_fichier,text="Choisir le Fichier",bg="#305389",fg="white",font=monfont,command=lambda:self.Supprimer_Etudiant("Chemin"), cursor="hand2")
        Boutton_fichier.pack()
        canvas_Supprimer_User.create_window(270, 230, window=Cadre_fichier)
        
        Boutton_ajouter=Button(canvas_Supprimer_User,text="SUPPRIMER",bg="#305389",fg="white",width=47,font=monfont,command=lambda:self.Supprimer_Etudiant("Supprimer"), cursor="hand2")
        canvas_Supprimer_User.create_window(275, 290, window=Boutton_ajouter)
        
    def Supprimer_Etudiant(self,Action):
        if Action=="Chemin":
            Supprimer_User_chemin.set(Ouvrir_Fichier(filetypes =[("Fichier excel","*.xlsx")]))
        elif Action=="Supprimer":
            if(Supprimer_User_chemin.get()==""):
                error("Erreur","Veuillez choisir un fichier")
            else:
                if path.isfile(Supprimer_User_chemin.get()):
                    self.place_forget()
                    identification("Supprimer_Etudiant",self.fenetre,self)
                else:
                    error("Erreur","Chemin incorrect")
        
""" _____________________________________________________Classe Identification____________________________________________________________________________"""

        
class identification(Frame):
    def __init__(self, action, fenetre, cadre):
        Frame.__init__(self, fenetre, bg="", width=1200, height=600)
        self.cadre = cadre
        self.fenetre = fenetre
        global Navigation, Action
        Navigation += "Identification>"
        Action = action

        # Creating the canvas with a left margin of 200 pixels
        self.canva = Canvas(self, width=650, height=265, highlightthickness=0, bg="#FFFFFF", bd=-2)
        self.canva.place(x=200, y=80)

        self.image = PhotoImage(file="Images/Your-paragraph-text-_1_.gif", master=fenetre)
        self.canva.create_image(0, 0, anchor=NW, image=self.image)
        self.texte_titre = self.canva.create_text(310, 25, text="IDENTIFICATION", fill="white", font=("Helvetica", 16), justify="center")
        self.texte_password = self.canva.create_text(275, 80, text="Entrez votre mot de passe", fill="white", font=("Helvetica", 12))
        self.cadre1 = Frame(self.canva)

        self.mot_de_passe = StringVar()
        self.entry_password = Entry(self.cadre1, bg="black", fg="white", show="*", insertbackground="white", font=("Helvetica", 12), width=35, textvariable=self.mot_de_passe)
        self.entry_password.bind('<Return>', self.valider)
        self.entry_password.pack(ipady="6")
        self.canva.create_window(320, 110, window=self.cadre1)
        self.boutton_entrer = Button(self.canva, text="ENTRER", bg="#386094", fg="white", font=("Helvetica", 12), width=30, height=1, command=self.valider_password, cursor="hand2")
        self.canva.create_window(320, 180, window=self.boutton_entrer)
        self.boutton_annuler = Button(self.canva, text="ANNULER", bg="#386094", fg="white", font=("Helvetica", 12), width=30, height=1, command=self.annuler_password, cursor="hand2")
        self.canva.create_window(320, 220, window=self.boutton_annuler)
        self.place(x=0, y=80)

    def valider(self, event):
        self.valider_password()

    def valider_password(self):
        global Navigation, Info_train, Importance_Filiere_Figure, figure, Login, Password, Nom, etat_general_info
        Navigation += "Valider_password>"
        if self.mot_de_passe.get() == Password:
            self.mot_de_passe.set("")
            if messagebox.askokcancel("Confirmation", "Voulez vous vraiment continuer ?"):
                if Action == "Algo":
                    bdd.Etat_MAJ("Algo", Algo_utilise)
                    messagebox.showinfo("Succès", "Algorithme changé avec succès")
                    Info_train = bdd.Information_Train()
                    figure = bdd.Info_Train()
                    etat_general_info = bdd.Etat_General()
                elif Action == "Train":
                    Chemin = Ouvrir_Fichier(filetypes=[("Fichier excel", "*.xlsx")])
                    bdd.Traitement_DATA(Chemin, train_filiere)
                    figure = bdd.Info_Train()
                    Info_train = bdd.Information_Train()
                    self.cadre.Info_Train(train_filiere)
                elif Action == "admin_nom":
                    retour = bdd.Modification_data_admin("Nom", Nom_admin.get(), Login, Password)
                    if retour:
                        Nom = Nom_admin.get()
                    else:
                        Nom_admin.set(Nom)
                elif Action == "admin_login":
                    retour = bdd.Modification_data_admin("Login", Login_admin.get(), Login, Password)
                    if retour:
                        Login = Login_admin.get()
                    else:
                        Login_admin.set(Login)
                elif Action == "admin_password":
                    retour = bdd.Modification_data_admin("Password", Password_admin.get(), Login, Password)
                    if retour:
                        Password = Password_admin.get()
                    else:
                        Password_admin.set(Password)
                elif Action == "Ajouter_admin":
                    bdd.Ajouter_data_admin(Nom_New_admin.get(), Login_New_admin.get(), Password_New_admin.get())
                    Nom_New_admin.set("")
                    Login_New_admin.set("")
                    Password_New_admin.set("")
                    Confirmer_New_admin.set("")
                elif Action == "Supprimer":
                    bdd.Supprimer_data_admin(Supprimer_Login_admin.get(), Supprimer_Password_admin.get())
                    if Supprimer_Login_admin.get() == Login and Supprimer_Password_admin.get() == Password:
                        self.fenetre.place_forget()
                    else:
                        Supprimer_Login_admin.set("")
                        Supprimer_Password_admin.set("")
                elif Action == "Ajouter_Etudiant":
                    bdd.Ajouter_Etudiant(Ajouter_User_chemin.get(), Parcours_Nouvel_Etudiant.get())
                elif Action == "Supprimer_Etudiant":
                    bdd.Supprimer_Etudiant(Supprimer_User_chemin.get())
                elif Action == "Supprimer_Filiere":
                    bdd.Modifier_Filiere("Supprimer_Filiere", Filieres, self.cadre.Changer, "")
                    Info_train = bdd.Information_Train()
                    Importance_Filiere_Figure = bdd.Filiere()
                    figure = bdd.Info_Train()
                    self.cadre = Filiere(self.fenetre)
                elif Action == "Ajouter_Filiere":
                    bdd.Modifier_Filiere("Ajouter_Filiere", Nom_Nouvelle_Filiere.get(), Parcours_Nouvelle_Filiere.get(), Description_Nouvelle_Filiere)
                    Info_train = bdd.Information_Train()
                    Importance_Filiere_Figure = bdd.Filiere()
                    figure = bdd.Info_Train()
                    self.cadre = Filiere(self.fenetre)
                self.cadre.place(x=0, y=80)
            else:
                messagebox.showinfo("", "Modification annulée")
                self.annuler_password()
            self.place_forget()
        else:
            self.mot_de_passe.set("")
            self.canva.create_text(320, 145, text="Mot de passe incorrecte", fill="red", font=("Helvetica", 12))

    def annuler_password(self):
        global Navigation
        Navigation += "Annuler_password>"
        self.mot_de_passe.set("")
        self.place_forget()
        if Action == "admin_nom" or Action == "admin_login" or Action == "admin_password":
            Nom_admin.set(Nom)
            Login_admin.set(Login)
            Password_admin.set(Password)
        elif Action == "Ajouter_admin":
            Nom_New_admin.set("")
            Login_New_admin.set("")
            Password_New_admin.set("")
            Confirmer_New_admin.set("")
        elif Action == "Supprimer":
            Supprimer_Login_admin.set("")
            Supprimer_Password_admin.set("")
        elif Action == "Ajouter_Etudiant":
            Ajouter_User_chemin.set("")
        elif Action == "Ajouter_Filiere":
            Nom_Nouvelle_Filiere.set("")
        self.cadre.place(x=0, y=80)

"""
fenetre=Tk()
x = int(fenetre.winfo_screenwidth()/2-500)
y = int(fenetre.winfo_screenheight()/2-300)-30
fenetre.geometry("1000x600+{}+{}".format(x,y))
fenetre.title("AIDE A L'ORIENTATION")
fenetre.resizable(0,0)
arnaud = ["a","a","a"]
bdd.admin("a","a")
interface_admin(fenetre, arnaud)
fenetre.mainloop()"""