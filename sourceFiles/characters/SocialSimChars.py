# Social Sim Game Project
# Antonio Ochoa, Joseph Endozo

class Character:
    """Parent class designed to hold the traits of a character
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


class Inventory:
    """Class for managing the player's inventory, with functions for adding and
        removing items, opening and closing, and returning whether the
        inventory is opened or closed"""
    def __init__(self, inventory = [], invState = False):
        self.__inventory = inventory
        self.__invState = invState

    def isOpen(self):
        return self.__invState
    def open(self):
        if len(self.__inventory) == 0:
            print("Inventory empty!\n")
        else:
            count = 1
            for item in self.__inventory:
                print(f"{count}) {self.readItemName(item)}")
                count += 1
            self.__invState = True
    def close(self):
        self.__invState = False 
    def addItem(self, item):
        self.__inventory.append(item)
    def readItemName(self, item):
        return item["Name"]
    def readItemDesc(self, selectedItem):
        for item in self.__inventory:
            if item["Name"] == selectedItem:
                    return item["Description"]
        else:
            return "You don't have that!"

class Player(Character):
    """Child class of parent, represents the user's player
    character. Contains an inventory that the player can hold
    gift items in and access during the beginning of the day"""
    def __init__(
        self, 
        playerTraits, 
        inventory=Inventory(), 
        energy = 0
    ):
        super().__init__(playerTraits)
        self.inventory = inventory
        self.energy = energy
    '''
    def giveItem(self):
        response = input("Which item would you like to gift?: ")
        if response in self.inventory:
            self.inventory.pop(response)
            return respons
            e
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
    '''
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
    confirm = ""
    while confirm != "Yes" and confirm != "yes":
        for key in infoHold.traits.keys():
            attribute = input(f"What's your {key}?:")
            infoHold.traits[key] = attribute
        for key, value in infoHold.traits.items():
            print(f"Your {key} is: {value}")
        confirm = input("is this okay?: ")
    return infoHold

def checkPlayerStats():
    chungs = 5

def main():
    
    mainCharacter = Player(getPlayerInfo())
    # print(len(mainCharacter.inventory))
    mainCharacter.inventory.open()

    giftItem = {
        "Name": "Apple",
        "Description": "A succulent, yet healthy snack. A favorite of those who take their nutrition seriously!"
    }

    giftItemTwo = {
        "Name": "Masamune",
        "Description": "A legendary holy sword used to fell a dark mage in 600 A.D. Smells a bit like a swamp..."
    }
    mainCharacter.inventory.addItem(giftItem)
    mainCharacter.inventory.addItem(giftItemTwo)
    
    mainCharacter.inventory.open()
    while(mainCharacter.inventory.isOpen()):
        try:
            action = int(input(
                "What would you like to do?\n1) close\n2) read item description\n(type the number of the action you want to perform):"))
            if action == 1:
                mainCharacter.inventory.close()
            elif action == 2:
                selectedItem = input("Which item would you like to see the description of?\n(type the name of the item):")
                print(mainCharacter.inventory.readItemDesc(selectedItem))
            else:
                print("That's not an option!")
        except ValueError:
             print("That's not an option!")

main()

