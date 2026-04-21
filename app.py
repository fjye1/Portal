from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# 1. The Main Portal
@app.route('/')
def index():
    return send_from_directory('projects/portal', 'index.html')

# 2. Event Builder (Matches your HTML link: /event_builder/)
@app.route('/Event_builder/')
@app.route('/Event_builder/<path:path>')
def event_builder(path='run.py'):
    return send_from_directory('projects/Event_builder', path)

# 3. Kit Website (Matches your HTML link: /kit_website/)
@app.route('/kit_website/')
@app.route('/kit_website/<path:path>')
def kit_website(path='index.html'):
    return send_from_directory('projects/kit_website', path)

# 4. Samadhi Therapies (Matches your HTML link: /SamadhiTherapies/)
@app.route('/SamadhiTherapies/')
@app.route('/SamadhiTherapies/<path:path>')
def samadhi_therapies(path='index.html'):
    # Ensure this folder name matches exactly what is on your Pi's disk
    return send_from_directory('projects/Samadhi-Therapies', path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

