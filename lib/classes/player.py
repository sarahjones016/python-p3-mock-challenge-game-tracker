class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []

    def get_username(self):
        return self._username

    def set_username(self, username):
        if type(username) == str and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception("Your username is not a string and/or not between 2 and 16 characters")

    username = property(get_username, set_username)
        
    def results(self, new_result=None):
        from classes.result import Result
        if new_result and type(new_result) == Result:
            self._results.append(new_result)
        return self._results

    def games_played(self, new_game=None):
        from classes.game import Game
        if new_game not in self._games_played and type(new_game) == Game:
            self._games_played.append(new_game)
        return self._games_played
    
    def played_game(self, game):
        if game in self._games_played:
            return True
        else: 
            return False
    
    def num_times_played(self, game):
        # List Comprehension
        return len([result for result in self._results if result.game == game])

        # For Loop
        # list_of_games_played = []
        # for result in self._results:
        #     if result.game == game:
        #         list_of_games_played.append(result)
        # return len(list_of_games_played)

    # For the results in the list of results, we want to return the number of results where their game matches the game parameter (the game that is inputted)
    
    @classmethod
    def highest_scored(cls, game):
        pass        
        
