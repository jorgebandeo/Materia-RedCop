import socket

# Endereço IP e porta do servidor
server_ip = 'localhost'
server_port = 1234

# Cria o socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Envia mensagens para o servidor
while True:
    message = input('Digite a mensagem para enviar ao servidor (ou "sair" para encerrar): ')

    if message.lower() == 'sair':
        break

    client_socket.sendto(message.encode(), (server_ip, server_port))

    # Recebe a resposta do servidor
    response, address = client_socket.recvfrom(1024)
    print('Resposta do servidor:', response.decode())

# Fecha o socket do cliente
client_socket.close()