import requests
import json

# --- MINHA CONFIGURAÇÃO ---
# 1. Aqui eu coloco a minha chave da API do Watchmode que peguei no site.
API_KEY = 'vPuvaCA0x0LCYtJgrwnClNIx6J4rp0c7kEOj2hmY' 
# 2. Este é o nome do filme que eu quero pesquisar.
NOME_DO_FILME = "Gone Girl"

# Esta é a URL base da API que eu vou usar para a busca.
URL_BUSCA = 'https://api.watchmode.com/v1/search/'


# --- MONTANDO E EXECUTANDO A MINHA REQUISIÇÃO ---
print(f"Estou buscando por '{NOME_DO_FILME}'...")

# Crio um dicionário com os parâmetros que eu vou enviar para a API.
parametros = {
    'apiKey': API_KEY,
    'search_field': 'name',
    'search_value': NOME_DO_FILME,
    'types': 'movie' # Defino que quero buscar apenas por filmes.
}

# Agora eu faço a chamada GET para a API, passando meus parâmetros.
resposta = requests.get(URL_BUSCA, params=parametros)


# --- TRATANDO A RESPOSTA QUE EU RECEBI ---
# Verifico se a minha requisição foi bem-sucedida (se o status code é 200).
if resposta.status_code == 200:
    dados = resposta.json()
    print("\n--- RESPOSTA BRUTA QUE A API ME ENVIOU ---")
    # Imprimo o JSON completo que recebi, de forma organizada.
    print(json.dumps(dados, indent=4))
else:
    print(f"\n--- OCORREU UM ERRO NA MINHA REQUISIÇÃO ---")
    print(f"A API me retornou o Status Code: {resposta.status_code}")
    # Imprimo a mensagem de erro que a API me deu, para eu saber o que aconteceu.
    print(resposta.text)
