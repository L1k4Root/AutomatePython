import requests

lat = 40.7128
lon = -74.0060

api_key="4de9a2c7d47be0be6860c14a92b9f7e7"
url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"

response = requests.get(url)
data = response.json()
data_list = data['list']
city = data['city']['name']


with open("02-data.txt", "a") as file:
    file.write(f"\n")
    for i in data_list:
        date_time = i['dt_txt']
        temperature = i['main']['temp']
        description = i['weather'][0]['description']
        file.write(f"{city},{date_time},{temperature},{description}\n")



# print(type(data['list'])) # List
# print(data['list'][0]['dt_txt'])
# print(data['city']['name'])
# print(data['list'][1]['main']['temp'])
# print(data['list'][1]['weather'][0]['description'])