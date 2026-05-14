import requests
import datetime
import smtplib, time

MY_LATITUDE = 16.572090
MY_LONGITUDE = 82.000854
MY_EMAIL = "bharatchikkala@gmail.com"
MY_PASSWORD = "Bharath@02122004"
def is_iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

    if MY_LATITUDE-5 <= latitude <= MY_LONGITUDE+5 and MY_LATITUDE-5 <= longitude <= MY_LONGITUDE+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0
    }
    response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # print(data)

    #getting hold of hour of sunrise and sunset
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
    # print(sunrise)
    # print(sunset)
    time_now = datetime.datetime.now()
    if time_now <= sunrise or time_now >= sunset:
        return True

while True:
    time.sleep(60)
    if is_iss_above() and is_night():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\nISS is above you in the sky!!"
        )
