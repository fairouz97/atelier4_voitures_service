class Voiture:

    def __init__(self, matricule, annee, marque, kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None

    def afficherInformations(self):
        print("Matricule :", self.matricule)
        print("Marque :", self.marque)
        print("Année :", self.annee)
        print("Kilometrage :", self.kilometrage)

        if self.chauffeur:
            print("Chauffeur :", self.chauffeur.nom)
        else:
            print("Aucun chauffeur")