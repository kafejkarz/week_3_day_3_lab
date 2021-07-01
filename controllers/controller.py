from flask import render_template
from app import app
from models.items import *


@app.route('/')
def index():
    return render_template('index.html', title='My Order List', items3=items3)

@app.route('/order')
def order():
    return render_template('order1.html', title='My first order', items3=items3)

