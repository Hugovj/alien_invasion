import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialise statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        #Start in an inactive state.
        self.game_active = False

        #Import the high score.
        filename = 'highscore.json'
        try:
            with open(filename) as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            self.high_score = 0

    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
