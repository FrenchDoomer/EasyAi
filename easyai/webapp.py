from flask import Flask, render_template
from easyai import core

class Webapp():
    def __init__(self, system_info):
        app = Flask(__name__, template_folder='htdocs', static_folder="htdocs/static")
        @app.route("/")
        def index(*self):
            return render_template("index.html", system_info=system_info)

        @app.route("/download")
        def download(*self):
            metadata_list = core.main.check_scripts()
            return render_template("download.html", metadata_list=metadata_list, system_info=system_info)

        @app.route("/settings")
        def settings(*self):
            return render_template("settings.html", system_info=system_info)

        @app.route("/exit")
        def exit(*self):
            return render_template("exit.html")

        app.run(host="0.0.0.0", port=system_info['flask_port'], debug=True)
