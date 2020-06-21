class Bird:
    def __init__(self, name, eggCount):
        self.name = name
        self.eggCount = eggCount

    def getInfo(self):
        info = "Birds name is " + self.name + " and they have " + str(self.eggCount) + " eggs."
        return info

    def setName(self, name):
        self.name = name
    def setEggCount(self, eggCount):
        if not 0 < eggCount < 11:
            raise Exception("Egg count must be between 1-10.")
        self.eggCount = eggCount
        

class Migratory(Bird):
    def __init__(self, country, month):
        self.country = country
        self.month = month

    def setCountry(self, country):
        if not 4 < len(country) < 21:
            raise Exception("Country name has to be between 5-20 characters")
        self.country = country.capitalize()
    def setMonth(self, month):
        if not 0 < month < 13:
            raise Exception("Month has to be an integer between 1-12.")
        self.month = month

    def getCountry(self):
        return self.country
    def getMonth(self):
        return self.month

bird1 = Migratory("Finland", 2)
bird1.setName("Crow")
bird1.setEggCount(3)
print(bird1.getInfo())

bird1.setCountry("Italy")
bird1.setMonth(12)
print(bird1.getInfo())
print(bird1.getCountry())
print(bird1.getMonth())

# bird1.setEggCount(20) would cause an exception error
# bird1.setMonth(13) would cause an error
# bird1.setCountry("USA") would cause error
