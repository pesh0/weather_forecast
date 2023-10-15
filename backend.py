import requests
API_KEY = "c7501907bd9a47816899e6fb0c681592"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filter_data = data["list"]
    filter_data = filter_data[:8*forecast_days]
    return filter_data

if __name__=="__main__":
    print(get_data(place="Sofia", forecast_days=3))
