import requests
import csv


def get_data_set(latitude, longitude, start_date, end_date):
    url = 'https://archive-api.open-meteo.com/v1/archive'
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'start_date': start_date,
        'end_date': end_date,
        'daily': 'temperature_2m_min,temperature_2m_mean,shortwave_radiation_sum,precipitation_sum,precipitation_hours,'
                 'windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant',
        'timezone': 'auto'
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        time = data['daily']['time']
        temperature_2m_min = data['daily']['temperature_2m_min']
        temperature_2m_mean = data['daily']['temperature_2m_mean']
        shortwave_radiation_sum = data['daily']['shortwave_radiation_sum']
        precipitation_sum = data['daily']['precipitation_sum']
        precipitation_hours = data['daily']['precipitation_hours']
        windspeed_10m_max = data['daily']['windspeed_10m_max']
        windgusts_10m_max = data['daily']['windgusts_10m_max']
        winddirection_10m_dominant = data['daily']['winddirection_10m_dominant']

        with open('data/weather_data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                ['temperature_2m_min', 'temperature_2m_mean', 'shortwave_radiation_sum', 'precipitation_sum',
                 'precipitation_hours', 'windspeed_10m_max', 'windgusts_10m_max', 'winddirection_10m_dominant'])

            for i in range(len(time)):
                row = [
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

        return 'Data set was created successfully'
    else:
        return 'Error during request complite: ', response.status_code
