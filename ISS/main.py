import requests, datetime, smtplib,time

email='tester7760775061@gmail.com'
password='mamb mymj uuus gcbh'
lat = 12.971599
lon = 77.594566
def isnight():
    parameters = {
    'lat': lat,
    'lng': lon,
    'formatted' : 0,
    }
    tim=datetime.datetime.now().hour
    response1 = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    data1=response1.json()
    sunrise= data1['results']['sunrise'].split('T')
    sunrise1=int(sunrise[1].split(':')[0])
    sunset=data1['results']['sunset'].split('T')
    sunset1=int(sunset[1].split(':')[0])
    if tim > sunset1 or tim < sunrise1:
        return True
    return False
def locationcheck():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    data = response.json()
    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])
    pos = (longitude, latitude)
    if latitude == lat+5 or lat-5:
        if longitude == lon+5 or lon-5:
            return True
    return False

while True:
    time.sleep(60)
    if locationcheck() and isnight():
        con = smtplib.SMTP("smtp.gmail.com", 587)
        con.starttls()
        con.login(user=email, password=password)
        con.sendmail(from_addr=email, to_addrs="sathwikshetty9876@gmail.com", msg=f"The International spae station is just above you.")
        con.close()