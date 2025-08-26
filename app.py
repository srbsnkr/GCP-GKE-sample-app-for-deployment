from flask import Flask
app = Flask(__name__)

@app.get("/")
def hello():
    return "Hi ! this is a sample app on GKE using autopilot!"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)