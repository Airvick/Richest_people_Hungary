from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Data about Hungary's richest people (net worth in USD)
RICHEST_PEOPLE = [
    {
        "name": "Sándor Csányi",
        "net_worth": 4.2,  # billion USD
        "company": "OTP Bank",
        "industry": "Banking",
        "image_url": "/static/images/csanyi.jpg.jpg"
    },
    {
        "name": "Lőrinc Mészáros",
        "net_worth": 1.8,  # billion USD
        "company": "Mészáros Group",
        "industry": "Construction, Energy",
        "image_url": "/static/images/meszaros.jpg.webp"
    },
    {
        "name": "Gábor Várszegi",
        "net_worth": 1.5,  # billion USD
        "company": "Főnix Group",
        "industry": "Real Estate, Retail",
        "image_url": "/static/images/varszegi.jpg.webp"
    }
]

@app.route('/')
def index():
    return render_template('index.html', richest_people=RICHEST_PEOPLE)

if __name__ == '__main__':
    app.run(debug=True) 