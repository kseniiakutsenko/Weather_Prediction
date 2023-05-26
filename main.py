from parcing_part import get_data_set
from predict_precipitation import predict_prep

latitude = input("Please, enter latitude")
longitude = input("Please, enter longitude")
start_date = input("Please, enter date to start with. Format: 2022-01-01")
end_date = input("Please, enter date to finish with. Format: 2023-01-01. Take a notice: date can't be later then "
                     "2023-05-26")

print(get_data_set(float(latitude), float(longitude), start_date, end_date))
print(predict_prep([-8.8, -3.1, 2.5, 6.0, 26.3, 48.2, 128]))


