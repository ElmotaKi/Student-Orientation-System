"""
Created 2024

@author:Abde el moutaki
"""
from tkinter import *
from tkinter import font
import DataBase as bdd
import User
import ADMIN as Admin
from tkinter.messagebox import showerror as error
import traceback
import sys

class Interface:
    def __init__(self):
        self.n = 0
        self.m = False
        self.fenetre = Tk()
        self.x = int(self.fenetre.winfo_screenwidth()/2-500)
        self.y = int(self.fenetre.winfo_screenheight()/2-300)-30
        self.fenetre.geometry("1000x600+{}+{}".format(self.x,self.y))
        self.fenetre.title("AIDE A L'ORIENTATION")
        self.font_titre = font.Font(family='Helvetica', size=25, weight='bold')
        self.font_texte = font.Font(family='Helvetica', size=10, weight='bold')
        
        self.fenetre.resizable(0,0)

        self.can = Canvas(self.fenetre, width=1000, height=600)
        self.can.pack()
        self.im = PhotoImage(file="Images/Notes-_1_.gif", master=self.fenetre)
        self.can.create_image(0, 0, anchor=NW, image=self.im)
        self.select_admin = PhotoImage(file="Images/admin.png", master=self.fenetre)
        self.select_user = PhotoImage(file="Images/user.png", master=self.fenetre)
        
        self.texte_titre = self.can.create_text(500, 80, text="AIDE A\nL'ORIENTATION", fill="white", font=self.font_titre, justify="center")
        self.texte_etudiant = self.can.create_text(420, 180, text="ETUDIANT", fill="white", font=self.font_texte, tag="mode")
        self.texte_admin = self.can.create_text(580, 180, text="ADMIN", fill="white", font=self.font_texte, tag="mode")
        self.mode_select = self.can.create_image(460, 160, anchor=NW, image=self.select_user, tag="mode")
        self.can.tag_bind("mode", "<Button-1>", self.choisir_mode)
        
        self.texte_cne = self.can.create_text(500, 220, text="CNE", fill="white", font=self.font_texte, tag="user")
        self.cadre1 = Frame(self.fenetre, bg="black")
        self.cne=StringVar()
        self.entry_cne = Entry(self.cadre1, bg="white", fg="black", insertbackground="black", font=self.font_texte, width=35,textvariable=self.cne)
        self.entry_cne.bind('<Return>',self.valider_cne)
        self.entry_cne.pack(ipady="6")
        self.cadre_cne = self.can.create_window(500, 250, window=self.cadre1, tag="user")
        
        self.texte_DN = self.can.create_text(500, 290, text="Date de naissance (JJ/MM/AAAA)", fill="white", font=self.font_texte, tag="user")
        self.cadre_DN = Frame(self.fenetre, bg="black")
        self.DN=StringVar()
        self.entry_DN = Entry(self.cadre_DN, bg="white", fg="black", insertbackground="black", font=self.font_texte, width=35,textvariable=self.DN)
        self.entry_DN.bind('<Return>',self.valider_DN)
        self.entry_DN.pack(ipady="6")
        self.cadre_DN = self.can.create_window(500, 320, window=self.cadre_DN, tag="user")
        
        self.texte_PERE = self.can.create_text(500, 360, text="Mot de passe", fill="white", font=self.font_texte, tag="user")
        self.cadre_PERE = Frame(self.fenetre, bg="black")
        self.PERE=StringVar()
        self.entry_PERE = Entry(self.cadre_PERE, bg="white", fg="black", insertbackground="black", font=self.font_texte, width=35,textvariable=self.PERE)
        self.entry_PERE.bind('<Return>',self.valider_PERE)
        self.entry_PERE.pack(ipady="6")
        self.cadre_PERE = self.can.create_window(500, 390, window=self.cadre_PERE, tag="user")
        
        self.texte_login = self.can.create_text(500, 220, text="Login", fill="white", font=self.font_texte, state="hidden", tag="admin")
        self.cadre2 = Frame(self.fenetre, bg="black")
        self.login=StringVar()
        self.entry_login = Entry(self.cadre2, bg="white", fg="black", textvariable=self.login,insertbackground="black", font=self.font_texte, width=35)
        self.entry_login.bind('<Return>',self.valider_login)
        self.entry_login.pack(ipady="6")
        self.cadre_login = self.can.create_window(500, 250, window=self.cadre2, state="hidden", tag="admin")
        
        self.texte_password = self.can.create_text(500, 290, text="Mot de passe", fill="white", font=self.font_texte, state="hidden", tag="admin")
        self.cadre3 = Frame(self.fenetre, bg="black")
        self.password=StringVar()
        self.entry_password = Entry(self.cadre3, show="*", textvariable=self.password,bg="white", fg="black", insertbackground="black", font=self.font_texte, width=35)
        self.entry_password.bind('<Return>',self.valider_password)
        self.entry_password.pack(ipady="6")
        self.cadre_password = self.can.create_window(500, 320, window=self.cadre3, state="hidden", tag="admin")
        
        self.eye1 = PhotoImage(file="Images/eye1.png", master=self.fenetre)
        self.eye2 = PhotoImage(file="Images/eye2.png", master=self.fenetre)
        self.can.create_image(660, 310, anchor=NW, image=self.eye1, tag=("eye","admin"), state="hidden")
        self.can.tag_bind("eye", "<Button-1>", self.afficher_password)
        
        self.boutton_entrer = Button(self.fenetre, text="ENTRER", bg="#386094", fg="white", font=self.font_texte, width=30, height=2,command=self.Valider)
        self.can.create_window(500, 450, window=self.boutton_entrer)
        self.texte_pied = self.can.create_text(500, 580, text="FST Errachidia - Année universitaire 2023-2024", fill="white", font=self.font_texte)
        
        self.Erreur = self.can.create_text(500, 510, text="", fill="red", font=self.font_texte)
        self.fenetre.mainloop()
        
    def afficher_password(self, event):
        if self.password.get()!="":
            if self.m:
                self.m=False
                self.can.itemconfig("eye", image=self.eye1)
                self.entry_password["show"]="*"
            elif not self.m:
                self.m=True
                self.can.itemconfig("eye", image=self.eye2)
                self.entry_password["show"]=""
    def choisir_mode(self, event):
        if self.n==0:
            self.n=1
            self.can.itemconfig(self.mode_select, image=self.select_admin)
            self.can.itemconfig("user", state="hidden")
            self.can.itemconfig("admin", state="normal")
            self.can.itemconfig("eye", image=self.eye1)
            self.entry_password["show"]="*"
            self.can.itemconfig(self.Erreur, text="")
            self.DN.set("")
            self.PERE.set("")
            self.cne.set("")
        elif self.n==1:
            self.n=0
            self.can.itemconfig(self.mode_select, image=self.select_user)
            self.can.itemconfig("admin", state="hidden")
            self.can.itemconfig("user", state="normal")
            self.can.itemconfig(self.Erreur, text="")
            self.login.set("")
            self.password.set("")
    def valider_cne(self,event):
       self.entry_DN.focus()
    def valider_DN(self,event):
        self.entry_PERE.focus()
    def valider_PERE(self,event):
        self.Valider()
        
    def valider_login(self,event):
        self.entry_password.focus()
    def valider_password(self,event):
        self.Valider()
    def Valider(self):
        if self.n==0:
            if (self.DN.get()!="" and self.PERE.get()!="" and self.cne.get()!=""):
                self.Identification_user()
            else:
                self.can.itemconfig(self.Erreur, text="Veuillez remplir tous les champs")
        else:
            if (self.login.get()!="" and self.password.get()!=""):
                self.Identification_admin()
            else:
                self.can.itemconfig(self.Erreur, text="Veuillez remplir tous les champs")
            
        
    def Identification_user(self):
        CNE=self.cne.get()
        DN=self.DN.get()
        Pere=self.PERE.get()
        self.DN.set("")
        self.PERE.set("")
        self.cne.set("")
        self.fenetre.focus()
        erreur=False
        
        try:
            CNE=int(CNE)
        except ValueError:
            erreur=True
        if erreur:
            self.can.itemconfig(self.Erreur, text="Veuillez saisir un CNE valide")
        else:  
            if len(DN)!=10:
                erreur=True
            elif (DN[2]!="/" or DN[5]!="/"):
                erreur=True
            else:
                try:
                    int(DN[0]+DN[1])
                    int(DN[3]+DN[4])
                    int(DN[6]+DN[7]+DN[8]+DN[9])
                except ValueError:
                    erreur=True
            if erreur:
                self.can.itemconfig(self.Erreur, text="Format de la date incorrect. (Ex:22/05/1997)")
            else:
                res = bdd.interrogation_bdd(CNE,DN,Pere)
                if(res is not False):
                    try:
                        self.can.itemconfig(self.Erreur, text="")
                        User.interface_user(self.fenetre,CNE,res)
                        bdd.Etat_MAJ("User",True)
                    except Exception as e:
                        traceback.print_exc(file=sys.stdout)
                        error("Erreur","Désolé!\nLe programme a rencontré un problème")
                        self.fenetre.destroy()
                        print(e)
                else:
                    bdd.Etat_MAJ("User",False)
                    self.can.itemconfig(self.Erreur, text="Informations éronées")
            
            
    def Identification_admin(self):
        login=self.login.get()
        password=self.password.get()
        res = bdd.admin(login,password)
        self.login.set("")
        self.password.set("")
        self.fenetre.focus()
        if(res is False):
            bdd.Etat_MAJ("Admin",False)
            self.can.itemconfig(self.Erreur, text="Login et/ou Mot de Passe Incorrecte(s)")
        else:
            try:
                bdd.Etat_MAJ("Admin",True)
                self.can.itemconfig(self.Erreur, text="")
                Admin.interface_admin(self.fenetre, res)
            except Exception as e:
                traceback.print_exc(file=sys.stdout)
                error("Erreur","Désolé!\nLe programme a rencontré un problème")
                self.fenetre.destroy()
                print(e)
            
try:
    Fenetre = Interface()
except Exception as e:
    traceback.print_exc(file=sys.stdout)
    error("Erreur","Désolé!\nLe programme a rencontré un problème")
    #exit()
