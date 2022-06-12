from flask import Flask
from threading import Thread

app = Flask("")
@app.route("/")
def home ():
    return "Hello there"

def run():
    app.run(host="127.0.0.1", port=5500)

def keep_alive():
    t = Thread(target=run)
    t.start()