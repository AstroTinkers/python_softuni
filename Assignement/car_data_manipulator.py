from Assignement import classes
import pandas

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
print(cars)
