from flask import Flask

app = Flask(__name__)  # Initialize the Flask app

@app.route("/")
def hello():
    return "Hello from Flask on EC2!"  # Response for the root URL

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Run the app on all available IPs

