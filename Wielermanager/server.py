from flask import Flask, request, jsonify
from employee import Employee
from wieler_manager import FantasyTeam
from leaderboard import Leaderboard
from job_data import job_data
import json
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# Werknemers lijst
employees = [Employee(name) for name in ["Ralph", "Sven", "Lisa", "Kenny", "Fatima"]]
for emp in employees:
    if emp.name in job_data:
        emp.stats = job_data[emp.name]

# Votes bestand
votes_file = "Wielermanager/votes.json"
if os.path.exists(votes_file):
    with open(votes_file, "r", encoding="utf-8") as f:
        votes = json.load(f)
else:
    votes = {
        "time_value": {},
        "coffee": {},
        "tires_changed": {},
        "returns": {},
        "service_score": {},
        "lateness": {}
    }

# Leaderboard bestand
leaderboard = Leaderboard()
if os.path.exists("Wielermanager/Front-end/leaderboard_data.json"):
    with open("Wielermanager/Front-end/leaderboard_data.json", "r", encoding="utf-8") as f:
        teams_data = json.load(f)
    for player_name, data in teams_data.items():
        old_team = FantasyTeam(player_name)
        old_team.set_picks(data["picks"])
        leaderboard.add_team(old_team)

@app.route('/submit', methods=['POST'])
def submit_team():
    data = request.get_json()
    player_name = data['player_name']
    picks = data['picks']

    # Nieuwe team aanmaken
    new_team = FantasyTeam(player_name)
    new_team.set_picks(picks)
    leaderboard.add_team(new_team)

    # Update scores
    leaderboard.calculate_scores(employees)

    # Update leaderboard JSON
    export_data = {
        name: {
            "picks": team.picks,
            "score": team.score
        }
        for name, team in leaderboard.teams.items()
    }
    with open("Wielermanager/Front-end/leaderboard_data.json", "w", encoding="utf-8") as f:
        json.dump(export_data, f, indent=4)

    # Update votes JSON
    for category, employee_name in picks.items():
        if employee_name not in votes[category]:
            votes[category][employee_name] = 0
        votes[category][employee_name] += 1

    with open(votes_file, "w", encoding="utf-8") as f:
        json.dump(votes, f, indent=4)

    return jsonify({"message": "Success!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
