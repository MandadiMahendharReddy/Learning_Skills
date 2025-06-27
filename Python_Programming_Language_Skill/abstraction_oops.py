from abc import ABC, abstractmethod


# 🚘 Step 1: Abstract Class - A common rulebook for all cars
class Car(ABC):

    @abstractmethod
    def start_engine(self):
        # This method must be written in each car type
        pass


# 🚗 Step 2: Tesla class follows the rule and defines its own way to start
class Tesla(Car):
    def start_engine(self):
        return "Starting Tesla: Fingerprint scan activated!"


# 🚙 Step 3: BMW class follows the rule with its own method
class BMW(Car):
    def start_engine(self):
        return "Starting BMW: Pressing push-to-start button!"


# 🚕 Step 4: Toyota class follows the rule too
class Toyota(Car):
    def start_engine(self):
        return "Starting Toyota: Turning the car key!"


# 🧑‍🔧 Step 5: Driver code - You start any car without knowing how it works inside
def start_my_car(car: Car):
    print(car.start_engine())


# 🚦 Step 6: Create car objects
my_tesla = Tesla()
my_bmw = BMW()
my_toyota = Toyota()

# 🏁 Step 7: Start all cars
start_my_car(my_tesla)  # Output: Starting Tesla...
start_my_car(my_bmw)  # Output: Starting BMW...
start_my_car(my_toyota)  # Output: Starting Toyota...
