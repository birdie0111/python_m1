import re
import outils as ot # importer les fonctions dans "outils.py"

# -------------------------------- donnée nécessaire -----------------------------
liste = []
h_aspire = ["hâbler", "hacher", "hachurer", "haïr", "haler", "hâler", "haleter", "hancher", "handicaper", "hanter", "happer", "haranguer", "harasser", "harceler", "harder", "harnacher", "harpailler", "harper", "harponner", "hasarder", "hâter", "haubaner", "hausser", "haver", "havir", "héler", "hercher", "hérisser", "hérissonner", "herscher", "herser", "heurter", "hisser", "hocher", "hongrer", "hongroyer", "honnir", "hoqueter", "hotter", "houblonner", "houer", "houpper", "hourder", "hourdir", "houspiller", "hucher", "huer", "hululer", "humer", "hurler"]
dictionary={} # pour exo 2

# -------------------------------- programme main --------------------------------

with open("dela-fr-public.dic", mode="r",encoding="UTF-16") as fd:
    # -------------------------- Creation de fichier csv ----------------------
    with open("dictionary.csv", mode="a", encoding="UTF-8") as output_f:
        title = "lemme" + '\t' + "forme fléchie" + "\t" + "grammaire" + "\n"
        output_f.write(title)

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
                phrase = lemme + "\t" + forme_f + '\t' + grammaire + '\n'
                phrase_muet = "*" + lemme + "\t" + forme_f + '\t' + grammaire + '\n'
                if(lemme in h_aspire):
                    output_f.write(phrase_muet)
                else:
                    output_f.write(phrase)
                '''


print(dictionary["geler"])




