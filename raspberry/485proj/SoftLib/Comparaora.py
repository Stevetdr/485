
################################################################################
# COMPARA LE ORE: specificate nell'intervallo da HH:MM-HH:MM se c'e' * e' sempre
################################################################################
def compara_ora(start_stop, OraOra, FOUND):

    (OraStart, OraStop) = (start_stop.split('-'))     # spezza gli orari

    (Ah, Am) = (OraOra.split(':'))                    # spezza ore e minuti
    OraOra_min = int(Ah)*60+int(Am)                   # converte in minuti

    (Ah, Am) = (OraStart.split(':'))                  # spezza ore e minuti
    OraStart_min = int(Ah)*60+int(Am)                 # converte in minuti

    (Ah, Am) = (OraStop.split(':'))                   # spezza ore e minuti
    OraStop_min = int(Ah)*60+int(Am)                  # converte in minuti

    if OraStart_min <= OraOra_min <= OraStop_min: FOUND = True

    return FOUND # ritorna True se una condizione e' stata trovata
# fine compara ore #############################################################