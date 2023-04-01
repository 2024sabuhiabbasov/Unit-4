# Quiz 050

![image](https://user-images.githubusercontent.com/111758436/222195839-5e9fc9b8-301b-4653-bd20-104962e46ed7.png)

## My codes
### Python
```.py
 # Program for Quiz 050

class Flight:
    def __init__(self, flight_number: str, origin: str, destination: str, departure_time: str, duration: list):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.duration = duration

    def get_duration(self):
        return f"{self.duration[0]} hours {self.duration[1]} minutes and {self.duration[2]} seconds"

# 1. Create the method get_duration() that returns the duration as a string "5 hours 30 minutes and 3 seconds"
flight1 = Flight("TK 199", "Haneda", "Istanbul", "21:55 PM", [13, 20, 0])
print(f"Duration of {flight1.flight_number} by {flight1.origin}: {flight1.get_duration()}")
# 2. Create two objects of the Flight class and demonstrate how to use the class to represent flights offered by an airline.
flight2 = Flight("ZB 1005", "Istanbul", "Tirana", "11:10 AM", [1, 40, 0])
print(f"{flight2.flight_number} from {flight2.origin} to {flight2.destination} will depart at {flight2.departure_time}")
flight3 = Flight("TK 340", "Tirana", "Baku Heydar Aliyev", "12:25 PM", [2, 40, 0])
print(f"{flight3.flight_number} from {flight3.origin} is going to {flight3.destination}. It will take {flight3.get_duration()} to arrive at {flight3.destination}")
```
### Proof
![image](https://user-images.githubusercontent.com/111758436/221759556-edb4cbfe-10f2-4306-a56d-606a1e480594.png)
