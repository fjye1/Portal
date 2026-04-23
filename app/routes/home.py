from flask import Blueprint, send_from_directory, render_template
from flask_login import login_required

home_bp = Blueprint('main', __name__)


@home_bp.route('/')
@login_required # Add this if you want only logged-in users to see the portal
def index():
    return send_from_directory('projects/portal', 'index.html')


@home_bp.route('/kit_website/')
@home_bp.route('/kit_website/<path:path>')
@login_required
def kit_website(path='index.html'):
    return send_from_directory('projects/kit_website', path)

# 4. Samadhi Therapies (Matches your HTML link: /SamadhiTherapies/)
@home_bp.route('/SamadhiTherapies/')
@home_bp.route('/SamadhiTherapies/<path:path>')
def samadhi_therapies(path='index.html'):
    # Ensure this folder name matches exactly what is on your Pi's disk
    return send_from_directory('projects/Samadhi-Therapies', path)