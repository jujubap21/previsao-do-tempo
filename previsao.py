import requests

api_key = "63770aadb3b89d49f80854bd2b2ace42"
cidade = input("Digite a cidade aqui: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br"

requisicao = requests.get(url)
requisicao_dic = requisicao.json()
descricao = requisicao_dic["weather"][0]["description"]
temperatura = requisicao_dic["main"]["temp"] - 273.15
sensacao = requisicao_dic["main"]["feels_like"] - 273.15
temperatura_min = requisicao_dic["main"]["temp_min"] - 273.15
temperatura_max = requisicao_dic["main"]["temp_max"] - 273.15

print(
    f"{descricao},",
    "temperatura de" " " f"{round(temperatura,2)} °C,",
    "mínima de" " " f"{round(temperatura_min,2)} °C,",
    "máxima de" " " f"{round(temperatura_max,2)} °C",
    " e sensação térmica de" " " f"{round(sensacao,2)} °C",
)
