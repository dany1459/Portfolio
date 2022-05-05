from flask import Blueprint, render_template, request, flash
from .models import Message
from . import db
import pickle
from .euclidean import euc_dist
from .preprocessing import preprocess_input
from .more_details import get_more_details

views = Blueprint('views', __name__)

@views.route("/")
def home():
    return render_template("home.html")

@views.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if len(message) < 2:
            flash('Your message is too short', category='error')
        else:
            new_message = Message(name=name, email=email, message=message)
            db.session.add(new_message)
            db.session.commit()
            flash('Message Sent!', category='success')
        
    return render_template("contact.html")

@views.route("/football", methods=['GET', 'POST'])
def football():
    if request.method == 'POST':
        if request.form['submit'] == "Get Similar Players":
            selected_player = request.form['similars']
            similars = euc_dist(selected_player)
            
            height = []
            weight = []
            age = []
            current_rating = []
            preferred_foot = []

            for i in range(0, 10):
                age.append(2022 - int(get_more_details(similars[i])['birth_year']))
                current_rating.append(str(round(float(get_more_details(similars[i])['overall_rating']), 2)) + '/100')
                height.append(str(float(get_more_details(similars[i])['height'])) + ' cm')
                weight.append(str(round(float(get_more_details(similars[0])['weight']), 2)) + ' kg')
                preferred_foot.append(str(get_more_details(similars[i])['preferred_foot'][0]))

            return render_template('football.html', selected_player=selected_player, similars=similars,
                height=height, weight=weight, age=age, current_rating=current_rating, preferred_foot=preferred_foot)

        if request.form['submit'] == 'Make Prediction':
            model = pickle.load(open('model.pkl', 'rb'))
            predict_player = request.form['predict-player']
            x = preprocess_input(predict_player)
            prediction = round( float(model.predict(x)), 2 )

            return render_template('football.html', prediction=prediction, predict_player=predict_player)
    else:
        return render_template('football.html')
