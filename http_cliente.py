import requests

url = 'http://localhost:8000'
response = requests.get(url)

print(response.status_code)  # Exibe o código de status da resposta
print(response.text)  # Exibe o conteúdo da resposta em formato de texto
