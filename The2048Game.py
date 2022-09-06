from cgitb import text
from tkinter import Frame,Label,CENTER
import logics2048 as getLogic
import constants as c

# Creating Game Class

class The_2048_Game(Frame):
    def __init__(self): #The_2048_Game Constructor # creates object of The_2048_Game

        Frame.__init__(self) #Frame class needs an object on which it creates the Frame. Here self is the object of
                            # The_2048_Game

        self.grid()
        self.master.title("The 2048 Game")
        self.master.bind("<Key>",self.getCommand) #The application is bind to all the keys Pressed
                                                # When any key is Pressed ,getCommand function is called to get the Logic

        self.commands={c.KEY_UP:getLogic.upMove,c.KEY_DOWN:getLogic.downMove,c.KEY_LEFT:getLogic.leftMove,c.KEY_RIGHT:getLogic.rightMove}  # Mapping Movement Keys to their Respective Logics

        self.gridCell=[] #contains Rows of Labels
        self.initiate_Grid() # Initialise the created Grid with Styling
        self.initiate_Matrix() # Initialise the Matrix
        self.updateGrid_acc_to_Matrix()    # We are maintaining internal Matrix according to which we
                                            # Updates Labels of our Grid

        self.mainloop() # it is an Infinite Loop which runs the Application until the windows is open

    def initiate_Grid(self):
        mainGridBG=Frame(self,bg=c.BACKGROUND_COLOR_GAME,width=c.SIZE,height=c.SIZE) # creates Frame above
                                                                                    # Parent Frame of same Size
        mainGridBG.grid() # Frame Created Above converted into Grid

        for row in range(c.GRID_LEN):
            gridRow=[]
            for col in range(c.GRID_LEN):
                cell=Frame(mainGridBG,bg=c.BACKGROUND_COLOR_CELL_EMPTY,width=c.SIZE//c.GRID_LEN,height=c.SIZE//c.GRID_LEN) # Frame of Size 100 is Created on the mainGridBG grid
                cell.grid(row=row,column=col,padx=c.GRID_PADDING,pady=c.GRID_PADDING) # adding padding

                cellLabel=Label(master=cell,text="",bg=c.BACKGROUND_COLOR_CELL_EMPTY,justify=CENTER,font=c.FONT,width=5,height=2)
                cellLabel.grid()
                gridRow.append(cellLabel)
            self.gridCell.append(gridRow)




    def initiate_Matrix(self):
        self.matrix=getLogic.startTheGame() # returns the 4 x 4 Matrix
        getLogic.add2(self.matrix) # add 2 in random position
        getLogic.add2(self.matrix)

    def updateGrid_acc_to_Matrix(self):
        for row in range(c.GRID_LEN):
            for col in range(c.GRID_LEN):
                newValue=self.matrix[row][col]
                if newValue == 0:
                    self.gridCell[row][col].configure(text="",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.gridCell[row][col].configure(text=str(newValue),bg=c.BACKGROUND_COLOR_DICT[newValue],fg=c.CELL_COLOR_DICT[newValue]) # fg is the Font colour set according to bg

        self.update_idletasks() # wait until all the updation happen

    def getCommand(self,event):
        key=repr(event.char) # gives string representation of key pressed
        if key in self.commands:
            self.matrix,changed=self.commands[key](self.matrix) #calling move functions
            if changed is True: 
                getLogic.add2(self.matrix)
                self.updateGrid_acc_to_Matrix()
                changed=False #reseting changed to False for next move
            if getLogic.getCurrentStateOfGame(self.matrix) == "WON":
                #winning text
                self.gridCell[1][1].configure(text="YOU",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                self.gridCell[1][2].configure(text="WON",bg=c.BACKGROUND_COLOR_CELL_EMPTY)

            if getLogic.getCurrentStateOfGame(self.matrix) == "LOST":
                #Lossing text
                self.gridCell[1][1].configure(text="YOU",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                self.gridCell[1][2].configure(text="LOST",bg=c.BACKGROUND_COLOR_CELL_EMPTY)

#Finally starting The 2048 Game

beginTheGame=The_2048_Game()




