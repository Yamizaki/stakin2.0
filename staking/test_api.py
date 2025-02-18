import json
import os
def fetch_and_save_data_stocks():
        ruta_archivo = os.path.join(os.getcwd(), 'staking/apis_examples/api_json_stocks.json')
        print(os.getcwd())
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                data = json.load(archivo)  # Carga el archivo JSON
                print(data)
                return {"data_stocks": data}
        except FileNotFoundError:
            print(f"Error: El archivo {ruta_archivo} no fue encontrado.")
            return {"data_stocks": "Nancy"}
        except json.JSONDecodeError:
            print(f"Error: El archivo {ruta_archivo} no tiene un formato JSON válido.")
            return {"data_stocks": "Nancy JSON"}

fetch_and_save_data_stocks()