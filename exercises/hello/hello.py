import string

def cout_words(chaine):
    m=0
    for k in range(1, len(chaine) - 1):
        if chaine[k] == " " and chaine[k+1] != " " and chaine[k+1] not in string.punctuation:
            m  += 1
    return m + 1

cout_words("Incroyable cette émission, tellement heureux que Trashtalk prenne de la notoriété !")
