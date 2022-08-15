import requests
r = requests.get("https://data.epa.gov.tw/api/v1/aqx_p_432?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=json", verify=False)
list_of_dicts = r.json()
Sensor=list_of_dicts['records']
for i in Sensor:
  print(i["SiteName"],i["County"],i["AQI"],i["PM2.5"],i["Status"],i["PublishTime"])