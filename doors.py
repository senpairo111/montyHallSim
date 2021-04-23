import random


class Doors:
    def __init__(self, switchDoor = bool):
        self.switchDoor = switchDoor
        self.doorarray = [0, 0, 0]
        self.doorarray[random.randrange(2)] = 1
        self.chosenDoor = random.randrange(2)
        self.chosenArrayDoor = self.doorarray[self.chosenDoor]
        self.scored = 0

    def doorSwitcher(self):
        for i in range(2):
            if self.doorarray[i] == 0 and self.chosenDoor != i:
                del self.doorarray[i]
        if self.switchDoor:
            del self.doorarray[self.chosenDoor]
            self.scored = self.doorarray[0]
        else:
            self.scored = self.doorarray[self.chosenDoor]
