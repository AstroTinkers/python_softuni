class Car:
    def __init__(self, data):
        self.model, self.plate, self.color, self.vin, self.part_price = data.split(", ")
        self.vin = int(self.vin)
        self.part_price = float(self.part_price) * 1.2

    def __repr__(self):
        return f"Car: {self.model}, Plate: {self.plate}, Color: {self.color}, VIN: {self.vin}, " \
               f"Part price: {self.part_price:.2f}"
