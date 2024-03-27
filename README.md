Get_Ports es una herramienta de escaneo de puertos TCP escrita en Python que te permite explorar la conectividad de red en un host específico. Esta herramienta es útil para identificar puertos abiertos en un sistema y puede ser empleada en pruebas de penetración, evaluaciones de seguridad, o simplemente para entender la topología de red.

Características
* Escaneo rápido y fiable de puertos TCP en un host dado.
* Interfaz de línea de comandos simple y fácil de usar.
* Personalizable para adaptarse a las necesidades específicas de escaneo.
Requisitos
* Python 3.x instalado.
* Privilegios de administrador (si es necesario dependiendo del sistema operativo y los puertos a escanear).

Uso
* Clona este repositorio en tu máquina local:
* git clone https://github.com/PiKas-Py/get_ports.git
* Navega al directorio del repositorio:
* cd get_ports
* Ejecuta la herramienta con el siguiente comando, especificando el host que deseas escanear:
* python get_ports.py <ip> <rango> <Theaders> 
* Reemplaza <host> con la dirección IP o el nombre de dominio del host que deseas escanear.

Ejemplo

- python get_ports.py <ip> <Rango> <Theaders>
- Este comando escaneará los puertos TCP en el host example.com y mostrará los puertos abiertos.
- El Parametro <Ip> Seria El Objetivo A Escanear  <Rango> seria asignarle Un Rango de puertos desde el 1-65535 <Theader>, Puede Variar En este caso El Usuario Elije La velocidad En La que quiere escanear Cada Puertos

Ten en cuenta que el escaneo de puertos sin permiso puede ser ilegal o violar políticas de seguridad. Asegúrate de tener permiso explícito para realizar escaneos de puertos en cualquier sistema o red que no sea de tu propiedad.


