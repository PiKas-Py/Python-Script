import socket,time
import sys
import threading
import signal


RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
RESET='\033[0m'

banner=f"""{RED}
  ____             _              _    _       _     
 | __ )  __ _  ___| | _____ _ __ | | _(_) __ _| |__  
 |  _ \ / _` |/ __| |/ / _ \ '_ \| |/ / |/ _` | '_ \ 
 | |_) | (_| | (__|   <  __/ | | |   <| | (_| | |_) |
 |____/ \__,_|\___|_|\_\___|_| |_|_|\_\_|\__,_|_.__/ {RESET}\n\n\t"""

print(banner)
time.sleep(2)
def C(sig, Frame):
    print("\n\t[^C]Saliendo...")
    sys.exit(1)
signal.signal(signal.SIGINT, C)

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, port))
        print(f"[√]{BLUE} Port {port} is open{RESET}")
        s.close()
    except socket.error:
        pass

def main(ip):
    try:
        for p in range(rango):
            scan_port(ip, p)
        print(f"\n\t{GREEN}[√] No Hay Mas Puertos{RESET}")
    except:
        print(f"\n\t{RED}[-] Error En El Parametro 2{RESET}")
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 %s <Ip> <Range>" % sys.argv[0])
        sys.exit(1)
    ip = sys.argv[1]
    rango = str(sys.argv[2])
    main(ip)
