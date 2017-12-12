#!/bin/env python3.4
import sys
import datetime

#import SoftLib.SSlib      as myLib
import SoftLib.Readfile         as RF
import SoftLib.Comparaora       as CO
import SoftLib.Comparagiornow   as CW
import SoftLib.Comparagiornon   as CN
import SoftLib.Comparamese      as CM

JOB                     = 0
STATO                   = 1
SLAVE                   = 2
PIN                     = 3
MESE                    = 4
GIORNO_NR               = 5
GIORNO_W                = 6
START_STOP              = 7
CMD                     = 8
VALUEON                 = 9
VALUEOFF                = 10
NOME_DISPOSITIVO        = 11

################################################################################
# Esame delle righe e eventuale esecuzione del comando   PROCESS
################################################################################
def processFile(dati):
    fDEBUG = False
    tempo = datetime.datetime.now()
    # le liste si possono definire come globali? perche' devo ripeterla per fare in modo di poterla referenziare?
    MESI = ['*', 'gen', 'feb', 'mar', 'apr','mag','giu','lug','ago','set','ott','nov','dic']
    if fDEBUG == False: print(" per vedere tutte le analisi mettere il debug = true")
    print ("===============================================================")
    flag_mese = False       # reset
    flag_giorno_nr = False  # reset

    for line in dati:            #esame riga per riga di tutti i dati letti

        myData = line.split()    # crea una LIST separando i BLANKs

        if myData[STATO] == 'A':    # status file letto, attivo e da esaminare
            if fDEBUG:print (" JOB number: [{0}]".format(myData[JOB]))
        #.......................................... VERIFICA SITUAZIONE MESE
            MeseOra_nr = tempo.month
            if CM.compara_mese(myData[MESE],MeseOra_nr, FOUND=False) == True:
                flag_mese = True            # servira' per il test finale
                if fDEBUG:print ("           MESE IN RANGE CORRETTO    : {0}  (siamo in  {1})".format(myData[MESE],MESI[tempo.month]))
            else:
                flag_mese = False
                if fDEBUG:print ("!          MESE non in range         : {0}  (siamo in  {1}!)".format(myData[MESE],MESI[tempo.month]))
        #.............................VERIFICA SITUAZIONE DATA DI ESECUZIONE
            GiornoOra_Nr = tempo.day
            if CN.compara_giorno_nr(myData[GIORNO_NR], GiornoOra_Nr, FOUND=False) == True:
                flag_mese_nr = True            # servira' per il test finale
                if fDEBUG:print ("           GIORNO IN RANGE CORRETTO  : {0}  (e' il  {1} )".format(myData[GIORNO_NR],tempo.day))
            else:
                flag_mese_nr = False
                if fDEBUG:print ("!          GIORNO non in range       : {0}  (e' il  {1} !)".format(myData[GIORNO_NR],tempo.day))
        #.............................VERIFICA SITUAZIONE range giorni settimana
            Giorno_w_Ora = int(tempo.today().strftime("%w"))    #da str a int
            if CW.compara_giorno_w(myData[GIORNO_W], Giorno_w_Ora, FOUND=False) == True:
                flag_giorno_w = True            # servira' per il test finale
                if fDEBUG:print ("           GIORNO WEEK CORRETTO      : {0}  (e' il  giorno {1} )".format(myData[GIORNO_W],int(tempo.today().strftime("%w"))))
            else:
                flag_giorno_w = False
                if fDEBUG:print ("!          GIORNO WEEK non in range  : {0}  (e' il  giorno {1} )".format(myData[GIORNO_W],int(tempo.today().strftime("%w"))))
        #................................ VERIFICA SITUAZIONE ORA START-STOP
            tempo = datetime.datetime.now()                     # aggiunta
            OraOra = ("%s:%s" % (tempo.hour, tempo.minute))     #  tolta da qui e messa nella funzione

            if CO.compara_ora(myData[START_STOP],OraOra, FOUND=False) == True:
                OraOra = ("%s:%s" % (tempo.hour, tempo.minute))     # aggiunta
                flag_giorno_nr = True            # servira' per il test finale
                if fDEBUG:print ("           ORARIO Start_stop IN RANGE: {0}  (sono le {1})".format(myData[START_STOP],OraOra))
            else:
                flag_giorno_nr = False
                if fDEBUG:print ("!          ORARIO non in range       : {0}  (sono le {1})!".format(myData[START_STOP],OraOra))
            if fDEBUG:print ("===============================================================")
            if (flag_mese == True and flag_mese_nr == True and flag_giorno_nr == True and flag_giorno_w == True):
                print ("ESECUZIONE comando di attivazione x JOB number: [{0}]".format(myData[JOB]))
                print ("Comando [{0}] da inviare a Arduino:{1} sul pin:{2} stato: {3}  (device:{4})".format(myData[CMD],myData[SLAVE],myData[PIN],myData[VALUEON],myData[NOME_DISPOSITIVO]))
                print ("===============================================================")
            else:
                print ("ESECUZIONE comando di reset:")
                print ("Comando [{0}] da inviare a Arduino:{1} sul pin:{2} stato: {3}  (device:{4})".format(myData[CMD],myData[SLAVE],myData[PIN],myData[VALUEOFF],myData[NOME_DISPOSITIVO]))
                print ("===============================================================")
# fine process #################################################################

################################################################################
# Mi serve solo per capire la scomposizione dell'ora
################################################################################
def esempioOra():
    tempo = datetime.datetime.now()
    print ("Data e ora corrente = %s" % tempo)
    #print ("Data e ora ISO format = %s" % tempo.isoformat())
    print ("Anno corrente = %s" % tempo.year)
    print ("Mese corrente = %s" % tempo.month)
    print ("Data corrente (giorno) =  %s" % tempo.day)
    print ("Formato dd/mm/yyyy =  %s/%s/%s" % (tempo.day, tempo.month, tempo.year))
    print ("Ora corrente = %s" % tempo.hour)
    print ("Minuto corrente = %s" % tempo.minute)
    print ("Secondo corrente =  %s" % tempo.second)
    print ("Formato hh:mm:ss = %s:%s:%s" % (tempo.hour, tempo.minute, tempo.second))
    print ("Numero del giorno nella settimana (0=dom,1=lun): ", tempo.today().strftime("%w"))
################################################################################

################################################################################
# - M A I N
################################################################################
#if __name__ == "__main__":
def main():
    while(1):
        filename = "dati1.txt"
        data = RF.ReadFile(myFile=filename, lineCmntStr='#')  # PROCESSO di analisi dati del file!!!!
        #esempioOra()
        processFile(data)       # all'esame dei dati!!!!
        sys.exit()

        X = 1
        while (1):                            #
            tempo = datetime.datetime.now()

            #if (X==X):   # solo pepr test !!!!!!!!!!!!!!!!!!!!!!! bypassa il controllo del minuto
            if (tempo.second == 0 and X == 1):    # Scatena il processo solo a secondi=0 ed una sola volta ogni minuto
                data = SoftLib.ReadFile(myFile=filename, lineCmntStr='#')  # PROCESSO di analisi dati del file!!!!
                myLib.processFile1(data)       # all'esame dei dati!!!!
                X=0
            elif (tempo.second != 0 and X == 0):
                X=1
################################################################################

if __name__ == "__main__":
    main()
################################################################################
################################################################################
################################################################################
################################################################################

# --- LIST -- http://effbot.org/zone/python-list.htm


