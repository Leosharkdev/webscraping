import requests
import os
import json

# URL da API
api_url = "https://financialmodelingprep.com/api/v3/search?query=.SA&apikey=8xyDYxij8kj1t7hBNTkyR8daePxo66WK"

# Pasta para salvar as imagens
folder_path = "logos_b3_api"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Fazer a solicitação à API
response = requests.get(api_url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    data = response.json()  # Converter a resposta para JSON
    
    # Iterar pelos resultados
    for i, item in enumerate(data):
        try:
            # URL da logo
            symbol = item.get("symbol")
            if symbol:
                logo_url = f"https://financialmodelingprep.com/images-New-jpg/{symbol}.jpg"
                print(f"Baixando logo {symbol}: {logo_url}")

                # Fazer o download da imagem
                img_data = requests.get(logo_url).content
                
                # Nome do arquivo
                img_filename = f"{folder_path}/{symbol}.jpg"
                
                # Salvar a imagem
                with open(img_filename, "wb") as f:
                    f.write(img_data)
                print(f"Logo {symbol} baixada com sucesso!")
            else:
                print(f"Símbolo inválido no item {i}: {item}")
        except Exception as e:
            print(f"Erro ao baixar a logo {i}: {e}")
else:
    print(f"Erro ao acessar a API: {response.status_code}")