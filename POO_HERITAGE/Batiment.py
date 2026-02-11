class Batiment:
    def __init__(self, adress:str, surface:int):
        self.adress = adress
        self.surface = surface


    def __str__(self):
        return "Adresse : " + self.adress + " , Surface habitable: " + str(self.surface)

    def get_category(self) -> int:
        if self.surface < 30:
            return 1
        if self.surface < 70:
            return 2
        else:
            return 3
