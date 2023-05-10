from classes.player import Player
from classes.game import Game

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

        player.results(self)
        game.results(self)

        player.games_played(game)
        game.players(player)

    def get_score(self):
        return self._score

    def set_score(self, score):
        if type(score) == int and 1 <= score <= 5000:
            self._score = score
        else:
            raise Exception("Your score is not an integer and/or is not between 1 and 5000")

    score = property(get_score, set_score)

    def get_player(self):
        return self._player

    def set_player(self, player):
        if type(player) == Player:
            self._player = player
        else:
            raise Exception("Your player is not a Player instance")

    player = property(get_player, set_player)

    def get_game(self):
        return self._game

    def set_game(self, game):
        if type(game) == Game:
            self._game = game
        else:
            raise Exception("Your game is not a Game instance")

    game = property(get_game, set_game)
