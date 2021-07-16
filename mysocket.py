import socket

response = 'Port: '
HOST = '0.0.0.0'
PORT = 65432
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
response = response + str(PORT)
print('Iniciando el servidor')


def respuesta(data):
    return 'IP del servidor: ' + ip_address + ' Puerto: ' + str(PORT) + ' Hola mquina: ' + data.decode()

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print('Servidor iniciado')

        s.bind((HOST, PORT))
        while True:
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        raise TypeError('No se recivio data')
                        break
                    data = respuesta(data)
                    print(data)
                    conn.sendall(data.encode())
except:
    print('Error en el servidor')


print('Respuesta', response)
print('Servidor terminado')
