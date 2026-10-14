from threading import Lock

class TrafficLight:
    def __init__(self):
        self.greean_road = 1
        self.lock = Lock()

    def carArrived(
        self, carID, roadID, direction, turnGreen, crossCar
        ):
        with self.lock:
            if self.green_road != roadID:
                turnGreen()
                self.greean_road = roadID

            crossCar()
