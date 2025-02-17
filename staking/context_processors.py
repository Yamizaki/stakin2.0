import requests

def fetch_and_save_data(request):
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=4&page=1"  # 🔹 API de ejemplo
    response = requests.get(url)

    if response.status_code == 200:  # ✅ Si la respuesta es exitosa
        data = response.json()
    return{
        "data_crypto": data,
    }




