import socket


def main():

    HOST = 'localhost'
    PORT = 50000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    nombre = input("Ingrese su Nombre: ")
    cedula = input("Ingrese su Cédula: ")
    origen = input("Ingrese su Origen: ")
    destino = input("Ingrese su Destino: ")
    hora = input("Ingrese su Hora: ")
    fecha = input("Ingrese su Fecha\n "+"Año-Mes-día:\n")
    aerolinea = input("Ingrese su Aerolinea: ")
    precio = input("Ingrese su Precio: ")

    mensajeE = nombre+", "+cedula+", "+origen+", "+destino+", "+hora+", "+fecha+", "+aerolinea+", "+precio

    s.sendall(mensajeE.encode())
    data = s.recv(1024)
    cadena = data.decode("utf-8")
    s.close()
    print(cadena)


if __name__ == "__main__":
    main()
