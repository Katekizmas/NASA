import P3kamera
#import picamera
import os
from datetime import datetime
import subprocess
from time import sleep

judesioBukle = False
nuotraukosKelias = "/home/pi/Documents/Nuotraukos/"

def fotografuoti():
    #nuotraukosPavadinimas = gautiLaika() + '.jpg'
    nuotraukosPavadinimas = "masina2" + '.jpg'
    with picamera.PiCamera() as kamera:
        kamera.resolution = (1280, 720)
        kamera.capture(nuotraukosKelias + nuotraukosPavadinimas)
        print("nufotkinta")
        return nuotraukosPavadinimas
def gautiLaika():
    esantisLaikas = datetime.now()
    return esantisLaikas.strftime("%Y-%m-%d %H:%M:%S")

def gautiNumerius(nuotraukosPavadinimas):
    gautiNumeris = subprocess.Popen("alpr -c eu " + nuotraukosKelias + nuotraukosPavadinimas + " | tail | head -1 | awk '{print $2}'", shell=True, stdout=subprocess.PIPE).stdout
    numeris = gautiNumeris.read().decode().strip()
    if(numeris == "license"):
        print("Numeris nuotraukoje neatpazintas")
        numeris = "neatpazintas"
    else:
        print("Nuotraukoje numeris yra : " + numeris)
    return numeris

while True:
    #judesioBukle = P3kamera.motion()
    judesioBukle = True
    if judesioBukle:
        #nuotraukosPavadinimas = fotografuoti()
        nuotraukosPavadinimas = "masina2" + '.jpg'
        numeris = gautiNumerius(nuotraukosPavadinimas);
        sleep(5)
        
        