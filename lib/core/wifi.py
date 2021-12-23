from socket import gethostbyname, create_connection, error
import sys

def CheckWifi():
    try:
        gethostbyname("google.com")
        conexion = create_connection(("google.com", 80), 1)
        conexion.close()

    except error:
        print("Check your internet connection.")