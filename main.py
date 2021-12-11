import re
import outils as ot # importer les fonctions dans "outils.py"

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




