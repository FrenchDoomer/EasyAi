import argparse, sys, socket, platform
from flask import Flask, render_template, url_for, send_from_directory
from easyai import metadata

class main:
    def __init__(self):
        # Creating arguments
        parser = argparse.ArgumentParser(add_help=True)
        parser.add_argument("-v", "--version", help="Show program's version number and exit.", version=metadata.get("name") + " " + metadata.get("version"), action="version")
        parser.add_argument("-c", "--check-update", help="Checking for update at launch.", dest="need_check_update", action="store_true")
        parser.add_argument("-s", "--server-mode", help="Will enable the server mode (for example it will not launch file explorer to chose location).", dest="server-mode",action="store_true")
        parser.add_argument("-p", "--port", help="Port where flask launch.", dest="flask_port", action="store", default="80")
        args = parser.parse_args()

        # Checking update
        if args.need_check_update == True:
            if self.internet_on()==True:
                print("OK")
            else:
                print("NOK")
                sys.exit()
        else:
            print("run")

        # Checking os
        if self.detect_os() == "macOS":
            os_logo = "os-logo/macos.png"
        elif self.detect_os() == "Windows":
            os_logo = "bi-windows"
        elif self.detect_os() == "Linux":
            os_logo = "os-logo/linux.png"

        # Running main program
        Webapp(args.flask_port, os_logo)

    def internet_on(self, host="8.8.8.8", port=53, timeout=3):
        """
        Host: 8.8.8.8 (google-public-dns-a.google.com)
        OpenPort: 53/tcp
        Service: domain (DNS/TCP)
        """
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error as ex:
            print(ex)
            return False

    def detect_os(self):
        return platform.system()

class Webapp():
    def __init__(self, flask_port, os_logo):
        app = Flask(__name__, template_folder='htdocs', static_folder="htdocs/static")
        @app.route("/")
        def index(*self):
            return render_template("index.html", flask_port=flask_port, os_logo=os_logo)


        app.run(host="0.0.0.0", port=flask_port, debug=True)