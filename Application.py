from Pages import *

#Fonctionnement des boutons
def changement_page(Actuelle, Suivante):
    Actuelle.cache()
    Suivante.affiche()

def appel_envois(Creation, Log):
    if (Creation.envois()) :
        changement_page(Creation, Log)

def Log_In(Log, Accueil_Ad, Accueil_Cl) : #modifié pour accueil client
    verif = Log.verifications()
    if verif == "admin":
        changement_page(Log, Accueil_Ad)
    elif verif == "client":
        changement_page(Log, Accueil_Cl)

def Log_Out(Log, Actuelle):
    global IdPersonne
    IdPersonne = 0
    changement_page(Actuelle, Log)

def changement_vers_Pres_circuit(Accueil_Cl, Pres_Cir):
    
    if Accueil_Cl.verification() :
        Accueil_Cl.cache()
        Pres_Cir.affiche()

def changement_vers_Pres_etape(Pres_Cir, Pres_Et): #à corriger pour ne pas caché si Id =0
    Id = Pres_Cir.cache()
    if Id != 0:
        Pres_Et.affiche()
    else:
        Pres_Cir.affiche()



#Main
def Application():
    ecran = tk.Tk()

    #design
    ecran.resizable(width=0, height=0)#on met ces deux lignes et magie ça marche
    ecran.geometry('1500x500')
    ecran.resizable(height=0,width= 0 )
    ecran['bg']='#F6CEF5'

   # ecran.geometry=("300x5000")
   # ecran.resizable(width=0, height=0)#on met ces deux lignes et magie ça marche

    #initialisation des pages
   #initialisation des pages
    Login_page = Login()
    Creation_Client = create_compte()
    Accueil_Ad = Accueil_Admin()
    Accueil_Cl = Accueil_Client() #attention elle n'a aucun boutons pour l'instant
    Liste_Ad = Liste_Admin()
    Liste_Li = Liste_Lieux()
    Liste_Et = Liste_Etape()
    Liste_Cl = Liste_Client()
    Creation_Client_Admin = create_compte()
    Liste_Ci = Liste_Circuit()
    Pres_Cir = Presentation_Circuit()
    Pres_Et = Presentation_Etape()
    Res_Pa = Reservation_passager()
    Pres_Re = Presentation_Reservation()
    Pres_Pa = Presentation_Passager()
    
    
    #initialisation des boutons d'interaction entre les pages
    #butons Logins
    login = tk.Button(master=Login_page.buton, text="Connexion", command= lambda: Log_In(Login_page, Accueil_Ad, Accueil_Cl))
    login.pack()
    #design
    Font_mot = ("Helvetica", 16, "bold")
    login.configure(font = Font_mot)

    compte = tk.Button(master=Login_page.buton, text="créer un compte", command= lambda: changement_page(Login_page, Creation_Client))
    compte.pack()
    #design
    Font_mot = ("Helvetica", 16, "bold")
    compte.configure(font = Font_mot)


    #butons Création de compte Client
    cree = tk.Button(master=Creation_Client.buton, text="créer", command= lambda: appel_envois(Creation_Client, Login_page))
    cree.pack()
    #design
    Font_mot = ("Helvetica", 10, "bold")
    cree.configure(font = Font_mot)

    retour_cc = tk.Button(master=Creation_Client.titre, text="Retour", command= lambda: changement_page(Creation_Client, Login_page))
    retour_cc.pack()
    #design
    Font_mot = ("Helvetica", 10, "bold")
    retour_cc.configure(font = Font_mot)
    
    #butons Accueil Admin
    clients_a_a = tk.Button(master=Accueil_Ad.buton, text="Listes Clients", command= lambda: changement_page(Accueil_Ad, Liste_Cl))
    clients_a_a.pack() 
    #design
    Font_mot = ("Helvetica", 13, "bold")
    clients_a_a.configure(font = Font_mot)

    administrateurs_a_a  = tk.Button(master=Accueil_Ad.buton, text="Listes Administrateurs", command= lambda: changement_page(Accueil_Ad, Liste_Ad))
    administrateurs_a_a.pack()
    #design
    Font_mot = ("Helvetica", 13, "bold")
    administrateurs_a_a.configure(font = Font_mot)

    circuits_a_a = tk.Button(master=Accueil_Ad.buton, text="Listes Circuits", command= lambda: changement_page(Accueil_Ad, Liste_Ci))
    circuits_a_a.pack()
    #design
    Font_mot = ("Helvetica", 13, "bold")
    circuits_a_a.configure(font = Font_mot)

    etapes_a_a = tk.Button(master=Accueil_Ad.buton, text="Listes Etapes", command= lambda: changement_page(Accueil_Ad, Liste_Et))
    etapes_a_a.pack()
    #design
    Font_mot = ("Helvetica", 13, "bold")
    etapes_a_a.configure(font = Font_mot)

    lieux_a_a = tk.Button(master=Accueil_Ad.buton, text="Listes Lieux", command= lambda: changement_page(Accueil_Ad, Liste_Li))
    lieux_a_a.pack()
    #design
    Font_mot = ("Helvetica", 13, "bold")
    lieux_a_a.configure(font = Font_mot)

    accueil_admin_logout = tk.Button(master=Accueil_Ad.buton, text="log out", command= lambda: Log_Out(Login_page, Accueil_Ad))
    accueil_admin_logout.pack()
    #design
    Font_mot = ("Helvetica", 10, "bold")
    accueil_admin_logout.configure(font = Font_mot)

    #butons Liste Admin
    retour_la = tk.Button(master=Liste_Ad.entete, text="Retour à la liste des pages", command= lambda: changement_page(Liste_Ad, Accueil_Ad))
    retour_la.pack()
    #design
    Font_mot = ("Helvetica", 10, "bold")
    retour_la.configure(font = Font_mot)
   

    #butons Liste Lieux
    retour_ll = tk.Button(master=Liste_Li.entete, text="Retour à la liste des pages", command= lambda: changement_page(Liste_Li, Accueil_Ad))
    retour_ll.pack()
    #design
    Font_mot = ("Helvetica", 10, "bold")
    retour_ll.configure(font = Font_mot)

    #butons Liste Etape
    retour_le = tk.Button(master=Liste_Et.entete, text="Retour à la liste des pages", command= lambda: changement_page(Liste_Et, Accueil_Ad))
    retour_le.pack()
    #design
    Font_mot = ("Helvetica", 10, "bold")
    retour_le.configure(font = Font_mot)
    
    #butons Liste Client
    retour_lc = tk.Button(master=Liste_Cl.entete, text="Retour à la liste des pages", command= lambda: changement_page(Liste_Cl, Accueil_Ad))
    retour_lc.pack()
    #design
    Font_mot = ("Helvetica", 10, "bold")
    retour_lc.configure(font = Font_mot)

    compte_lc = tk.Button(master=Liste_Cl.buton, text="Ajouter", command= lambda: changement_page(Liste_Cl, Creation_Client_Admin))
    compte_lc.pack()
    #design
    Font_mot = ("Helvetica", 11, "bold")
    compte_lc.configure(font = Font_mot)

    #butons Création de compte Client par Admin
    cree_admin = tk.Button(master=Creation_Client_Admin.buton, text="créer", command= lambda: appel_envois(Creation_Client_Admin, Liste_Cl))
    cree_admin.pack()
    #butons Liste Circuit
    retour_lci = tk.Button(master=Liste_Ci.entete, text="Retour à la liste des pages", command= lambda: changement_page(Liste_Ci, Accueil_Ad))
    retour_lci.pack()
    #design
    Font_mot = ("Helvetica", 10, "bold")
    retour_lci.configure(font = Font_mot)

    #butons Accuiel Client
    accueil_client_logout = tk.Button(master=Accueil_Cl.entete, text="log out", command= lambda: Log_Out(Login_page, Accueil_Cl))
    accueil_client_logout.pack()
    #design
    Font_mot = ("Helvetica", 10, "bold")
    accueil_client_logout.configure(font = Font_mot)

    chercher_circuit = tk.Button(master=Accueil_Cl.buton, text="Voir les circuits disponibles", command= lambda: changement_vers_Pres_circuit(Accueil_Cl, Pres_Cir))
    chercher_circuit.grid(row=0, column=0)
    #design
    Font_mot = ("Helvetica", 10, "bold")
    chercher_circuit.configure(font = Font_mot)

    
    reservation_a_c = tk.Button(master=Accueil_Cl.buton, text="Voir mes reservations", command= lambda: changement_page(Accueil_Cl, Pres_Re))
    reservation_a_c.grid(row=0, column=1)
    #design
    Font_mot = ("Helvetica", 10, "bold")
    reservation_a_c.configure(font = Font_mot)

    #butons Présentation des Circuits
    retour_pc = tk.Button(master=Pres_Cir.entete, text="Retour à l'Accueil", command= lambda: changement_page(Pres_Cir, Accueil_Cl))
    retour_pc.pack()
    #design
    Font_mot = ("Helvetica", 10, "bold")
    retour_pc.configure(font = Font_mot)

    etapes_pc = tk.Button(master=Pres_Cir.entete, text="Détails du Circuit Selectionné", command= lambda: changement_vers_Pres_etape(Pres_Cir, Pres_Et))
    etapes_pc.pack()
    #design
    Font_mot = ("Helvetica", 12, "bold")
    etapes_pc.configure(font = Font_mot)

    #butons Présentation des Etapes
    retour_pe = tk.Button(master=Pres_Et.entete, text="Retour à la Selection", command= lambda: changement_page(Pres_Et, Pres_Cir))
    retour_pe.pack()
    #design
    Font_mot = ("Helvetica", 10, "bold")
    retour_pe.configure(font = Font_mot)

    reserve_pe =tk.Button(master=Pres_Et.buton, text="Reserver", command= lambda: changement_page(Pres_Et, Res_Pa))
    reserve_pe.pack()
    #design
    Font_mot = ("Helvetica", 10, "bold")
    reserve_pe.configure(font = Font_mot)

    #butons Reservation des passagers
    retour_rp = tk.Button(master=Res_Pa.buton_2, text="Retour à l'Accueil", command= lambda: changement_page(Res_Pa, Accueil_Cl))
    retour_rp.pack()
    #design
    Font_mot = ("Helvetica", 10, "bold")
    retour_rp.configure(font = Font_mot)

    #butons Présention des reservations
    retour_pr = tk.Button(master=Pres_Re.entete, text="Retour à l'Accueil", command= lambda: changement_page(Pres_Re, Accueil_Cl))
    retour_pr.pack()
    #design
    Font_mot = ("Helvetica", 10, "bold")
    retour_pr.configure(font = Font_mot)

    details_pr =tk.Button(master=Pres_Re.buton, text="Details", command= lambda: changement_page(Pres_Re, Pres_Pa))
    details_pr.pack()
    #butons Présention des passagers
    retour_pp = tk.Button(master=Pres_Pa.entete, text="Retour à l'Accueil", command= lambda: changement_page(Pres_Pa, Accueil_Cl))
    retour_pp.pack()
    #design
    Font_mot = ("Helvetica", 10, "bold")
    retour_pp.configure(font = Font_mot)

    reserv_pp = tk.Button(master=Pres_Pa.buton, text="Retour aux reservations", command= lambda: changement_page(Pres_Pa, Accueil_Cl))
    reserv_pp.pack()
    #design
    Font_mot = ("Helvetica", 10, "bold")
    reserv_pp.configure(font = Font_mot)

    #Fonctionnement
    Login_page.affiche()
    #Liste_Li.affiche()
    ecran.mainloop()
    connexion.close()
    #Liste_Ci.affiche()

Application()