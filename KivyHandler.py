from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

import PlayGame
import minimax

import time

# all graphics/widgets: grids, btns, labels for all data
class Main_Page(BoxLayout):
    def __init__(self, **kwargs):
        super(Main_Page, self).__init__(**kwargs)      # this is only for if kivy code goes in the py file

        self.orientation = "vertical"
        self.winner = ""
        self.openSpots = 9   # do some action if we run out of spots

        # > reason I make these vars instead of adding straight in, is I want easier
        #   accessability.
        # > board is mirror of grid, but other files can't use grid since it's a kivy function
        #   so they interact with board
        self.grid = self.Make_Grid()
        self.board = [ ['', '', ''], ['', '', ''], ['', '', ''] ]
        result = Label(text = "", size_hint_y = 0.15)   
                
        restartBtn = Button(text = "Play Again?", disabled = True, size_hint_y = 0.15)
        restartBtn.bind(on_release = self.RestartGame)

        self.add_widget(self.grid)
        self.add_widget(result)
        self.add_widget(restartBtn)

    
    # white: [255,255,255]
    def Make_Grid(self):
        grid = GridLayout(cols = 3, rows = 3, size_hint_y = .7)

        # for visibility of grid, add invisible widgets
        for i in range(0, 9):
            btn = Button(text = "", id = str(i))
            btn.bind(on_release = self.btnClicked)

            grid.add_widget(btn)
        
        return grid


    # event: user wants to make a move
    def btnClicked(self, instance):        
        # is spot is taken
        if (instance.text != ""):
            return

        else:
            instance.text = "X"                           # update gridlayout
            location = (int(instance.id) // 3, int(instance.id) % 3)   # update board
            self.board[location[0]][location[1]] = "X"
            self.openSpots -= 1

            winner = PlayGame.CheckWinner(self.board, self.openSpots)

            if (winner == ""):     # if no winner
                time.sleep(.100)   # pause for .3 sec

                # call AI
                aiLocation = minimax.BestMove(self.board, self.openSpots)     # AI makes its move
                self.grid.children[8 - aiLocation].text = "O"
                self.openSpots -= 1

                winner = PlayGame.CheckWinner(self.board, self.openSpots)

            else:
                if (winner == "X"):
                    self.children[1].text = "You Won!"

                elif (winner == "O"):
                    self.children[1].text = "AI Won!"
                
                else:
                    self.children[1].text = "It's a tie!"
            
                self.children[0].disabled = False


    def RestartGame(self, instance):
        for btn in self.grid.children:
            btn.text = ""
        
        self.board = [ ['', '', ''], ['', '', ''], ['', '', ''] ]
        self.children[1].text = ""
        instance.disabled = True








class myApp(App):
    def build(self):
        return Main_Page()

if __name__ == "__main__":
    myApp().run()