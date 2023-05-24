import socket

# Endereço IP e porta do servidor
server_ip = 'localhost'
server_port = 1234

# Cria o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))

print('Servidor aguardando conexões...')

# Recebe e exibe as mensagens recebidas do cliente
while True:
    data, address = server_socket.recvfrom(1024)
    print('Mensagem recebida do cliente:', data.decode())

    # Envia uma resposta para o cliente
    response = 'Mensagem recebida com sucesso!'
    server_socket.sendto(response.encode(), address)