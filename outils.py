
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
function: faire la partition de la recherche de l'utilisateur
arguments:  
        demande: phrase inséré par l'utilisateur, type chaîne de caractères
return:
        une liste
'''
def split_demande(demande):
    # 用split把用户输入的短语分段
    # 返回一个数组

def chk_je(lemme):
    # 检查je是否要简写成j'
    # 返回 True 或者 False

def lemme_search(lemme, dictionary):
    print("Pour le lemme : " + lemme + ", les résultats de recherche sont:\n")
    # 在dictionary中找出这条lemme的所有变位
    # 用print显示出来

def lemme_mode_search(lemme, mode, dictionary):
    print("Pour le lemme : " + lemme + " en mode de " + mode + ", les résultats de recherche sont:\n")
    # 在dictionary中找出这条 lemme+mode 的所有变位
    # 用print显示出来

def lemme_mode_temps_search(lemme, mode, temps, dictionary):
    print("Pour le lemme : " + lemme + " en mode de " + mode + ", les résultats de recherche sont:\n")
    # 在dictionary中找出这条 lemme+mode+temps 的所有变位
    # 用print显示出来

