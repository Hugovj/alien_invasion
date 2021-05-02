class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's static settings."""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        #ship settings
        self.ship_speed = 0.35
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 3

        #alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        """Initialise the settings that change throughout the game."""
        self.ship_speed = 0.6
        self.bullet_speed = 0.8
        self.alien_speed = 0.35

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale\

        self.alien_points = int(self.alien_points * self.score_scale)
