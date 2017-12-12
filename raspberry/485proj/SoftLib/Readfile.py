
################################################################################
# Legge una riga per volta il file dati
################################################################################
def ReadFile(myFile, lineCmntStr=None):

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
