from random import choice, randint

class Animal:
    ESPECES_INCOMPATIBLES = {
        'zèbre':('lion','crocodile'),
        'hippopotame': 'lion',
        'gazelle':('lion','crocodile'),
        'crocodile':('zèbre','gazelle'),
        'lion':('zèbre','hippopotame','gazelle','crocodile'),
        'elephant': (),
        'lapin': ('lion', 'crocodile')
    }
    identifiant = 1

    ESPECES_CREATION=["zèbre", "elephant", "lion", "gazelle", "hippopotame", "crocodile", "lapin"]
    ESPECES = {
        "zèbre" : {'name': 'zèbre', 'poids_min': 10, 'poids_max': 300},
        "elephant" : {'name': 'elephant', 'poids_min': 100, 'poids_max': 5000},
        "gazelle": {'name': 'gazelle', 'poids_min': 80, 'poids_max': 3000},
        "crocodile" : {'name': 'crocodile', 'poids_min': 80, 'poids_max': 4000},
        "lion" : {'name': 'lion', 'poids_min': 60, 'poids_max': 1500},
        "lapin" : {'name': 'lapin', 'poids_min': 1, 'poids_max': 9},
        "hippopotame" : {'name': 'hippopotame', 'poids_min': 100, 'poids_max': 3000},
    }

    def __init__(self, nom:str, sexe:str, poids:int, espece:str, age:int):
        self.nom = nom
        self.sexe = sexe
        self.poids = poids
        if self.poids < Animal.ESPECES[espece]['poids_min'] or self.poids > Animal.ESPECES[espece]['poids_max']:
            raise ValueError("Le poids est incompatible avec l'espèce")
        self.espece = espece
        self.age = age
        self.faim = 5
        self.is_reproduced = False
        self.id = Animal.identifiant
        Animal.identifiant +=1


    def description(self):
        if self.sexe == "m":
            return "id:" + str(self.id) + "nom: " + self.nom + " : " + self.espece + " Male, " + str(self.age//365) + "ans " + str(self.poids) + "kg"
        else:
            return "id:" + str(self.id) + "nom: " + self.nom + " : " + self.espece + " Female, " + str(self.age//365) + "ans " + str(self.poids) + "kg"


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
        if self.espece.lower() not in Animal.ESPECES_INCOMPATIBLES.keys():
            print("Espèce non repertoriée")
            return True
        return other.espece.lower() not in Animal.ESPECES_INCOMPATIBLES[self.espece.lower()]


    @classmethod
    def animal_random_creation(cls) -> 'Animal':
        espece = choice(Animal.ESPECES_CREATION)
        sexe = choice(('m', 'f'))
        poids = randint(Animal.ESPECES[espece]['poids_min'], Animal.ESPECES[espece]['poids_max'])
        age = 0
        name = espece + "_" + str(Animal.identifiant)
        return Animal(name, sexe, poids, espece, age)
