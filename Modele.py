"""
Created 2024

@author:Abde el moutaki
"""

#Importer les librairies
import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv1D, MaxPooling1D
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.optimizers import Adam
import sqlite3
import traceback
import sys
from tkinter.messagebox import showerror as error

class modele:
    def __init__(self, dataset, algo):
        self.features = dataset.iloc[:, 0:24]
        self.features = np.array(self.features)
        self.target = dataset.iloc[:,24:26]
        self.target = np.array(self.target)
        self.train_features, self.test_features, self.train_target, self.test_target = train_test_split(self.features, self.target, test_size=0.2, random_state=42)
        if algo=="cnn":
            self.mod = Sequential([
            Conv1D(64, 3, activation='relu', input_shape=(self.train_features.shape[1], 1)),
            MaxPooling1D(2),
            Conv1D(128, 3, activation='relu'),
            MaxPooling1D(2),
            Flatten(),
            Dense(256, activation='relu'),
            Dense(128, activation='relu'),
            Dense(64, activation='relu'),
            Dense(2)  # Deux neurones pour les deux cibles, avec softmax pour la classification
        ])
            self.mod.compile(optimizer='adam', loss='mse', metrics=['accuracy'])
            self.mod.fit(self.train_features, self.train_target , epochs=1)

          
            self.var_importances = [] 

        elif algo=="mlp":
            self.mod = Sequential([
                Dense(64, activation='relu', input_shape=(self.train_features.shape[1], )),
                Dense(128, activation='relu'),
                Dense(64, activation='relu'),
                Dense(32, activation='relu'),
                Dense(2)  # Deux neurones pour les deux cibles, pas besoin de softmax ici car la perte spécifiée sera utilisée
              ])
            self.mod.compile(optimizer='adam', loss='mse', metrics=['accuracy'])
            self.mod.fit(self.train_features, self.train_target , epochs=1 )
   
            self.var_importances = [] 
           
        elif algo=="AD":
            self.mod = DecisionTreeRegressor()
            self.var_importances = [] 
        self.mod.fit(self.train_features, self.train_target )
        self.predictions=self.mod.predict(self.test_features)
        
    

        
    def prediction(self,data):
        
        data_list = [data]

# Convertir la liste en tableau numpy
        data_np = np.array(data_list)
        return self.mod.predict(data_np)[0]
  

    def Erreur_Precision(self):
        error =np.mean( abs(self.predictions-self.test_target))
        mape=100*(error/self.test_target)
        accuracy = 100-np.mean(mape)
        Systeme = {}
        Systeme["error"]=error
        Systeme["precision"]=accuracy
        return Systeme
    def Info_Train(self):
        Info={}
        Info["Train"]=int(np.size(self.train_target)/2)
        Info["Test"]=int(np.size(self.test_target)/2)
        Info["Max"]=np.max( abs(self.predictions-self.test_target))
        Info["Min"]=np.min( abs(self.predictions-self.test_target))
        Info["Moy"]=self.Erreur_Precision()["error"]
        Info["Prec"]=self.Erreur_Precision()["precision"]
        return Info
 
Filieres=0    
Filieres_MIP=0
Filieres_BCG=0    
MIP=0
BCG=0
Erreur_precision_MIP = 0
Erreur_precision_BCG = 0
Info = 0
def MAJ_Modeles():
    global Filieres,MIP,BCG,Erreur_precision_MIP,Erreur_precision_BCG,Info,Filieres_MIP,Filieres_BCG
    Erreur_precision_MIP = {}
    Erreur_precision_BCG = {}
    Info = {}
    try:
        Connexion = sqlite3.Connection("C:\\New Folder (2)\\Application\\Base.db")
        Curseur = Connexion.cursor()
        Curseur.execute("select * from Filiere")
        Filieres=Curseur.fetchall()
        Curseur.execute("select * from Filiere where Parcours='MIP'")
        Filieres_MIP=Curseur.fetchall()
        Curseur.execute("select * from Filiere where Parcours='BCG'")
        Filieres_BCG=Curseur.fetchall()
        MIP1={}
        for j in ("cnn","mlp","AD"):
            mip={}
            for i in range(len(Filieres_MIP)):
                dataset= pd.read_excel(Filieres_MIP[i][2])
                model = modele(dataset,j)
                mip[Filieres_MIP[i][0]]=model
            MIP1[j]=mip
        MIP=MIP1
        BCG1={}
        for j in ("cnn","mlp","AD"):
            bcg={}
            for i in range(len(Filieres_BCG)):
                dataset= pd.read_excel(Filieres_BCG[i][2])
                model = modele(dataset,j)
                bcg[Filieres_BCG[i][0]]=model
            BCG1[j]=bcg
        BCG=BCG1
        
        for j in MIP:
            Erreur=0
            Precision=0
            dic={}
            for i in MIP[j]:
                Erreur+=MIP[j][i].Erreur_Precision()["error"]
                Precision+=MIP[j][i].Erreur_Precision()["precision"]
            dic["error"]=Erreur/len(MIP[j])
            dic["precision"]=Precision/len(MIP[j])
            Erreur_precision_MIP[j]=dic
            
        for j in BCG:
            Erreur=0
            Precision=0
            dic={}
            for i in BCG[j]:
                Erreur+=BCG[j][i].Erreur_Precision()["error"]
                Precision+=BCG[j][i].Erreur_Precision()["precision"]
            dic["error"]=Erreur/len(BCG[j])
            dic["precision"]=Precision/len(BCG[j])
            Erreur_precision_BCG[j]=dic
        
        for j in MIP:
            info = {}
            Info1={}
            for i in MIP[j]:
                info[i]=MIP[j][i].Info_Train()
            Info1["MIP"] = info
            info = {}
            for i in BCG[j]:
                info[i]=BCG[j][i].Info_Train()
            Info1["BCG"] = info
            Info[j]=Info1
    except Exception:
        traceback.print_exc(file=sys.stdout)
        error("Erreur","Impossible de se connecter à la base de données")
    finally:
        Connexion.close()
        

MAJ_Modeles()  #Appel de la fonction afin de l'exécuter    
def Chemin_Filiere(Nom_Filiere):
    Fil =Filieres
    res=[]
    for i in range(len(Fil)):
        if Fil[i][0]==Nom_Filiere:
            res.append(Fil[i][2])
            res.append(Fil[i][1])
            return res