from owm_key import owm_api_key
import json
import requests

from getweatherdata import get_weather_data

# TODO 1
def get_weather_data(place, api_key=None):
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}').text
    res_obj = json.loads(res)
    formatted_data = {
            "name": res_obj.get("name"),
            "coord": {
                "lon": res_obj['coord']['lon'],
                "lat": res_obj['coord']['lat']
            },
            "country": res_obj["sys"].get("country"),
            "feels_like": res_obj["main"]["feels_like"] - 273.15,  
            "timezone": f"UTC{'+3' if res_obj['timezone'] == 10800 else ''}"  
        }

    print(json.dumps(formatted_data, indent=4))


   
    #

if __name__ == '__main__':
    get_weather_data('Moscow', api_key=owm_api_key)
    get_weather_data('Chicago', api_key=owm_api_key)
    get_weather_data('Dhaka', api_key=owm_api_key)
