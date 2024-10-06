import socket
import sys

def portScanning(remote_host, start_port=1, end_port=1023):
    try:
        for port in range(start_port, end_port+1):
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_socket.settimeout(1)
            data = tcp_socket.connect_ex((remote_host, port))

            try:
                service_name = socket.getservbyport(port)

            except OSError:
                service_name = "Desconhecido"
            
            if data == 0:
                print(f"[+] Aberta {port} ::: {service_name}")
            else:
                print(f"[-] Fechada {port} ::: {service_name}")
            
            tcp_socket.close()
    
    except socket.gaierror:
        print("[-] Host remoto não encontrado [-]")
        exit()

    except socket.error:
        print("[-] Erro durante o socket [-]")
        exit()

    return

def main():
    if len(sys.argv) < 2 or sys.argv[1] == '-h':
          print("Uso: python3 escanearPortas.py [host] [porta_inicio] [porta_fim]")
    else:
        remote_host = sys.argv[1]

        if len(sys.argv) == 4:
            start_port = int(sys.argv[2])
            end_port = int(sys.argv[3])
        else:
            start_port = 1
            end_port = 254
            
        portScanning(remote_host, start_port, end_port)

if __name__ == "__main__":
    main()