################################################################################
# COMPARA I MESI: specificati nell'intervallo separati da - oppure con *
################################################################################
def compara_mese(mese, MeseOra_nr, FOUND):

    MESI = ['*', 'gen', 'feb', 'mar', 'apr','mag','giu','lug','ago','set','ott','nov','dic']

    ranges = mese.split(',')       # split del valore in eventuali range
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
            if MeseStart_nr <= MeseOra_nr  <= MeseStop_nr:
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