# Social Sim Game Project
# Antonio Ochoa's Code

class Character:
    """Parent class designed to hold the traits of a character
    in the game"""
    def __init__(
        self, 
        traits
    ):
        self.traits = traits


class Inventory:
    """Class for managing the player's inventory, with functions for adding and
        removing items, opening and closing, and returning whether the
        inventory is opened or closed"""
    def __init__(self, inventory = [], invState = False):
        self.__inventory = inventory
        self.__invState = invState
    
    @property
    def inventory(self):
        """Return the player's current inventory"""
        return self.__inventory
    @inventory.setter
    def inventory(self, loadedInv):
        self.__inventory = loadedInv
    def isOpen(self):
        """Return whether or not the inventory is currently open"""
        return self.__invState
    def open(self):
        """Open the player's inventory if any items are in it. Used to 
        support menu logic"""
        if len(self.__inventory) == 0:
            print("Inventory empty!\n")
        else:
            self.__invState = True
    def close(self):
        """Close the player's inventory. Used to support menu logic"""
        self.__invState = False
    def checkForItem(self, name):
        """checks whether a given item exists in the player's current inventory.
        Used for error handling before returning or editing inventory values."""
        for item in self.__inventory:
            # print(item.values())
            if name in item.values():
                return item
        else:
            return False
    def addItem(self, item):
        """Adds an item to the player's inventory"""
        self.__inventory.append(item)
    def readItemName(self, item):
        """Returns the name of an item in the player's inventory"""
        return item["Name"]
    def readItemDesc(self, selectedItem):
        """Returns the description of a chosen item in the player's inventory,
        if it exists. Otherwise, states that the player does not have that
        item."""
        item = self.checkForItem(selectedItem)
        if item:
            return item["Description"]
        else:
            return "You don't have that!"
    def readCurrentInventory(self):
        """Prints the names of all items currently in inventory in a numbered
        list"""
        count = 1
        for item in self.__inventory:
            print(f"{count}) {self.readItemName(item)}")
            count += 1
        

class Player(Character):
    """Child class of parent, represents the user's player
    character. Contains an inventory that the player can hold
    gift items in and access during the beginning of the day"""
    def __init__(
        self, 
        playerTraits = {
            "Name": "",
            "Hair Color": "",
            "Eye Color": "",
            "Blood Type": "",
            "Preferred Compliment": ""
        }, 
        inventory=Inventory(), 
        energy = 0
    ):
        super().__init__(playerTraits)
        self.inventory = inventory
        self.energy = energy

    def checkStats(self):
        """Prints out the player's current stats"""
        for key, value in self.traits.items():
            print(f"{key}: {value}")
        print(f"Current energy: {self.energy}")

    def giveGift(self, item):
        gift = {}

class NPC(Character):
    """Child class of parent, represents a non-player
    character that the player can interact with. Contains
    preferences for items they like and dislike, as well as
    an attachment score that influences the win condition"""
    def __init__(
        self, 
        npcTraits = {
            "Name": "",
            "Hair Color": "",
            "Eye Color": "",
            "Blood Type": ""
        }, 
        preferences = {
            "Likes": [], 
            "Dislikes": []
        }
    ):
        super().__init__(npcTraits)
        self.preferences = preferences
        self.attachment = 0
        
    def receiveGift(self, gift):
        if gift["Name"] in self.preferences["Likes"]:
            print(f"{self.name} likes your gift!")
            self.attachment += 10
        elif gift["Name"] in self.preferences["Dislikes"]:
            print(f"{self.name} didn't like your gift...")
            self.attachment -= 10
        else:
            print(f"{self.name} appreciated the thought.")     

def getPlayerInfo():
    """Prompts the player for the required info to store into a Player object. 
    Will loop until the player confirms their selection."""
    infoHold = Player()
    confirm = ""
    while confirm != "Yes" and confirm != "yes":
        for key in infoHold.traits.keys():
            attribute = input(f"What's your {key}?:")
            infoHold.traits[key] = attribute
        for key, value in infoHold.traits.items():
            print(f"Your {key} is: {value}")
        confirm = input("is this okay? (yes / no): ")
    return infoHold

def loadNPC(npcName):
    """Loads the data for the specified NPC from the json."""
    npcFile = "charFiles/npcs.json"
    loadedNPC = NPC()
    with open(npcFile) as file:
        npcData = json.load(file)
        loadedNPC.traits = npcData[npcName][0]
        loadedNPC.preferences = npcData[npcName][1]
    print(f"{npcName} loaded!")
    return loadedNPC

def loadPlayer():
    """Loads previously existing data for the player, if it exists."""
    playerFile = "charFiles/charSave.json"
    loadedPlayer = Player()
    with open(playerFile) as file:
        playerData = json.load(file)
        loadedPlayer.traits = playerData["Traits"]
        loadedPlayer.inventory.inventory = playerData["Inventory"]
        loadedPlayer.energy = playerData["Energy"]
    return loadedPlayer

def savePlayer(player):
    """Creates a fresh save for the current player."""
    with open("charFiles/charSave.json", "w") as file:
        playerData = {
            "Traits": player.traits,
            "Inventory": player.inventory.inventory,
            "Energy": player.energy
        }
        json.dump(playerData, file)
        

def displayOptions(**options):
    """Displays options for the menu that is passed in."""
    for optionNumber, optionDesc in options:
        print(f"{optionNumber}) {optionDesc["action"]}")

def testBlock():
    itemFile = "charFiles/gameItems.json"
    itemList = []
    with open(itemFile) as file:
        itemList = json.load(file)
    try:
        mainCharacter = loadPlayer()
    except FileNotFoundError:
        mainCharacter = getPlayerInfo()
        for item in itemList:
            mainCharacter.inventory.addItem(item)
    savePlayer(mainCharacter)
    date = loadNPC("Magus")
    print(f"{date.traits["Name"]} wants to hang out!")

    while True:
        try:
            print("What would you like to do?")
            print(
                " 1) leave\n",
                "2) check stats\n",
                "3) open inventory"
            )
            action = int(input("(type the number of the action you want to perform):"))
            if action == 1:
                break
            elif action == 2:
                mainCharacter.checkStats()
            elif action == 3:
                mainCharacter.inventory.open()
                while mainCharacter.inventory.isOpen():
                    mainCharacter.inventory.readCurrentInventory()
                    print("What would you like to do with your inventory?")
                    print(
                        " 1) close\n",
                        "2) read item description"
                    )
                    try:
                        menuAction = int(input("(type the number of the action you want to perform):"))
                        if menuAction == 1:
                            mainCharacter.inventory.close()
                        elif menuAction == 2:
                            print("What item would you like to see the description of?")
                            print(mainCharacter.inventory.readItemDesc(
                                input("(type the name of the item): ")
                            ))
                        else:
                            print("That's not an option!")
                    except ValueError:
                        print("That's not an option!")               
            else:
                print("That's not an option!")
        except ValueError:
             print("That's not an option!")

testBlock()
