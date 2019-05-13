import os
import time
import datetime
import pymysql

global zymeklis
global duomenuBaze

raktasIsvaziuoja = "Stovi"
raktasIvaziuoja = "Nebestovi"

raktasNesumoketa = "Nesumoketa"
raktasParuosta = "Paruosta"

#numeris = "ABC123"
numeris = "69"

#Prideti dar aiksteles id ir pagal ji uzklausa pakeist
def gautiLaika():
    #esantisLaikas = datetime.now()
    return (datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"))
def masinaIsvaziuoja(ID):
    atnaujintiIsvaziuojanti = "UPDATE Semestras_Transporto_priemone SET Semestras_Transporto_priemone.Busena='%s' WHERE Semestras_Transporto_priemone.id_Transporto_priemone='%s';" % (raktasIvaziuoja, ID)
    atnaujintiIsvaziuojanti2 = "UPDATE Semestras_Stovejimo_laikas SET Semestras_Stovejimo_laikas.stovejimo_pabaiga='%s', Semestras_Stovejimo_laikas.Busena='%s' WHERE Semestras_Stovejimo_laikas.fk_Transporto_priemone='%s' AND Semestras_Stovejimo_laikas.Busena='%s';" % (gautiLaika(), raktasParuosta, ID, raktasNesumoketa)
    try:
        zymeklis.execute(atnaujintiIsvaziuojanti)
        zymeklis.execute(atnaujintiIsvaziuojanti2)
        duomenuBaze.commit()
        print ("Duomenys sekmingai atnaujinti")
    except:
        print ("Ivyko klaida atnaujinant duomenis (Isvaziuojant)")
        duomenuBaze.rollback()
    #duomenuBaze.close()
def masinaIvaziuoja(ID):
    atnaujintiIvaziuojanti = "UPDATE Semestras_Transporto_priemone SET Semestras_Transporto_priemone.Busena='%s' WHERE Semestras_Transporto_priemone.id_Transporto_priemone='%s';" % (raktasIsvaziuoja, ID)
    atnaujintiIvaziuojanti2 = "INSERT INTO Semestras_Stovejimo_laikas(Semestras_Stovejimo_laikas.stovejimo_pradzia, Semestras_Stovejimo_laikas.stovejimo_pabaiga, Semestras_Stovejimo_laikas.Busena, Semestras_Stovejimo_laikas.fk_Transporto_priemone) VALUES ('%s', '%s', '%s', '%s');" % (gautiLaika(), gautiLaika(), raktasNesumoketa, ID)
    try:
        zymeklis.execute(atnaujintiIvaziuojanti)
        zymeklis.execute(atnaujintiIvaziuojanti2)
        duomenuBaze.commit()
        print ("Duomenys sekmingai atnaujinti")
    except:
        print ("Ivyko klaida atnaujinant duomenis (Ivaziuojant)")
        duomenuBaze.rollback()
    #duomenuBaze.close()
def naujaMasina():
    
    
    
def tikrintiNumeri():
    patikrintiArYraNumeris = "SELECT Semestras_Transporto_priemone.Numeris, Semestras_Transporto_priemone.id_Transporto_priemone, Semestras_Transporto_priemone.Busena FROM Semestras_Transporto_priemone WHERE Semestras_Transporto_priemone.Numeris='%s'" % (numeris)
    try:
        zymeklis.execute(patikrintiArYraNumeris)
        rezultatai = zymeklis.fetchone()
        if (rezultatai[2] == raktasIsvaziuoja):
            masinaIsvaziuoja(rezultatai[1])
            print ("Jusu numeris : %s. Aciu, kad naudojates musu paslaugomis. ISVAZIUOJA" % numeris)
        elif (rezultatai[2] == raktasIvaziuoja):
            masinaIvaziuoja(rezultatai[1])
            print (rezultatai[1])
            print ("Jusu numeris : %s. Aciu, kad naudojates musu paslaugomis. IVAZIUOJA" % numeris)
            
    except:
        print ("Ivyko klaida")
def main():
    while 1:
        tikrintiNumeri()
        time.sleep(10000)
    
        
if __name__ == '__main__':
    try:
        duomenuBaze = pymysql.connect("remotemysql.com","UST4tbdtjQ","CMn3WAPDfR","UST4tbdtjQ" )
        zymeklis = duomenuBaze.cursor()
    except:
        print ("Nepavyko prisijungti prie duomenu serverio")
             
    try:
      main()
    except KeyboardInterrupt:
      print ("bye bye...")
      pass
#zymeklis.execute("SELECT * FROM TAB_CPU ORDER BY ID DESC LIMIT 1")
#sql =  "INSERT INTO TAB_CPU (TValue, T_Date, T_Time) VALUES (%s, %s, %s)" 
#c.execute(sql,( str(temperatur) , str(datum), str(zeit)))