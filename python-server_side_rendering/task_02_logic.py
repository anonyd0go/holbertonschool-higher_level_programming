from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    json_dict = None
    with open("items.json", "r", encoding="utf-8") as jf:
        json_dict = json.load(jf)
    return render_template('items.html', items=json_dict["items"])


if __name__ == '__main__':
    app.run(debug=True, port=5000)
