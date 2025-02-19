import requests
from django.core.cache import cache
import json, os 
def fetch_and_save_data(request):
    cache_key = "api_response"
    cached_data = cache.get(cache_key)

    if cached_data:
        print("CACHEED")
        return {"data_crypto": cached_data}

    try:
        response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=4&page=1")
        response.raise_for_status()  # Lanza una excepción si el status no es 200
        data = response.json()

        # Almacenar en caché por 10 minutos
        cache.set(cache_key, data, timeout=600)
        print("data fetched")
        return {"data_crypto": data}

    except requests.RequestException:
        # En caso de error, devolver datos cacheados (si existen)
        print("Data cached")
        return {"data_crypto": cached_data or {}}

def fetch_and_save_data_stocks(requests):
        ruta_archivo = os.path.join(os.getcwd(), 'staking/apis_examples/api_json_stocks.json')
        print(os.getcwd())
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                data = json.load(archivo)  # Carga el archivo JSON
                return {"data_stocks": data}
        except FileNotFoundError:
            print(f"Error: El archivo {ruta_archivo} no fue encontrado.")
            return {"data_stocks": "Hubo un error, intente nuevamente."}
        except json.JSONDecodeError:
            print(f"Error: El archivo {ruta_archivo} no tiene un formato JSON válido.")
            return {"data_stocks": "Hubo un error, intente nuevamente."}