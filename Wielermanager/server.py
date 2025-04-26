from employee import Employee
from wieler_manager import FantasyTeam
from leaderboard import Leaderboard
from job_data import job_data
import json
import os
import uuid
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask import Flask, request, jsonify, send_from_directory, render_template, url_for

app = Flask(__name__, static_folder="Wielermanager/Front-End", static_url_path='/static')

basedir = os.path.abspath(os.path.dirname(__file__))

# Set up upload folder
UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
PROCESSED_FOLDER = os.path.join(basedir, 'processed')
ALLOWED_EXTENSIONS = {'txt', 'mp3', 'pdf', 'doc', 'docx'}
MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Create upload and processed directories if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

# Enable CORS for all domains on all routes
CORS(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return send_from_directory(os.path.join(basedir, 'Front-End'), 'talenttournament.html')

@app.route('/evaluation')
def evaluation():
    return send_from_directory(os.path.join(basedir, 'Front-End'), 'evaluation.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    print("Upload endpoint called")
    # Check if file part exists in the request
    if 'file' not in request.files:
        print("No file part in request")
        return jsonify({'status': 'error', 'message': 'No file part'}), 400
    
    file = request.files['file']
    
    # Check if file is selected
    if file.filename == '':
        print("No file selected")
        return jsonify({'status': 'error', 'message': 'No file selected'}), 400
    
    # Check if file type is allowed
    if not allowed_file(file.filename):
        print(f"File type not allowed: {file.filename}")
        return jsonify({'status': 'error', 'message': 'File type not allowed'}), 400
    
    # Save the file with a secure filename
    filename = secure_filename(file.filename)
    unique_filename = f"{uuid.uuid4()}_{filename}"
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
    
    try:
        file.save(file_path)
        print(f"File saved to {file_path}")
        
        # Process the file (placeholder for your AI processing)
        processed_filename = process_file(unique_filename, file_path)
        
        return jsonify({
            'status': 'success',
            'message': 'File uploaded successfully',
            'original_file': unique_filename,
            'processed_file': processed_filename
        }), 200
    except Exception as e:
        print(f"Error saving file: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

def process_file(filename, file_path):
    """
    Process the uploaded file. This is a placeholder for your AI processing.
    In a real implementation, this would convert the audio/text to a CV.
    """
    # Get the file extension
    file_ext = filename.rsplit('.', 1)[1].lower()
    
    # Create a processed filename (a PDF in this example)
    processed_filename = f"processed_{filename.rsplit('.', 1)[0]}.pdf"
    processed_path = os.path.join(app.config['PROCESSED_FOLDER'], processed_filename)
    
    print(f"Processing file: {filename} -> {processed_filename}")
    
    # Placeholder for processing logic
    # TODO: Implement your AI processing here
    # For now, just create an empty PDF file as a placeholder
    with open(processed_path, 'w') as f:
        f.write("This is a placeholder for the processed CV")
    
    return processed_filename

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename, as_attachment=True)

# Keep your existing routes below this line
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
    votes = {category: {} for category in ["time_value", "coffee", "tires_changed", "returns", "service_score", "lateness"]}

# Leaderboard bestand
leaderboard = Leaderboard()
if os.path.exists("Wielermanager/Front-End/leaderboard_data.json"):
    with open("Wielermanager/Front-End/leaderboard_data.json", "r", encoding="utf-8") as f:
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

    # Save leaderboard
    export_data = {name: {"picks": team.picks, "score": team.score} for name, team in leaderboard.teams.items()}
    with open("Wielermanager/Front-End/leaderboard_data.json", "w", encoding="utf-8") as f:
        json.dump(export_data, f, indent=4)

    # Update votes
    for category, employee_name in picks.items():
        if employee_name not in votes[category]:
            votes[category][employee_name] = 0
        votes[category][employee_name] += 1

    with open(votes_file, "w", encoding="utf-8") as f:
        json.dump(votes, f, indent=4)

    return jsonify({"message": "Success!"}), 200

photos_urls = {
    "Ralph": "http://127.0.0.1:5000/pictures/Ralph.jpg",
    "Quinten": "http://127.0.0.1:5000/pictures/Quinten.jpg",
    "Jelle": "http://127.0.0.1:5000/pictures/Jelle.jpg",
    "David": "http://127.0.0.1:5000/pictures/David.jpg",
    "Ahmed": "http://127.0.0.1:5000/pictures/Ahmed.jpg",
    "Elian": "http://127.0.0.1:5000/pictures/Elian.jpg"
}

@app.route('/pictures/<path:filename>')
def serve_picture(filename):
    pictures_folder = os.path.join(basedir, 'Front-End', 'Pictures')
    return send_from_directory(pictures_folder, filename)

@app.route('/employees', methods=['GET'])
def get_employees():
    employees_data = []
    for name in job_data.keys():
        photo = photos_urls.get(name, "http://127.0.0.1:5000/pictures/default.jpg")
        employees_data.append({"name": name, "photo": photo})
    return jsonify(employees_data)

@app.route('/js/<path:filename>')
def serve_js(filename):
    js_folder = os.path.join(basedir, 'Front-End')
    return send_from_directory(js_folder, filename)

@app.route('/css/<path:filename>')
def serve_css(filename):
    css_folder = os.path.join(basedir, 'Front-End')
    return send_from_directory(css_folder, filename)

@app.route('/ping', methods=['GET', 'OPTIONS'])
def ping():
    """Simple endpoint to check if the server is up and running"""
    return jsonify({'status': 'ok', 'message': 'Server is running'}), 200

if __name__ == "__main__":
    app.run(debug=True)