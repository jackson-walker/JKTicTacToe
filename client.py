#Client.py
#Prototype developed by Jackson Walker
#ALL COMMANDS ARE LOWERCASE

from tkinter import *
from socket import *
import random

def randomColor():
    colors = ["red", "orange", "green", "blue", "violet"]
    stringColorOut = random.choice(colors)
    return stringColorOut

def testMessage(clientSocket):
    di = '00x'
    clientSocket.send(bytes(di, encoding='utf-8'))
    return 0

def sendMessage(self, clientSocket, playerFaction):
    print(playerFaction)
    debug = self.config('text')[-1]
    debug = debug.replace(',', '')
    debug = str(debug)+playerFaction
    print(debug)
    debug = bytes(debug, encoding='utf-8')
    clientSocket.send(debug)
    return 0

def victoryCheck(playerFaction, iVictoryInt):
    # toplevel windows init
    top = Toplevel()

    if iVictoryInt == 1:
        if playerFaction == "x":
            # help from effbot toplevel tutorial
            top.title("You Win!")
            msg = Message(top, text="You are the winner, go gloat")
            msg.pack()
            button = Button(top, text="Dismiss", command=top.destroy)
            button.pack()
        else:
            top.title("You Lose!")
            msg = Message(top, text="git gud")
            msg.pack()
            button = Button(top, text="Dismiss, loser", command=top.destroy)
            button.pack()
    if iVictoryInt == 2:
        if playerFaction == "y":
            # help from effbot toplevel tutorial
            top.title("You Win!")
            msg = Message(top, text="You are the winner, go gloat")
            msg.pack()
            button = Button(top, text="Dismiss", command=top.destroy)
            button.pack()
        else:
            top.title("You Lose!")
            msg = Message(top, text="git gud")
            msg.pack()
            button = Button(top, text="Dismiss, loser", command=top.destroy)
            button.pack()
    if iVictoryInt == 3:  # cat's game
        top.title("Cat's Game")
        msg = Message(top, text="Good effort, champ. Nobody won, just like \'nam")
        msg.pack()
        button = Button(top, text="Dismiss", command=top.destroy)
        button.pack()
    return 0 #all went well

#tkinter startup
root = Tk()
root.wm_title("Net Tac Toe")
root.geometry('{}x{}'.format(250, 120))

topFrame = Frame(root)
topFrame.pack()
middleFrame = Frame(root)
middleFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()
bottomestFrame = Frame(root)
bottomestFrame.pack()

#Initialize Networking
serverName = '10.135.51.154'
serverPort = 9050
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
playerFaction = clientSocket.recv(1024)

#Python 3 string replace features
playerFaction = str(playerFaction).replace('\'', '')
playerFaction = str(playerFaction).replace('b', '')

#create tic tac toe board
w, h = 3, 3
gameBoard = [["-" for x in range(w)] for y in range(h)]

####INITIALIZE BUTTS####
button00 = Button(bottomFrame, text ="0,0",fg = randomColor(), command= lambda: sendMessage(button00, clientSocket, playerFaction))
button10 = Button(bottomFrame, text="1,0", fg=randomColor(), command= lambda: sendMessage(button10, clientSocket, playerFaction))
button20 = Button(bottomFrame, text="2,0", fg=randomColor(), command= lambda: sendMessage(button20, clientSocket, playerFaction))
button01 = Button(middleFrame, text="0,1", fg=randomColor(), command= lambda: sendMessage(button01, clientSocket, playerFaction))
button11 = Button(middleFrame, text="1,1", fg=randomColor(), command= lambda: sendMessage(button11, clientSocket, playerFaction))
button21 = Button(middleFrame, text="2,1", fg=randomColor(), command= lambda: sendMessage(button21, clientSocket, playerFaction))
button02 = Button(topFrame, text="0,2", fg=randomColor(), command= lambda: sendMessage(button02, clientSocket, playerFaction))
button12 = Button(topFrame, text="1,2", fg=randomColor(), command= lambda: sendMessage(button12, clientSocket, playerFaction))
button22 = Button(topFrame, text="2,2", fg=randomColor(), command= lambda: sendMessage(button22, clientSocket, playerFaction))
buttonTest = Button(bottomestFrame, text= "Send Kent a Test Message", fg = 'black', command=testMessage(clientSocket))
button00.pack(side = LEFT)
button10.pack(side = LEFT)
button20.pack(side = LEFT)
button01.pack(side = LEFT)
button11.pack(side = LEFT)
button21.pack(side = LEFT)
button02.pack(side = LEFT)
button12.pack(side = LEFT)
button22.pack(side = LEFT)
buttonTest.pack(side = BOTTOM)
buttonList = [button00, button01, button02, button10, button11, button12, button20, button21, button22]

root.mainloop()

##BOARD INITALIZED##
print("pooploop fam")
while 1:    #game logic loop
    for button in buttonList:
        print("forbegin")
        chars = list(button.config('text')[-1])
        x = int(chars[0])
        y = int(chars[2])
        if gameBoard[x][y] == "-":
            button['state'] = 'normal'
    #endfor

    #inmessage confirmation from server: victory int, x move coord, y move coord, playerFaction
    inMsgConfirm = clientSocket.recv(1024)
    chars = list(inMsgConfirm)
    iVictoryInt = chars[0]  #1 == player x wins, 2 is player y wins, 3 is cat's game
    iXCoord = chars[1]
    iYCoord = chars[2]
    playerFactionConfirm = chars[3]

    #quick error checking for player faction
    if playerFactionConfirm != playerFaction:
        print("SOMETHING REALLY FUCKED UP")

    #update gameBoard
    gameBoard[iXCoord][iYCoord] = playerFactionConfirm

    for button in buttonList:
        chars = list(button.config('text')[-1])
        x = chars[0]
        y = chars[2]
        if x == iXCoord and y == iYCoord:
            button["text"] = str(playerFactionConfirm)

    #disable all buttons while waiting for other player
    for button in buttonList:
        button['state'] = 'disabled'

    victoryCheck(playerFaction, iVictoryInt) #call victory check, should print correct windows



    #update from server on opponent move
    inMsgOppo = clientSocket.recv(1024)

    chars = list(inMsgOppo) #overwrite previous variable in game loop for player turn with opponent
    iVictoryInt = chars[0]  # 1 == player x wins, 2 is player y wins, 3 is cat's game
    iXCoord = chars[1]
    iYCoord = chars[2]
    playerFactionConfirm = chars[3]

    # quick error checking for player faction
    if playerFactionConfirm == playerFaction:
        print("SOMETHING REALLY FUCKED UP")

    # update gameBoard
    gameBoard[iXCoord][iYCoord] = playerFactionConfirm

    for button in buttonList:
        chars = list(button.config('text')[-1])
        x = chars[0]
        y = chars[2]
        if x == iXCoord and y == iYCoord:
            button["text"] = str(playerFactionConfirm)

    victoryCheck(playerFaction, iVictoryInt)
    break
    #allow game to be played
    #send update


    #disable buttons and wait for server response
    #updateBoard()
    #block again for other user
    #updateBoard()




