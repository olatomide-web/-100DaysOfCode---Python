import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "2cb82b34d9068c5cb5d55a41e0d318c8"

account_sid = "ACfc2a3889fb9af79babc7ce22bcee1fc6"
auth_token = "b9d30c4b62322974ededb9f5e458bf10"

weather_params = {
    "lat": 6.687590,
    "lon": 3.234390,
    "appid": api_key,
    "exclude" : "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
                .create(
                     body="It's going to rain today, Remember to move with your umbrella.",
                     from_='+19382532331',
                     to='+234 811 853 1985'
                 )
    print(message.status)

