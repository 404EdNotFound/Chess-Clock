from tkinter import * #Imports all the submodules and packages within Tkinter

#Timer Class created for the 2 chess clocks
class Timer():
    def __init__(self):
        #Attributes are initialised with each separate timer for the player
        self.startTime = self.playerOneTime = self.playerTwoTime = 0 #Hardcoded value as the initial value is set to 5 Minutes in seconds
        self.minutes = self.seconds = 0 #Used for formatting into Minutes and Seconds
        self.running = False #Ensures that the timer runs perfectly
        self.currentPlayer = 1 #Attribute that changes state based on whose turn it is (using basic turn based logic that changes each time)
    
    #Starts the timer when the game begins and updates the time
    def start_time(self):
        if (not self.running):
            self.running = True
            self.updateTime()
    
    #Switches the Player based on whose turn it is and switches each time
    def switchPlayer(self):
        self.currentPlayer = 1 if (self.currentPlayer == 2) else 2
    
    def setTimes(self):
        self.playerOneTime = int(playerOneTimerOptionVar.get()) * 60
        self.playerTwoTime = int(playerTwoTimerOptionVar.get()) * 60
        
        self.minutes, self.seconds = divmod(self.playerOneTime, 60)
        playerOneTimer.config(text = f"{timer.minutes:02d}:{timer.seconds:02d}")
        
        self.minutes, self.seconds = divmod(self.playerTwoTime, 60)
        playerTwoTimer.config(text = f"{timer.minutes:02d}:{timer.seconds:02d}")
    
    #The Function is called to update the time displayed on the interface for the user and when it switches between each player
    def updateTime(self):
        """ Controls the Timing depending on each player, decrements the time based on each player and then formats the time to convert from Seconds to Minutes and Seconds """
        if (self.currentPlayer == 1 and self.running):
            self.playerOneTime -= 1
            self.minutes, self.seconds = divmod(self.playerOneTime, 60)
            playerOneTimer.config(text = f"{timer.minutes:02d}:{timer.seconds:02d}")
        
        elif (self.currentPlayer == 2 and self.running):
            self.playerTwoTime -= 1
            self.minutes, self.seconds = divmod(self.playerTwoTime, 60)
            playerTwoTimer.config(text = f"{timer.minutes:02d}:{timer.seconds:02d}")
        
        self.endGame() #The Function is called once the timer reaches 0 (calls each time and checks each condition)
        window.after(1000, self.updateTime) #The window is updated every second (1000 ms = 1 second and calls a reference to the Update Time function)
    
    #Quits the Interface based on if one timer reaches 0
    def endGame(self):
        if self.playerOneTime < 0 or self.playerTwoTime < 0:
            self.running = False
            quit()
        
        else:
            return

#Used for the button click to ensure that the timer is running and switches between 2 players each time
def updatePlayer():
    if (not timer.running):
        timer.start_time()
    
    else:
        timer.switchPlayer()
    switchButton.config(text = "Switch")

timer = Timer() # 1 Timer Object created for initally formatting the time before it can be used
window = Tk() #Window Created
window.title("Chess Clock") #Window Caption

#Formatting the Timer into Minutes and Seconds
timer.minutes, timer.seconds = divmod(timer.startTime, 60)

#Creates the Frame
chessFrame = Frame(window, background = "white", highlightbackground = "black", highlightthickness = 2)

#Creates the Titles of the 2 players
playerOneLabel = Label(chessFrame, background = "white", foreground = "black", font = ("Verdana", 40, "bold"), text = "Player 1")
playerTwoLabel = Label(chessFrame, background = "white", foreground = "black", font = ("Verdana", 40, "bold"), text = "Player 2")

#Creates the labels for each timer 
playerOneTimer = Label(chessFrame, background = "white", foreground = "black", font = ("Verdana", 40, "bold"), text = f"{timer.minutes:02d}:{timer.seconds:02d}")
playerTwoTimer = Label(chessFrame, background = "white", foreground = "black", font = ("Verdana", 40, "bold"), text = f"{timer.minutes:02d}:{timer.seconds:02d}")

playerOneTimerOptionVar = StringVar()
playerOneTimerOptionEntry = OptionMenu(chessFrame, playerOneTimerOptionVar, 1, 2, 5, 10, 15, 30)

playerTwoTimerOptionVar = StringVar()
playerTwoTimerOptionEntry = OptionMenu(chessFrame, playerTwoTimerOptionVar, 1, 2, 5, 10, 15, 30)

titleFrame = Frame(window, highlightbackground = "black", highlightthickness = 2)
text = Label(titleFrame, text = "Please select a time, it is in Minutes!")

chessButtonFrame = Frame(window, background = "white", highlightbackground = "black", highlightthickness = 2)
switchButton = Button(chessButtonFrame, text = "Start", command = updatePlayer) #Creates the buttons that is used for the user to switch between different players
submitButton = Button(chessButtonFrame, text = "Submit Time Options!", background = "black", foreground = "white", command = timer.setTimes)

#Positions the Frames and Labels
chessFrame.grid(row = 0, column = 0)

playerOneLabel.grid(row = 0, column = 0, padx = 5, pady = 5)
playerTwoLabel.grid(row = 0, column = 1, padx = 5, pady = 5)

playerOneTimer.grid(row = 1, column = 0, padx = 5, pady = 5)
playerTwoTimer.grid(row = 1, column = 1, padx = 5, pady = 5)

playerOneTimerOptionEntry.grid(row = 2, column = 0, padx = 5, pady = 5)
playerTwoTimerOptionEntry.grid(row = 2, column = 1, padx = 5, pady = 5)

titleFrame.grid(row = 1, column = 0)
text.grid(row = 1, column = 0, padx = 5, pady = 5)

chessButtonFrame.grid(row = 2, column = 0)
switchButton.grid(row = 2, column = 0, padx = 5, pady = 5)
submitButton.grid(row = 2, column = 1, padx = 5, pady = 5)
window.mainloop() #Event Driven Loop