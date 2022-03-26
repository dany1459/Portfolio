from flask import Blueprint, render_template, request, flash
from .models import Message, Note
from . import db
import pickle
import numpy as np
import pandas as pd

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
def predict():
    return render_template('football.html')

