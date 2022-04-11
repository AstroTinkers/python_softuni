import pandas as pd
from Assignement import classes

car_class = classes.Car
cars = []
while True:
    input_data = input("Please enter car data or 'Stop' to stop: ")
    if input_data == 'Stop':
        break
    elif input_data == "":
        continue
    else:
        cars.append(car_class(input_data))

car_data = {"Manufacturer": [], "Plate Nº": [], "VIN": [], "Part Price": []}
for car in cars:
    car_data["Manufacturer"].append(car.model)
    car_data["Plate Nº"].append(car.plate)
    car_data["VIN"].append(car.vin)
    car_data["Part Price"].append(car.part_price)
file_to_write = pd.DataFrame(car_data)

while True:
    print("Please select your output format:\n1).csv\n2).json\n3).parquet")
    output_select = input()
    if output_select == "1":
        file_to_write.to_csv(path_or_buf='cars.csv')
        break
    elif output_select == "2":
        file_to_write.to_json(path_or_buf='cars.json')
        break
    elif output_select == "3":
        file_to_write.to_parquet('cars.parquet')
        break
    else:
        print("Invalid selection. Please choose from the options below.")
        continue
