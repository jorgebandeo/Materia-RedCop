# Materia-RedCop
instruções específicas:
1) Implemente um serviço HTTP (servidor e cliente) através da biblioteca http.server para python,conforme exemplo dado na aula do dia 02.05.2023 (disponível no material da disciplina).

    - Inicie a coleta e análise dos pacotes através do WireShark, para o segmento de rede local.

    - Execute novamente o código exemplificado (servidor e cliente), no número de vezes que achar adequado.
<p align="center">
    <img width="854" height="480" src = "ezgif.com-video-to-gif.gif">
    </p>
    
   - Finalize a coleta de pacotes do WireShark.A partir disso, forneça os detalhes do socket criado nesta comunicação na forma de uma tupla:
            
            -Socket(source IP, destination IP, source port, destination port, service).
            
            -Socket(source IP: 127.0.0.1, destination IP: 127.0.0.1, source port: 8000, destination port: 65401, service: HTTP)
   L  embre-se de anexar as evidências e relatar adequadamente o processo de análise.

2) Adapte o mesmo código de modo que agora a resposta para o método HTTP GET direcione a umasaída HTML listando os arquivos que estão no diretório raíz do servidor (“/”). Como sugestão, vocêpode utilizar a biblioteca os do python para construir a lista e gerar a saída no formato HTML.

    a) Demonstre a construção do código para este exercício.
    1) Importações:

    - No segundo código, a importação http.server é usada em vez de from http.server import BaseHTTPRequestHandler, HTTPServer. Isso permite que a classe BaseHTTPRequestHandler seja referenciada diretamente como http.server.BaseHTTPRequestHandler no segundo código.
    
            import http.server
            import os
   
    
    2) Classe MyHTTPRequestHandler:

    - A classe RequestHandler foi renomeada para MyHTTPRequestHandler no segundo código.
    - A herança de classe foi modificada de BaseHTTPRequestHandler para http.server.BaseHTTPRequestHandler.
                    
            class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    
    3) Método do_GET():

    - No primeiro código, o método do_GET() envia uma resposta simples 'Hello, world!' para qualquer solicitação GET. No segundo código, o método do_GET() foi modificado para fornecer uma listagem de arquivos no diretório raiz do servidor quando a solicitação GET é feita para a rota '/'.
    - No segundo código, a lógica dentro do método do_GET() verifica se o caminho da solicitação é '/' usando if self.path == '/':. Se for '/', ele lista os arquivos no diretório raiz do servidor. Caso contrário, ele envia uma resposta de erro 404.
   
            def do_GET(self):
                if self.path == '/':
                    files = os.listdir('.')
                    file_list = '<ul>'
                    for file in files:
                        file_list += f'<li>{file}</li>'
                    file_list += '</ul>'
                    content = f"<html><body><h1>Arquivos no diretório raiz:</h1>{file_list}</body></html>"
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(content.encode())
                else:
                    self.send_error(404)
   
    
    4) Método run_server():

    - O método run_server() é adicionado no segundo código para iniciar o servidor HTTP. Ele cria uma instância de http.server.HTTPServer com o endereço do servidor ('', 8000) e a classe MyHTTPRequestHandler.
    - O método serve_forever() é chamado na instância do servidor HTTP para iniciar o loop de servidor e atender às solicitações indefinidamente.
            
            def run_server():
                server_address = ('', 8000)
                httpd = http.server.HTTPServer(server_address, MyHTTPRequestHandler)
                httpd.serve_forever()
    

    Essas são as principais diferenças entre os dois códigos. No segundo código, foi adicionada a funcionalidade de listar os arquivos no diretório raiz quando uma solicitação GET é feita para a rota '/'.
    
    b) Demonstre a saída, tanto a partir do browser quanto a partir de um client HTTP escrito porvocê.
<p align="center">
    <img width="854" height="480" src = "ezgif.com-video-to2-gif.gif">
    </p>
    c) Comente, em um parágrafo, os aspectos de segurança em aplicações HTTP e possíveisimplicações a partir do código desenvolvido nesta questão.
    
   - O HTTP é um protocolo que envia informações em texto simples, o que significa que qualquer pessoa que interceptar o tráfego de rede pode ver as     informações sendo transmitidas. Além disso, o HTTP não possui nenhum mecanismo de autenticação ou criptografia, o que torna fácil para hackers     interceptar e manipular os dados enviados através do protocolo. Para tornar as aplicações HTTP mais seguras, é importante usar técnicas como       criptografia, autenticação, validação de entrada de usuário e proteção contra ataques de injeção de código. No caso específico deste código, uma   possível implicação de segurança é que qualquer pessoa que tenha acesso à rede local pode fazer uma solicitação HTTP para o servidor e ver a lista de arquivos no diretório raiz. Se houver arquivos sensíveis nesse diretório, eles podem ser expostos a pessoas não autorizadas.
3) O diagrama abaixo, explorado na aula do dia 18.04.2023, traz as funções ou métodos necessáriospara o estabelecimento de conexões via sockets utilizando como protocolo de transporte o TCP –tal como é o caso do protocolo de aplicação HTTP.Com base nisto, identifique o trecho de código desenvolvido nas questões anteriores que implementeou corresponda a cada uma dessas funções.
<p align="center">
    <img width="460" height="300" src = "Captura de pantalla 2023-05-14 182333 copy.png">
    </p>
