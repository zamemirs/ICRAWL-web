from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
   return "<h1>Hello Azure we are now in the webscrapping poc!</h1>"
