from parcing_part import get_data_set
from predict_precipitation import predict_prep

# latitude = input("Please, enter latitude")
# longitude = input("Please, enter longitude")
# start_date = input("Please, enter date to start with. Format: 2022-01-01")
# end_date = input("Please, enter date to finish with. Format: 2023-01-01. Take a notice: date can't be later then "
# "2023-05-26")

print(get_data_set(49.98, 36.25, '2022-01-01', '2023-01-30', 0))
print(predict_prep([00, -4.5, 93, 998.4, 100, 0.0, 0.0, 11.3]))
