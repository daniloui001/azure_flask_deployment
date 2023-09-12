from flask import Flask, render_template
import pandas as pd
import random
from faker import Faker
fake = Faker()



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/randomnumber')
def randomnumner():
    number_var = random.randint(1, 10000)
    fake_address = fake.address()
    return render_template('randomnumber.html', single_number = number_var, single_address = fake_address)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )