from flask import Blueprint, request, jsonify
from models import db, About
import requests
from datetime import datetime

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/api/getMenu', methods=['GET'])
def get_menu():
    locale = request.args.get('locale', 'en')
    if locale == 'en':
        return jsonify(menu)
    return jsonify({"error": "Locale not supported"}), 400

@main_blueprint.route('/api/rules/us_population', methods=['GET'])
def get_us_population_data():
    response = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
    if response.status_code == 200:
        data = response.json()
        transformed_data = [{"year": int(item["Year"]), "population": int(item["Population"])} for item in data["data"]]
        return jsonify(transformed_data)
    return jsonify({"Error": "Failed to retrieve data"}), 500

@main_blueprint.route('/api/rules/about', methods=['GET'])
def get_about():
    about = About.query.first()
    if about:
        return jsonify({"text": f"{about.text} Last updated: {datetime.now()}"})
    return jsonify({"Error": "No about text was found"}), 404

'''
from app import app, db
from models import About

with app.app_context():
    db.create_all()
    about = About(text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut semper at quam eupretium. Aliquam ac pellentesque ex. Pellentesque fermentum imperdiet justo, acfeugiat ligula rhoncus sed. Duis tempor diam nec purus hendrerit, vitae temporsapien vulputate. Sed pharetra augue id dui convallis sollicitudin. Aenearhoncus, enim a rutrum molestie, tellus lorem feugiat tellus, eu consectetur lectusnisl in odio. Curabitur convallis elit vitae eleifend eleifend. Quisque a magna idmassa hendrerit dictum. Fusce eu mollis lectus. Sed laoreet ligula eu mi finibuslaoreet. Praesent id viverra nisl, a hendrerit justo. Nulla eget augue nibh. Aeneanvitae lobortis ante, sit amet interdum arcu. Sed non tortor ut ante bibendumlacinia.")
    db.session.add(about)
    db.session.commit()
'''

menu = [
    {
        "label": "US Population Table",
        "rule": "/api/rules/us_population",
        "type": "table"
    },
    {
        "label": "US Population Chart",
        "rule": "/api/rules/us_population",
        "type": "chart",
        "params": {
            "fill": "red",
        },
    },
    {
        "label": "About",
        "rule": "/api/rules/about",
        "type": "text",
        "params": {
            "font-size": "30px"
        },
    }
]