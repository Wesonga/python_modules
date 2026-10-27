
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.__is_rented = False

    def rent(self):
        if self.__is_rented:
            print(f"{self.brand} {self.model} is already rented.")
            return False

        self.__is_rented = True
        print(f"{self.brand} {self.model} rented successfully.")
        return True

    def return_vehicle(self):
        if not self.__is_rented:
            print(f"{self.brand} {self.model} was not rented.")
            return False

        self.__is_rented = False
        print(f"{self.brand} {self.model} returned successfully.")
        return True

    def is_available(self):
        return not self.__is_rented

    def calculate_rental_cost(self, days):
        raise NotImplementedError(
            "Subclasses must implement calculate_rental_cost()."
        )

    def display_info(self):
        status = "Available" if self.is_available() else "Rented"
        print(
            f"{self.brand} {self.model} ({self.year}) "
            f"- Status: {status}"
        )


class Car(Vehicle):
    def calculate_rental_cost(self, days):
        if days <= 0:
            raise ValueError("Rental days must be positive.")
        return 3000 * days


class Motorcycle(Vehicle):
    def calculate_rental_cost(self, days):
        if days <= 0:
            raise ValueError("Rental days must be positive.")
        return 1000 * days


class Truck(Vehicle):
    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity

    def calculate_rental_cost(self, days):
        if days <= 0:
            raise ValueError("Rental days must be positive.")

        base_cost = 10000 * days
        extra_days = max(0, days - 3)
        extra_cost = 2000 * extra_days

        return base_cost + extra_cost

    def display_info(self):
        super().display_info()
        print(f"Load capacity: {self.load_capacity} tonnes")


# Create different vehicles
vehicles = [
    Car("Toyota", "Corolla", 2022),
    Motorcycle("Honda", "CB125", 2023),
    Truck("Isuzu", "FRR", 2021, 5),
]

# Rent some vehicles
vehicles[0].rent()  # Rent the car
vehicles[2].rent()  # Rent the truck

print("\n--- Vehicle Information ---")
for vehicle in vehicles:
    vehicle.display_info()

print("\n--- Rental Cost for 5 Days ---")

for vehicle in vehicles:
    if vehicle.is_available():
        cost = vehicle.calculate_rental_cost(5)
        print(
            f"{vehicle.brand} {vehicle.model}: "
            f"KSh {cost} for 5 days"
        )
    else:
        print(
            f"{vehicle.brand} {vehicle.model}: "
            "Currently rented; not available for a new rental."
        )
