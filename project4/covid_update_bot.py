import requests
from win10toast import ToastNotifier
import json
import time


def update():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    text = f"Confirm Cases : {data['cases']} \nDeath : {data['deaths']} \nRecovered : {data['recovered']}"

    # print(text)
    while True:
        toast = ToastNotifier()
        toast.show_toast('Covid-19 Updates',text,duration=10)
        # toast.notification_active()
        time.sleep(100)
    
update()