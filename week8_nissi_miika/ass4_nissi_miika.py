class Elevator:
    def __init__(self, currentFloor):
        self.currentFloor = currentFloor

    def getCurrentFloor(self):
        return "Elevator is on floor " + str(self.currentFloor)

    def move(self, goalFloor):
        self.currentFloor = goalFloor
        return "Moved to floor " + str(self.currentFloor)

class FloorButton:
    def __init__(self, requestFloor):
        self.requestFloor = requestFloor

    def newFloorRequest(self, Elevator):
        Elevator.move(self.requestFloor)

class ElevatorButton:
    def __init__(self, goalFloor):
        self.goalFloor = goalFloor

    def goalFloorRequest(self, Elevator):
        Elevator.move(self.goalFloor)

elevator1 = Elevator(1)
print(elevator1.getCurrentFloor())
floorButton1 = FloorButton(4)
floorButton1.newFloorRequest(elevator1)
print(elevator1.getCurrentFloor())
elevatorButton1 = ElevatorButton(2)
elevatorButton1.goalFloorRequest(elevator1)
print(elevator1.getCurrentFloor())
