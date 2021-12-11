
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

'''
function: Verifie si "je" doit être élidé
arguments:  
    lemme: le mots
return:
    True ou False
'''
# 雨荷马肖begin
voyelle = ['a','e','i','o','u','h']
def chk_je(lemme):
    if (lemme[0] in voyelle):
        return True
    else:
        return False
# 雨荷马肖end
'''
function: Ajouter un sujet pour chaque conjugaison
arguments:  
        word: un dictionnaire qui contient le mots avec sa grammaire
        i: clé dans le dictionnaire
'''
def add_sujet(word, i):
    if("3s" in word[i]):
        if (chk_je(i)):
            print("j'", i)
        else:
            print("je ", i)
        print("il/elle ", i)
    elif("2s" in word[i]):
        print("tu ", i)
    elif("1p" in word[i]):
        print("nous ", i)
    elif("2p" in word[i]):
        print("vous ", i)
    elif("3p" in word[i]):
        print("ils/elles ", i)

