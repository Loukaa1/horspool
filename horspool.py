def naive_search(text, pattern, case_sensitive=True) :
    t = len(text)
    p = len(pattern)
    result = []
    for i in range(t-p+1) :
        j = 0
        if case_sensitive :
            while j<p and text[j+i] == pattern[j] :
                j += 1
        else :
            while j<p and text[j+i].upper() == pattern[j].upper() :
                j += 1
        if j == p :
            result.append(i)
    return result


def shift(pattern, case_sensitive=True):
    """
    Retourne le dictionnaire des sauts pour les différentes lettres du motif (on exclu la dernière lettre)"""
    D = {}
    for i, letter in enumerate(pattern[:-1]) :
        if case_sensitive :
            D[letter] = len(pattern)-1-i
        else :
            letter = letter.upper()
            D[letter] = len(pattern)-1-i
    return D
        
assert shift('CGGCAG') == {'C':2, 'G':3, 'A':1}


def search(text, pattern, case_sensitive=True):
    """
    Cherche un motif dans un texte
    Retourne Vrai si le motif est trouvé, faux sinon
    """
    t = len(text)
    p = len(pattern)
    # Si le motif est plus long que le texte ou que le texte est vide, on retourne False
    if t == 0 or p>t:# Si le motif est vide ou +grand que le texte
        return []
    # On crée la table des sauts
    jumps = shift(pattern, case_sensitive=case_sensitive)
    results = []
    # On initialise l'indice i à 0
    i = 0
    while i<=t-p:
        j = p-1
        if case_sensitive :
            while j >= 0 and text[i+j] == pattern[j] :
                j -=1
        else :
            while j >= 0 and text[i+j].upper() == pattern[j].upper() :
                j -=1
        if j == -1 :
            results.append(i)
            i+=1
        else :
            if  case_sensitive :
                jump = jumps.get(text[i+j], p) #saut sinon saut complet
            else :
                jump = jumps.get(text[i+j].upper(), p)
            decalage = p-1-j
            real_jump = jump-decalage
            if real_jump < 0 :
                i+=1
            else :
                i+= real_jump
    return results
