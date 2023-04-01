# Quiz 051

![image](https://user-images.githubusercontent.com/111758436/223024308-fa46cc17-50bf-4c5f-9a68-23cbef8fc768.png)

## Codes
### My solution
```.py
# Program for Quiz 051

class Wheel:
    def __init__(self, size):
        self.size = size

    # Method to get the size of the wheel
    def get_size(self):
        return self.size

    # Method to get the circumference (perimeter) of the wheel
    def get_perimeter(self):
        return 2 * self.size * 3.14

    # Method to get the distance in kilometers traveled per rotation of the wheel
    def get_km_per_rotation(self):
        return self.get_perimeter() / 100000

class Bicycle:
    def __init__(self, wheel_size, frame_material):
        self.wheel = Wheel(wheel_size)
        self.frame_material = frame_material

    # Method to print the details of the bicycle object
    def ride(self):
        # Print the wheel size and frame material of the bicycle
        print(f"The bicycle has a {self.wheel.get_size()} inch wheel and a {self.frame_material} frame.")

# Create a Bicycle object with wheel size 26 and frame material "almunium
wheel_size = 26
frame_material = "almunium"
my_bike = Bicycle(wheel_size, frame_material)

print(f"{my_bike.wheel.get_km_per_rotation()} km per rotation")
```

### Proof
![image](https://user-images.githubusercontent.com/111758436/223025543-5c432dfc-e1a2-495d-93a6-8ecd1d09ae82.png)
