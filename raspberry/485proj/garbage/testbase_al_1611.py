#!/bin/env python3.4
import sys
import datetime

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
# Legge una riga per volta il file dati
################################################################################
def readFile(myFile, lineCmntStr=None):

    dati = []                    # crea lista vuota di nome 'dati'
    f = open(myFile, "r")
    for line in f:
        line = line.strip()      # remove BLANKS
        if not line:
            continue
        if lineCmntStr and line[0] == lineCmntStr: # se vuoi verificare commento ed il primo char della riga == commento... continua
            continue
        line = line.strip('\n')  # rimuovi il newLine
        dati.append(line)        # mette le righe in dati
    f.close()
    return dati
# fine lettura file dati #######################################################

################################################################################
# COMPARA I MESI: specificati nell'intervallo separati da - oppure con *
################################################################################
def compara_mese(month):

    fDEBUG = True
    FOUND = False

    tempo = datetime.datetime.now()
    MeseOra_nr = tempo.month
    MESI = ['*', 'gen', 'feb', 'mar', 'apr','mag','giu','lug','ago','set','ott','nov','dic']

    ranges = month.split(',')       # split del valore in eventuali range
    for item in ranges:             # loop su tutti gli item in ranges
        # ======================================================================
        if '-' in item:             # con il - trova i 2 mesi da-a
            mesi = item.split('-')
            (MeseStart, MeseStop) = (item.split('-'))     # spezza i mesi
            # ------------------------------------------------------------------
            for index in range(len(MESI)):  # converte mese Start in mese numero
                if (MESI[index] == MeseStart): MeseStart_nr = index
            # ------------------------------------------------------------------
            for index in range(len(MESI)):  # converte mese Stop in mese numero
                if (MESI[index] == MeseStop): MeseStop_nr = index
            # ------------------------------------------------------------------
            # sotto: compara se siamo nel range o no tra MeseStart_nr e MeseStop_nr
            if (MeseOra_nr >= MeseStart_nr and  MeseOra_nr <= MeseStop_nr):
                FOUND = True
                break
        else:                       # altrimenti mette item in mesi
            mesi = [item]
        # ======================================================================
        for mese in mesi:   # verifica se il mese e' lo stesso oppure se c'e' '*'
            for index in range(len(MESI)):
                if (MESI[index] == mese): mese_nr = index
            if mese_nr == MeseOra_nr or mese == '*':  # trovato mese uguale o '*'
                FOUND = True
                break
    return FOUND # ritorna True se una condizione corretta e' stata trovata
# fine compara_mese ############################################################

################################################################################
# COMPARA I GIORNI: specificati nell'intervallo separati da - oppure con *
################################################################################
def compara_giorno_nr(giorno_nr):

    fDEBUG = True
    FOUND = False

    tempo = datetime.datetime.now()
    GiornoOra_nr = tempo.day

    ranges = giorno_nr.split(',')       # split del valore in eventuali range
    for item in ranges:             # loop su tutti gli item in ranges
       # ======================================================================
        if '-' in item:             # con il - trova i due orari separati  da-a
            (GiornoStart, GiornoStop) = item.split('-')       # spezza le date
            if (GiornoOra_nr >= int(GiornoStart) and GiornoOra_nr <= int(GiornoStop)):
                FOUND = True
        else:
            if (item == '*'):
                FOUND = True

    return FOUND # ritorna True se una condizione corretta e' stata trovata
# fine compara giorni nr ############################################################

################################################################################
# COMPARA LE ORE: specificate nell'intervallo da HH:MM-HH:MM se c'e' * e' sempre
################################################################################
def compara_ora(start_stop, OraOra):

    FOUND = False
    (OraStart, OraStop) = (start_stop.split('-'))     # spezza gli orari

    if (OraOra >= OraStart and OraOra <= OraStop): FOUND = True

    return FOUND # ritorna True se una condizione e' stata trovata
################################################################################

################################################################################
# Esame delle righe e eventuale esecuzione del comando   PROCESS
################################################################################
def processFile1(dati):
    tempo = datetime.datetime.now()
    # le liste si possono definire come globali? perche' devo ripeterla per fare in modo di poterla referenziare?
    MESI = ['*', 'gen', 'feb', 'mar', 'apr','mag','giu','lug','ago','set','ott','nov','dic']
    print ("===============================================================")
    flag_mese = False       # reset
    flag_giorno_nr = False  # reset

    for line in dati:            #esame riga per riga di tutti i dati letti

        myData = line.split()    # crea una LIST separando i BLANKs

        if myData[STATO] == 'A':    # file letto, attivo e da esaminare
            print (" JOB number: [{0}]".format(myData[JOB]))
            #.......................................... VERIFICA SITUAZIONE MESE
            if compara_mese(myData[MESE]) == True:
                flag_mese = True            # servira' per il test finale
                print ("           MESE IN RANGE CORRETTO   :{0}  (siamo in  {1})".format(myData[MESE],MESI[tempo.month]))
            else:
                flag_mese = False
                print ("!          MESE non in range        :{0}  (siamo in  {1}!)".format(myData[MESE],MESI[tempo.month]))
            #.............................VERIFICA SITUAZIONE DATA DI ESECUZIONE
            if compara_giorno_nr(myData[GIORNO_NR]) == True:
                flag_mese_nr = True            # servira' per il test finale
                print ("           GIORNO IN RANGE CORRETTO :{0}  (e' il  {1} )".format(myData[GIORNO_NR],tempo.day))
            else:
                flag_mese_nr = False
                print ("!          GIORNO non in range      :{0}  (e' il  {1} !)".format(myData[GIORNO_NR],tempo.day))
            #................................ VERIFICA SITUAZIONE ORA START-STOP
            OraOra = ("%s:%s" % (tempo.hour, tempo.minute))
            if compara_ora(myData[START_STOP],OraOra) == True:
                flag_giorno_nr = True            # servira' per il test finale
                print ("           ORARIO IN RANGE CORRETTO :{0}  (sono le {1})".format(myData[START_STOP],OraOra))
            else:
                flag_giorno_nr = False
                print ("!          ORARIO non in range      :{0}  (sono le {1})!".format(myData[START_STOP],OraOra))
            print ("===============================================================")
            if (flag_mese == True and flag_mese_nr == True and flag_giorno_nr == True):
                print ("ESEGUIRE L'INVIO DEL COMANDO per il JOB number: [{0}]".format(myData[JOB]))
                print ("===============================================================")
################################################################################

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
if __name__ == "__main__":
    while(1):
        filename = "dati1.txt"
        data = readFile(myFile=filename, lineCmntStr='#')  # PROCESSO di analisi dati del file!!!!
        #esempioOra()
        processFile1(data)       # all'esame dei dati!!!!
        sys.exit()

        X = 1
        while (1):                            #
            tempo = datetime.datetime.now()

            #if (X==X):   # solo per test !!!!!!!!!!!!!!!!!!!!!!! bypassa il controllo del minuto
            if (tempo.second == 0 and X == 1):    # Scatena il processo solo a secondi=0 ed una sola volta
                data = readFile(myFile=filename, lineCmntStr='#')  # PROCESSO di analisi dati del file!!!!
                processFile1(data)       # all'esame dei dati!!!!
                X=0
            elif (tempo.second != 0 and X == 0):
                X=1
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################

# --- LIST -- http://effbot.org/zone/python-list.htm
