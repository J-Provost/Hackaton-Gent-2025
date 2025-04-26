from employee import Employee
from wieler_manager import FantasyTeam
from leaderboard import Leaderboard
from setup import select_employees_for_categories
from job_data import job_data
import json
import os

# 1. Initialiseer correcte lege structuur
empty_votes = {
    "time_value": {},
    "coffee": {},
    "tires_changed": {},
    "returns": {},
    "service_score": {},
    "lateness": {}
}

# 2. Probeer te laden van bestand
votes_file = "Wielermanager/votes.json"
if os.path.exists(votes_file):
    with open(votes_file, "r", encoding="utf-8") as f:
        votes = json.load(f)
    # 3. Zorg dat ALLE categorieën zeker bestaan
    for category in empty_votes:
        if category not in votes:
            votes[category] = {}
else:
    votes = empty_votes.copy()

# 1. Lijst van werknemers
employees = [Employee(name) for name in ["Ralph", "Sven", "Lisa", "Kenny", "Fatima"]]

# Gebruik vaste data (geen random!)
for emp in employees:
    if emp.name in job_data:
        emp.stats = job_data[emp.name]

# 2. Laad bestaande fantasy teams
leaderboard = Leaderboard()

if os.path.exists("Front-end/leaderboard_data.json"):
    with open("Front-end/leaderboard_data.json", "r", encoding="utf-8") as f:
        teams_data = json.load(f)
    for player_name, data in teams_data.items():
        old_team = FantasyTeam(player_name)
        old_team.set_picks(data["picks"])
        leaderboard.add_team(old_team)

# 3. Interactie: nieuwe speler
print("Welkom bij de Fantasy Garage Manager!")
player_name = input("Wat is je naam? ")
new_team = FantasyTeam(player_name)
employee_names = [e.name for e in employees]
picks = select_employees_for_categories(employee_names)
new_team.set_picks(picks)

leaderboard.add_team(new_team)

# 4. Bereken scores
leaderboard.calculate_scores(employees)
leaderboard.show_leaderboard()

# (optioneel) Print werknemers stats
print("\n--- Werknemer Statistieken ---")
for e in employees:
    print(f"{e.name}: {e.stats}")

# 5. Bewaar alle fantasy teams
export_data = {
    name: {
        "picks": team.picks,
        "score": team.score  # ✅ voeg ook de score toe!
    }
    for name, team in leaderboard.teams.items()
}


with open("Front-end/leaderboard_data.json", "w", encoding="utf-8") as f:
    json.dump(export_data, f, indent=4)


# 6. Update HTML automatisch
def update_html(employees, leaderboard, fantasy_team):
    with open("Wielermanager/wielermanager.html", "r", encoding="utf-8") as f:
        html_template = f.read()

    # Leaderboard invullen
    leaderboard_rows = ""
    sorted_scores = sorted(leaderboard.scores.items(), key=lambda x: x[1], reverse=True)
    for player_name, score in sorted_scores:
        leaderboard_rows += f"<tr><td>{player_name}</td><td>{score}</td></tr>"

    # Fantasy team invullen
    fantasy_rows = ""
    for cat, emp in fantasy_team.picks.items():
        fantasy_rows += f"<tr><td>{cat.replace('_', ' ').capitalize()}</td><td>{emp}</td></tr>"

    # Employees invullen
    employee_rows = ""
    for e in employees:
        employee_rows += (
            f"<tr><td>{e.name}</td><td>{e.stats['time_value']}</td><td>{e.stats['coffee']}</td>"
            f"<td>{e.stats['tires_changed']}</td><td>{e.stats['returns']}</td>"
            f"<td>{e.stats['service_score']}</td><td>{e.stats['lateness']}</td></tr>"
        )

    html_filled = html_template.replace("<!-- Dynamisch leaderboard data -->", leaderboard_rows)
    html_filled = html_filled.replace("<!-- Dynamisch fantasy team data -->", fantasy_rows)
    html_filled = html_filled.replace("<!-- Dynamisch werknemersdata -->", employee_rows)

    with open("Wielermanager/fantasy_manager_dashboard.html", "w", encoding="utf-8") as f:
        f.write(html_filled)

    print("✅ HTML dashboard geüpdatet als fantasy_manager_dashboard.html!")

# Call update_html
update_html(employees, leaderboard, new_team)

# Update votes
for category, employee_name in new_team.picks.items():
    if employee_name not in votes[category]:
        votes[category][employee_name] = 0
    votes[category][employee_name] += 1

# Save votes
with open(votes_file, "w", encoding="utf-8") as f:
    json.dump(votes, f, indent=4)
