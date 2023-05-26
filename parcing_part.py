import requests
import csv


def get_data_set(latitude, longitude, start_date, end_date, code):
    if code == 0:
        data_set_name = 'weather_data_for_checking'
    else:
        data_set_name = 'weather_data_for_prediction'
    url = 'https://archive-api.open-meteo.com/v1/archive'
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'start_date': start_date,
        'end_date': end_date,
        'hourly': 'temperature_2m,relativehumidity_2m,surface_pressure,precipitation,cloudcover,'
                 'direct_radiation,diffuse_radiation,windspeed_10m',
        'timezone': 'auto'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        time = data['hourly']['time']
        temperature_2m_min = data['hourly']['temperature_2m']
        temperature_2m_mean = data['hourly']['relativehumidity_2m']
        shortwave_radiation_sum = data['hourly']['surface_pressure']
        precipitation_sum = data['hourly']['precipitation']
        precipitation_hours = data['hourly']['cloudcover']
        windspeed_10m_max = data['hourly']['direct_radiation']
        windgusts_10m_max = data['hourly']['diffuse_radiation']
        winddirection_10m_dominant = data['hourly']['windspeed_10m']

        with open('data/'+data_set_name+'.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                ['time', 'temperature_2m', 'relativehumidity_2m', 'surface_pressure', 'precipitation',
                 'cloudcover', 'direct_radiation', 'diffuse_radiation', 'windspeed_10m'])

            for i in range(len(time)):
                row = [
                    str(time[i])[11:13],
                    temperature_2m_min[i],
                    temperature_2m_mean[i],
                    shortwave_radiation_sum[i],
                    precipitation_sum[i],
                    precipitation_hours[i],
                    windspeed_10m_max[i],
                    windgusts_10m_max[i],
                    winddirection_10m_dominant[i]
                ]
                writer.writerow(row)

    else:
        return 'Error during request complite: ', response.status_code

