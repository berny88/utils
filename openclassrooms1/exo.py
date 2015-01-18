# -*- coding: utf-8 -*-
import logging
import os

# O = mur
# . = porte
# X = robot
# U = Sortie

""" Example de carte : placées dans ./cartes/
OOOOOOOOOO
O   O O  O
O.O O OO O
O O      O
O OO.OO.OO
OO   O  OO
O O   OO
O   O OO O
O  OO    O
OOOOOOOOOO

row = Y axis
col = X axis
coord 0,0 = left top corner
coord 1,0 = second row / first col
"""

class Robot:
    """Position of Robot in the Map"""
    def __init__(self):
        self.posX = 0
        self.posY = 0

class Play:
    """
    Define the map to play
    This class has a name = the file name which store the game
    This class display on console the map and the Robot position
    """
    def __init__(self, name):
        self.name = name
        self.map = list()
        self.originalMap = list()
        self.robot = Robot()
        logging.info("New Play:: {}".format(self.name))

    def display(self):
        """
        Display a Map directly on console
        """
        logging.info("Display Carte : {}".format(self.name))
        for row in self.map:
            #print(row)
            for cell in row:
                print(cell, end="")
            print("")

    def locateRobot(self):
        """
        find where is the Robot in the original Map
        """
        logging.info("Display Carte : {}".format(self.name))
        for r, row in enumerate(self.map):
            #print(row)
            for c, cell in enumerate(row):
                if (cell == "X"):
                    logging.info("r={} / c={}".format(r, c))
                    self.robot.posX = c
                    self.robot.posY = r

    def checkMap(self):
        """Possibility to control the map"""
        return True

    def move(self, usercmd):
        """compute command entered by user"""
        newPosX = self.robot.posX
        newPosY = self.robot.posY
        logging.info("Avant action :: newPosX={} / newPosY={}".\
            format(newPosX, newPosY))
        step = 1
        cmd = usercmd[0:1]
        if (len(usercmd) != 1):
            stpStr = usercmd[1:]
            if (stpStr.isdigit()):
                step = int(stpStr)
            else:
                step = 0
        if cmd.startswith("E"):
            newPosX = newPosX + step
        elif cmd.startswith("W"):
            newPosX = newPosX - step
        elif cmd.startswith("N"):
            newPosY = newPosY - step
        elif cmd.startswith("S"):
            newPosY = newPosY + step
        elif (cmd == "Q"):
            #quit
            print("Quit")
            return False
        logging.info("newPosX={} / newPosY={}".format(newPosX, newPosY))
        oldCar = ""
        newCar = ""
        if (self.canMove(cmd, self.robot, newPosX, newPosY)):
            oldCar = self.map[newPosY][newPosX]
            logging.info("originalMap[{}] : {}".format(self.robot.posY, \
                self.originalMap[self.robot.posY]))
            if (self.originalMap[self.robot.posY][self.robot.posX] == "."):
                self.map[self.robot.posY][self.robot.posX] = "."
            else:
                self.map[self.robot.posY][self.robot.posX] = " "
            self.robot.posX = newPosX
            self.robot.posY = newPosY
            self.map[newPosY][newPosX] = "X"
            logging.info("self.map[{}]={}".format(newPosY, self.map[newPosY]))
            newCar = self.map[newPosY][newPosX]
        #print(oldCar, newCar)
        if (oldCar == "U" and newCar == "X"):
            print("Bravo, vous avez gagné !!!!!")
            return False #Quit
        return True

    def canMove(self, direction, robot, newPosX, newPosY):
        """test if robot can move on a new coordonate"""
        result = False
        if (newPosY < 0 or newPosY > len(self.map)):
            print ("Déplacement impossible")
        elif (newPosX < 0 or newPosX > len(self.map[newPosY])):
            print ("Déplacement impossible")
        else:
            if (self.isThereWallInDirection(direction, robot, \
                newPosX, newPosY)):
                print("Déplacement impossible (mur sur le chemin)")
                result = False
            else:
                car = self.map[newPosY][newPosX]
                logging.info("self.map[{}]={}".format(newPosY, \
                    self.map[newPosY]))
                logging.info("new coord X={} : Y={} :: {}".\
                    format(newPosX, newPosY, car))
                if (car == "O"):
                    print("Déplacement impossible (mur)")
                else:
                    logging.info("Déplacement possible")
                    result = True
            return result

    def isThereWallInDirection(self, direction, robot, newPosX, newPosY):
        """
        check if there is wall on the path of the robot
        """
        sub = list()
        if direction.startswith("E"):
            logging.info("isThereWallInDirection:: {} : {} {}".format(\
                self.map[newPosY], robot.posX + 1, newPosX))
            sub = self.map[newPosY][robot.posX:newPosX + 1]
        elif direction.startswith("W"):
            logging.info("isThereWallInDirection:: {} : {} {}".format(\
                self.map[newPosY], newPosX, robot.posX))
            sub = self.map[newPosY][newPosX:robot.posX]
        elif direction.startswith("N"):
            sub1 = self.map[newPosY:self.robot.posY]
            for x in sub1:
                sub.append(x[self.robot.posX])
        elif direction.startswith("S"):
            sub1 = self.map[self.robot.posY:newPosY]
            for x in sub1:
                sub.append(x[self.robot.posX])
        logging.info("sub : {}".format(sub))
        if ("O" in sub):
            print("Déplacement Impossible car mur sur le trajet")
            return True
        else:
            return False


def loadPlays():
    playList = dict()
    logging.info(os.listdir("./cartes"))
    #each map are stored in one file in subdirectory "cartes"
    for i, mapFile in enumerate(os.listdir("./cartes")):
        logging.info("./cartes/" + mapFile)
        name = mapFile.replace(".txt", "")
        newPlay = Play(name)
        playList[i] = newPlay
        with open("./cartes/" + mapFile, "r") as myFile:
            rows = myFile.readlines()
            for row in rows:
                #row definition
                line = row.replace("\n", "")
                #print("line={0} - nbOfLines={1}".format(line, len(newPlay.map)))
                newPlay.map.append(splitRow(line))
                newPlay.originalMap.append(splitRow(line))
    for play in playList.values():
        #play.display()
        if (not newPlay.checkMap()):
            print("error in Map")
    return playList


def splitRow(row):
    result = list()
    for pos in row:
        result.append(pos)
    return result

def displayFirstMenu(playList):
    """Display the main menu and control the choice"""
    choiceInt = -1
    print("Labyrinthes existants : ")
    for i, key in enumerate(playList):
        play = playList[key]
        print("\t{} - {}".format(i, play.name))
    res = input("\t\t Entrez un numéro de labyrinthe pour commencer à jouer ? (pour quitter tapper Q) : ")
    if (not res == "Q"):
        if (res.isdigit()):
            choiceInt = int(res)
            if (not choiceInt < len(playList)):
                print("Choix incorrect : Saisir entre 0 et {}".\
                    format(len(playList) - 1))
                choiceInt = displayFirstMenu(playList)
        else:
            choiceInt = displayFirstMenu(playList)
    return choiceInt


def enterAction(play):
    os.system('cls')
    os.system('clear')
    play.display()
    logging.info(play.locateRobot())
    res = input("\t\t Saisissez une action ? (pour quitter tapper Q) : ")
    if (play.move(res.upper())):
        enterAction(play)
        logging.info("move")


def menu():
    """Display the menu before play : to choose the game available"""
    os.system('cls')
    os.system('clear')
    playList = loadPlays()
    choiceInt = displayFirstMenu(playList)
    if (choiceInt == -1):
        print("Bye")
    else:
        play = playList[choiceInt]
        enterAction(play)
# ************************
#
def main():
    logging.basicConfig(format='%(asctime)s|%(levelname)s|%(message)s',
        filename='exo1.log', level=logging.DEBUG)
    logging.info('Started')#
    menu()
    logging.info('Finished')

if __name__ == '__main__':
    main()