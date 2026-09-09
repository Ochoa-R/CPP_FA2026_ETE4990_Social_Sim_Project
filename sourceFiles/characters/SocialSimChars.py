# Social Sim Game Project
# Antonio Ochoa, Joseph Endozo

class Character:
    """Parent class designed to hold the name of a character
    in the game"""
    def __init__(
        self, 
        traits = {
            "Name": "",
            "Hair Color": "",
            "Blood Type": "",
            "Preferred Compliment": ""
        }
    ):
        self.traits = traits

class Player(Character):
    """Child class of parent, represents the user's player
    character. Contains an inventory that the player can hold
    gift items in and access during the beginning of the day"""
    def __init__(
        self, 
        playerTraits, 
        inventory=["Apple"], 
        energy = 0
    ):
        super().__init__(playerTraits)
        self.inventory = inventory
        self.energy = energy
    def openInventory(self):
        if len(self.inventory) == 0:
            print("Inventory empty!\n")
        else:
            count = 1
            for item in self.inventory:
                print(count,")",item)
                count += 1
    def giveItem(self):
        response = input("Which item would you like to gift?: ")
        if response in self.inventory:
            self.inventory.pop(response)
            return response
        else:
            print("You don't have that!")
'''
class NPC(Character):
    """Child class of parent, represents a non-player
    character that the player can interact with. Contains
    preferences for items they like and dislike, as well as
    an attachment score that influences the win condition"""
    def __init__(self, npcName, preferences = {"likes": [], "dislikes": []}):
        super().__init__(npcName, attachment=0)
        self.preferences = preferences
        self.attachment = 0
    def receiveGift(self, gift):
        if gift in self.preferences["likes"]:
            print(f"{self.name} likes your gift!")
            self.attachment += 10
        elif gift in self.preferences["dislikes"]:
            print(f"{self.name} didn't like your gift...")
            self.attachment -= 10
        else:
            pirint(f"{self.name} appreciated the thought.")
'''       
        

def getPlayerInfo():
    infoHold = Character()
    for key in infoHold.traits.keys():
        attribute = ""
        confirm = ""
        while confirm != "Yes" and confirm != "yes":
            attribute = input(f"What's your {key}?: ")
            print(f"Your {key} is:", attribute)
            confirm = input("is this okay?: ")
        infoHold.traits[key] = attribute
    return infoHold

mainCharacter = Player(getPlayerInfo())
# print(len(mainCharacter.inventory))
mainCharacter.openInventory()
leave = input("Press any key to leave: ")
