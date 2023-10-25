import argparse, socket, platform, os, GPUtil, cpuinfo, datetime
from colorama import init, just_fix_windows_console, Fore
from easyai import metadata, webapp

class main:
    def __init__(self):
        # Creating arguments
        parser = argparse.ArgumentParser(add_help=True)
        parser.add_argument("-v", "--version", help="Show program's version number and exit.", version=metadata.get("name") + " " + metadata.get("version"), action="version")
        parser.add_argument("-c", "--check-update", help="Checking for update at launch.", dest="need_check_update", action="store_true", default=False)
        parser.add_argument("-s", "--server-mode", help="Will enable the server mode (for example it will not launch file explorer to chose location).", dest="server_mode",action="store_true", default=False)
        parser.add_argument("-p", "--port", help="Port where flask launch.", dest="flask_port", action="store", default="80")
        parser.add_argument("-d", "--debug",help="Will enable the Falsk debug mode (usefull for creating custom scripts).",dest="debug_mode", action="store_true", default=False)
        args = parser.parse_args()

        # Setting needed things
        init(autoreset=True)
        just_fix_windows_console()

        # Checking update

        # Check internet connection
        if self.internet_on()==True:
                main.cli_print("You are connected to internet")
        else:
            main.cli_print("You are not connected to internet", type="alert")
            os._exit(0)

        # Giving system infos
        self.actual_os = platform.system()
        if self.actual_os == "macOS":
            self.os_logo = "os-logo/macos.png"
        elif self.actual_os == "Windows":
            self.os_logo = "bi-windows"
        elif self.actual_os == "Linux":
            self.os_logo = "os-logo/linux.png"
        cpu_info = "Unknown"
        try:
            cpu_info = cpuinfo.get_cpu_info()["brand_raw"]
        except Exception as e:
            print(f"Error while trying to get information on CPU : {e}")
            os._exit(0)

        # Obtenez le nom du GPU
        gpu_info = "Unknown"
        try:
            gpus = GPUtil.getGPUs()
            if gpus:
                gpu_info = gpus[0].name
        except Exception as e:
            print(f"Error while trying to get information on GPU: {e}")
            os._exit(0)
        system_info = {"os":self.actual_os, "os_logo":self.os_logo,"cpu":cpu_info, "gpu":gpu_info ,"flask_port":args.flask_port, "server_mode":args.server_mode, "debug_mode":args.debug_mode}

        # Running main program
        webapp.Webapp(system_info)

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
            main.cli_print(ex)
            return False

    def check_scripts(*self):
        scripts_directory = os.path.dirname(os.path.abspath(__file__))
        relative_directory_path = './scripts'
        directory = os.path.join(scripts_directory, relative_directory_path)

        metadata_list = []
        for subdir, dirs, files in os.walk(directory):
            for file_name in files:
                if file_name == '__init__.py':
                    init_file_path = os.path.join(subdir, file_name)
                    metadata = {}
                    try:
                        with open(init_file_path, 'r') as init_file:
                            exec(init_file.read(), metadata)
                        if 'METADATA' in metadata:
                            metadata_list.append(metadata['METADATA'])
                    except Exception as e:
                        print(f"Erreur lors de la lecture du fichier {init_file_path}: {e}")
        metadata_list = sorted(metadata_list, key=lambda x: x['name'])
        return metadata_list

    def cli_print(msg, type="info"):
        now = datetime.datetime.now()
        if type == "info":
            print(f"[{now}] : {msg}")
        elif type == "warning":
            print(f"[{now}] : {Fore.YELLOW+msg}")
        elif type == "alert":
            print(f"[{now}] : {Fore.RED+msg}")