import requests
import json
import unicodedata
open_quizz_db_data = (
    ("Cinemas", "startrek", "https://www.kiwime.com/oqdb/files/3244386486/OpenQuizzDB_244/openquizzdb_244.json"),
    ("Fruit", "Pomme", "https://www.kiwime.com/oqdb/files/1067886592/OpenQuizzDB_067/openquizzdb_67.json"),
    ("Nature", "Arbre Fruitiers", "https://www.kiwime.com/oqdb/files/1012546289/OpenQuizzDB_012/openquizzdb_12.json"),
    ("Cinéma", "Alien", "https://www.kiwime.com/oqdb/files/3241454997/OpenQuizzDB_241/openquizzdb_241.json"),
    ("Cinéma", "Star wars", "https://www.kiwime.com/oqdb/files/1090993427/OpenQuizzDB_090/openquizzdb_90.json"),
)


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def get_quizz_filename(categorie, titre, difficulte):
    return strip_accents(categorie).lower().replace(" ", "") + "_" + strip_accents(titre).lower().replace(" ", "") + "_" + strip_accents(difficulte).lower().replace(" ", "") + ".json"


def generate_json_file(categorie, titre, url):
   # print(url)
    out_questionnaire_data = {"categorie": categorie, "titre": titre, "questions": []}
    out_questions_data = []
    try:
        response = requests.get(url)
    except:
        print("there's no file like ",url)
    else:
        try:
            data = json.loads(response.text)
            all_quizz = data["quizz"]["fr"]
            for quizz_title, quizz_data in all_quizz.items():
                out_filename = get_quizz_filename(categorie, titre, quizz_title)
                #print(out_filename)
                out_questionnaire_data["difficulte"] = quizz_title
                for question in quizz_data:
                    question_dict = {}
                    question_dict["titre"] = question["question"]
                    question_dict["choix"] = []
                    for ch in question["propositions"]:
                        question_dict["choix"].append((ch, ch==question["réponse"]))
                    out_questions_data.append(question_dict)
                out_questionnaire_data["questions"] = out_questions_data
                out_json = json.dumps(out_questionnaire_data)
                # print(out_filename)
                file = open(out_filename, "w")
                file.write(out_json)
                file.close()
                # print("end")
        except:
            print("l'url:",url)

 




for quizz_data in open_quizz_db_data:
    filename=generate_json_file(quizz_data[0], quizz_data[1], quizz_data[2])
  #  
  #  x=[].append(filename)
#print(x)