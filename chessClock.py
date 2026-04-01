from tkinter import *

class Timer():
    def __init__(self):
        self.startTime = self.playerOneTime = self.playerTwoTime = 300
        self.minutes = self.seconds = 0
        self.running = False
        self.currentPlayer = 1
    
    def start_timer(self):
        if (not self.running):
            self.running = True
            self.updateFunction()
    
    def switchPlayer(self):
        self.currentPlayer = 1 if (self.currentPlayer == 2) else 2
    
    def updateFunction(self):
        if (self.currentPlayer == 1):
            self.playerOneTime -= 1
            self.minutes, self.seconds = divmod(self.playerOneTime, 60)
            player_1_timer.config(text = f"{self.minutes:02d}:{self.seconds:02d}")
        
        elif (self.currentPlayer == 2):
            self.playerTwoTime -= 1
            self.minutes, self.seconds = divmod(self.playerTwoTime, 60)
            player_2_timer.config(text = f"{self.minutes:02d}:{self.seconds:02d}")
        
        window.after(1000, self.updateFunction)

def updateButton():
    if (not timer.running):
        timer.start_timer()
    
    else:
        timer.switchPlayer()

timer = Timer()
window = Tk()
window.title("Chess Clock")

timer.minutes, timer.seconds = divmod(timer.startTime, 60)

chessFrame = Frame(window, background = "white", highlightbackground = "black", highlightthickness=2)

player_1_label = Label(chessFrame, background = "white", foreground = "black", text = "Player 1", font = ("Verdana", 40, "bold"))
player_2_label = Label(chessFrame, background = "white", foreground = "black", text = "Player 2", font = ("Verdana", 40, "bold"))

player_1_timer = Label(chessFrame, background = "white", foreground = "black", text = f"{timer.minutes:02d}:{timer.seconds:02d}", font = ("Verdana", 40, "bold"))
player_2_timer = Label(chessFrame, background = "white", foreground = "black", text = f"{timer.minutes:02d}:{timer.seconds:02d}", font = ("Verdana", 40, "bold"))

chessButtonFrame = Frame(window, background = "white", highlightbackground = "black", highlightthickness = 2)
chessButton = Button(chessButtonFrame, background = "white", foreground = "black", text = "Switch", command = updateButton)

chessFrame.grid(row = 0, column = 0)
player_1_label.grid(row = 0, column = 0, padx = 10, pady = 10)
player_2_label.grid(row = 0, column = 1, padx = 10, pady = 10)

player_1_timer.grid(row = 1, column = 0, padx = 10, pady = 10)
player_2_timer.grid(row = 1, column = 1, padx = 10, pady = 10)

chessButtonFrame.grid(row = 2, column = 0)
chessButton.grid(row = 2, column = 0)

window.mainloop()