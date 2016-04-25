#Client.py
#Prototype developed by Jackson Walker
#ALL COMMANDS ARE LOWERCASE

from Tkinter import *
from socket import *
import random

def randomColor():
    colors = ["red", "orange", "yellow", "green", "blue", "violet"]
    stringColorOut = random.choice(colors)
    return stringColorOut

def sendMessage(out):
    outMessage = out
    clientSocket.send(outMessage)
    return 0

def b00():
    return 0

#tkinter startup
root = Tk()
root.wm_title("Net Tac Toe")
root.geometry('{}x{}'.format(250, 250))

topFrame = Frame(root)
topFrame.pack()
middleFrame = Frame(root)
middleFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()
bottomestFrame = Frame(root)
bottomestFrame.pack()

#initializeButtons(topFrame, middleFrame, bottomFrame)
####INITIALIZE BUTTS####
button00 = Button(bottomFrame, text ="0,0",fg = randomColor(), command=b00)
button10 = Button(bottomFrame, text="1,0", fg=randomColor())
button20 = Button(bottomFrame, text="2,0", fg=randomColor())
button01 = Button(middleFrame, text="0,1", fg=randomColor())
button11 = Button(middleFrame, text="1,1", fg=randomColor())
button21 = Button(middleFrame, text="2,1", fg=randomColor())
button02 = Button(topFrame, text="0,2", fg=randomColor())
button12 = Button(topFrame, text="1,2", fg=randomColor())
button22 = Button(topFrame, text="2,2", fg=randomColor())
buttonTest = Button(bottomestFrame, text= "Send Kent a Test Message", fg = 'black')
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
##BOARD INITALIZED##

serverName = '10.135.51.154'
serverPort = 9050
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send("00x")

root.mainloop()

while 1:
    break
    #allow game to be played
    #send update


    #disable buttons and wait for server response
    #updateBoard()
    #block again for other user
    #updateBoard()




#w, h = 3, 3
#GameBoard = [[0 for x in range(w)] for y in range(h)]



