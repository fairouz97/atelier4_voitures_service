from employe import Employe
from voiture import Voiture


v1 = Voiture("AA123", 2022, "Toyota", 40000)
v2 = Voiture("BB456", 2021, "BMW", 30000)

e1 = Employe("P111", "Ali", "Karim")
e2 = Employe("P222", "Sara", "Amine")


e1.affecterVoiture(v1)

e1.afficherInformations()
v1.afficherInformations()
e2.affecterVoiture(v1)
