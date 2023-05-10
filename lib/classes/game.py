class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []
        
    def get_title(self):
        return self._title

    def set_title(self, title):
        if type(title) == str and len(title) > 0 and not hasattr(self, "title"):
            self._title = title
        else:
            raise Exception("Your title was not a string and/or greater than 0 characters")

    title = property(get_title, set_title)

    def results(self, new_result=None):
        from classes.result import Result
        if new_result and type(new_result) == Result:
            self._results.append(new_result)
        return self._results
    
    def players(self, new_player=None):
        from classes.player import Player
        if new_player and new_player not in self._players and type(new_player) == Player:
            self._players.append(new_player)
        return self._players
    
    def average_score(self, player):
        # List Comprehension
        return sum([result.score for result in self._results if result.player == player]) / len(self._results)
    
        # For Loop
        # list_of_scores = []
        # for result in self._results:
        #     if result.player == player:
        #         list_of_scores.append(result.score)
        # return sum(list_of_scores) / len(self._results)

    # For the scores in the list of results, we want to return the sum of the scores where their player matches the player parameter (the player that is inputted). Then we want to divide that by the total number of results.