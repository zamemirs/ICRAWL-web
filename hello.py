from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
   return "<h1>Hello Azure!</h1>"

if __name__ == "__main__":
    # Run the Flask app on port 80 (or any other port you prefer)
    app.run(host='0.0.0.0', port=80)
