"""
Created 2024

@author:Abde el moutaki
"""
import pandas as pd
import numpy as np
from matplotlib.figure import Figure
import Modele
from tkinter.messagebox import askokcancel as ok, showinfo as info,showerror as error,showwarning as warning
from tkinter.filedialog import askopenfilename as Ouvrir_Fichier
import sqlite3
import traceback
from os import remove
import sys


try:
    Connexion = sqlite3.Connection("C:\\New Folder (2)\\Application\\Base.db")
    Curseur = Connexion.cursor()
    
    Modules_MIP = ('C121','C132','I111','I132','I143','I144','L111','L122','L133','M111','M112','M123',
     'M124','M135','M136','M147','M148','P111','P112','P123','P124','P135','P146','P147')
    
    Modules_BCG = ('B211','B222','B233','B244','B245','C211','C222','C233','C234','C245','G211','G222',
     'G233','G244','I241','L211','L222','L243','M211','M222','M233','P211','P222','P233')
    
    Curseur.execute("select * from Etat_General")
    Etat_general=Curseur.fetchone()
    lis=[]
    for i in range(5):
        lis.append(Etat_general[i])
    Etat_general=lis

    Notes = [0,0]
    Parcours_Etudiant = 0
    
    modele_utilise = Etat_general[4]
except Exception:
    traceback.print_exc(file=sys.stdout)
    error("Erreur","Impossible de se connecter à la base de données")
finally:
    Connexion.close()
    
def interrogation_bdd(cne,DN,Pere):
    try:
        Connexion = sqlite3.Connection("C:\\New Folder (2)\\Application\\Base.db")
        Curseur = Connexion.cursor()
        global Notes,Parcours_Etudiant
        cne=int(cne)
        User=(cne,DN,Pere.upper())
        Curseur.execute("""select Note from Notes  natural join Etudiant where 
                    (Etudiant.CNE=? and DN=? and Pere=?)""",User)
        notes=Curseur.fetchall()
        if(len(notes) != 24):
            return False
        else:
            Curseur.execute("select Parcours,Nom from Etudiant where CNE=?",[cne])
            inf = Curseur.fetchone()
            Parcours_Etudiant = inf[0]
            Nom = inf[1]
            n=[]
            for i in notes:
                n.append(i[0])
            Notes[0]=n
            if Parcours_Etudiant=="MIP":
                Notes[1]=Modules_MIP
            else:
                Notes[1]=Modules_BCG
            return Nom
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        error("Erreur","Impossible de se connecter à la base de données")
    finally:
        Connexion.close()
def admin(l,p):
    try:
        Connexion = sqlite3.Connection("C:\\New Folder (2)\\Application\\Base.db")
        Curseur = Connexion.cursor()
        Ad=(l,p)
        Curseur.execute("select * from Admin where(Login=? and Mot_de_passe=?)",Ad)
        Administrateur=Curseur.fetchone()
        if(Administrateur is None or len(Administrateur)!=3):
            return False
        else:
            return Administrateur
    except Exception:
        traceback.print_exc(file=sys.stdout)
        error("Erreur","Impossible de se connecter à la base de données")
    finally:
        Connexion.close()
        
def recap():
    dic = {}
    Notes_Etudiant={}
    if Parcours_Etudiant == 'MIP':
        ms1 = (Notes[0][9] + Notes[0][10])/2
        ms2 = (Notes[0][11] + Notes[0][12])/2
        ms3 = (Notes[0][13] + Notes[0][14])/2
        ms4 = (Notes[0][15] + Notes[0][16])/2
        m =round( (ms1+ms2+ms3+ms4)/4,2)
        inter=[9,10,11,12,13,14,15,16]
        for i in inter:
            Notes_Etudiant[Notes[1][i]]=Notes[0][i]
       
        fig = Figure(figsize=(8, 6), dpi=65)
        ax = fig.add_subplot(111,facecolor='#FFFFFF')
        ax.plot(["S1", "S2", "S3", "S4"], [ms1, ms2, ms3, ms4], color='#386094', linewidth=3)
        ax.set_ylabel('Moyenne')
        ax.set_xlabel('Semestre')
        ax.set_title('Mathématiques')
        fig.patch.set_facecolor('#FFFFFF')
        t={}
        t["moy"]=m
        t["fig"]=fig
        t["Notes"]=Notes_Etudiant
        dic["Mathématiques"]=t
        
        ms1 = Notes[0][2]
        ms3= Notes[0][3]
        ms4= (Notes[0][4] + Notes[0][5])/2
        m = round((ms1+ms3+ms4)/3,2)
        
        Notes_Etudiant={}
        inter=[2,3,4,5]
        for i in inter:
            Notes_Etudiant[Notes[1][i]]=Notes[0][i]
        fig = Figure(figsize=(8, 6), dpi=65)
        ax = fig.add_subplot(111,facecolor='#FFFFFF')
        fig.patch.set_facecolor('#FFFFFF')
        ax.plot(["S1", "S3", "S4"], [ms1, ms3, ms4], color='#386094', linewidth=3)
        ax.set_ylabel('Moyenne')
        ax.set_xlabel('Semestre')
        ax.set_title('Informatique')
        t={}
        t["moy"]=m
        t["fig"]=fig
        t["Notes"]=Notes_Etudiant
        dic["Informatique"]=t
        
        
        ms1 = (Notes[0][17] + Notes[0][18])/2
        ms2= (Notes[0][19] + Notes[0][20])/2
        ms3= Notes[0][21]
        ms4= (Notes[0][22] + Notes[0][23])/2
        m = round((ms1+ms2+ms3+ms4)/4,2)
        
        Notes_Etudiant={}
        inter=[17,18,19,20,21,22,23]
        for i in inter:
            Notes_Etudiant[Notes[1][i]]=Notes[0][i]
        fig = Figure(figsize=(8, 6), dpi=65)
        ax = fig.add_subplot(111,facecolor='#FFFFFF')
        fig.patch.set_facecolor('#FFFFFF')
        ax.plot(["S1", "S2","S3", "S4"], [ms1,ms2, ms3, ms4], color='#386094', linewidth=3)
        ax.set_ylabel('Moyenne')
        ax.set_xlabel('Semestre')
        ax.set_title('Physique')
        t={}
        t["moy"]=m
        t["fig"]=fig
        t["Notes"]=Notes_Etudiant
        dic["Physique"]=t
        
         
        ms1 = Notes[0][6]
        ms2= (Notes[0][0] + Notes[0][7])/2
        ms3= (Notes[0][8]+Notes[0][1])/2
        m = round((ms1+ms2+ms3)/3,2)
        
        Notes_Etudiant={}
        inter=[0,1,6,7,8]
        for i in inter:
            Notes_Etudiant[Notes[1][i]]=Notes[0][i]
        fig = Figure(figsize=(8, 6), dpi=65)
        ax = fig.add_subplot(111,facecolor='#FFFFFF')
        fig.patch.set_facecolor('#FFFFFF')
        ax.plot(["S1", "S2","S3", "S4"], [ms1,ms2, ms3, ms4], color='#386094', linewidth=3)
        ax.set_ylabel('Moyenne')
        ax.set_xlabel('Semestre')
        ax.set_title('Autres')
        t={}
        t["moy"]=m
        t["fig"]=fig
        t["Notes"]=Notes_Etudiant
        dic["Autres"]=t
        
        
    elif Parcours_Etudiant == 'BCG':
        ms1 = Notes[0][0]
        ms2 = Notes[0][1]
        ms3 = Notes[0][2]
        ms4 = (Notes[0][3] + Notes[0][4])/2
        m =round( (ms1+ms2+ms3+ms4)/4,2)
        
        Notes_Etudiant={}
        inter=[0,1,2,3,4]
        for i in inter:
            Notes_Etudiant[Notes[1][i]]=Notes[0][i]
        fig = Figure(figsize=(8, 6), dpi=65)
        ax = fig.add_subplot(111,facecolor='#FFFFFF')
        ax.plot(["S1", "S2", "S3", "S4"], [ms1, ms2, ms3, ms4], color='#386094', linewidth=3)
        ax.set_ylabel('Moyenne')
        ax.set_xlabel('Semestre')
        ax.set_title('Biologie')
        fig.patch.set_facecolor('#FFFFFF')
        t={}
        t["moy"]=m
        t["fig"]=fig
        t["Notes"]=Notes_Etudiant
        dic["Biologie"]=t
        
        
        ms1 = Notes[0][5]
        ms2= Notes[0][6]
        ms3= (Notes[0][7] + Notes[0][8])/2
        ms4= Notes[0][9]
        m = round((ms1+ms2+ms3+ms4)/4,2)
        
        Notes_Etudiant={}
        inter=[5,6,7,8,9]
        for i in inter:
            Notes_Etudiant[Notes[1][i]]=Notes[0][i]
        fig = Figure(figsize=(8, 6), dpi=65)
        ax = fig.add_subplot(111,facecolor='#FFFFFF')
        fig.patch.set_facecolor('#FFFFFF')
        ax.plot(["S1", "S2", "S3", "S4"], [ms1, ms2, ms3, ms4], color='#386094', linewidth=3)
        ax.set_ylabel('Moyenne')
        ax.set_xlabel('Semestre')
        ax.set_title('Chimie')
        t={}
        t["moy"]=m
        t["fig"]=fig
        t["Notes"]=Notes_Etudiant
        dic["Chimie"]=t
        
        
        ms1 = Notes[0][10]
        ms2= Notes[0][11]
        ms3= Notes[0][12]
        ms4= Notes[0][13]
        m = round((ms1+ms2+ms3+ms4)/4,2)
        
        Notes_Etudiant={}
        inter=[10,11,12,13]
        for i in inter:
            Notes_Etudiant[Notes[1][i]]=Notes[0][i]
        fig = Figure(figsize=(8, 6), dpi=65)
        ax = fig.add_subplot(111,facecolor='#FFFFFF')
        fig.patch.set_facecolor('#FFFFFF')
        ax.plot(["S1", "S2","S3", "S4"], [ms1,ms2, ms3, ms4], color='#386094', linewidth=3)
        ax.set_ylabel('Moyenne')
        ax.set_xlabel('Semestre')
        ax.set_title('Géologie')
        t={}
        t["moy"]=m
        t["fig"]=fig
        t["Notes"]=Notes_Etudiant
        dic["Géologie"]=t
        
        ms1 = (Notes[0][15]+Notes[0][18]+Notes[0][21])/3
        ms2= (Notes[0][16]+Notes[0][19]+Notes[0][22])/3
        ms3= (Notes[0][20]+Notes[0][23])/2
        ms4= (Notes[0][14]+Notes[0][17])/2
        m = round((ms1+ms2+ms3+ms4)/4,2)
        
        Notes_Etudiant={}
        inter=[14,15,16,17,18,19,20,21,22,23]
        for i in inter:
            Notes_Etudiant[Notes[1][i]]=Notes[0][i]
        fig = Figure(figsize=(8, 6), dpi=65)
        ax = fig.add_subplot(111,facecolor='#FFFFFF')
        fig.patch.set_facecolor('#FFFFFF')
        ax.plot(["S1", "S2","S3", "S4"], [ms1,ms2, ms3, ms4], color='#386094', linewidth=3)
        ax.set_ylabel('Moyenne')
        ax.set_xlabel('Semestre')
        ax.set_title('Autres')
        t={}
        t["moy"]=m
        t["fig"]=fig
        t["Notes"]=Notes_Etudiant
        dic["Autres"]=t
    Somme=0
    for i in Notes[0]:
        Somme+=i
    dic["Moyenne_DEUST"]=round(Somme/24,2)
    return dic

def Information_Train():
    Modele.MAJ_Modeles()
    return Modele.Info[modele_utilise]

def Info_Train():
    figure = {}
    figure_parcours = {}
    for i in Modele.MIP[modele_utilise]:
        y1 = Modele.MIP[modele_utilise][i].predictions
        y2 = Modele.MIP[modele_utilise][i].test_target
        y1_s5=[]
        y1_s6=[]
        for j in y1:
            y1_s5.append(j[0])
            y1_s6.append(j[1])
        y2_s5=[]
        y2_s6=[]
        for j in y2:
            y2_s5.append(j[0])
            y2_s6.append(j[1])
        
        fig = Figure(figsize=(9, 6.5), dpi=65)
        ax = fig.add_subplot(2,1,1,facecolor='#FFFFFF')      
        ax.plot(y1_s5, color='#386094', label="Moyenne prédite")
        ax.plot(y2_s5, color='red', label="Moyenne obtenue")
        ax.set_ylabel('Moyenne')
        ax.set_title("Semestre 5: "+i)
        ax.grid(True)
        ax.legend()
        
        ax = fig.add_subplot(2,1,2,facecolor='#FFFFFF')      
        ax.plot(y1_s6, color='#386094', label="Moyenne prédite")
        ax.plot(y2_s6, color='red', label="Moyenne obtenue")
        ax.set_ylabel('Moyenne')
        ax.set_xlabel('Etudiant')
        ax.set_title("Semestre 6: "+i)
        ax.grid(True)
        ax.legend()
        fig.patch.set_facecolor('#FFFFFF')
        figure[i] = fig
    figure_parcours["MIP"] = figure
    
    figure = {} 
    for i in Modele.BCG[modele_utilise]:
        y1 = Modele.BCG[modele_utilise][i].predictions
        y2 = Modele.BCG[modele_utilise][i].test_target
        y1_s5=[]
        y1_s6=[]
        for j in y1:
            y1_s5.append(j[0])
            y1_s6.append(j[1])
        y2_s5=[]
        y2_s6=[]
        for j in y2:
            y2_s5.append(j[0])
            y2_s6.append(j[1])
        
        fig = Figure(figsize=(9, 6.5), dpi=65)
        ax = fig.add_subplot(2,1,1,facecolor='#FFFFFF')      
        ax.plot(y1_s5, color='#386094', label="Moyenne prédite")
        ax.plot(y2_s5, color='red', label="Moyenne obtenue")
        ax.set_ylabel('Moyenne')
        ax.set_title("Semestre 5: "+i)
        ax.grid(True)
        ax.legend()
        
        ax = fig.add_subplot(2,1,2,facecolor='#FFFFFF')      
        ax.plot(y1_s6, color='#386094', label="Moyenne prédite")
        ax.plot(y2_s6, color='red', label="Moyenne obtenue")
        ax.set_ylabel('Moyenne')
        ax.set_xlabel('Etudiant')
        ax.set_title("Semestre 6: "+i)
        ax.grid(True)
        ax.legend()
        fig.patch.set_facecolor('#FFFFFF')
        figure[i] = fig
    figure_parcours["BCG"] = figure 
        
    return figure_parcours
                                
                                
def predict():
    Couleur=["#384054","#305389","#9AC5F6","#7A96E3","#008FB3"]
    Predictions={}
    if Parcours_Etudiant == "MIP":
        for i in Modele.MIP[modele_utilise]:
            Predictions[i]=np.array(Modele.MIP[modele_utilise][i].prediction(Notes[0]))
    elif Parcours_Etudiant == "BCG":
        for i in Modele.BCG[modele_utilise]:
            Predictions[i]=np.array(Modele.BCG[modele_utilise][i].prediction(Notes[0]))
    
    
    Figures = {}
    fig = Figure(figsize=(5, 7), dpi=65)
    ax = fig.add_subplot(111,facecolor='#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')
    a=1
    
    for i in Predictions:
        ax.bar(a, np.mean(Predictions[i]), color=Couleur[a-1], width=1, edgecolor='white', linewidth = 2,label=i)
        a+=1
    ax.xaxis.set_ticklabels("")
    ax.set_ylabel('Prédictions')
    ax.set_xlabel('Spécialités')
    ax.set_title('Histogramme des prédictions')
    ax.legend()
    ax.set_ylim(0,20)
    Figures["General"]=fig
    
    for i in Predictions:
        fig = Figure(figsize=(5, 7), dpi=60)
        ax = fig.add_subplot(111,facecolor='#FFFFFF')
        fig.patch.set_facecolor('#FFFFFF')
        ax.bar(1, Predictions[i][0], width=1, color="#384054", edgecolor='white', linewidth = 2)
        ax.bar(2, Predictions[i][1], width=1, color="#305389", edgecolor='white', linewidth = 2)
        ax.set_ylabel('Prédictions')
        ax.set_xlabel('Semestres')
        ax.set_title(i)
        ax.set_ylim(0,20)
        ax.xaxis.set_ticklabels(('','',' ','Semestre 5','','',' ','Semestre 6'), fontsize=11)
        Figures[i]=fig
    
    data = {}
    for i in Predictions:
        data[i]=Predictions[i]
    data["fig"]=Figures
    return data
    
    
def Erreur_Precision():
    if Parcours_Etudiant=="MIP":
        return Modele.Erreur_precision_MIP[modele_utilise]
    elif Parcours_Etudiant=="BCG":
        return Modele.Erreur_precision_BCG[modele_utilise]
    
        
def Traitement_DATA(Chemin,Filiere):
    try:
        Connexion = sqlite3.Connection("C:\\New Folder (2)\\Application\\Base.db")
        Curseur = Connexion.cursor()
        Erreur=False
        try:
            data=pd.read_excel(Chemin)
            taille=data.iloc[0,:]
            taille=np.size(np.array(taille))
            if(taille!=26):
                error("Erreur","Colonnes manquantes")
            else:
                for i in data:
                    for j in data[i]:
                        if j==0:
                            Erreur=True
                            break
                        else:
                            try:
                                int(j)
                            except ValueError:
                                Erreur=True
                                break
                if(Erreur==True):
                    error("Erreur","Valeurs nulles ou incorrectes dans les données")
                else:
                    Info_Filiere = Modele.Chemin_Filiere(Filiere)
                    New_Data=pd.concat([pd.read_excel(Info_Filiere[0]),data],ignore_index=True)
                    if Info_Filiere[1]=="MIP":
                        Info_train_old = Modele.MIP[modele_utilise][Filiere].Info_Train()
                    elif Info_Filiere[1]=="BCG":
                        Info_train_old = Modele.BCG[modele_utilise][Filiere].Info_Train()
            
                    Erreur = New_Data.isnull().any().any()
                    if(Erreur==True):
                        error("Erreur","Noms des colonnes invalides")
                    else:
                        Modele_temp=Modele.modele(New_Data,modele_utilise)
                        Info_train=Modele_temp.Info_Train()
                        
                        Texte=("Nombre de données d'entrainement\n:" 
                               "     -Nouvelle: {}\n"
                               "      -Ancienne: {}\n\n"
                            "Nombre de données de test:\n"
                             "     -Nouvelle: {}\n"
                             "      -Ancienne: {}\n\n"
                            "Erreur Maximale: \n"
                            "     -Nouvelle: {}\n"
                            "      -Ancienne: {}\n\n"
                            "Erreur Minimale: \n"
                            "     -Nouvelle: {}\n"
                            "      -Ancienne: {}\n\n"
                            "Erreur Moyenne: \n"
                            "     -Nouvelle: {}\n"
                            "      -Ancienne: {}\n\n"
                            "Précision: \n"
                            "     -Nouvelle: {}%\n"
                            "      -Ancienne: {}%\n\n\n\n"
                            "Sauvegarder les modifications?".format(Info_train["Train"],Info_train_old["Train"],
                                                               Info_train["Test"],Info_train_old["Test"],
                                                               Info_train["Max"],Info_train_old["Max"],
                                                               Info_train["Min"],Info_train_old["Min"],
                                                               Info_train["Moy"],Info_train_old["Moy"],
                                                               Info_train["Prec"],Info_train_old["Prec"],))
                        if ok("Confirmation",Texte):
                            Curseur.execute("select Chemin from Filiere where Nom=?",[Filiere])
                            New_Data.to_excel(Curseur.fetchone()[0])
                            if Info_Filiere[1]=="MIP":
                                Modele.MIP[modele_utilise][Filiere]=Modele_temp
                            elif Info_Filiere[1]=="BCG":
                                Modele.BCG[modele_utilise][Filiere]=Modele_temp
                            info("Succès","Entrainer avec succès")
                        else:
                            info("Annuler","Annuler avec succès")
        except FileNotFoundError:
            info("Annuler","Annuler avec succès")
    except Exception:
        traceback.print_exc(file=sys.stdout)
        error("Erreur","Impossible de se connecter à la base de données")
    finally:
        Connexion.close()
def Modification_data_admin(Action,Valeur,Login,Password):
    try:
        Connexion = sqlite3.Connection("C:\\New Folder (2)\\Application\\Base.db")
        Curseur = Connexion.cursor()
        Adm=(Valeur,Login,Password)
        if(Action=="Nom"):
            Curseur.execute("update Admin set Nom=? where (Login=? and Mot_de_passe=?)",Adm)
            info("Succès","Votre nouveau nom est :{}".format(Valeur))
        elif(Action=="Password"):
            Curseur.execute("update Admin set Mot_de_passe=? where (Login=? and Mot_de_passe=?)",Adm)
            info("Succès","Votre nouveau mot de passe est :{}".format(Valeur))
        elif(Action=="Login"):
            Curseur.execute("select * from Admin where Login=?",[Valeur])
            Admin=Curseur.fetchone()
            if Admin is None:
                Curseur.execute("update Admin set Login=? where (Login=? and Mot_de_passe=?)",Adm)
                info("Succès","Votre nouveau login est :{}".format(Valeur))
            else:
                error("Erreur","Login déjà utilisé")
                return False
        Connexion.commit()
        return True
    except Exception:
        traceback.print_exc(file=sys.stdout)
        error("Erreur","Impossible de se connecter à la base de données")
        return False
    finally:
        Connexion.close()
def Ajouter_data_admin(Nom,Login,Password):
    try:
        Connexion = sqlite3.Connection("C:\\New Folder (2)\\Application\\Base.db")
        Curseur = Connexion.cursor()
        Curseur.execute("select * from Admin where Login=?",[Login])
        Admin=Curseur.fetchone()
        if Admin is None:
            Adm=[Login,Password,Nom]
            Curseur.execute("insert into Admin values(?,?,?)",Adm)
            texte=("Administrateur ajouté avec succès\n\n Informations:\n"
                   "Nom: {}\n Login: {}\n Mot de Passe: {}".format(Nom,Login,Password))
            info("Succès",texte)
            Connexion.commit()
        else:
            error("Erreur","Login déjà utilisé")
    except Exception:
        traceback.print_exc(file=sys.stdout)
        error("Erreur","Impossible de se connecter à la base de données")
    finally:
        Connexion.close()

def Supprimer_data_admin(Login,Password):
    try:
        Connexion = sqlite3.Connection("C:\\New Folder (2)\\Application\\Base.db")
        Curseur = Connexion.cursor()
        Adm=[Login,Password]
        Curseur.execute("select * from Admin where (Login=? and Mot_de_passe=?)",Adm)
        Admin=Curseur.fetchone()
        if Admin is not None:
            Curseur.execute("delete from Etat_Admin where (Login=? and Mot_de_passe=?)",Adm)
            Curseur.execute("delete from Admin where (Login=? and Mot_de_passe=?)",Adm)
            Connexion.commit()
            info("Succès","Admin supprimé avec succès")
        else:
            error("Erreur","Login et Mot de Passe inexistants")
    except Exception:
        traceback.print_exc(file=sys.stdout)
        error("Erreur","Impossible de se connecter à la base de données")
    finally:
        Connexion.close()
def Etat_MAJ(Action,Option):
    try:
        Connexion = sqlite3.Connection("C:\\New Folder (2)\\Application\\Base.db")
        Curseur = Connexion.cursor()
        global modele_utilise
        if Action=="Admin":
            if Option:
                Etat_general[3]+=1
            else:
                Etat_general[1]+=1
        elif Action=="User":
            if Option:
                Etat_general[2]+=1
            else:
                Etat_general[0]+=1
        elif Action=="Algo":
            modele_utilise = Option
            Etat_general[4]=Option
        
        Curseur.execute("update Etat_General set T_user=?, T_admin=?,C_user=?,C_admin=?,Algo=?",Etat_general)
        Connexion.commit()
    except Exception:
        traceback.print_exc(file=sys.stdout)
        error("Erreur","Impossible de se connecter à la base de données")
    finally:
        Connexion.close()
def Etat_detaille_MAJ(Action,Info):
    try:
        Connexion = sqlite3.Connection("C:\\New Folder (2)\\Application\\Base.db")
        Curseur = Connexion.cursor()
        if Action=="User":
            Curseur.execute("""insert into Etat_User(CNE,Parcours,Connexion,Deconnexion,Navigation)
                            values(?,?,?,?,?)""",Info)
        elif Action=="Admin":
            Curseur.execute("""insert into Etat_Admin(Login,Mot_de_passe,Connexion,Deconnexion,Navigation)
                            values(?,?,?,?,?)""",Info)
        Connexion.commit() 
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        error("Erreur","Impossible de se connecter à la base de données")
    finally:
        Connexion.close()
def Etat_General():
    try:
        Connexion = sqlite3.Connection("C:\\New Folder (2)\\Application\\Base.db")
        Curseur = Connexion.cursor()
        t = []
        Curseur.execute("select count(*) from Etudiant")
        t.append(Curseur.fetchone()[0])
        Curseur.execute("select count(*) from Admin")
        t.append(Curseur.fetchone()[0])
        for i in range(5):
            t.append(Etat_general[i])
        return t
    except Exception:
        traceback.print_exc(file=sys.stdout)
        error("Erreur","Impossible de se connecter à la base de données")
    finally:
        Connexion.close()
def Etat_historique(Login,Password,Action):
    try:
        Connexion = sqlite3.Connection("C:\\New Folder (2)\\Application\\Base.db")
        Curseur = Connexion.cursor()
        if(Action=="Admin"):
            Adm=[Login,Password]
            Curseur.execute("select Connexion,Deconnexion,Navigation from Etat_Admin where (Login=? and Mot_de_passe=?)",Adm)
            data = Curseur.fetchall()
        elif Action=="User":
            Curseur.execute("select CNE,Parcours,Connexion,Deconnexion,Navigation from Etat_User")
            data = Curseur.fetchall()
        if data is not None:
            t=[len(data)]
            for i in range(1,len(data)+1):
                t.append(data[len(data)-i])
        else:
            t=[0,""]
        return t
    except Exception:
        traceback.print_exc(file=sys.stdout)
        error("Erreur","Impossible de se connecter à la base de données")
    finally:
        Connexion.close()
def Supprimer_Historique_Admin(Action,Login,Password):
    try:
        Connexion = sqlite3.Connection("C:\\New Folder (2)\\Application\\Base.db")
        Curseur = Connexion.cursor()
        Adm=[Login,Password]
        if Action=="*":
            Curseur.execute("delete from Etat_Admin where (Login=? and Mot_de_passe=?)",Adm)
            info("Succès","Historique Supprimé avec succès")
        else:
            Adm.append(Action)
            Curseur.execute("delete from Etat_Admin where (Login=? and Mot_de_passe=? and Connexion=?)",Adm)
            info("Succès","Historique courant supprimé avec succès")
        Connexion.commit()
    except Exception:
        traceback.print_exc(file=sys.stdout)
        error("Erreur","Impossible de se connecter à la base de données")
    finally:
        Connexion.close()    
        
        
        
def Ajouter_Etudiant(Chemin,Parcours):
    try:
        Connexion = sqlite3.Connection("C:\\New Folder (2)\\Application\\Base.db")
        Curseur = Connexion.cursor()
        Erreur=False
        data=pd.read_excel(Chemin)
        taille=data.iloc[0,:]
        taille=np.size(np.array(taille))
        if(taille!=28):
            error("Erreur","Colonnes manquantes")
        else:
            cols=["CNE","Nom","DN","Pere"]
            if Parcours=="MIP":
                for p in Modules_MIP:
                    cols.append(p)
            elif Parcours=="BCG":
                for p in Modules_BCG:
                    cols.append(p)
            data_temp=[[x for x in range(28)]]
            data_temp=pd.DataFrame(data_temp,columns=cols)
            data_temp=data_temp.drop([0])
            new=pd.concat([data_temp,data],ignore_index=True)
            Erreur = new.isnull().any().any()
            if(Erreur==True):
                error("Erreur","Noms des colonnes invalides et/ou Valeurs non définies dans les données")
            else:
                Existant=[]
                Probleme=[]
                for i in range(len(new)):
                    try:
                        tab=[int(new["CNE"][i]),new["DN"][i].strftime('%d/%m/%Y'),str(new["Pere"][i]),Parcours,str(new["Nom"][i])]
                        for z in new.columns:
                                if z not in ["CNE","DN","Pere","Nom"]:
                                    float(new[z][i])
                    except Exception:
                        Probleme.append(i)
                for i in range(len(new)):
                    if i not in Probleme:
                        try:
                            tab=[int(new["CNE"][i]),new["DN"][i].strftime('%d/%m/%Y'),str(new["Pere"][i]),Parcours,str(new["Nom"][i])]
                            Curseur.execute("insert into Etudiant values(?,?,?,?,?)",tab)
                            Connexion.commit()
                            for z in new.columns:
                                if z not in ["CNE","DN","Pere","Nom"]:
                                    tabb=[str(z),tab[0],float(new[z][i])]
                                    Curseur.execute("insert into Notes values(?,?,?)",tabb)
                                    Connexion.commit()
                        except sqlite3.IntegrityError:
                            Existant.append(tab[0])
                if (len(Existant)==0 and len(Probleme)==0):
                    info("","Etudiants ajoutés avec succès")
                else:
                    texte=""
                    if len(Existant)!=0:
                        texte="Les CNE suivants sont déjà dans la base de données:\n\n"
                        if len(Existant)==1:
                            texte="Le CNE suivant est déjà dans la base de données:\n\n"
                        for w in Existant:
                            texte+=("{}\t".format(w))
                    if len(Probleme)!=0:
                        texte+="\n\n\n" if len(texte)!=0 else ""
                        texte+="Problèmes rencontrés aux lignes suivantes:\n\n"
                        for w in Probleme:
                            texte+=("{}\t".format(w))
                    warning("",texte)
    except Exception:
        traceback.print_exc(file=sys.stdout)
        error("Erreur","Impossible de se connecter à la base de données")
    finally:
        Connexion.close()
    
def Supprimer_Etudiant(Chemin):
    try:
        Connexion = sqlite3.Connection("C:\\New Folder (2)\\Application\\Base.db")
        Curseur = Connexion.cursor()
        data=pd.read_excel(Chemin)
        taille=data.iloc[0,:]
        taille=np.size(np.array(taille))
        if(taille!=1):
            error("Erreur","Le fichier doit contenir une colonne")
        else:
            if(data.isnull().any().any()):
                error("Erreur","Valeurs non définies dans les données")
            else:
                try:
                    k=0
                    for k in range(len(data)):
                        int(data["CNE"][k])
                except ValueError:
                    error("Erreur","Chaine de caractère dans les données: ligne {}".format(k))
                else:
                    for i in range(len(data)):
                        tab=[int(data["CNE"][i])]
                        Curseur.execute("delete from Notes where CNE=?",tab)
                        Connexion.commit()
                        Curseur.execute("delete from Etudiant where CNE=?",tab)
                        Connexion.commit()
                    info("Succès","Etudiants supprimés avec succès")
    except Exception:
        traceback.print_exc(file=sys.stdout)
        error("Erreur","Impossible de se connecter à la base de données")
    finally:
        Connexion.close()
    
    
    
    
    
# def Filiere():
    # data = {}
    # dic = {}
    # if (modele_utilise=="cnn" or modele_utilise=="AD"):
    #     titre="Importances des Modules: "
    #     y="Importances"
    # elif modele_utilise=="mlp":
    #     titre="Coefficients directeurs des Modules: "
    #     y="Coefficients"
    # for i in Modele.MIP[modele_utilise]:
    #     variables =Modele.MIP[modele_utilise][i].var_importances
    #     print(modele_utilise)
    #     fig = Figure(figsize=(10, 6), dpi=65)
    #     ax = fig.add_subplot(111,facecolor='#FFFFFF')
    #     fig.patch.set_facecolor('#FFFFFF')
    #     for j in range(len(variables)):
    #         ax.bar(j+1, variables[j], color='#384054', width=1, edgecolor='white', linewidth = 2)
    #     ax.set_ylabel(y)
    #     ax.set_xlabel('Modules')
    #     texte=titre+i
    #     ax.set_title(texte)
    #     ax.xaxis.set_ticks(range(1,len(variables)+1))
    #     # ax.xaxis.set_ticks(1,24)

    #     # ax.xaxis.set_ticklabels(Modules_MIP, fontsize=11,rotation=90)
    #     # dic[i]=fig
    # data["MIP"]=dic
    # dic = {}
    # for i in Modele.BCG[modele_utilise]:
    #     variables =Modele.BCG[modele_utilise][i].var_importances
    #     fig = Figure(figsize=(10, 6), dpi=65)
    #     ax = fig.add_subplot(111,facecolor='#FFFFFF')
    #     fig.patch.set_facecolor('#FFFFFF')
    #     for j in range(len(variables)):
    #         ax.bar(j+1, variables[j], color='#384054', width=1, edgecolor='white', linewidth = 2)
    #     ax.set_ylabel(y)
    #     ax.set_xlabel('Modules')
    #     texte=titre+i
    #     ax.set_title(texte)
    #     # ax.xaxis.set_ticks(range(1,len(Modules_BCG)+1))
    #     # # ax.xaxis.set_ticks(1,24)
    #     # ax.xaxis.set_ticklabels(Modules_BCG, fontsize=11,rotation=90)
    #     dic[i]=fig
    # data["BCG"] = dic
    
    # return data 
  
def Modifier_Filiere(Action,Filiere,Parcours,Description):
    try:
        Connexion = sqlite3.Connection("C:\\New Folder (2)\\Application\\Base.db")
        Curseur = Connexion.cursor()
        if(Action=="Supprimer_Filiere"):
            if Parcours=="MIP":
                Taille=len(Modele.Filieres_MIP)
            else:
                Taille=len(Modele.Filieres_BCG)
            if Taille>1:
                Curseur.execute("select Chemin from Filiere where Nom=?",[Filiere])
                Chemin_Supprimer=Curseur.fetchone()[0]
                remove(Chemin_Supprimer)
                Curseur.execute("delete from Filiere where Nom=?",[Filiere])
                Connexion.commit()
                
                Modele.MAJ_Modeles()
                info(Filiere,"Supprimer avec Succès")
            else:
                error(Filiere,"Impossible de supprimer toutes  les filières")
        elif(Action=="Ajouter_Filiere"):
            Filiere=Filiere.upper()
            Curseur.execute("select * from Filiere where Nom=?",[Filiere])
            var=Curseur.fetchone()
            if(var is not None):
                error(Filiere,"La filière existe déjà")
            else:
                 texte=("Pour créer une nouvelle filière, il faut l'entrainer auparavant\n"
                       "Pour ce faire, il faut importer un fichier contenant les notes des etudiants:\n\n"
                       "  - au format .xlsx(fixhier excel)\n\n"
                       "  - Les 24 premieres colonnes sont les notes du DEUST\n"
                       "    avec pour en-têtes les codes des 24 modules\n    du DEUST(ex:M135)\n\n"
                       "  - Les deux dernières colonnes sont les moyennes générales\n"
                       "   des semestres 5 et 6 avec pour en-tête 'Moyenne_S5' et 'Moyenne_S6'.\n\n\n"
                       "Voulez-vous continuer?")
                 if ok(Filiere,texte):
                    Chemin=Ouvrir_Fichier(filetypes =[("Fichier excel","*.xlsx")])
                    Erreur=False
                    try:
                        data=pd.read_excel(Chemin)
                        taille=data.iloc[0,:]
                        taille=np.size(np.array(taille))
                        if(taille!=26):
                            error("Erreur","Colonnes manquantes")
                        else:
                            for i in data:
                                for j in data[i]:
                                    if j==0:
                                        Erreur=True
                                        break
                                    else:
                                        try:
                                            int(j)
                                        except ValueError:
                                            Erreur=True
                                            break
                            if(Erreur==True):
                                error("Erreur","Valeurs nulles ou incorrectes dans les données")
                            else:
                                Erreur = data.isnull().any().any()
                                if(Erreur==True):
                                    error("Erreur","Valeurs non définies dans les données")
                                else:
                                    cols=[]
                                    if Parcours=="MIP":
                                        for p in Modules_MIP:
                                            cols.append(p)
                                    elif Parcours=="BCG":
                                        for p in Modules_BCG:
                                            cols.append(p)
                                    cols.append("Moyenne_S5")
                                    cols.append("Moyenne_S6")
                                    data_temp=[[x for x in range(26)]]
                                    data_temp=pd.DataFrame(data_temp,columns=cols)
                                    data_temp=data_temp.drop([0])
                                    new=pd.concat([data_temp,data],ignore_index=True)
                                    Erreur = new.isnull().any().any()
                                    if(Erreur==True):
                                        error("Erreur","Noms des colonnes invalides")
                                    else:
                                        Modele_temp=Modele.modele(data,modele_utilise)
                                        Info_train=Modele_temp.Info_Train()
                                        
                                        Texte=("Nombre de données d'entrainement : {} \n\n"
                                            "Nombre de données de test : {} \n\n"
                                            "Erreur Maximale : {} \n\n"
                                            "Erreur Minimale: {} \n\n"
                                            "Erreur Moyenne: {} \n\n"
                                            "Précision: {} \n\n"
                                            "Sauvegarder la filière : {}?".format(Info_train["Train"],
                                                                               Info_train["Test"],
                                                                               Info_train["Max"],
                                                                               Info_train["Min"],
                                                                               Info_train["Moy"],
                                                                               Info_train["Prec"],
                                                                               Filiere))
                                        if ok("Confirmation",Texte):
                                            chem="fichier/"+Filiere+".xlsx"
                                            data.to_excel(chem)
                                            Inf=(Filiere,Parcours,chem,Description)
                                            Curseur.execute("insert into Filiere values(?,?,?,?)",Inf)
                                            Modele.MAJ_Modeles()
                                            info("Succès",Filiere+" ajoutée avec succès")
                                            Connexion.commit()
                                        else:
                                            info("Annuler","Annuler avec succès")
                    except FileNotFoundError:
                        info("Annuler","Annuler avec succès")
    except Exception:
        traceback.print_exc(file=sys.stdout)
        error("Erreur","Impossible de se connecter à la base de données")
    finally:
        Connexion.close()






