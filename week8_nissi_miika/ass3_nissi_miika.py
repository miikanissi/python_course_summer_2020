class House:
    def __init__(self, address):
        self.address = address

    def getHouseSize(self, room1, room2, room3):
        size = room1 + room2 + room3
        return "House is " + str(size) + "m²."

class Room:
    def __init__(self, size, floorType):
        self.size = size
        self.floorType = floorType
    
    def getInfo(self):
        return "Room size: " + str(self.size) + "m²" + "\nFloor type: " + str(self.floorType)

class Kitchen:
    def __init__(self, size, floorType):
        self.room = Room(size, floorType)

    def getSize(self):
        return self.room.size
    
    def getKitchenInfo(self):
        return self.room.getInfo()

    def makeFood():
        pass

class LivingRoom:
    def __init__(self, size, floorType):
        self.room = Room(size, floorType)

    def getSize(self):
        return self.room.size
    
    def getLivingRoomInfo(self):
        return self.room.getInfo()
    
    def watchTv(self):
        pass

class Bathroom:
    def __init__(self, size, floorType):
        self.room = Room(size, floorType)

    def getSize(self):
        return self.room.size
    
    def getBathroomInfo(self):
        return self.room.getInfo()
    def brushTeeth(self):
        pass

kitchen1 = Kitchen(15, "wood")
print(kitchen1.getKitchenInfo())

livingroom1 = LivingRoom(20, "wood")
print(livingroom1.getLivingRoomInfo())

bathroom1 = Bathroom(7, "stone")
print(bathroom1.getBathroomInfo())

house1 = House("215st")
print(house1.getHouseSize(kitchen1.getSize(), bathroom1.getSize(), livingroom1.getSize()))
