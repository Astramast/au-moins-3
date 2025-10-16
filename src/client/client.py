from client_socket import ClientSocket
import sys
import re

def verif_ip(ip: str) -> bool:
    regex = r"^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"
    return re.match(regex, ip) is not None

def verif_port(port: str) -> bool:
    regex = r"^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$"   
    return re.match(regex, port) is not None

def main(host: str, port: int) -> None:
    """ Main loop """
    try:
        serv_sock = ClientSocket(host, port)
    except:
        print("Can't connect to the server.")
    
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error: python3 server.py HOST PORT")
        exit(0)
    
    if not verif_ip(sys.argv[1]):
        print("Error: HOST IP should be [0-255].[0-255].[0-255].[0-255]")
        exit(0)
    
    if not verif_port(sys.argv[2]):
        print("Error: PORT should be [1-65535]" )
        exit(0)
    
    main(sys.argv[1], sys.argv[2])