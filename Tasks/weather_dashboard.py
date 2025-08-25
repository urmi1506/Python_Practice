import requests
import json

class WeatherApp:
    base_url="https://api.openweathermap.org/data/2.5/weather"

    def __init__(self,base_url=None,api_key=None):
        self.base_url=base_url or WeatherApp.base_url
        self.api_key=api_key

    def set_city(self,city_name):
        data={'city_name':city_name}
        r=requests.post(f"{self.base_url}/posts",json=data)
        details=r.json()
        pretty_json = json.dumps(details, indent=4, sort_keys=True)
        return pretty_json

    def display(self,temperature,humidity,weather_desc):
        r=requests.get(f"{self.base_url}/posts/{temperature}{humidity}{weather_desc}")
        details=r.json()
        pretty_json = json.dumps(details, indent=4, sort_keys=True)
        return pretty_json

def main():
    weather=WeatherApp(base_url="https://openweathermap.org/api",
    api_key="xyz123")

    print("Set City name:")
    print(weather.set_city("Jalgaon"))
        
    print("\n Fetch and Display details:")
    print(weather.display())

main()