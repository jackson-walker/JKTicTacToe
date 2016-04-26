from socket import *
from random import *

#Function to handle board updating and victory checking
def BoardUpdating(inMessage, GameBoard):
    VicInt = 0
    chars = list(inMessage)
    if chars[0] == '0':
        if chars[1] == '0':
            GameBoard[0][0] = chars[2]
            #Check column for win
            if GameBoard[0][1] == chars[2] and GameBoard[0][2] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
            #Check row for win
            elif GameBoard[1][0] == chars[2] and GameBoard[2][0] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
            #Check diagonal for win
            elif GameBoard[1][1] == chars[2] and GameBoard[2][2] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
        if chars[1] == '1':
            GameBoard[0][1] = chars[2]
            #Check column for win
            if GameBoard[0][0] == chars[2] and GameBoard[0][2] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
            #Check row for win
            elif GameBoard[1][1] == chars[2] and GameBoard[2][1] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
        if chars[1] == '2':
            GameBoard[0][2] = chars[2]
            #Check column for win
            if GameBoard[0][0] == chars[2] and GameBoard[0][1] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
            #Check row for win
            elif GameBoard[1][2] == chars[2] and GameBoard[2][2] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
            #Check diagonal for win
            elif GameBoard[1][1] == chars[2] and GameBoard[0][2] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2

    if chars[0] == '1':
        if chars[1] == '0':
            GameBoard[1][0] = chars[2]
            #Check column for win
            if GameBoard[1][1] == chars[2] and GameBoard[1][2] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
            #Check row for win
            elif GameBoard[0][0] == chars[2] and GameBoard[2][0] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2

        if chars[1] == '1':
            GameBoard[1][1] = chars[2]
            #Check column for win
            if GameBoard[1][0] == chars[2] and GameBoard[1][2] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
            #Check row for win
            elif GameBoard[0][1] == chars[2] and GameBoard[2][1] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
            #Check diagonal for win
            elif GameBoard[0][0] == chars[2] and GameBoard[2][2] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
            #Check other diagonal for win
            elif GameBoard[2][0] == chars[2] and GameBoard[0][2] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
        if chars[1] == '2':
            GameBoard[1][2] = chars[2]
            #Check column for win
            if GameBoard[1][0] == chars[2] and GameBoard[1][2] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
            #Check row for win
            elif GameBoard[0][2] == chars[2] and GameBoard[2][2] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2

    if chars[0] == '2':
        if chars[1] == '0':
            GameBoard[2][0] = chars[2]
            #Check column for win
            if GameBoard[2][1] == chars[2] and GameBoard[2][2] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
            #Check row for win
            elif GameBoard[0][0] == chars[2] and GameBoard[1][0] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
            #Check diagonal for win
            elif GameBoard[1][1] == chars[2] and GameBoard[0][2] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
        if chars[1] == '1':
            GameBoard[2][1] = chars[2]
            #Check column for win
            if GameBoard[2][0] == chars[2] and GameBoard[2][2] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
            #Check row for win
            elif GameBoard[1][1] == chars[2] and GameBoard[0][1] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
        if chars[1] == '2':
            GameBoard[2][2] = chars[2]
            #Check column for win
            if GameBoard[2][1] == chars[2] and GameBoard[2][0] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
            #Check row for win
            elif GameBoard[1][2] == chars[2] and GameBoard[0][2] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
            #Check diagonal for win
            elif GameBoard[1][1] == chars[2] and GameBoard[0][0] == chars[2]:
                if chars[2] == "x":
                    VicInt == 1
                else:
                    VicInt == 2
    if '-' not in GameBoard:
        VicInt = 3
    print GameBoard
    return (VicInt + inMessage, GameBoard)



#2D arrays with help from http://stackoverflow.com/questions/6667201/how-to-define-two-dimensional-array-in-python
w, h = 3, 3
GameBoard = [["-" for x in range(w)] for y in range(h)]
Player1Char = 'x'
Player2Char = 'y'
serverPort = 9050
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)

while True:
    print 'Waiting for players'
    VicInt = 0;
    Player1Socket, addr1 = serverSocket.accept()
    PlayerRandInt = random.randint(0,10)
    if (PlayerRandInt % 2) == 0:
        Player1Char = 'y'
        Player2Char = 'x'
    print 'Player 1 connected as {0}'.format(Player1Char)
    Player2Socket, addr2 = serverSocket.accept()
    print 'Player 2 connected as {0}'.format(Player2Char)

    while VicInt == 0:

        inMessage = Player1Socket.recv(1024)
        print 'Player 1 move {0}'.format(inMessage)
        outMessage, GameBoard = BoardUpdating(inMessage)
        VicInt = list(outMessage)[0]
        Player1Socket.send(outMessage)
        Player2Socket.send(outMessage)
        if VicInt != 0:
            break;
        inMessage = Player2Socket.recv(1024)
        print 'Player 2 move {0}'.format(inMessage)
        outMessage, GameBoard = BoardUpdating(inMessage)
        Player2Socket.send(outMessage)
        Player1Socket.send(outMessage)
        VicInt = list(outMessage)[0]

    #GBString = str(GameBoard)
    #GBString = GBString.translate(None, '[],\'')
    #GBString = GBString.replace(" ", "")
    #GBString = GBString.replace("x", "1")
    #GBString = GBString.replace("y", "0")
    #print GBString
#outMessage = "0" + inMessage
#clientSocket.send(outMessage)
#clientSocket.close()




