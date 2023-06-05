# PROJET QUESTIONNAIRE V3 : POO
#
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement
#
# -> Définir les entitées (données, actions)
#
# Question
#    - titre       - str
#    - choix       - (str)
#    - bonne_reponse   - str
#
#    - poser()  -> bool
#
# Questionnaire
#    - questions      - (Question)
#
#    - lancer()
#
import json
import os

# def data_recieve():
#     import os

#     # Get the current directory
#     current_directory = os.getcwd()

#     # List all files in the directory
#     files = os.listdir(current_directory)

#     # Filter out JSON files
#     json_files = [file for file in files if file.endswith('.json')]

#     # Print the JSON files
#     for file in json_files:
#         print(file)
#         with open (file,'r') as file:
#             ch=json.load(file)
#             print(ch)
class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def FromJsonData(data):
        choix=[i[0] for i in data["choix"]]
        Br=[i[0] for i in data["choix"] if i[1]]
        
        if len(Br)!=1:
            return None
        bonne_rep=''.join(Br)
        q = Question(data["titre"], choix, bonne_rep)
        return q

    def poser(self):
        print("QUESTION")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i])
        
        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
    
        if self.choix[reponse_int-1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    def lancer(self):
        score = 0
        for question in self.questions:
            if question.poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score


"""questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

lancer_questionnaire(questionnaire)"""

# q1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
# q1.poser()

# data = (("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris", "Quelle est la capitale de la France ?")
# q = Question.FromData(data)
# print(q.__dict__)


#Questionnaire(
 #   (
        
#    )
#).lancer()


filename="fruit_pomme_confirme.json"
f=open(filename,"r")
json_data=f.read()
f.close()
questionnaire_data=json.loads(json_data)
question=questionnaire_data['questions']
q=Question.FromJsonData(question[0])
q.poser()



