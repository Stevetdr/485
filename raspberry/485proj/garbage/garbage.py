


################################################################################
################################################################################
################################################################################
################################################################################

# --- LIST -- http://effbot.org/zone/python-list.htm

################################################################################
# Esame delle righe e eventuale esecuzione del comando
################################################################################
def processFile1(dati):
    for line in dati:            #esame riga per riga di tutti i dati letti
        myData = line.split()    # crea una LIST separando i BLANKs

        #print('LEN=', len(myData), 'data: ', myData)
        if myData[STATO] == 'A':    # file letto, attivo e da esaminare
            (OraStart, OraStop) = (myData[START_STOP].split('-'))     # spezza gli orari
#prova per comparazione ora attuale con OraStart o OraStop
            OraOra = ("%s:%s" % (tempo.hour, tempo.minute))
            print (" ora attuale --> %s" % (OraOra))
            print (" ora di partenza : %s     ora di fermata : %s" % (OraStart, OraStop))

            #print (myData[0:12])
            if (OraOra >= OraStart and OraOra <= OraStop):
                print ("--> invia comando %s allo slave %s  pin %s  - device %s - con valore %s" % (myData[8],myData[2],myData[3],myData[11],myData[9]))
                # se si e' nel range manda il ValueON
                print ("COMANDO DA INVIARE:%s-%s-%s-%s" % (myData[8],myData[2],myData[3],myData[9]))
            #    print(myData[11])
            else:
                print ('fuori range')
                # se si e' nel range manda il ValueOFF
                print ("COMANDO DA INVIARE:%s-%s-%s-%s" % (myData[8],myData[2],myData[3],myData[10]))


################################################################################
def meseSS(month):


    fDEBUG = True
    fDEBUGs = True
    FOUND = False

    tempo = datetime.datetime.now()
    MeseOra_nr = tempo.month

    MESI = ['*', 'gen', 'feb', 'mar', 'apr','mag','giu','lug','ago','set','ott','nov','dic']

    #if fDEBUGs: print('inizio prova')
    print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #for index in range(len(MESI)):
    #    if (MESI[index] == MeseOra): #cerca corrispondenza tra il mese ed il relativo numero
    #        print("Trovato!   :indice [{0}] relativo al mese di [{1}]".format(index, MESI[index]))
    #        MeseOra_nr = index  # identifica il mese con il numero
    #        print (" MeseOra_nr in numero : ",MeseOra_nr)
    #        break

    #    if fDEBUGs:
    #        print (index,MESI[index])

    #if fDEBUGs:print('fine prova')

    #if fDEBUG: print ("mese.....{0:<15}".format(month)) # se fDEBUG=True esegue la print
    ranges = month.split(',')       # split del valore in eventuali più range
    #if fDEBUG: print ("    ranges.....", ranges)
    for item in ranges:             # loop su tutti gli item in ranges
        #if fDEBUG: print ("    item.....", item)

#        if fDEBUG: print ("    nr. mese.",range(MESI))

        if '-' in item:             # con il - trova i 2 mesi da-a
            mesi = item.split('-')
            (MeseStart, MeseStop) = (item.split('-'))     # spezza i mesi
            #print ("mese start  e mese stop",MeseStart, MeseStop)
            for index in range(len(MESI)):  # converte mese Start in numero/mese
                if (MESI[index] == MeseStart):
                    MeseStart_nr = index
                    #print("----> MeseStart, index",MeseStart,index)
                    #print("  mese start: {0}  numero [{1}]".format(MeseStart,MeseStart_nr))

            for index in range(len(MESI)):
                if (MESI[index] == MeseStop):  # converte mese Stop in numero/mese
                    MeseStop_nr = index
                    #print("----> MeseStop, index",MeseStop,index)
                    #print("  mese stop : {0}  numero [{1}]".format(MeseStop,MeseStop_nr))
            # sotto: compara se siamo nel range o no
            if (MeseOra_nr >= MeseStart_nr and  MeseOra_nr <= MeseStop_nr):
                #print ("                           sono nel range !!!!")
                #print()
                FOUND = True
                break
            #else:
                #print ("                          __non sono nel range__")
                #print()

        else:
            mesi = [item]           # altrimenti mette item in mesi

        #if fDEBUG: print ("    mesi.....", mesi)
        for mese in mesi:
            for index in range(len(MESI)):
                if (MESI[index] == mese):
                    mese_nr = index
            if mese_nr == MeseOra_nr or mese == '*':  # trovato * OK!!!!
                FOUND = True
                #print()
                break
    #print()
    return FOUND

################################################################################
# COMPARA LE ORE: specificate nell'intervallo da HH:MM-HH:MM se c'e' * e' sempre
################################################################################
def compara_oras(start_stop, OraOra):

    fDEBUG = True
    FOUND = False
    (OraStart, OraStop) = (start_stop.split('-'))     # spezza gli orari
#prova per comparazione ora attuale con OraStart o OraStop
    #OraOra = ("%s:%s" % (tempo.hour, tempo.minute))
    #print (" ora attuale --> %s" % (OraOra))
    #print (" ora di partenza : %s     ora di fermata : %s" % (OraStart, OraStop))

            #print (myData[0:12])
    if (OraOra >= OraStart and OraOra <= OraStop):
        #print (' Ora nel range indicato')
        #print ("--> invia comando %s allo slave %s  pin %s  - device %s - con valore %s" % (myData[8],myData[2],myData[3],myData[11],myData[9]))
                # se si e' nel range manda il ValueON
        #print ("COMANDO DA INVIARE:%s-%s-%s-%s" % (myData[8],myData[2],myData[3],myData[9]))
            #    print(myData[11])
        FOUND = True
    #else:
        #print ('fuori range')
                # se si e' nel range manda il ValueOFF
        #print ("COMANDO DA INVIARE:%s-%s-%s-%s" % (myData[8],myData[2],myData[3],myData[10]))
    return FOUND # ritorna True se una condizione e' stata trovata


################################################################################
def giornos(day):
    if day.startswith('lun'):
        print ("giorno...", day)
        return True
    return False



    ################################################################################
# COMPARA I GIORNI: specificati nell'intervallo separati da - oppure con *
################################################################################
def compara_giorno_nr(giorno_nr):

    fDEBUG = True
    FOUND = False

    tempo = datetime.datetime.now()
    GiornoOra_nr = tempo.day
    #print ("numero del giorno odierno: ",tempo.day)
    #print ("dato passato: ",(giorno_nr))

    ranges = giorno_nr.split(',')       # split del valore in eventuali range
    for item in ranges:             # loop su tutti gli item in ranges
       # ======================================================================
        if '-' in item:             # con il - trova i due orari separati  da-a
            (GiornoStart, GiornoStop) = item.split('-')       # spezza le date
            #print (GiornoStart, GiornoStop)
            if (GiornoOra_nr >= int(GiornoStart) and GiornoOra_nr <= int(GiornoStop)):
                FOUND = True
                #print ("Trovata corrispondenza: giorno nel range")
            else:
                FOUND = False
                #print ("! no corrispondenza!")
        else:
            if (item == '*'):
                #print ("TROVATO ASTERISCO")
                FOUND = True

    return FOUND # ritorna True se una condizione corretta e' stata trovata
# fine compara giorni nr ############################################################