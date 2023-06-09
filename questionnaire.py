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
import sys

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


    

    def poser(self,num_quest,nb_quest):
        print("QUESTION",num_quest,"/",nb_quest)
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
    def __init__(self, questions ,categorie,titre,difficulte):

        self.questions = questions
        self.categorie = categorie

        self.titre = titre

        self.difficulte = difficulte

    def FromJsonData(data):
        question=data['questions']
        questions=[Question.FromJsonData(i) for i in question ]
        questions=[i for i in questions if i]
          
        return Questionnaire(questions,data["categorie"],data["titre"],data["difficulte"])

        
    def lancer_quest(filename):
        try:
            f=open(filename,"r")
            json_data=f.read()
            f.close()
            questionnaire_data=json.loads(json_data)
        except:
            print("i can't read the file or lunch it check the file form ")
            return None
        return Questionnaire.FromJsonData(questionnaire_data)

    def lancer(self):
        score = 0
        print("Questionnaire:",self.titre)
        print("categorie:",self.categorie)
        print("difficulte:",self.difficulte)
        print("Nombre des questions:",len(self.questions))

        for i in range( len(self.questions)):
            question=self.questions[i]
            if question.poser(i+1,len(self.questions)):
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



#Questionnaire.lancer_quest("cinemas_startrek_debutant.json").lancer()

print(sys.argv)
if len(sys.argv)<2:
    print("Eurreur : choose a file to run ")
    exit(0)

filename=sys.argv[1]
questionnaire=Questionnaire.lancer_quest(sys.argv[1])
if questionnaire:
    questionnaire.lancer()