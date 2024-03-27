import socket,time
import sys
import signal
import subprocess
import concurrent.futures


RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
RESET='\033[0m'

banner=f"""{RED}
  ____      _       ____            _       
 / ___| ___| |_    |  _ \ ___  _ __| |_ ___ 
| |  _ / _ \ __|   | |_) / _ \| '__| __/ __|
| |_| |  __/ |_    |  __/ (_) | |  | |_\__\\
\____|\___|\__|___ |_|   \___/|_|  \__|___/
                |_____|                
        
          Scaner De Puertos TCP
 {RESET}\n\n\t"""

print(banner)

def C(sig, Frame):
    print(f"\n\t{RED}[^C]Saliendo...{RESET}")
    sys.exit(1)
signal.signal(signal.SIGINT, C)

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, port))
        print(f"[💻]{BLUE} Port {port} is open{RESET}")
        s.close()
    except socket.error:
        pass
def main(ip):
    try:
        print(f"\n\t{GREEN}[√] Buscando Puertos{RESET}\n")
        with concurrent.futures.ThreadPoolExecutor(max_workers=theader) as executor:
            futures = [executor.submit(scan_port, ip, p) for p in range(1, rango + 1)]

        for p in range(rango):
            try:   
                puertos_abiertos = set()
                for future in concurrent.futures.as_completed(futures):
                    puerto = future.result()
                    if puerto is not None:
                        puertos_abiertos.add(puerto)
                        for puerto in puertos_abiertos:
                            print(f"[💻] Port {puerto} is open")
            except:
                pass
        print(f"\n\t{GREEN}[√] No Hay Mas Puertos{RESET}")
    except Exception as e:
        print("Error %s" % e)




if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python3 %s <Ip> <Range> <Theaders>" % sys.argv[0])
        sys.exit(1)
    ip = sys.argv[1]
    rango = int(sys.argv[2])
    theader = int(sys.argv[3])
    main(ip)
    
