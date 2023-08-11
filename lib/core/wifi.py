from socket import gethostbyname, create_connection, error
from lib.core.utils import Colors
import sys

def check_wifi():
    """Check wifi connection status.

    Returns:
        True: Connection is ok.
        Exit: Connection is unstable.
    """
    try:
        gethostbyname("google.com")
        conexion = create_connection(("google.com", 80), 1)
        conexion.close()

        return True

    except error:
        sys.exit(Colors.FAIL + "[BashTube] " + Colors.RESET + "Check your internet connection.")
