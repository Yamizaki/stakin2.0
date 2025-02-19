import requests

your_api_key = "14c499a1c37f4ea18f13d19ede8adb0f"
url = "https://api.profit.com/data-api/fundamentals/stocks/general/GOOGL?token="+your_api_key


respose = requests.get(url)
print(respose.json())