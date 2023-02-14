'''Author Francis Jonathan Lloyd'''
from kivy.uix.screenmanager import Screen

class AppLogic(Screen):
    '''Contains all logic for the game'''

    # Player scores
    x_score = 0
    o_score = 0

    # Logical variables
    on_x: bool = True
    spaces_played: list[int] = []

    # Spaces played separated
    spaces_played_x: list[int] = []
    spaces_played_o: list[int] = []

    def character_logic(self, button_number: int) -> str:
        '''Logic for who's turn it is'''
        return_string = ''
        if button_number not in self.spaces_played:
            if self.on_x:
                return_string = "X"
                self.on_x = False
                self.spaces_played_x.append(button_number)
            else:
                return_string = "O"
                self.on_x = True
                self.spaces_played_o.append(button_number)
            self.spaces_played.append(button_number)
            return return_string
        return "-1"

    def set_turn(self) -> str:
        '''Handles the turn text logic'''
        if self.on_x:
            return "Turn: X"
        return "Turn: O"
        
    def button(self, button_number: int) -> None:
        # TEST REMOVE
        print("X ",self.spaces_played_x)
        print("O ",self.spaces_played_o)
        print("All ", self.spaces_played)
        '''Handles game button presses'''
        # The game board logic
        set_char: str = self.character_logic(button_number)
        if set_char != "-1":
            # Set the turn indicator
            self.ids.turn_indicator.text = self.set_turn()
            match button_number:
                case 1:
                    self.ids.button_1.text = set_char
                case 2:
                    self.ids.button_2.text = set_char
                case 3:
                    self.ids.button_3.text = set_char
                case 4:
                    self.ids.button_4.text = set_char
                case 5:
                    self.ids.button_5.text = set_char
                case 6:
                    self.ids.button_6.text = set_char
                case 7:
                    self.ids.button_7.text = set_char
                case 8:
                    self.ids.button_8.text = set_char
                case 9:
                    self.ids.button_9.text = set_char
        # Checks win condition every time button is pressed
        self.win_conditions()
            
    def reset_board(self)-> None:
        '''Reset the board'''
        for widget in self.ids.board_grid.children:
            widget.text = '-'
        # Resets variables
        self.on_x = True
        self.spaces_played = []
        self.spaces_played_x = []
        self.spaces_played_o = []
        self.ids.turn_indicator.text = "Turn: X"

    def reset_score(self):
        self.x_score = 0   
        self.o_score = 0   
        self.ids.x_score.text = f"X Score: {self.x_score}"
        self.ids.o_score.text = f"O Score: {self.o_score}"

    def win_conditions(self) -> None:
        '''Logic for win conditions'''
        # Win possibilities
        win_conditions : list[list[int]] = [
            [1,2,3],[4,5,6],[7,8,9],[1,4,7],
            [2,5,8],[3,6,9],[3,5,7],[1,5,9]]
        if len(self.spaces_played) < 9:
            for condition in win_conditions:
                if set(condition) <= set(self.spaces_played_x):
                    self.ids.turn_indicator.text = "X Won"
                    self.x_score += 1
                    self.ids.x_score.text = f"X Score: {self.x_score}"
                    self.reset_board()
                elif set(condition) <= set(self.spaces_played_o):
                    self.ids.turn_indicator.text = "O Won"
                    self.o_score += 1
                    self.ids.o_score.text = f"O Score: {self.o_score}"
                    self.reset_board()

