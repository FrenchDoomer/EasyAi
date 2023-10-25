from flask import Flask, render_template
from easyai import core
from unittest import mock
from werkzeug._internal import _log
import webbrowser, flask.cli, os


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

        @app.route("/close-server", methods=["POST"])
        def close_server():
            core.main.cli_print("Server closed", type="alert")
            os._exit(0)
            return "Closing server"

        def on_startup(*self):
            port = system_info['flask_port']
            core.main.cli_print(f"Launched at: http://127.0.0.1:{port}")
            if system_info['server_mode'] == False:
                webbrowser.open_new_tab(f"http://127.0.0.1:{port}")
            elif system_info['server_mode'] == True:
                core.main.cli_print("You are running in server mode, see documentation: https://google.com", "warning")
            else:
                core.main.cli_print("Can't etablish if you are in server mode.", type="alert")
            if system_info['debug_mode'] == False:
                pass
            elif system_info['debug_mode'] == True:
                core.main.cli_print("You are running in debug mode, see documentation: https://google.com", "warning")
            else:
                core.main.cli_print("Can't etablish if you are in debug mode.", type="alert")
        with mock.patch('werkzeug.serving._log') as mocked:
            # patch the logger object and replace with own logger
            flask.cli.show_server_banner = lambda *args: None
            mocked.side_effect = on_startup()
            app.run(host="0.0.0.0", port=system_info['flask_port'], debug=system_info['debug_mode'])
