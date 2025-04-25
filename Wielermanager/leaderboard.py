# File: leaderboard.py
class Leaderboard:
    def __init__(self):
        self.scores = {}  # speler_naam: score (int)
        self.teams = {}   # speler_naam: FantasyTeam object

    def add_team(self, team):
        self.teams[team.player_name] = team

    def calculate_scores(self, employees):
        best = {
            'time_value': max(employees, key=lambda e: e.stats['time_value']).name,
            'coffee': max(employees, key=lambda e: e.stats['coffee']).name,
            'tires_changed': max(employees, key=lambda e: e.stats['tires_changed']).name,
            'returns': min(employees, key=lambda e: e.stats['returns']).name,
            'service_score': max(employees, key=lambda e: e.stats['service_score']).name,
            'lateness': max(employees, key=lambda e: e.stats['lateness']).name
        }

        for player_name, team in self.teams.items():
            score = sum(1 for cat, emp_name in team.picks.items() if best[cat] == emp_name)
            team.score = score
            self.scores[player_name] = score

    def show_leaderboard(self):
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        print("=== Leaderboard ===")
        for player_name, score in sorted_scores:
            print(f"{player_name}: {score} punten")
