from datetime import datetime
import json
now = datetime.now()

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

#achievement menu below
achievementDict = {
    "achievement1": {"haveAchievement": True, "timeComplete": 0, "dateComplete": 0},
    "achievement2": {"haveAchievement": False, "timeComplete": 0, "dateComplete": 0}
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
    playerResponse = input("Would you like to create a new save file?    Type Yes or No")
    if playerResponse == "Yes":
        
    elif playerResponse == "No":

    else:
        print("That wasn't an option, please try again.")
    with open(save, 'w') as f:
        json.dump(achievementDict, f)
        print("Game Saved")

#Loading saves
def loadSave():
    
        
                           

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