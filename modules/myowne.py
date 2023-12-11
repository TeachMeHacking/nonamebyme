import async_worker
from flask_ngrok import run_with_ngrok
from flask import Flask

def okrun():
    print(async_worker.publicurl)
    app = Flask(__name__)
    run_with_ngrok(app)
    @app.route("/geturl")
    def getUrl():
        return async_worker.publicurl
    app.run()