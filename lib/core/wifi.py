from socket import gethostbyname, create_connection, error
from lib.core.banner import Colors
import sys

def CheckWifi():
    try:
        gethostbyname("google.com")
        conexion = create_connection(("google.com", 80), 1)
        conexion.close()

    except error:
        print(Colors.FAIL + "[BashTube] " + Colors.RESET + "Check your internet connection.")
