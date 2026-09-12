from datetime import datetime
import json
now = datetime.now()
id_list = []

def startGame():
    askUserAfterStart = input("New Game | Load Save | Achievements | Exit")
    if askUserAfterStart == "New Game":
        newGame()
    elif askUserAfterStart == "Load Save":
        loadSave()
    elif askUserAfterStart == "Achievements":
        openAchievementsMenu()
    elif askUserAfterStart == "End Game":
        exitGame()
    else
        print("Invalid Function")

saves = {
    0: {
        "achievement1": {
            "haveAchievement": True, 
            "timeComplete": "hello", 
            "dateComplete": "your mom"},
        "achievement2": {
            "haveAchievement": False, 
            "timeComplete": 0, 
            "dateComplete": 0
        }
    }
}
#achievement menu below
achievementDict = {
    "achievement1": {
        "haveAchievement": True, 
        "timeComplete": "hello", 
        "dateComplete": "your mom"},
    "achievement2": {
        "haveAchievement": False, 
        "timeComplete": 0, 
        "dateComplete": 0
    }
}

def achievementGet(refAchiev):
    if achievementDict[refAchiev]["haveAchievement"] == True:
        return
    else:
        achievementDict[refAchiev]["haveAchievement"] = True
        achievementDict[refAchiev]["timeComplete"] = f"{now.hour}:{now.minute}"
        achievementDict[refAchiev]["dateComplete"] = f"{now.month}/{now.day}/{now.year}"

#Creating Saves
def saveGame():
    def saveGame():
    filename = "save"
    #Check if user has save file already
    if fileExistsCheck() == False:
        #Creates new save file
        id_list.append(0)
        with open(filename, 'w') as f:
            json.dump(saves, f)
    #Creates a new save depending on input
    elif fileExistsCheck() == True:
        #Creates a new save
        newSaveResponse = input("Would you like to create a new save?    Type Yes or No")
        if playerResponse == "Yes":
            #Appends the new save ID to a list then saves the achievement dictionary to that ID
            id_list.append(len(id_list))
            saves[len(id_list) - 1] = achievementDict
            with open(filename, 'w') as f:
                json.dump(saves, f)
        elif playerResponse == "No":
            #Replaces the specified save the user chooses
            print("Please type the number of save you want to replace")
            for number in id_list:
                print("Save ", number)
            replaceSaveResponse = int(input())
            saves[replaceSaveResponse] = achievementDict
            with open(filename, 'w') as f:
                json.dump(saves,f)
    else:
        print("Something went wrong here.... Please try again")

#Loading saves
def loadSave():
    filename = 'saves_file'
    with open(filename) as f:
        saves = json.load(f)
    print("Please choose which save you would like to load")
    for number in id_list
        print(id_list[number])
    loadSaveResponse = input()
    achievementDict = saves[loadSaveResponse]
                           

def newGame():
    print("new works")

def openAchievementsMenu():
    print("Locked Achievements")
    for name, info in achievementDict.items():
        if info["haveAchievement"] == False:
            print(name)

    #Iterates through each achievement in the dictionary and checks if player has achievement
    #If player does have the achievement, it is printed out under Unlocked Achievements
    print("Unlocked Achievements")
    for name, info in achievementDict.items():
        if info["haveAchievement"] == True:
            time = info["timeComplete"]
            date = info["dateComplete"]
            print(name, end="", flush = True)
            print(f" Completed on {time}, {date}")
    input("Type B to go back")
    #I'm sure there will be a lot of clutter over time as the player progresses
    #I searched up a solution but from what I've seen it depends on where the file is ran
    #We should figure this out later

def exitGame():
    print("exit works")
