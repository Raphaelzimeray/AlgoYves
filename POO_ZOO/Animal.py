from random import choice

class Animal:
    ESPECES_INCOMPATIBLES = {
        'zèbre':('lion','crocodile'),
        'hippopotame': 'lion',
        'gazelle':('lion','crocodile'),
        'crocodile':('zèbre','gazelle'),
        'lion':('zèbre','hippopotame','gazelle','crocodile')
    }
    identifiant = 1

    def __init__(self, nom:str, sexe:str, poids:int, espece:str, age:int):
        self.nom = nom
        self.sexe = sexe
        self.poids = poids
        self.espece = espece
        self.age = age
        self.faim = 5
        self.is_reproduced = False
        self.id = Animal.identifiant
        Animal.identifiant +=1


    def description(self):
        if self.sexe == "m":
            return self.nom + " : " + self.espece + " Male, " + str(self.age//365) + "ans " + str(self.poids) + "kg"
        else:
            return self.nom + " : " + self.espece + " Female, " + str(self.age//365) + "ans " + str(self.poids) + "kg"

    def nourrir(self):
        self.faim = max(0, self.faim -5)

# utilisation du type du nom de classe au sein de la classe avec ''
    def reproduction(self, a2:'Animal') -> 'Animal':
        if self.age < 365 or a2.age < 365 \
            or self.faim >= 5 or a2.faim >= 5 \
            or self.sexe == a2.sexe \
            or self.espece != a2.espece:
            return None
        bb_name = "Enfant de " + self.nom + " et " + a2.nom
        bb_sexe = choice(('m', 'f'))
        bb_poids = int(((self.poids + a2.poids) / 2) * 0.05)
        bb_espece = self.espece
        bb_age = 0
        return Animal(bb_name, bb_sexe, bb_poids, bb_espece, bb_age)

    def compatibilite(self, other:'Animal') -> bool:
        return other.espece not in Animal.ESPECES_INCOMPATIBLES[self.espece]
