################################################################################
# COMPARA I GIORNI: specificati nell'intervallo separati da - oppure con *
################################################################################
def compara_giorno_nr(giorno_nr, GiornoOra_Nr, FOUND):

    ranges = giorno_nr.split(',')       # split del valore in eventuali range
    for item in ranges:             # loop su tutti gli item in ranges
       # ======================================================================
        if '-' in item:             # con il - trova i due orari separati  da-a
            (GiornoStart, GiornoStop) = item.split('-')       # spezza le date
            if int(GiornoStart) <= GiornoOra_Nr  <= int(GiornoStop): FOUND = True
        else:
            if (item == '*'):
                FOUND = True

    return FOUND # ritorna True se una condizione corretta e' stata trovata
# fine compara giorni nr #######################################################
