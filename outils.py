
'''
function: ajouter les verbes dans une dictionnaire
arguments:  
        lemme: key dans dictionnaire, contient une sous dictionnaire
        forme_f: key de sous dictionnaire
        grammaire: valeur de sous dictionnaire
        dictionary: un dictionnaire avec lemme comme le key
'''
def add_dict(lemme, forme_f, grammaire, dictionary):
    if(lemme not in dictionary.keys()): # Si lemme pas dans le dictionaire, on y ajoute
        lemme_name = {}
        lemme_name.update({forme_f:grammaire})
        dictionary.update({lemme:lemme_name})
    else: # Si lemme est deja dedans:
        dictionary[lemme].update({forme_f:grammaire})

