from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_endpoint = "https://api.npoint.io/8ea399838b3778277af1"
response = requests.get(blog_endpoint)
response.raise_for_status()
blog_data = response.json()


@app.route("/")
def index():
    return render_template('index.html', blog_data=blog_data)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


app.run(debug=True)
