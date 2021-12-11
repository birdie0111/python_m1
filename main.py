import outils as ot # importer les fonctions dans "outils.py"
from tkinter import *
# -------------------------------- donnée nécessaire -----------------------------
# 雨荷马肖begin
h_aspire = ["hâbler", "hacher", "hachurer", "haïr", "haler", "hâler", "haleter", "hancher", "handicaper", "hanter", "happer", "haranguer", "harasser", "harceler", "harder", "harnacher", "harpailler", "harper", "harponner", "hasarder", "hâter", "haubaner", "hausser", "haver", "havir", "héler", "hercher", "hérisser", "hérissonner", "herscher", "herser", "heurter", "hisser", "hocher", "hongrer", "hongroyer", "honnir", "hoqueter", "hotter", "houblonner", "houer", "houpper", "hourder", "hourdir", "houspiller", "hucher", "huer", "hululer", "humer", "hurler"]
search_filtre = ["W","K","G","P","I","J","F","C","S","Y"] # les temps et modes disponibles pour faire un recherche
dictionary={} # pour exo 2
# 雨荷马肖end
# -------------------------------- programme main --------------------------------

with open("dela-fr-public.dic", mode="r",encoding="UTF-16") as fd:
    # -------------------------- Creation de fichier csv ----------------------
    # 雨荷马肖begin
    with open("dictionary.csv", mode="a", encoding="UTF-8") as output_f:
        title = "lemme" + '\t' + "forme fléchie" + "\t" + "grammaire" + "\n"
        output_f.write(title)
    # 雨荷马肖end
    # -------------------------- Traitement de texte dans .dic ----------------
        line = fd.readline().strip()
        while line:
            line = fd.readline().strip()
            if (".V" in line):
                # partition des elements dans chaque ligne
                verb = line.split(".")[0]
                grammaire = line.split(".")[1]
                lemme = verb.split(",")[1]
                forme_f = verb.split(",")[0]
                # ajoute dans la variable dictionary
                ot.add_dict(lemme, forme_f, grammaire, dictionary)

                # ajoute dans le fichier .csv
                '''
        # 雨荷马肖begin
                phrase = lemme + "\t" + forme_f + '\t' + grammaire + '\n'
                phrase_muet = "*" + lemme + "\t" + forme_f + '\t' + grammaire + '\n'
                if(lemme in h_aspire):
                    output_f.write(phrase_muet)
                else:
                    output_f.write(phrase)
        # 雨荷马肖end
                '''
# ---------------------------------------- Treat conjugaison ----------------------------------


#print(dictionary["geler"])
'''
play = "p"
while(play != "q"):
    phrase = input("Entrez votre expression pour recherche, séparez par ',' (par exemple: faire,S)\n")
    phrase = phrase.split(",")
    lemme = phrase[0].lower() # user friendly
    if (lemme in dictionary.keys()):
        word = dictionary[lemme] # tous les conjugaisons de ce mots (type dict)
        # recherche tous les conjugaisons d'un lemme
        if(len(phrase) == 1):
            for i in word.keys():
                ot.add_sujet(word,i)
        # recherche tous les conjugaisons avec un mode d'un lemme
        elif(len(phrase) == 2 and phrase[1].upper() in search_filtre):
            for i in word.keys():
                if(phrase[1].upper() in word[i]):
                    ot.add_sujet(word,i)
        # recherche tous les conjugaisons avec un mode et un temps d'un lemme
        elif(len(phrase) == 3 and phrase[1].upper() in search_filtre and phrase[2].upper() in search_filtre):
            for i in word.keys():
                if(phrase[1].upper() in word[i] and phrase[2].upper() in word[i]):
                    ot.add_sujet(word,i)
    else:
        print("Invalid search")
    play = input("Si vous voulez quitter le programme, tapez q, sinon, tapez Enter\n")
'''
def add_s(word, i):
    if("3s" in word[i]):
        if (ot.chk_je(i)):
            phrase="j'" + i + "\n"
            txt.insert(END,phrase)
        else:
            phrase="je " + i + "\n"
            txt.insert(END,phrase)
        phrase="il/elle " + i  + "\n"
        txt.insert(END,phrase)
    elif("2s" in word[i]):
        phrase="tu " + i + "\n"
        txt.insert(END,phrase)
    elif("1p" in word[i]):
        phrase="nous " + i + "\n"
        txt.insert(END,phrase)
    elif("2p" in word[i]):
        phrase="vous " + i + "\n"
        txt.insert(END,phrase)
    elif("3p" in word[i]):
        phrase="ils/elles " + i + "\n"
        txt.insert(END,phrase)



def search(dictionary):
    txt.delete(1.0,END)
    lemme = inp1.get().lower() # user friendly
    temps = inp2.get().lower()
    modes = inp3.get().lower()
    if (lemme in dictionary.keys()):
        word = dictionary[lemme] # tous les conjugaisons de ce mots (type dict)
        # recherche tous les conjugaisons d'un lemme
        if(temps == "" and modes == ""):
            for i in word.keys():
                add_s(word,i)
        # recherche tous les conjugaisons avec un mode d'un lemme
        elif(modes == "" and temps.upper() in search_filtre):
            for i in word.keys():
                if(temps.upper() in word[i]):
                    add_s(word,i)
        # recherche tous les conjugaisons avec un mode et un temps d'un lemme
        elif( temps.upper() in search_filtre and modes.upper() in search_filtre):
            for i in word.keys():
                if(temps.upper() in word[i] and modes.upper() in word[i]):
                    add_s(word,i)
    else:
        print("Invalid search")
        txt.insert(END,"Invalid search")
    


root = Tk()
root.geometry('500x500')
root.title("user-friendly version")

frm_left = Frame(root)
frm_left.grid(column=0,row=0)
frm_right = Frame(root)
frm_right.grid(column=1,row=0)

lab1 = Label(frm_left, text='Insérez votre phrase pour rechercher\n les conjugaisons des mots',\
                        width="50")
lab1.pack()
txt = Text(frm_left, width="50")
txt.pack()


lemme = Label(frm_right, text="lemme", width="15")
lemme.pack()
inp1 = Entry(frm_right, width="15")
inp1.pack()
temps = Label(frm_right, text="temps ou modes", width="15")
temps.pack()
inp2 = Entry(frm_right, width="15")
inp2.pack()
modes = Label(frm_right, text="temps ou modes", width="15")
modes.pack()
inp3 = Entry(frm_right, width="15")
inp3.pack()
btt = Button(frm_right, text="recherche", command=lambda: search(dictionary))
btt.pack()
root.mainloop()



