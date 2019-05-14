import P3kamera
#import picamera
import subprocess
import time
import datetime
import pymysql

global zymeklis
global duomenuBaze

raktasIsvaziuoja = "Stovi"
raktasIvaziuoja = "Nebestovi"

raktasNesumoketa = "Nesumoketa"
raktasParuosta = "Paruosta"

idAikstele = "2" #Cia bus visada fiksuota reiksme, pagal prietaisa kur jis stovi yra nustatoma

judesioBukle = False
nuotraukosKelias = "/home/pi/Documents/Nuotraukos/"

def gautiLaika():
    return (datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"))

def fotografuoti():
    #nuotraukosPavadinimas = gautiLaika() + '.jpg'
    nuotraukosPavadinimas = "masina2" + '.jpg'
    with picamera.PiCamera() as kamera:
        kamera.resolution = (1280, 720)
        kamera.capture(nuotraukosKelias + nuotraukosPavadinimas)
        print("Sekmingai nufotografuota")
        return nuotraukosPavadinimas

def gautiNumerius(nuotraukosPavadinimas):
    gautiNumeris = subprocess.Popen("alpr -c eu " + nuotraukosKelias + nuotraukosPavadinimas + " | tail | head -1 | awk '{print $2}'", shell=True, stdout=subprocess.PIPE).stdout
    numeris = gautiNumeris.read().decode().strip()
    if(numeris == "license"):
        numeris = "Neatpazintas"
    return numeris

def gautiVietuSkaiciu():
    gautiSkaiciu = "SELECT Semestras_Aikstele.Vietu_skaicius, COUNT(IF(Semestras_Transporto_priemone.Busena='%s',1,NULL))AS Uzimtos_vietos FROM Semestras_Aikstele INNER JOIN Semestras_Transporto_priemone ON Semestras_Transporto_priemone.fk_Aikstele=Semestras_Aikstele.id_Aikstele WHERE Semestras_Transporto_priemone.fk_Aikstele='%s' GROUP BY Semestras_Aikstele.Vietu_skaicius;" % (raktasIsvaziuoja, idAikstele)
    try:
        zymeklis.execute(gautiSkaiciu)
        rezultatai = zymeklis.fetchone()
        return rezultatai[0]-rezultatai[1]
    except:
        print("Ivyko klaida, skaitant vietu skaiciu")
        return 0;

def masinaIsvaziuoja(ID):
    atnaujintiIsvaziuojanti1 = "UPDATE Semestras_Transporto_priemone SET Semestras_Transporto_priemone.Busena='%s' WHERE Semestras_Transporto_priemone.id_Transporto_priemone='%s';" % (raktasIvaziuoja, ID)
    atnaujintiIsvaziuojanti2 = "UPDATE Semestras_Stovejimo_laikas SET Semestras_Stovejimo_laikas.stovejimo_pabaiga='%s', Semestras_Stovejimo_laikas.Busena='%s' WHERE Semestras_Stovejimo_laikas.fk_Transporto_priemone='%s' AND Semestras_Stovejimo_laikas.Busena='%s';" % (gautiLaika(), raktasParuosta, ID, raktasNesumoketa)
    try:
        zymeklis.execute(atnaujintiIsvaziuojanti1)
        zymeklis.execute(atnaujintiIsvaziuojanti2)
        duomenuBaze.commit()
        print ("Duomenys sekmingai atnaujinti (Isvaziuoja)")
    except:
        print ("Ivyko klaida atnaujinant duomenis (Isvaziuojant)")
        duomenuBaze.rollback()
    #duomenuBaze.close()

def masinaIvaziuoja(ID):
    atnaujintiIvaziuojanti1 = "UPDATE Semestras_Transporto_priemone SET Semestras_Transporto_priemone.Busena='%s' WHERE Semestras_Transporto_priemone.id_Transporto_priemone='%s';" % (raktasIsvaziuoja, ID)
    atnaujintiIvaziuojanti2 = "INSERT INTO Semestras_Stovejimo_laikas(Semestras_Stovejimo_laikas.stovejimo_pradzia, Semestras_Stovejimo_laikas.stovejimo_pabaiga, Semestras_Stovejimo_laikas.Busena, Semestras_Stovejimo_laikas.fk_Transporto_priemone) VALUES ('%s', '%s', '%s', '%s');" % (gautiLaika(), gautiLaika(), raktasNesumoketa, ID)
    try:
        zymeklis.execute(atnaujintiIvaziuojanti1)
        zymeklis.execute(atnaujintiIvaziuojanti2)
        duomenuBaze.commit()
        print ("Duomenys sekmingai atnaujinti (Ivaziuoja)")
    except:
        print ("Ivyko klaida atnaujinant duomenis (Ivaziuojant)")
        duomenuBaze.rollback()
    #duomenuBaze.close()

def masinaNauja(numeris):
    idetiNauja1 = "INSERT INTO Semestras_Transporto_priemone(Semestras_Transporto_priemone.Numeris, Semestras_Transporto_priemone.Busena, Semestras_Transporto_priemone.fk_Aikstele) VALUES ('%s', '%s', '%s');" % (numeris, raktasIsvaziuoja, idAikstele)
    idetiNauja2 = "INSERT INTO Semestras_Stovejimo_laikas(Semestras_Stovejimo_laikas.stovejimo_pradzia, Semestras_Stovejimo_laikas.stovejimo_pabaiga, Semestras_Stovejimo_laikas.Busena, Semestras_Stovejimo_laikas.fk_Transporto_priemone) VALUES('%s', '%s', '%s', LAST_INSERT_ID());" % (gautiLaika(), gautiLaika(), raktasNesumoketa)
    try:
        zymeklis.execute(idetiNauja1)
        zymeklis.execute(idetiNauja2)
        duomenuBaze.commit()
        print ("Duomenys sekmingai prideti (Kuria nauja)")
    except:
        print ("Ivyko klaida pridedant duomenis (Kuria nauja)")
        duomenuBaze.rollback()
    #duomenuBaze.close()

def tikrintiNumeri(numeris):
    patikrintiArYraNumeris = "SELECT Semestras_Transporto_priemone.Numeris, Semestras_Transporto_priemone.id_Transporto_priemone, Semestras_Transporto_priemone.Busena FROM Semestras_Transporto_priemone WHERE Semestras_Transporto_priemone.Numeris='%s'" % (numeris)
    vietuSkaicius = gautiVietuSkaiciu()
    try:
        zymeklis.execute(patikrintiArYraNumeris)
        rezultatai = zymeklis.fetchone()
        if (rezultatai[2] == raktasIsvaziuoja):
            masinaIsvaziuoja(rezultatai[1])
            print ("Jusu numeris : %s. Aciu, kad naudojates musu paslaugomis.\nLikusiu vietu skaicius: %s" % (numeris, vietuSkaicius))
        elif (rezultatai[2] == raktasIvaziuoja):
            if (vietuSkaicius > 0):
                masinaIvaziuoja(rezultatai[1])
                print ("Jusu numeris : %s. Aciu, kad naudojates musu paslaugomis.\nLikusiu vietu skaicius: %s" % (numeris, vietuSkaicius))
            else:
                print("Aiksteleje, nera pakankamai vietos, prasome atvaziuoti veliau")
            
    except:
        masinaNauja(numeris)
        print ("Jusu numeris : %s. Aciu, kad naudojates musu paslaugomis.\nLikusiu vietu skaicius: %s" % (numeris, vietuSkaicius))

def main():
    while 1:
        #judesioBukle = P3kamera.motion()
        judesioBukle = True # Kai kamera bus prijungta atkomentuoti virsutini
        if judesioBukle:
            try:
            #nuotraukosPavadinimas = fotografuoti()
                nuotraukosPavadinimas = "masina" + '.jpg' # Kai kamera bus prijungta atkomentuoti virsutini
                numeris = gautiNumerius(nuotraukosPavadinimas);
                if (numeris != "Neatpazintas"):
                    print("Numeriai sekmingai nuskaityti")
                    tikrintiNumeri(numeris)
                    time.sleep(15)
                else:
                    print ("Nepavyko atpazinti numerio!")
                    time.sleep(15)
            except:
                print ("Nepavyko atpazinti numerio!\nNerasta nuotrauka aplankale")
                time.sleep(15)
if __name__ == '__main__':
    try:
        duomenuBaze = pymysql.connect("remotemysql.com","UST4tbdtjQ","CMn3WAPDfR","UST4tbdtjQ" )
        zymeklis = duomenuBaze.cursor()
    except:
        print ("Nepavyko prisijungti prie duomenu serverio")
    try:
      main()
    except KeyboardInterrupt:
      print ("Programa baige darba...")
      pass