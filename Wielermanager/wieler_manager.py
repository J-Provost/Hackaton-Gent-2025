class FantasyTeam:
    def __init__(self, player_name):
        self.player_name = player_name
        self.picks = {
            'time_value': None,
            'coffee': None,
            'tires_changed': None,
            'returns': None,
            'service_score': None,
            'lateness': None
        }
        self.score = 0

    def set_picks(self, picks):
        self.picks = picks
