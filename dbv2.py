#!/usr/bin/python3

import pymysql

# Open database connection
duomenuBaze = pymysql.connect("remotemysql.com","UST4tbdtjQ","CMn3WAPDfR","UST4tbdtjQ" )

numeris = "ABC222"
# prepare a cursor object using cursor() method
zymeklis1 = duomenuBaze.cursor()
zymeklis2 = duomenuBaze.cursor()

raktasIsvaziuoja = "Stovi"
raktasIvaziuoja = "Nebestovi"
def tikrintiNumeri():
    patikrintiArYraNumeris = "SELECT Semestras_Transporto_priemone.Numeris, Semestras_Transporto_priemone.id_Transporto_priemone,Semestras_Transporto_priemone.Busena FROM Semestras_Transporto_priemone WHERE Semestras_Transporto_priemone.Numeris='%s'" % (numeris)
    try: #Kai numeris egzistuoja bazeje
        # Execute the SQL command
        zymeklis1.execute(patikrintiArYraNumeris)
        #Fetch all the rows in a list of lists.
        rezultatai1 = zymeklis1.fetchone()
        # Now print fetched result
        print ("Jusu numeris : %s. Aciu, kad naudojates musu paslaugomis. ISVAZIUOJA" % numeris)
        #Rezultatai[1] = bus id
        #Pakeisti Semestras_Transporto_priemone lenteles Busena i "Vaziuoja"
        #Ideti i Semestras_Transporto_laikas isvaziavimo laika
        ID = rezultatai[1]
        if(rezultatai1[2] == raktasIsvaziuoja):
            masinaIsvaziuoja(ID)
            duomenuBaze.close()
    except: #Kai numerio nera duomenu bazeje
        print ("Jusu numeris : %s. Aciu, kad naudojates musu paslaugomis. IVAZIUOJA" % numeris)
def masinaIsvaziuoja(ID):
    atnaujintiIsvaziuojanti = "UPDATE Semestras_Transporto_priemone SET Semestras_Transporto_priemone.Busena='Nebestovi' WHERE Semestras_Transporto_priemone.id_Transporto_priemone='%s'; UPDATE Semestras_Stovejimo_laikas SET Semestras_Stovejimo_laikas.stovejimo_pabaiga= '%s', Semestras_Stovejimo_laikas.Busena='Paruosta' WHERE Semestras_Stovejimo_laikas.fk_Transporto_priemone='%s' AND Semestras_Stovejimo_laikas.Busena='Nesumoketa';" % (ID, gautiLaika(), ID)
    try:
        zymeklis2.execute(atnaujintiIsvaziuojanti)
        print("Blagadariu")
        duomenuBaze.commit()
    except:
        print("Failas blyn")
        duomenuBaze.rollback()
def gautiLaika():
    esantisLaikas = datetime.now()
    return esantisLaikas.strftime("%Y-%m-%d %H:%M:%S")
# Fetch a single row using fetchone() method.
#print ("Database version : %s " % results[0])
# disconnect from server
tikrintiNumeri()