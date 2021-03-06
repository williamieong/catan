#
# Catan starter code
##
# Alex Rosenfeld
# Jake Dharmasiri
# William Ieong

debug = True

class Player:
    def __init__(self, name="" , color=""):
        self.name = name
        if str.lower(color) in\
           ["black", "white", "orange", "blue", "red"]:
            self.color = color
        else:
            ## THROW ERROR HERE
            print("Please select a color that has not been chosen yet")
            return
        
        # order: brick, ore, sheep, wheat, wood
        self.resources = {'Bricks': 0, 'Ore': 0, 'Sheep': 0, 'Wheat': 0, 'Wood': 0}
        
        # dev_cards = [TBD]

    def __init__(self):
        self.name = ""
        self.color = ""
        self.resources = {'Bricks': 0, 'Ore': 0, 'Sheep': 0, 'Wheat': 0, 'Wood': 0}
        
    def __repr__(self):
        s = "Name: " + self.name + \
            "\nColor: " + self.color +\
            "\nCurrent resources:\n"
        for key in self.resources:
            s += "Number of " + key + ": " + str(self.resources[key]) + "\n"
        return s

    def add_resource(self, resource):
        self.resources[resource] += 1

    def subtract_resource(self, resource):
        self.resources[resource] -= 1


