################################################################################    new new new
# COMPARA GIORNO SETTIMANA: verifica se giorno ok per lavoro (dom=0, lun=1 ..)     da controllare ------------------------------!!!
################################################################################
def compara_giorno_w(giorno_w, giorno_w_ora, FOUND):       # giorno numerico della settimana

    if (giorno_w == '*'):   #trovato l'* setta FOUND ed esce
        FOUND = True
    else:
        ranges = giorno_w.split('-') #da str a int
        # sotto: trova il nr del giorno attuale, per es. giovedi e' =4, dom=0
        ranges = giorno_w.split('-') #splitta il campo ranges
        point = -1              # puntatore per partire con lo zero al primo index

        for item in ranges:
            point = point + 1
            giorni = item.split('-')
            if (item == 'y' and point == giorno_w_ora): # trovato valore
                FOUND = True
    return FOUND # ritorna True se una condizione corretta e' stata trovata
# fine compara giorno numerico della settimana #################################